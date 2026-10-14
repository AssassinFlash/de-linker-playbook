# 询盘数据从哪读

主读取路径：用一把 WooCommerce 只读密钥，`GET https://de-linker.com/wp-json/wc/v3/orders`。`status` 只传四个 slug：`inquiry-received`、`proforma-issued`、`completed`、`cancelled`。`include_meta` 只传 `_linker_proforma_issued`。表格写入前只留单号、内部 id、公司名、`date_created_gmt`、状态、以及有值的签发秒。

理由：这套代码里的询盘就是 Woo 订单。联系表单的提交不落库，直接来信没有别的只读计数，这两类按没有处理。线上路由已经把两个自定义状态放进 `status` 枚举；WooCommerce 11.1.2 在经典文章表和 HPOS 两条查询里都会按这个参数过滤。只读密钥不能改订单。返回的是请求当时的数据，公司名不会被换成占位。`just pull` 要整库、靠人手、公司名被抹掉。加载插件的 WP-CLI 可能在 `init` 上补一条摘要 cron。

每次用这把密钥从外部发来的 GET，会更新密钥行的 `last_access`。订单数据本身不被改写。响应里的 `billing` 对象仍带着姓名、邮箱、电话、地址，写入表格之前丢掉。

核查日：2026-10-14。线上只做了 GET / HEAD，没有提交表单、下单或登录。

## 1. 形式发票申请

询盘是 `shop_order`，不是单独的文章类型。两个自定义状态在代码里不带 `wc-` 前缀注册，库存和接口里的键带 `wc-`。

| 状态 slug | 存储键 | 客人看到的名字 | 算不算已提交的询盘 |
| --- | --- | --- | --- |
| `inquiry-received` | `wc-inquiry-received` | Inquiry received | 算 |
| `proforma-issued` | `wc-proforma-issued` | Proforma invoice issued | 算 |
| `completed` | `wc-completed` | Completed | 算 |
| `cancelled` | `wc-cancelled` | Cancelled | 算 |
| `pending` | `wc-pending` | Not sent | 不算 |

`pending` 被改名为 “Not sent”：订单建出来了，但没有发出去。不计入询盘。线上状态名单里还有 `processing`、`on-hold`、`refunded`、`failed`、`checkout-draft`、`auto-draft`、`trash`。规格规定公司侧在签发之后只手动改 `completed` 或 `cancelled`，没有别的动作。这四步之外的状态不计入。

流程：

- 已批准账号在 `/proforma-request/`、`/de/proforma-anfrage/` 提交。`ProformaGateway::process_payment` 把订单设为 `inquiry-received`。减库存被关掉。
- 员工按 Issue Proforma，或把状态直接改成 `wc-proforma-issued`，走 `Issuer::ensure_issued`。签发时写入三个 meta：`_linker_proforma_number`、`_linker_proforma_issued`、`_linker_proforma_file`。
- `_linker_proforma_issued` 是签发当时的 Unix 秒（站点时区的 `DateTimeImmutable`，再 `getTimestamp()`）。没有这个 meta，签发时刻未知；每日摘要会把这类单排除。
- 之后员工手动设 `completed` 或 `cancelled`。插件没有“完成时刻”或“取消时刻”的 meta。

创建时刻是订单的 `date_created`，不是进入 `inquiry-received` 的时刻。摘要用的就是 `get_date_created()`。REST 对应字段是 `date_created`（站点时区）和 `date_created_gmt`。表格用 `date_created_gmt`。

完成时刻用 REST 的 `date_completed` / `date_completed_gmt`：官方字段，状态变为 completed 时由 Woo 写下。取消时刻没有对应字段。`date_modified` 没有被证明等于取消那一下，按没有这个时刻处理，表格不设取消时间列。

匿名打开两个请求页都是登录门，看不到账单表单。英文页标题 “Get your Proforma”，德文页标题 “Proformarechnung anfordern”，正文要求用合作伙伴账号登录。`billing_email`、`linker_proforma` 都不在匿名 HTML 里。已登录买家的提交不在本次只读核查范围内。

插件声明兼容 HPOS（`custom_order_tables`）。读订单走 `WC_Order` / `wc_get_orders`，经典 `posts` 和 HPOS 同一条代码路径。线上当前用的是哪一种存储，公开 GET 看不到。

