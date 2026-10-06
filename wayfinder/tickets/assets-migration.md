---
wayfinder: task
status: open
assignee:
blocked_by: [extraction-spec, repo-skeleton]
---

# schemas / templates / eval / docs 迁入

## Question

从 `~/Documents/marketing-playbook-v3` 迁入方法资产：

- `schemas/`（交付物 JSON schema）→ 本仓库 `schemas/`
- `data/templates/`（29 个 Excel 模板）→ 本仓库 `templates/`
- `scripts/eval/`（校验脚本）→ 本仓库 `evals/`
- `docs/` 选篇（v2→v3 迁移、agent 编写指南等仍有价值的）→ 本仓库 `docs/`

规则：绝对路径一律改相对；`data/working-drafts/`、`data/eval-reports/`、根目录产品 xlsx 不迁（那是不锈钢线的工作数据）。lead-gen 侧如有同类通用资产（`scripts/export/` 的 Excel/Obsidian 导出）一并评估迁入。
