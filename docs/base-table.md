# 底表

底表是一本 Google 表格，存放执行登记和反馈分级的数据（术语见 `CONTEXT.md`）。脚本和 AI 往里写，操作者阅读。Looker Studio 和本地运营看板都只读这一本；本地页不直连表格，读的是回流链导出的 JSON。本页只写角色名；表格链接和 ID 记在私有 vault 的 `deliverables/marketing/00-system/base-table.md` 里。

## 两本表

| 表 | 用途 | 数据 |
| --- | --- | --- |
| 底表 | 正式数据。看板和 AI 的「下一步」只读这一本 | 由脚本和 AI 写入；`build` 从不清数据行 |
| 底表（样例） | 给人看懂表的样子，也给后续脚本票当对照 | 全是假数据；每次 `build --target sample` 都整页重写 |

两本表都由 `所有者账号` 持有，并以编辑者身份共享给 `日常账号` 和 `服务账号`。服务账号自己不建文件，因为它没有 Drive 存储配额，所以表格由人建好后再共享给它。

## 表结构

正典是 [`schemas/base-table.schema.json`](../schemas/base-table.schema.json)。每个工作表对应一个定义，属性的顺序就是列的顺序，属性名就是中文表头。每列还标注了这列是什么、从哪来、谁写、示例和空值含义。要改列，先改这个文件，再重新 `build`。

工作表依次为：首页；执行登记、网页收录、网页表现、搜索词、邮件反馈、询盘、动作进度；每张数据表后面紧跟一张同名的「说明」页。时刻列一律北京时间（`年-月-日 时:分`）；网页表现、搜索词的日期按 Google 的太平洋时间切日。列一律摆开、往细里分（操作者要清晰详细，不要合并）。

| 工作表 | 一行代表什么 | 不重复键 | 级别 |
| --- | --- | --- | --- |
| 执行登记 | 一个网址（或一封信）在一天里的一次变化（动作大类 + 动作，清单在 schema 里，不够用先记「其他」）；由 `scripts/execution_log.py` 查证后写入，流程见 `skills/marketing-execution-log/SKILL.md` | 登记编号 `E-YYYYMMDD-NN` | L0 |
| 网页收录 | 一个网址的一次收录检查（URL Inspection）：收录结论 → 收录状态（中文细分）→ 英文原文三层，加和上次比、四个原因分项与一句原因说明 | 检查日期 + 网址 | L0 / L1 |
| 网页表现 | 一个网址一天的搜索数据（Search Analytics），按搜索类型 × 国家 × 设备分开 | 日期 + 网址 + 搜索类型 + 国家 + 设备 | L1 / L2 |
| 搜索词 | 同上再细分到搜索词；因隐私丢行，合计小于网页表现 | 日期 + 网址 + 搜索词 + 搜索类型 + 国家 + 设备 | L1 / L2 |
| 邮件反馈 | 一封已登记邮件上发生的一件事 | 登记编号 + 事件类型 + 回信 Message-ID | L0 / 未到 L1 / L1 / L2 |
| 询盘 | 一笔形式发票申请；状态变化时原地更新这一行 | 询盘内部编号 | L3 |
| 动作进度 | 执行登记的一行，汇总它目前走到哪一级 | 登记编号 | 汇总 |

「备注」列有固定标记时，脚本会读：

- 执行登记里写 **「不要求收录」** → 这页不算「应被收录」，W-03 / W-04 这类阻断不再报。站点有意 noindex 的页（如分类归档）用它。写入：`uv run scripts/execution_log.py note --id E-… --note "不要求收录（操作者 日期 定）"`。
- 网页收录里写 **「已核（W-13）」**、执行登记里写 **「已查（W-24）」** → 一次性核查已经做过，不再排队。

## 归因锚

所有反馈都按登记编号接回某次动作：

- 网页类（网页收录、网页表现、搜索词）：按网址到执行登记的「网址」或「旧网址」里找，取执行日期不晚于数据日期的最近一条。站点地图里从未登记过的页面，编号留空，只用于看全站情况。
- 邮件类：执行登记的「邮件 Message-ID」与来信的 `In-Reply-To` / `References` 对上。对不上任何登记的来信不进表。
- 询盘：AI 有证据时才填「归因登记编号」，并在「归因依据」里写明凭什么。没有证据就留空（未归因）。未归因的询盘照样计入北极星，但不计入任何一次动作的成效。
- 动作进度由脚本在每次回流后整表重算，算法就是 `scripts/base_table.py` 里的 `action_progress`。