客户能力 `linker/inquiry-status` 只返回当前登录客户自己的询盘：`id`、`number`、`status`、`status_label`、`date`、`total`，有号时再加 `proforma_number`。没有公司名，没有签发秒，也不是全部询盘。不作为团队的读取路径。

每日 09:00（Europe/Berlin）的摘要会列出超 24 小时仍停在 `inquiry-received` 的单，以及签发超 72 小时仍停在 `proforma-issued` 的单，标签里有单号和账单公司名。收件人是团队邮箱。按约定不读该邮箱，摘要不是读取路径。

## 2. `/kontakt/` 联系表单

`https://de-linker.com/kontakt/` 返回 404，标题 “Page not found”。活着的页面是 `https://de-linker.com/contact/`（200）和 `https://de-linker.com/de/kontakt/`（200）。

两页的挂载点 `div[data-linker-contact-mount]` 里面仍是旧的 `div.cp-contact-fallback`。英文和德文的回退句都让访客改发团队邮箱。短代码 `[linker_contact_form]` 不在这两页的 HTML 里。规格里的迁移 `tools/migrate/68-contact-form.py` 就是用来把这个回退块换成短代码的。新表单在仓库里，没有挂到线上页面。当前这两页的访客路径是发信到团队邮箱，和直接来信同一类，按没有处理。

仓库里的新表单，一旦被挂上，行为是：

- 短代码 `[linker_contact_form]`，字段为 `message`（≤5000）、`name`、`company`（选填）、`email`、`consent`、蜜罐 `website`、nonce、`lang`、回跳地址。
- POST 到 `admin-post.php`，动作 `linker_contact`。`Handler::process` 校验 nonce、蜜罐、限流和字段，然后发两封 `wp_mail`：访客回执，以及给团队邮箱的团队信。随后 302。这个函数不写订单，也不写业务文章。
- 限流是 transient，键 `linker_contact_` 加连接地址的 md5，窗口 1 小时、3 次，存的是时间戳。过期即消失，不能当作提交档案。
- 邮件走 Outbox。配额允许时当场发出，成功且尚未入队的信不产生记录。没发出去的才写成私有文章类型 `linker_mail_job`；后来发送成功会被删掉；重试耗尽的留在草稿，正文在 meta `_linker_mail_message`。这是失败队列，不是成功提交的台账。线上有没有这种草稿，未持密钥看不到；即使有，也不拿来计数。

所以：新表单的设计是只发邮件到团队邮箱，不落询盘库。线上页面目前连这个表单都没挂。这一入口不可得，按没有处理。

## 3. 直接来信到团队邮箱

团队邮箱是设置项 `linker_commerce_team_to`，空值回落到常量 `DEFAULT_TEAM_TO`。按约定不读这个邮箱。

新站仓库的 PHP、Markdown、Python 里没有 IMAP，也没有入站邮件计数。每日摘要数的是 Woo 订单和发不出去的出站信，不是寄进来的信。旧插件表 `tv_b2b_contact_request` 在 `just pull` 的伪名化里整表丢行。失败的 `linker_mail_job` 和一小时的限流 transient 都不是入站计数。

没有别的只读计数来源。不可得，按没有处理。

## 4. 三条读取路径

### Woo REST API：主路径

线上 `GET /wp-json/` 的命名空间含 `wc/v3` 和 `linker/v1`。`GET /wp-json/wc/v3/orders` 未带密钥时是 401，`woocommerce_rest_cannot_view`，正文 “Sorry, you cannot list resources.”。`GET /wp-json/wc/v3/orders/statuses` 未带密钥是 200，只有 slug 和显示名，没有件数，没有客户字段。名单里 `pending` 的名字是 “Not sent”，两个自定义状态的名字与插件一致。这个端点证明状态过滤器已经在线上生效，本身不能当计数来源。

`GET /wc/v3/orders` 的集合参数（2026-10-14 的路由索引）：`status` 类型是数组，默认 `any`，枚举为 `any`、`trash`、`auto-draft`、`pending`、`inquiry-received`、`proforma-issued`、`processing`、`on-hold`、`completed`、`cancelled`、`refunded`、`failed`、`checkout-draft`。另有 `per_page`（默认 10，最大 100）、`page`、`after`、`before`、`modified_after`、`modified_before`、`dates_are_gmt`、`include_meta`、`exclude_meta`、`created_via` 等。索引里没有 `_fields`。

