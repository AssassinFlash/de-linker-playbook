---
wayfinder: task
status: closed
assignee: chesterjohn+agent
resolved: 2026-10-06
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

## Resolution（2026-10-06）

**已迁入**（子代理执行，主模型 review 通过）：

- `schemas/` ← v3 `schemas/` 6 个 JSON，原样复制（内容本就别无绝对路径/产品词）。
- `templates/` ← v3 `data/templates/` **28** 个 xlsx（票面写 29，实际 28 个 xlsx + 1 个 README）+ 改写后的 `README.md`（`{{VAULT}}/<phase>/` → `deliverables/marketing|lead/<phase>/` 小写；excel_writer.py 引用改为「原为脚本生成，现静态维护」）。
- `evals/` ← v3 `scripts/eval/` 9 个 py（扁平）。校验规则对齐抽取规格：frontmatter 只允许 name+description、禁字段翻转为报错、name 须 `^(marketing|lead)-`、description 300–700；整段删除 agent.md / dependency-graph / slash 入口 / per-skill evals.json 检查；`track_history` 落 `deliverables/marketing/00-system/eval-history`；`run_eval` 报告落同树 `eval-reports/`；新增 `.agents/skills` 软链检查（WARN 不挡 exit）。本机 Python 3.9 兼容已处理。
- `docs/` ← `getting-started.md`、`legacy-command-migration.md`，全篇改写：slash 入口 → 打开 `skills/<name>/SKILL.md`；产品档案 → 台账 `product_context`（默认 `~/Documents/New/CONTEXT.md`）；产出根 → `deliverables/` 双树。
- `templates/scripts/` ← lead `scripts/export/to_excel.py` + `to_obsidian.py`。关键判断：这两个脚本在源仓库根 `scripts/` 下、不在任何 skill 目录里，lead 抽取票的白名单覆盖不到，不本轮迁就会丢；落 `templates/scripts/` 与其填充的 Excel 模板配对。`write_vault_markdown` 改名 `write_deliverable_markdown`，归档探测改 `deliverables/lead/` 小写阶段目录，正文无 Obsidian 字样。

**评估后不迁**（结论即决策，不进 backlog）：

- `update_commands.py`（改写 `.claude/commands`，harness 专属）；`generate_eval_templates.py`（生成 per-skill evals.json，与「夹具集中 evals/ 另做」冲突）。
- `docs/codex-adaptation.md`（Codex 不在兼容五家）；`docs/agent-authoring.md`（`.claude/agents` 接线文档，其通用质量红线已进抽取规格）；`docs/audit/`、`docs/superpowers/`（不锈钢整改史）。
- v3 根 `templates/agent|skill`（旧格式编写模板）；`scripts/build_excel.py` + `scripts/common/excel_writer.py`（1145 行，规格 §7 终稿布局无根级 scripts/ 容身之处，28 个模板已是静态产物）。
- `evals.json`（规格已定）、`data/working-drafts/`、`data/eval-reports/`、根目录 9 个产品 xlsx（不锈钢工作数据）。

**验证**：禁词/绝对路径扫描（schemas/templates/evals/docs）零命中；`py_compile` 全过；`evals/validate_project.py` 实跑 exit 0（WARN 全是 lead 抽取并行窗口的未收口项，非本票产物）；`quick_validate.py skills/marketing-orchestrator` PASS；28 xlsx 与源 diff 仅多 `scripts/` 目录。

**后续票注意**：lead skill 若引用导出脚本，函数名已是 `write_deliverable_markdown`（旧名 `write_vault_markdown` 不再存在）；填写 xlsx 依赖本机装 openpyxl（缺库时脚本可 import、调用才报错）。