## 隐私

公司名可以进表。人名、邮箱地址、电话、地址、邮件正文、询盘备注、IP 和浏览器标识都不进表，读取时在内存里丢弃。询盘来源只留来源类型、设备类型和会话页数。UTM 没有活动值，不加。浏览器标识不进表。回信只记 Message-ID、公司、日期和分类，不放正文。

## 脚本

脚本是 [`scripts/base_table.py`](../scripts/base_table.py)：一个文件，用 `uv` 运行，依赖写在文件头里（PEP 723）。任何能执行 shell 的 harness 都用同一条命令跑。

```sh
uv run scripts/base_table.py check --target main     # 核对表结构与 schema 一致，不一致退出码 1
uv run scripts/base_table.py build --target main     # 建/补正式底表结构，可重跑，不动数据行
uv run scripts/base_table.py build --target sample   # 重建样例表（假数据整页覆盖）
uv run scripts/base_table.py xlsx                    # 生成 templates/base-table-sample.xlsx
```

配置都放在两个仓库之外，后续的回流脚本也照这个约定读：

- 凭据：先看 `GOOGLE_APPLICATION_CREDENTIALS`，没有则用 `~/.config/de-linker-playbook/service-account.json`（权限 600）。
- 表格 ID：先看 `PLAYBOOK_CONFIG`，没有则用 `~/.config/de-linker-playbook/config.toml`（权限 600），格式如下：

```toml
[base_table]
spreadsheet_id = "..."         # 底表
sample_spreadsheet_id = "..."  # 底表（样例）
```

「下一步」脚本 [`scripts/next_step.py`](../scripts/next_step.py) 也复用这层读表，规则与用法见 [`docs/feedback-rules.md`](feedback-rules.md)。

询盘回流不用这把服务账号读网站。Woo 只读密钥的文件和 `config.toml` 指针见「询盘回流」，密钥本身不写进本页。

回流脚本复用 `base_table.py` 的读写层：`google_service`、`read_table`、`upsert_rows`（按不重复键新增或覆盖；内容没变的行不碰）、`replace_rows`、`refresh_progress`（按网址重挂登记编号，再重算动作进度）。写行一律写到固定行号，不用 `values.append`。所有接口调用都设了超时，遇到 429、5xx 或网络超时会自动重试。

## GSC 回流

[`scripts/gsc_pull.py`](../scripts/gsc_pull.py) 负责把 Search Console 的数据写进三张表：网页收录、网页表现、搜索词。写完这三张表后，它会重算一次动作进度。

```sh
uv run scripts/gsc_pull.py run                # 跑一次
uv run scripts/gsc_pull.py run --dry-run      # 只取数、打印条数，不写表
uv run scripts/gsc_pull.py run --recheck      # 今天的收录行也重查一遍（重建当天基线；平时按天跳过）
uv run scripts/gsc_pull.py schedule install   # 装/更新每日定时（这台 Mac 的 launchd，每天 08:30）。同一条任务先跑本脚本，再跑询盘回流，再跑邮箱回流，再导出看板 JSON，然后发每日提醒；必须先按「询盘回流」配好 Woo 只读密钥再重装。更新定时不会立刻跑，不要 kickstart，那会发出真的提醒
uv run scripts/gsc_pull.py schedule status    # 看装没装、上次退出码、日志最后几行
uv run scripts/gsc_pull.py schedule remove    # 卸掉定时
```

- **网页收录**：先查执行登记里的网址（含旧网址），再查站点地图里的网址。每个网址每天查一次；当天已经有那一行，就不再查。每天最多查 1900 个，官方上限是每站每天 2000 个。
- **网页表现、搜索词**：每次取最近 10 天的数据（按太平洋时间），取的时候带上还没定稿的数据。最近几天的数先写成「初步」，之后的运行会用「定稿」数覆盖同一行。Google 有几处不给拆分：
  - Discover 的数据不按设备拆，「设备」列写「不区分（Discover 不给设备）」。
  - Discover 和 Google 新闻不给搜索词，所以搜索词表里没有这两类。