公开的订单文档仍把 `status` 写成原生那几个值。线上枚举和 11.1.2 的 v3 控制器才是本站的事实：v3 把 `status` 收成数组，枚举来自 `wc_get_order_statuses()`，插件用 `wc_order_statuses` 把两个自定义状态加进去。

过滤怎么落到查询上（11.1.2）：

- v3 `prepare_objects_query` 把每个已知 slug 写成 `wc-` 加 slug，放进 `post_status`；`any` 则设为 `any`。
- HPOS 关闭时，`get_objects` 交给父类，父类用这些参数跑 `WP_Query`。`post_status` 就是文章状态。
- HPOS 打开时，同一组参数交给 `WC_Order_Query`。订单数据存储换成 `OrdersTableDataStore`，它建 `OrdersTableQuery`。`maybe_remap_args` 把 `post_status` 映成 `status`，`sanitize_status` 保留已经是合法 `wc-` 键的值，再按 `orders.status` 做 WHERE。

因此自定义状态可以查。经典表和 HPOS 两条代码都滤得动。线上到底开没开 HPOS，不影响这条 REST 过滤；它只影响想改写 SQL 的人。本次没有带密钥发出成功的列表请求，上面是路由索引加 11.1.2 源码，不是一次真实列表的响应体。

权限：

- 密钥在后台 WooCommerce → Settings → Advanced → REST API 生成，绑到一个 WordPress 用户，调用时服从该用户的角色和能力。HTTPS 上用 HTTP Basic：Consumer Key 当用户名，Consumer Secret 当密码。
- `check_permissions`：GET 和 HEAD 只允许密钥权限 `read` 或 `read_write`；POST、PUT、PATCH、DELETE 要 `write` 或 `read_write`。一把 Read 密钥改不了订单。
- 列表还要过 `wc_rest_check_post_permissions( shop_order, 'read' )`，查的是该文章类型的 `read_private_posts`。`shop_order` 的 `capability_type` 是 `shop_order`，WordPress 由此得到 `read_private_shop_orders`。规格把订单页交给 shop_manager。密钥绑到持有这一能力的后台用户。
- 未带密钥时线上已经返回同一个 401。是否已经存在一把 Read 密钥，不登录看不到。按没有这把密钥处理：用一次后台操作建一把 Read 密钥。这不是新站仓库里的插件改动。密钥放在两个仓库之外。

字段：

- 官方订单属性里有 `id`、`number`（只读）、`status`、`date_created`、`date_created_gmt`、`date_completed`、`date_completed_gmt`、`billing`（含 `company`，也含姓名、邮箱、电话、地址）、`customer_note`、`customer_ip_address`、`customer_user_agent`、`meta_data`。
- `linker-commerce` 里没有 `woocommerce_order_number` 过滤器，本插件不会把 `number` 改得和 `id` 不同。别的在线插件会不会改，未证实。表格两列都留。
- `include_meta` 优先于 `exclude_meta`，只返回点名的 meta。HPOS 下会剥掉经典订单的内部键（账单索引、金额、IP 这类），`_linker_proforma_issued` 不在那份内部键里，点名之后能读到。
- 响应在写进表格之前仍是完整订单。线上参数表没有 `_fields`。嵌套的 `billing` 能不能被裁到只剩 `company`，未证实。表格规则不依赖这一点：写入前只留公司名。

频率：每次 GET 是当时的订单。`per_page` 最大 100，按页取完。本票不排站点 cron，也不定调用间隔。

站点侧：读订单不需要改插件。把新联系表单挂上去，要在新站仓库跑迁移 68；挂上之后提交仍然只发邮件，不产生可回读的询盘记录。

### `just pull`：状态和日期的后备，不是表格源

`just pull` 就是 `snapshot`。经 `ssh hostinger-de-linker` 读线上，写到仓库外的 `~/de-linker-data/<YYYYMMDD-HHMM>/`。库用主机上的 `mysqldump`，gzip 流回本机，边读边伪名化，原始导出不落盘。规格写明不写线上。远端 WP-CLI 带 `--skip-plugins --skip-themes --skip-update-check`，避免插件在被列出时初始化和写更新 transient。

`pull.just` 里没有计划任务。新鲜度等于上次有人手工跑 `just pull` 的时刻。

