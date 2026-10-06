---
wayfinder: task
status: closed
assignee: kimi（2026-10-06 认领）
resolved: 2026-10-06
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

## Resolution

2026-10-06 六条全部落实；验收：`evals/quick_validate.py` 全量 81/81 全绿，`evals/validate_project.py` 退出码 0。

1. **marketing 交付树补建**：`deliverables/marketing/` 按规格 §7 建 9 目录（00-system、00-research、01-foundation、02-seo、03-content、04-acquisition、05-cro、06-growth、07-measurement），各带空 `.gitkeep`，对齐 lead 树形态。
2. **copywriting 路径对齐**：以方法 skill 正典为准，统一为 `deliverables/marketing/03-content/copywriting/`（`copy-library.xlsx` 在该子目录内）；改了 `marketing-orchestrator/references/dependency-graph.md` 两处（登记行 + JSON 块）与 `marketing-content/SKILL.md` 两处（步骤 4、产出对照表），全仓无 `website-copy` 残留。顺带修同类缺陷：`marketing-content` 步骤 5 的 `visual-style-guide.xlsx`「同上目录」有歧义，改为「在 `03-content/` 根」，与 `marketing-visual-content` 正典及对照表一致。
3. **入口文档刷新为真实 playbook**：`AGENTS.md` 台账节扩为双线（营销/内容/「下一步」→ marketing-orchestrator；获客线索类 → lead-generation），Skill 节删试点行、四目录改现状描述；`README.md` 目录注释与「当前状态」更新为 81 skill 已迁入、机械校验全绿；`state/status.md` 从试点 phase 0–2 换成 orchestrator 真实 0–7 阶段表，`method_skill: marketing-profile`、`output_dir: deliverables/marketing/`。冷启动进真实流水线。
4. **【决议】evals 的 17 个 schema 映射缺口 = 补映射，不降级 WARN**。理由：该检查在规格里就是 ERROR 级契约完备闸（"Promised JSON deliverables in skills/ have schema mappings"），已有 12 条映射先例且多数指 `rowset-deliverable.schema.json`；降级 WARN 会永久放空闸门，违背「承诺的 JSON 交付物必有 schema 契约」的规格意图。执行：12 个缺口 JSON（ai-visibility-report、analytics-and-optimization、cro-experiment-queue、funnel-redesign、paid-advertising(-blueprint)、prospect-research、referral-program-design、retention-strategy、seo-audit-data、sequence-builder、social-calendar）全部映射到 `rowset-deliverable.schema.json`——它们都是 xlsx 不能写时的同结构 JSON 替代、行级带 source/evidence。另修一处误报：正文引用 `*.schema.json`（如「符合 schemas/site-schema-blueprint.schema.json」）是对 schema 文件本身的引用，不是交付物，匹配时跳过。修后退出码 0。
5. **`to_obsidian.py` → `to_markdown.py`**：`git mv` 完成；全仓（除 wayfinder/ 历史票正文）无旧名与 Obsidian 残留。
6. **search-protocol.md 补「内容生成」行**：最低查证表新增「内容生成（冷邮件等 outreach 文案）：目标 3 次网页搜索，冷邮件 best practices / 主题行写法 / 行业模板各至少 1 次，模板原文禁入交付物」；查询模板新增「内容生成 / 冷邮件」小节（源 cold-email-gen 的 Mandatory Search Steps 去不锈钢化后落此）。

执行分工：4 个子代理并行（目录树+脚本改名 / 路径对齐 / evals 映射 / 入口文档+搜索协议），主模型只做组织、diff review 与验收。`examples-from-new` 票由另一窗口并行执行，本票未触碰其文件。
