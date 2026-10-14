---
wayfinder: research
status: open
assignee: grok-build (dispatched 2026-10-14)
grok_session: a557532d-2be0-428a-a884-8a6c4ea8f1e7
step: 2
blocked_by: []
---

# 询盘数据从哪读

## Question

（派 Grok Build）`CONTEXT.md`「询盘」= 任一入口进来的买家联系（形式发票申请、联系表单、直接来信），不去重。每个入口的数据**存在哪、能怎么只读地取、取得到哪些字段**？

须查清（证据 = 新站仓库文件路径 + 官方文档 URL + 线上只读核查）：

1. 形式发票申请：Woo 订单状态 `wc-inquiry-received` / `wc-proforma-issued` / 完成 / 取消；创建时刻、签发时刻 meta（`_linker_proforma_issued`，见新站 `docs/specs/74-daily-digest.md`、`11-commerce.md`）。
2. `/kontakt/` 联系表单：提交是否落库（哪张表 / 哪个 post type），还是只发邮件到 `团队邮箱`。
3. 直接来信到 `团队邮箱`（sales@）：按约定不读该邮箱——确认是否有其他只读可得的计数来源；没有就写「不可得，按没有处理」。
4. 读取路径比较：Woo REST API（只读密钥，权限范围、自定义状态是否可查）、新站 `just pull` 伪名化快照（`docs/specs/6-live-pull.md`：多新、多久一次、字段是否被伪名化掉）、WP-CLI 经 ssh。每条写可行性、频率、需要谁做什么（站点侧改动归 agent 在新站仓库做）。
5. 个人数据：哪些字段属个人数据；写进 `所有者账号` 私有 Google 表格的最小集合建议（单号、公司、日期、状态？），并给出依据。

产出：`wayfinder/closed-loop/research/l3-inquiry-source.md`，每条事实带来源。不写「问老板」，查不到标〔未证实〕。

## 完成标准

- 五问各有结论 + 来源；推荐一条主读取路径并说明理由。主模型抽查至少两条（一条仓内路径、一条官方文档），写进 Resolution，并向用户汇报。