伪名化对这份表格是硬伤：订单地址表的 `company` 换成 “Example Company”；姓名、街道、电话换占位；`ip_address`、`user_agent`、`customer_note`、`transaction_id` 置空；邮箱按规则替换。`_linker_proforma_issued` 不在被清空的订单元数据名单里，订单状态列和创建时间列也不在 `_orders` 清空的四列里，所以状态、创建时间、签发秒还能留在快照里。公司名留不住。旧的 `tv_b2b_contact_request` 整表丢行。

适合在已经有一份快照时核对状态和日期的件数。不适合当所有者表格的来源。

### WP-CLI 经 SSH：能读，不作为主路径

生产上的 WP-CLI 在 `ssh hostinger-de-linker` 之后的 `/usr/local/bin/wp`。不加载插件时，自定义状态只是库里的 `wc-` 值，数得出来，但公司名在哪张表取决于存储模式，而线上是 HPOS 还是经典文章表没有证实。加载插件则走 `wc_get_orders`，存储模式被抽象掉；可是 `Digest\Module` 在 `init` 上调用 `Scheduler::ensure`，当前没有 `linker_commerce_digest` 事件时会 `wp_schedule_single_event`。一次“只读”的 WP-CLI 可能写下一条 cron。

REST 把存储抽象掉，又用 Read 密钥挡住改订单。主路径用 REST。

## 5. 个人数据与表格最小集合

依据是 GDPR、BDSG 和欧法院 C-710/23，不是本站的隐私页。

- GDPR 第 4 条(1)：个人数据是与已识别或可识别的自然人有关的任何信息。可识别包括通过姓名、识别号码、位置数据、在线标识，或身体、经济、社会身份等特征来识别。
- 第 4 条(5)：假名化之后，没有另行保管的附加信息就不能再归属到特定自然人。
- 序言(14)：条例不适用于法人的个人数据处理，尤其是作为法人设立的企业的名称、法律形式和联系方式。
- 序言(26)：借助附加信息仍可归属到自然人的假名化数据，仍是可识别自然人的信息。要考虑控制者或其他人合理可能使用的手段。无法再识别的匿名信息不适用条例。
- 第 5 条(1)(c)：与目的相当、相关，并限于实现目的所必需（数据最小化）。
- BDSG 2018 第 1 条把该法适用于非公共机构的自动化处理等情形。它不另写一套“什么是个人数据”，也不给公司名单独开例外。定义仍以 GDPR 第 4 条(1) 为准。
- 欧法院 2025-04-03，C-710/23，ECLI:EU:C:2025:231。第 22 段：有权代表公司的自然人，其身份信息是第 4 条(1) 的个人数据。第 31 段对第一个问题的回答：公开一名代表法人的自然人的名、姓、签名和联系方式，是第 4 条(1) 和(2) 意义上的个人数据处理。序言(14) 拿掉的是法人本身，不是代表它的人。

落到字段上：

| 字段 | 判定 |
| --- | --- |
| 姓名、邮箱、电话、地址、IP、UA、客户备注、联系表单正文、代表本人的增值税号 | 个人数据 |
| `billing.company` 这个字符串 | 混合。法人名称按序言(14) 不是个人数据；字符串若是自然人姓名（个体户）则是。控制者不能从字符串本身判断是哪一种 |
| 订单 `id` / `number` 放在所有者能接回 Woo 的表里 | 对这个控制者仍是个人数据（序言(26)） |
| 单独一个时间戳，不连到可回接的单 | 本身不是个人数据。连到订单之后，整行对所有者是个人数据 |

最小集合已经是一份个人数据存储。最小化要求的是不要再加字段。

建议写入所有者账号私有 Google 表格的列：

| 列 | 取自 | 为什么留 |
| --- | --- | --- |
| 内部 id | REST `id` | 稳定主键。`number` 可能被别的插件改掉，这一列未证实之前不能单靠单号 |
| 单号 | REST `number` | 员工和摘要用 `get_order_number()` 认单 |
| 公司 | 只留 `billing.company` | 摘要用它认是哪家。姓名、邮箱、电话、地址、增值税号不进表 |
| 日期 | `date_created_gmt` | 规格里的创建时刻，不随站点时区显示漂移 |
| 状态 | 四个询盘 slug 之一 | 不含 `pending`（Not sent） |
| 签发秒 | meta `_linker_proforma_issued`，没有就空 | 摘要的 72 小时窗用它。空着表示签发时刻未知 |

