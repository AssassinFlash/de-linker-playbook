---
wayfinder: task
status: closed
assignee: chesterjohn+agent
blocked_by: [extraction-spec, repo-skeleton]
resolved: 2026-10-06
---

# 43 个 lead skill 抽取改写

## Question

从 `~/Documents/lead-generation_副本/skills/`（canonical，43 个；`.kimi/`、`.codex/` 是适配层不抽）按抽取规格迁入本仓库 `skills/`，裸名统一加 `lead-` 前缀（如 `icp-analysis` → `lead-icp-analysis`）。

执行方式：子代理 swarm，每 skill 一个子代理；按主题分批出 review checkpoint（研究管线/触达邮件/LinkedIn/SEO/售后/meta）。

注意：方法论源自用户自购付费 prompt——自用，不分发；跳过 `config.md`、`product-context.md`、`icp-*.json/xlsx`、`scripts/cookies.txt`、`downloads/` 等一切产品与机器数据。

## Resolution

2026-10-06 完成。5 批子代理 swarm（meta 5 → 研究管线 10 → 触达邮件 7 → LinkedIn 11 → SEO 4 + 售后 6），每批主模型 checkpoint，43/43 全量验收绿。

- **产出**：`skills/lead-*/` 43 个（裸名 39 个加 `lead-` 前缀；`lead-generation` / `lead-interview` / `lead-magnet-gen` / `lead-teach` 保持原名未双重前缀）；`.agents/skills/lead-*` 软链 43 条；`deliverables/lead/` 12 个阶段目录（00-system…99-archive）。黑名（AGENTS.md、evals.json、config.md、product-context.md、icp-*、cookies、downloads）零迁入。
- **不止机械抽取（用户追加要求）**：每个 skill 过了编辑性 review——普遍修正了角色扮演剧本化、五层工具链（收敛为「网页搜索 + 抓取 URL」一条能力一个逃逸）、不可执行硬配额（凑数会逼编造，改为目标+缺口）、内部矛盾（硬依赖口径、步骤数打架）、过时事实（ISO/TS 16949→IATF 16949、写死的 2024/2025 年份、Google My Business 更名、Unbounce 分数线）等。
- **主模型当轮清账三处**：①`lead-product-knowledge` 产出落点从 `10-sales/` 改回编排登记的 `05-usp/product-knowledge.md`；②`lead-generation/references/dependency-graph.md` 审查清单补「配额口径」段（至少 N 行=目标，缺口记 CONCERN，凑数编造直接 FAIL）；③`search-protocol.md` 最低查证次数改目标制+缺口，与方法 skill 的「不空搜凑数」对齐。
- **验收**：规格第 8 节 1–10 条对 43 个 lead skill 全部通过（name 正则/目录一致、description 300–700、无禁用 frontmatter、无工具 ID、无禁词、例子标注齐、<500 行、软链齐、无 `{{VAULT}}`）；references >100 行均有目录。冒烟 S1–S5 归 `acceptance-review-and-smoke` 票。
- **遗留（不阻塞关票）**：与 marketing 重叠对未合并（归 overlap-dedup-adjudication 票）；营销树 `deliverables/marketing/` 归并行窗口的营销抽取票。

资产已就位（assets-migration 票，2026-10-06）：源仓库根 `scripts/export/` 的两个导出脚本已迁到本仓库 `templates/scripts/`（它们不在任何 skill 目录下，本票白名单覆盖不到）。函数已改名 `write_vault_markdown` → `write_deliverable_markdown`，归档逻辑走 `deliverables/lead/` 小写阶段目录；源 skill 若引用旧路径 `scripts/export/` 或旧函数名，按此改写。
