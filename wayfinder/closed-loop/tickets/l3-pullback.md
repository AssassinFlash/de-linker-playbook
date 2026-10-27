---
wayfinder: task
status: closed
resolved: 2026-10-20
assignee: Codex 会话 2026-10-20（本会话）
step: 2
blocked_by: [l3-inquiry-source, base-table-build, looker-dashboard]
---

# 询盘回流 L3

## Question

（AFK；需要站点侧改动或建只读密钥时含 HITL / 新站仓库工作）按「询盘数据从哪读」推荐的路径，仓内脚本把询盘写进底表询盘表（北极星），并补上看板的 L3 版面。

- 只写「底表原型」定下的最小字段；个人数据不进公开仓库，不进 vault 以外的任何地方。
- 若需站点侧改动（如只读端点、联系表单落库），在新站仓库按其 `AGENTS.md` 规矩另开票做，本票记链接。
- 若需 Woo 只读密钥：操作者在 WP 后台建（给清单），密钥放仓库外。
- 与 GSC 回流共用定时与脚本层（见「建底表」「GSC 数据回流」的交接）。
- 看板：按「Looker Studio 看板」交接的方法补 L3 版面，并更新 `docs/` 里的指南。

## 调研交接（「询盘数据从哪读」关票时写入）

- 依据：`wayfinder/closed-loop/research/l3-inquiry-source.md`。
- 路径：Woo REST `GET https://de-linker.com/wp-json/wc/v3/orders`，`status=inquiry-received,proforma-issued,completed,cancelled`，`include_meta=_linker_proforma_issued`，`per_page=100` 翻页，可用 `after` / `modified_after` 增量。不走 `just pull`（公司名被抹）、不走 WP-CLI（加载插件会写 cron）、不写 SQL。
- 操作者清单：WP 后台 WooCommerce → Settings → Advanced → REST API 建一把 **Read** 密钥，绑到有 `read_private_shop_orders` 能力的后台用户（如 shop_manager 角色）；Consumer Key / Secret 放两个仓库之外，vault 只记位置。HTTPS Basic 认证。
- 写表只留：内部 id（`id`）、单号（`number`）、公司（仅 `billing.company`）、创建时刻（`date_created_gmt`）、状态、签发秒（`_linker_proforma_issued`，无则空）。响应里的姓名、邮箱、电话、地址、IP、UA、备注在**内存中丢弃**，不落盘、不进日志。
- 首次真实调用时核实调研留下的〔未证实〕：返回体里自定义状态确实被滤出；`_linker_proforma_issued` 在 `meta_data` 里；`number` 是否等于 `id`。另：调研按 Woo 11.1.2 源码推断（readme 的 Stable tag），但线上脚本版本号与 changelog 首条是 11.2.0（2026-10-14 主模型核查），过滤行为以真实响应为准。结果写进本票 Resolution。
- **顺带核实订单来源（Order Attribution）**：线上首页已加载 `sourcebuster.min.js` 与 `order-attribution.min.js`。首次真实调用时看询盘订单的 `meta_data` 里有没有订单来源字段（来源类型、UTM、设备类型、会话页数；字段名以真实响应为准），以及自建的形式发票申请页提交的订单是否带上它们。只核实、记进 Resolution，不在本票写进底表（不进底表的个人数据边界不变：user agent 一类不要）；是否加列由地图「询盘归因到动作」那片 fog 毕业成票后再定。
- 联系表单与直接来信**不可计**：看板与指南写明「L3 只含形式发票申请」，北极星因此偏低。

## 底表交接（「建底表」关票时写入，2026-10-14）

- 表结构正典 `schemas/base-table.schema.json`（列顺序、中文表头、下拉选项、翻译对照都在里面）；人读说明 `docs/base-table.md`。要改列先改 schema，再 `uv run scripts/base_table.py build --target main`，然后 `check --target main`。
- 脚本层：`scripts/base_table.py`，用 `uv run` 跑，依赖写在文件头（PEP 723）。新脚本放 `scripts/`，用同样的写法；也可以把函数加进这个文件。
- 配置：凭据读 `GOOGLE_APPLICATION_CREDENTIALS`，否则读 `~/.config/de-linker-playbook/service-account.json`。表格 ID 读 `PLAYBOOK_CONFIG`，否则读 `~/.config/de-linker-playbook/config.toml` 的 `[base_table] spreadsheet_id`。直接复用脚本里的 `load_target("main")` 和 `sheets_service()`。
- 目前脚本只会建表和核对，**还不会追加或更新数据行**；写行的函数由第一张需要它的票补上。正式表的写入要按每张表的不重复键去重，键见 `docs/base-table.md`「表结构」。
- 时刻列一律北京时间，格式「年-月-日 时:分」；网页表现、搜索词两张表的日期按太平洋时间。数据单元格都是纯文本格式，数字列除外。
- 「动作进度」每次回流后用 `action_progress` 整表重算。
- 本票相关：询盘表的列见 schema `$defs.询盘`。和调研不同的一点：时刻改成北京时间，表头是「创建时刻（北京时间）」「形式发票签发时刻（北京时间）」。`date_created_gmt` 和 `_linker_proforma_issued` 秒数都要换算成北京时间。「归因登记编号」「归因依据」只在有证据时填，没有就留空。
- 键是询盘内部编号。状态变了就原地更新那一行，不追加新行。