不进表：姓名、邮箱、电话、地址、增值税号、IP、UA、客户备注、表单正文、行项目、客户用户 id、完成时刻以外的修改时间。联系表单和直接来信没有行。完成时刻如果以后要加，来源只能是 `date_completed_gmt`，本最小集合先不放。

## 〔未证实〕

查不到的按没有处理。

1. 线上订单存在 HPOS 还是经典 `posts`。公开 GET 读不到这个选项。REST 在 11.1.2 的两条查询里都会按状态过滤，主路径不因此改。改走手写 SQL 时会选错表，所以不走 SQL。
2. 别的在线插件是否过滤 `woocommerce_order_number`，使 `number` 不等于 `id`。`linker-commerce` 没有这个过滤器。表格两列都留。
3. `_fields` 或别的投影能否让响应里的 `billing` 只剩 `company`，从而不把姓名、邮箱、地址、IP 放上线路。线上该路由的参数表没有 `_fields`。未持密钥，没有看过一份真实列表响应。写入规则不依赖它：进表之前只留公司名。
4. 是否已经有一把 Read 密钥。未登录不可见。按没有处理，用一次后台操作新建。
5. 取消的那一下发生在何时。没有专用 meta。`date_modified` 不等于取消时刻。按没有这个时刻处理。
6. 联系页上的回退块是迁移 68 没跑，还是有意留着。HTML 就是迁移要换掉的那块，新表单不在页面上。这一入口按没有处理，不追原因。
7. 线上是否躺着失败的 `linker_mail_job`。看不到。即使有，也不当询盘计数。

## 来源

