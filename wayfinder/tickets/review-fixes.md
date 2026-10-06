---
wayfinder: task
status: open
assignee:
blocked_by: []
---

# 抽取复核修复清单

## Question

主模型组织三路子代理复核（机械合规 81/81 全绿；保真抽查 8 个：6 faithful + 2 minor-loss；卫生检查发现漏项）。以下问题当轮修复（当轮清账原则，不进 backlog）：

1. **【高】补建 `deliverables/marketing/` 树**：按规格 §7 建全目录（00-system、00-research、01-foundation … 07-measurement）并放 `.gitkeep`。lead 树已建，marketing 树被漏建（lead 票在 Resolution 里把它派给了 marketing 票，marketing 票的提交里没有它）；40 个 SKILL.md 已引用这棵树
2. **【高】copywriting 路径对齐**：`marketing-copywriting` 写 `deliverables/marketing/03-content/copywriting/`，但 orchestrator 的 `references/dependency-graph.md` 登记的是 `website-copy/` 且 `copy-library.xlsx` 在 03-content/ 根——以规格 §7 的交付物结构为准，把两边对齐成一致
3. **【中】入口文档刷新为真实 playbook**：`AGENTS.md`、`README.md`、`state/status.md` 仍是试点版（2 skill、phase 0-2、`output_dir: deliverables/`）——更新为 81 skill + 双交付物树 + orchestrator 0–7 阶段的形态，冷启动应进入真实流水线而不是试点薄片
4. **【中】`evals/validate_project.py` 的 17 个 JSON schema 映射缺口**：skills 引用了若干交付物 `*.json`，evals/ 无对应 schema 映射导致退出码 1——补齐映射/schema，或按规格意图把该检查降级为 WARN（二选一，决议写进 Resolution）
5. **【低】`templates/scripts/to_obsidian.py` 改名**：正文已去 Obsidian 化，文件名残留（改 `to_markdown.py`，同步改引用）
6. **【低】`lead-generation/references/search-protocol.md` 补「内容生成」行**：lead-cold-email-gen 的必备调研步（best practices / 主题行 / 行业模板查证）抽取后无家可归，补回去

另有一项较大工程单独立票「例子 New 化」（examples-from-new），**不阻塞本票与后续票**，可并行。

完成标准：六条逐项落实；`evals/quick_validate.py` 保持 81/81 全绿；`validate_project.py` 退出码 0（或按第 4 条决议降级）；关票、地图记账、git 提交。