## 看板交接（「Looker Studio 看板」关票时写入，2026-10-19）

- 正式报表链接在私有 vault `marketing/00-system/looker-dashboard.md`；报表已接 `底表 - 询盘` 数据源，页 1 有形式发票询盘总数 scorecard，页 2 有 L3 版面留位。
- 询盘回流完成后，直接在正式报表扩展 L3 留位：按询盘内部编号、状态、创建时刻、签发时刻展示明细与趋势；仍注明“L3 只含形式发票申请，联系表单与直接来信不可计”。不新建对照报表。

## 完成标准

- 底表询盘表与线上实际一致（抽一段日期，脚本结果 = 后台 / 每日摘要所见数量）；重跑不重复；看板 L3 版面有数。

## Resolution（2026-10-20）

关票。对照的是后台订单列表的同一条只读路径，不是一封摘要邮件。摘要邮件不在手。每日摘要的口径另按新站 `docs/specs/74-daily-digest.md` 用同一批订单算了一遍，写在下面，不拿它冒充创建日计数。

**全量。** `uv run scripts/inquiry_pull.py run` 取到 58 笔：询盘已收到 5，形式发票已开 0，已完成 0，已取消 53。Woo 响应头 `X-WP-Total` 在同样四个状态上是 58，四个状态分开查也是 5、0、0、53。底表询盘表 58 行，内部编号 58 个互不重复。内部编号范围与脚本日志相同：`1066…7463`。

**抽日期。** 窗口是创建时刻 UTC `2026-07-03T00:00:00` 含、到 `2026-08-02T00:00:00` 不含，也就是 UTC 日历日 2026-07-03 至 2026-08-01。脚本投影 20，同一窗口的 Woo `after` / `before` 响应头 20，底表里对应的北京时间 `2026-07-03 08:00` 至 `2026-08-02 08:00` 也是 20。邻日 UTC 2026-07-02 两边都是 0。

**重跑不重复。** 16:08 与 16:10 各写一次正式底表。两次都是新增 0、覆盖 0、移除 0，动作进度各重算 71 行。没有发信，没有补假行。

**自定义状态确实被滤出。** 不带状态的默认列表是 63。四个计入状态是 58。多出来的 5 笔是 `on-hold`，不在询盘四态里，脚本没有写入。`checkout-draft` 另有 2 笔，不在默认列表里，也不在四态里。只查 `inquiry-received` 得到 5，不是 63。返回的 58 笔里只有询盘已收到和已取消。

**签发 meta。** 审计模式不传 `include_meta`，58 笔的 `meta_data` 里都没有 `_linker_proforma_issued`（0/58）。当前没有形式发票已开的订单，所以这个键无处可出现。不是没读到。

**单号。** 58 笔的 `number` 都等于 `id`，不同的是 0。

**订单来源。** 只记字段名和存在笔数，没有记值，也没有加列。58 笔里：`_wc_order_attribution_source_type` 35，`_wc_order_attribution_utm_source` 30，`_wc_order_attribution_device_type` 30，`_wc_order_attribution_session_count` 30，`_wc_order_attribution_session_entry` 30，`_wc_order_attribution_session_pages` 30，`_wc_order_attribution_session_start_time` 30，`_wc_order_attribution_user_agent` 30。没有 referrer，也没有 `utm_medium`、`utm_campaign`、`utm_content`、`utm_term`。浏览器标识字段不进底表、不进日志、不进看板 JSON。要不要加列，交给「询盘归因到动作」，不在本票做。

**入口标记。** `created_via` 不是归因列。58 笔里 checkout 29、dlk-quote 23、linker_contact 4、store-api 2。linker_contact 的 4 笔已经在四个计入状态里，没有从询盘表剔除。

**每日摘要口径。** 计算时刻 2026-10-20 16:05:52 +08。未处理询盘按「创建早于该时刻 86400 秒，且仍为询盘已收到」是 4。五笔里有一笔还没满 24 小时，所以不是 5。形式发票已开是 0，PI 未响应是 0，缺签发 meta 的也是 0。这不是按创建日计数，也不能代替上面的 20 与 58。当天摘要已于 2026-10-20 07:00:07 UTC 发出，主题 `Daily digest, October 20, 2026`。日志没有正文。用同一套代码、把时刻定在发送瞬间重算：未处理询盘 4，PI 未响应 0，与上面的口径一致。

**看板。** 操作者 2026-10-20 已把看板路径改到自建页，Looker 没有改。回流后导出的本地 JSON：L0 71、L1 28、L2 0、L3 0，申请 58，已签发 0，已归因 0，四态与底表一致，正文读取无错误。L3 是 0，因为没有询盘归因到动作；申请 58 是另一件事。总览和询盘页都写了「L3 只含形式发票申请，联系表单和直接来信不可计。」新构建由 `http://127.0.0.1:8767/` 提供。8766 仍是旧页。
