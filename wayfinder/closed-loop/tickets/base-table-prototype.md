---
wayfinder: prototype
status: open
assignee: claude-opus-5-5 会话 2026-10-14
step: 1
blocked_by: []
---

# 底表原型

## Question

底表（Google 表格）长什么样，操作者看得懂、脚本写得进、Looker Studio 接得上、AI 读得出下一步？做一个粗糙但具体的原型给操作者看，按反应改到定稿。

要定的：

- 分几张工作表：至少执行登记（L0，两线共用）、网页反馈（GSC：收录状态、展示、点击，按页 × 日期）、询盘（L3）、邮件反馈（送达 / 回复）、说明页。是否需要一张「动作 ↔ 反馈」对照表。
- 每列：中文列名、含义、来源（操作者口述 / 脚本 / AI）、谁写、取值示例、空值含义。长表（一行一条观测）便于 Looker Studio；给初学者另配一张「怎么读这张表」说明。
- 归因锚：执行登记的编号如何与 URL、邮件 Message-ID、询盘单号挂钩。
- 隐私：底表在 `所有者账号` 的私有表格里，但只放判断所需的最少个人数据。询盘已由调研定最小集合（见下）；回信由本票定（建议同口径：Message-ID、公司名、日期、分类，不放正文与私人邮箱）。
- 数据可得性以已有调研为准（`wayfinder/feasibility/research/google-channel-access.md`、`mailbox-readonly-access.md`、`feedback-ladder-practice.md`）；询盘字段以「询盘数据从哪读」为准（已关）：询盘表最小列 = 内部 id、单号、公司名、创建时刻（UTC）、状态（询盘已收到 / 形式发票已开 / 已完成 / 已取消）、签发时刻（可空）；不放姓名、邮箱、电话、地址；联系表单与直接来信不可得，不设行。详见 `wayfinder/closed-loop/research/l3-inquiry-source.md` 第 5 节。

原型形态：仓内 `templates/` 下的 xlsx 或 CSV 样例（含几行假数据，标「样例」）+ 列定义写进 `schemas/`（公开，无真实数据）。HITL：操作者看原型，回答「看得懂吗、哪列不明白、想在看板上看到什么」，不问行业判断。

## 完成标准

- 操作者确认原型看得懂；列定义定稿在 `schemas/`；样例在 `templates/`。

## 交接

- 定稿的表结构写进「建底表」「执行登记流程」「反馈分级规则定稿」三票正文（文件路径即可）。