| 事实 | 来源 |
| --- | --- |
| 四步状态、请求页地址、减库存关闭、签发与手动完成/取消、联系表单只发邮件、HPOS 与 posts 都走 `wc_get_orders` | 新站 `docs/specs/11-commerce.md` 第 14–15、49、56–77、96、109 行 |
| 创建时刻 = `date_created`；签发时刻 = `_linker_proforma_issued`；缺 meta 不计入；09:00 Europe/Berlin；窗口 86400 秒与 259200 秒 | 新站 `docs/specs/74-daily-digest.md` 第 4、7、12–13、19 行 |
| 快照手工、`mysqldump`、边读边伪名化、不写线上、公司名与地址被替换、旧联系表丢行 | 新站 `docs/specs/6-live-pull.md` 第 8–9、16–20、30 行；`tools/pull/pull.just` 第 1–18 行 |
| 状态常量、`wc-` 注册、pending 改名 Not sent、completed / cancelled 改名 | 新站 `plugins/linker-commerce/includes/Inquiry/Statuses.php` 第 26–27、42–90 行 |
| `wc_order_statuses`、减库存关闭、声明 HPOS 兼容 | 新站 `plugins/linker-commerce/includes/Inquiry/Module.php` 第 47、51、79 行 |
| 支付把状态设为 `inquiry-received` | 新站 `plugins/linker-commerce/includes/Inquiry/ProformaGateway.php` 第 92 行 |
| 三个 proforma meta；签发秒的写法 | 新站 `plugins/linker-commerce/includes/Proforma/Issuer.php` 第 43–45、200–216 行 |
| 摘要查询与公司名标签 | 新站 `plugins/linker-commerce/includes/Digest/InquiriesAwaitingProforma.php` 第 32、65–77、100–104 行；`ProformasAwaitingReply.php` 第 35、64–76、100–102 行 |
| `init` 上可能写下一次摘要 cron | 新站 `plugins/linker-commerce/includes/Digest/Module.php` 第 37 行；`Scheduler.php` 第 27、32、37、42–46、81–82 行 |
| 表单字段与只发信的提交 | 新站 `plugins/linker-commerce/includes/Contact/Form.php` 第 99–111 行；`Handler.php` 第 40、45、84–118、160–188 行；`docs/specs/11-commerce.md` 第 65–73 行 |
| 成功的信不留档，失败才留 `linker_mail_job` | 新站 `plugins/linker-commerce/includes/Mail/JobStore.php` 第 13–24、179 行；`Outbox.php` 第 13–18、124–156 行 |
| 团队邮箱设置项，空则用缺省常量 | 新站 `plugins/linker-commerce/includes/Settings/Options.php` 第 22、39、59–60 行（常量的值是团队邮箱地址，此处不抄） |
| 客户自查能力的字段 | 新站 `plugins/linker-commerce/includes/Abilities/InquiryStatus.php` 第 25–65、147–152 行 |
| 伪名化把公司换成 Example Company，不清 `_linker_proforma_issued`，丢掉 `tv_b2b_contact_request` | 新站 `tools/pull/src/linker_pull/anonymize.py` 第 18–27、70、168–171、266–288、597–627 行 |
| 生产 WP-CLI 的 SSH 与二进制 | 新站 `AGENTS.md` 第 66 行 |
| 仓库内无 `woocommerce_order_number`，无 IMAP / 入站计数 | 新站 `plugins/` 与 `*.php` / `*.md` / `*.py` 检索，2026-10-14 |
| `/kontakt/` 404；`/contact/`、`/de/kontakt/` 200 且仍是 `cp-contact-fallback`，无短代码 | 2026-10-14 HEAD，以及两页 HTML |
| 两个请求页匿名 200，正文是登录门 | 2026-10-14 `GET /proforma-request/`、`GET /de/proforma-anfrage/` |
| 订单列表未授权 401；状态名单公开且含两个自定义状态与 “Not sent” | 2026-10-14 `GET /wp-json/wc/v3/orders`、`GET /wp-json/wc/v3/orders/statuses` |
| 集合参数：`status` 为数组且枚举含自定义状态；`per_page` 最大 100；有 `include_meta`；无 `_fields` | 2026-10-14 `GET /wp-json/` 中路由 `/wc/v3/orders` |
| 线上 WooCommerce 自述 Stable tag 11.1.2 | 2026-10-14 `GET /wp-content/plugins/woocommerce/readme.txt` |
| Read 密钥不能写；HTTPS Basic；密钥服从所选用户的能力；后台生成位置 | https://developer.woocommerce.com/docs/apis/rest-api/authentication/ ；Woo 11.1.2 `class-wc-rest-authentication.php` 第 747–772、785–824 行，https://github.com/woocommerce/woocommerce/blob/11.1.2/plugins/woocommerce/includes/class-wc-rest-authentication.php |
| 列表权限与 `shop_order` 能力类型 | Woo 11.1.2 `class-wc-rest-posts-controller.php` 第 55–60 行；`wc-rest-functions.php` 第 229–246 行；`class-wc-post-types.php` 第 464 行。能力名由 `capability_type` 映射：https://developer.wordpress.org/reference/functions/get_post_type_capabilities/ |
| 官方订单字段（文档中的 `status` 枚举仍是原生值） | https://developer.woocommerce.com/docs/apis/rest-api/v3/orders/ |
| v3 把 `status` 收成数组并写入 `post_status` | Woo 11.1.2 `class-wc-rest-orders-controller.php` 第 336–354、444–456 行 |
| 经典表走 `WP_Query`；HPOS 走 `WC_Order_Query` | Woo 11.1.2 `class-wc-rest-crud-controller.php` 第 367–369 行；`class-wc-rest-orders-v2-controller.php` 第 2213–2233 行 |
| HPOS 把 `post_status` 映成 `status` 并过滤 `orders.status` | Woo 11.1.2 `OrdersTableQuery.php` 第 261–268、682–707、783、1141–1164 行；`OrdersTableDataStore.php` 第 3289–3331 行；`CustomOrdersTableController.php` 第 140、253–284 行；`class-wc-order-query.php` 第 84–86 行 |
| `include_meta` 限制 meta；HPOS 只剥内部键 | Woo 11.1.2 `class-wc-rest-controller.php` 第 635–673 行；`class-wc-rest-orders-v2-controller.php` 第 352–363、2185–2201 行 |
| GDPR 第 4 条(1)、(5)，第 5 条(1)(c)，序言(14)、(26) | https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32016R0679 |
| BDSG 2018 第 1 条 | https://www.gesetze-im-internet.de/bdsg_2018/__1.html |
| 法人代表的姓名和联系方式是个人数据 | 欧法院 C-710/23，ECLI:EU:C:2025:231，第 22、31 段，https://curia.europa.eu/juris/document/document.jsf?docid=297537&doclang=DE |
