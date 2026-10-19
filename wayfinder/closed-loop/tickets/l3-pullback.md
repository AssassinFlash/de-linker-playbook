---
wayfinder: task
status: open
assignee:
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