- **耗时**：收录检查一个一个查，Google 每次要几秒才回。2026-10-14 首跑查 297 个网址，用了约 38 分钟。偶尔 Google 会回「内部错误」（500），脚本自动重试 5 次仍失败，就把这个网址记进日志，第二天再查。
- **日志**：定时运行时写到 `~/Library/Logs/de-linker-playbook/gsc-pull.log`。哪一步出了错，日志里会写明，退出码不为 0，`schedule status` 能看到。
- **断档**：Mac 睡眠时，launchd 会在唤醒后补跑；关机那天就跳过。搜索数据每次重取 10 天，所以断几天会自己补上。收录检查补不回来，那几天就没有行。
- **容量**：一本 Google 表格最多 1000 万个格子。网页收录每天大约 300 行 × 18 列，一年约 200 万格，是最大的一张。总量接近上限时，要把旧数据移到存档表里（见地图「Not yet specified」）。

`build` 每次都整页重写首页和各「说明」页。数据表只重写表头、格式、下拉、冻结行和列宽。若某张数据表已经有数据，而表头又与 schema 不同，`build --target main` 会停下来报错，不会覆盖；这种情况需要手动迁移。所有数据单元格都设为纯文本（数字列除外），日期和编号不会被表格自作主张改格式。

## 询盘回流

[`scripts/inquiry_pull.py`](../scripts/inquiry_pull.py) 把网站上的形式发票申请写进「询盘」表，写完后重算一次动作进度。它和 GSC 回流共用上面那条每日定时：08:30 先跑 GSC，再跑本脚本，再跑邮箱回流，再导出看板 JSON，然后发每日提醒。手动跑：

```sh
uv run scripts/inquiry_pull.py run                              # 对账并写表
uv run scripts/inquiry_pull.py run --dry-run                    # 只取数、打印条数，不写表
uv run scripts/inquiry_pull.py run --audit-order-attribution    # 只核对订单来源字段在不在，不写表
uv run scripts/inquiry_pull.py run --dry-run --audit-order-attribution
```

两个可选开关可以单独用，也可以一起用。`--audit-order-attribution` 只看订单来源字段在不在，不打印值。正式回流会写来源类型、设备类型、会话页数。UTM 没有活动值，不加列。浏览器标识不进表。归因登记编号仍然只在有证据时由人填，脚本不猜。


## 邮箱回流

[`scripts/mailbox_pull.py`](../scripts/mailbox_pull.py) 只读 `chester@de-linker.com` 的已发送和收件箱，回填执行登记的邮件查证，并把事件写进「邮件反馈」。写完后重算动作进度。它走上面同一条 08:30 定时，排在询盘回流之后、看板导出之前。手动跑：

```sh
uv run scripts/mailbox_pull.py run            # 对上已发送并写表
uv run scripts/mailbox_pull.py run --dry-run  # 只读、打印条数，不写表
uv run scripts/mailbox_pull.py selftest       # 不联网的规则自测
```

打开文件夹用 EXAMINE，取信用 BODY.PEEK，不改已读、不移动、不删除。日志只打条数、登记编号和未读数。正文、地址、主题不进表。每日提醒（主题以「de-linker 下一步」开头，或 Message-ID 域名是 `de-linker-playbook.local`）跳过。没有退信时写「未见退信（推断已送达）」，这是推断，不是投递回执。真人回复的分类在读取时判断，正文不保存。

专用密码不进仓库。`config.toml` 的 `[mailbox]` 只记主机、端口、账号和密码文件位置。密码文件权限 600。

## 本地看板

[`scripts/dashboard.py`](../scripts/dashboard.py) 在两条回流之后，把底表收成一份只读 JSON，再读一次网站订单，供本机页面点开查看。页面不直连 Google 表格。JSON 在仓外 `~/.config/de-linker-playbook/dashboard.json`，权限 600，不进仓库。

这是操作者自己看的页面。申请正文写在这份本地 JSON 里：公司、联系人、邮箱、电话、地址、客户备注、行项目、规格、项目和单据。底表仍只留最小列，这些字段不写回表格。密钥、表格 ID、IP、浏览器标识和支付凭证不进 JSON，也不进日志。

```sh
uv run scripts/dashboard.py export       # 读底表和订单正文，更新本地 JSON，不写表、不发信
uv run scripts/dashboard.py open         # 打开旧版页面，命令保留
ops-dashboard                            # 任何目录都能开新版。桌面「运营看板」双击的是同一条
uv run scripts/dashboard.py self-check   # 不连网，核对计数和正文投影
```

