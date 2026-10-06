---
wayfinder: prototype
status: closed
assignee: chesterjohn+agent
blocked_by: [skill-conventions-research, orchestration-workflow-form]
resolved: 2026-10-06
---

# 抽取规格定稿

## Question

把已定方向落成一份可执行的抽取规格，子代理照单干活、主模型照单验收。规格须覆盖：

- **SKILL.md 正典格式**：frontmatter 字段集、正文结构、长度上限——吸收研究票结论
- **去不锈钢化规则**：产品词扫描清单（不锈钢/屏风/Alibaba/Shopify/Foshan/PVD……）、通用化改写规范
- **例子标注格式**：固定的「仅供理解，禁止引用到输出」标注表述与放置位置
- **工具能力化对照表**：`mcp__tavily__*` 等 → 能力描述的具体映射写法
- **命名规则**：`marketing-*` 保持；lead-gen 裸名统一加 `lead-` 前缀
- **上下文指路策略**：Linker 产品事实一律指路 `~/Documents/New`，不复制
- **目录布局终稿**：skills/、schemas/、templates/、evals/、docs/、wayfinder/ 各自的收纳规则，**以及营销/获客交付物的 `deliverables/` 结构**（lead-gen 产出不再写外部 vault，须定义本仓库内的对应目录）
- **验收清单**：对照 review 的逐条检查项 + 冒烟方式（喂给验收票）

形态：子代理起草规格文档（prototype），主模型 review，用户定稿。

## Resolution

2026-10-06 用户定稿：规格全文在 [`wayfinder/extraction-spec.md`](../extraction-spec.md)（394 行，8 节 + 编排系改写方向 §0 + lead-gen 43 个命名映射附录 A）。起草由子代理完成（含两源 canonical 实测扫描），主模型 review 修 4 处一致性后用户拍板。

定稿要点：

- **命名**：v3 无前缀 23 个一律加 `marketing-`；`product-profile` → `marketing-product-profile`、`skill-eval` → `marketing-skill-eval`；验收正则一刀切 `^(marketing|lead)-`。lead-gen 43 个加 `lead-`（已带前缀的 4 个不双重前缀），映射全表在规格附录 A。
- **description**：300–700 字符硬标准（v3 37/38 条须扩、lead-gen 36 条须砍），验收清单第 2 条有检查脚本。
- **evals.json 不迁**（不锈钢样本库）；评测夹具以后用本仓库 `evals/` 另做。
- **deliverables/ 双树**：`deliverables/marketing/`（00-system/00-research…07-measurement）与 `deliverables/lead/`（00-system…10-sales + 99-archive），取代 `~/Documents/Marketing-Vault-v3` 与 `~/Documents/LeadGen-Vault`。
- 最大产品锁是路径锁（`vault`/`{{VAULT}}` v3 578 次、lead-gen 224 次），其次渠道词（Alibaba 62 次）；材质词集中在 `skill-eval/references/` 与 lead-gen `evals.json`（随 evals.json 不迁而大部消解）。

下游：`marketing-skills-extraction`、`lead-skills-extraction`、`assets-migration` 解除一张阻塞票；验收清单与冒烟 S1–S5 直接喂给 `acceptance-review-and-smoke`。
