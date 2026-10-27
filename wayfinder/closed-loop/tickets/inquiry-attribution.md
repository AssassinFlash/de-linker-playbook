---
wayfinder: task
status: closed
resolved: 2026-10-20
assignee: Codex 会话 2026-10-20（本会话）
step: 6
blocked_by: []
---

# 询盘归因到动作

## Question

一条询盘能不能接回某一次执行登记。订单来源字段已经能从 Woo REST 读到，事实在「询盘回流 L3」的 Resolution，不要再为了确认字段在不在而重拉一遍正文。

本票决定：要不要把来源类型、UTM、设备类型、会话页数加进底表询盘表，并在有证据时填写「归因登记编号」。

已核实：

- 58 笔四态订单里，`_wc_order_attribution_source_type` 35 笔，`_wc_order_attribution_utm_source` 30 笔。设备类型、会话页数、会话次数、会话入口、会话开始时刻各 30 笔。
- 没有 referrer。没有 `utm_medium`、`utm_campaign`、`utm_content`、`utm_term`。
- `_wc_order_attribution_user_agent` 有 30 笔。这个字段不进底表、不进日志、不进看板 JSON。
- `created_via` 只是入口标记，不是归因：checkout 29、dlk-quote 23、linker_contact 4、store-api 2。linker_contact 的 4 笔已在四个计入状态里，不要从询盘表剔除。
- 横幅上线后只记同意了的访客。这条限制还在。

若决定不加列，关票并写明原因。若决定加列，先改 schema，再 `uv run scripts/base_table.py build --target main`，再让回流写下新列。没有证据不要填归因登记编号。

## 完成标准

- 加或不加已写进 Resolution，地图只留一行指针。
- 若加列：正式底表有新列，重跑询盘回流不重复，浏览器标识仍然不落盘。


## Resolution（2026-10-20）

加三列，不填归因编号。

58 笔里，来源类型是直接访问 30、后台创建 5、没有记录 23。设备类型是桌面 30、没有记录 28。会话页数有记录 30。`utm_source` 只有 `(direct)`，没有 `utm_medium`、`utm_campaign`、`utm_content`、`utm_term`，也没有 referrer。会话入口是账户、结账、首页、申请页这些通用路径，对不上某一次执行登记。所以 UTM 不加列，「归因登记编号」保持空，不猜。

正式底表已有「来源类型」「设备类型」「会话页数」。回流覆盖 35 行，新增 0。再跑一次是新增 0、覆盖 0、移除 0。浏览器标识没有落盘。归因到动作的询盘仍是 0。