新版是 React + Vite，样子按 Preline 看板，图表用 ApexCharts。应用在 `apps/ops-dashboard`。`ops-dashboard` 优先用 8766，被占用就用下一个空端口，并自己打开浏览器。关掉那个终端窗口，页面就停。不登录自启。

点开一行看全文。网页表现或搜索词是 0 行时，趋势页是空状态，不是假图。每天 08:30 的定时任务会在邮箱回流之后调用 `export`，然后才发每日提醒。改定时用上面的 `schedule install`，不要 kickstart。

导出时另读 GA4 近 7 天汇总，只写进这份本地 JSON，不写底表。反馈规则没有用到站内行为，所以 AI「下一步」不读这些数。只含同意分析的访客，没有建模补齐，不能和 GSC 点击对账。媒体资源编号在仓外 `config.toml` 的 `[ga4]`，不进仓库。

### 操作者清单：建一把 Woo 只读密钥

密钥由操作者在站点后台建，放在两个仓库之外。本页不写后台地址、账号或密钥内容。

1. 登录站点后台。
2. 打开 **WooCommerce → Settings → Advanced → REST API**。
3. 添加一把密钥。用户绑到 `shop_manager`，或另一个具有 `read_private_shop_orders` 能力的后台用户。
4. 权限只选 **Read**。不要选 Write 或 Read/Write。这把密钥不能改订单。
5. 生成后页面只显示一次。用文本编辑把 Consumer Key、Consumer Secret 各存成一行，分别覆盖写入下面两个文件。不要贴进仓库、对话、日志或截图。
6. 脚本用 HTTPS Basic 认证，密钥只进 Authorization 头；不要把 Consumer Key / Secret 放进 URL 或查询参数。
7. 把两个文件的权限设为 600：

```sh
chmod 600 ~/.config/de-linker-playbook/woo-consumer-key ~/.config/de-linker-playbook/woo-consumer-secret
```

把下面这段**追加**到现有的 `~/.config/de-linker-playbook/config.toml`，保留原有的 `[base_table]`、`[reminder]` 等段落；本文件只放指针，不放密钥本身：

```toml
[woocommerce]
consumer_key_file = "~/.config/de-linker-playbook/woo-consumer-key"
consumer_secret_file = "~/.config/de-linker-playbook/woo-consumer-secret"
```

### 写进表的规则

- **全量状态对账**：每次按四个计入状态把线上询盘和表对一遍，不是只追加新单。四个状态是 `inquiry-received`（询盘已收到）、`proforma-issued`（形式发票已开）、`completed`（已完成）、`cancelled`（已取消）。新单追加一行；单号、公司、创建时刻、状态、签发时刻任一脚本字段变了，都按「询盘内部编号」改原行，不另起一行。重跑不重复。还没发出去的 `pending`（后台显示 Not sent），以及其他状态，不进表；已经进表后又离开四个状态的行要删除，让表和线上口径一致。
- **AI 列保留**：回流先从旧行合并「归因登记编号」「归因依据」「备注」，再整行更新脚本列（询盘内部编号、单号、公司、创建时刻、状态、形式发票签发时刻、写入时刻）。这三列若已有内容，原样留下，不覆盖、不清空。没有证据不要填归因。
- **隐私丢弃**：读到的响应只留内部编号、单号、账单公司名、创建时刻、状态、签发时刻。姓名、邮箱、电话、地址、IP、浏览器标识、询盘备注在内存里丢掉，不进表、不进日志、不落盘。
- **L3 只含形式发票申请**：联系表单和直接发到邮箱的询盘现在读不到，表里没有它们。看板和每日提醒里的询盘数因此偏低。未归因的询盘仍计入北极星，但不计入任何一次动作的成效。

## 翻译对照

Google 接口给的英文原值（coverageState、robotsTxtState、indexingState、pageFetchState、搜索类型、设备、国家代码）怎么翻成表里的中文，写在 schema 对应列的 `x-map` 里，收录状态的含义与所属结论写在 `x-states` 里。回流脚本用 `scripts/base_table.py` 的 `translate_inspection`、`compare_with_previous`、`translate_search_row` 照这些对照翻译。国家对照覆盖 ISO 3166 的全部 249 个三字母代码：中文名取自 ISO 3166 的简体中文译名，其中韩国、朝鲜和港澳台改用常用叫法；Google 判断不出国家时给的 `zzz`，表里写「未知」。对照表里英文的确切写法以首次真实调用为准，对不上的落到「不在对照表里（看英文原文）」。
