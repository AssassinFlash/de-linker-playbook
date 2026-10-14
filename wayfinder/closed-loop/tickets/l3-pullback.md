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

## 完成标准

- 底表询盘表与线上实际一致（抽一段日期，脚本结果 = 后台 / 每日摘要所见数量）；重跑不重复；看板 L3 版面有数。
