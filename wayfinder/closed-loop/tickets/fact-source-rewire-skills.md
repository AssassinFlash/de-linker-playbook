---
wayfinder: task
status: closed
assignee: claude-code-fact-source-entry (同会话续) 2026-10-14
step: 0
blocked_by: [fact-source-entry]
---

# 101 个 skill 改指新事实源

## Question

（AFK）把 `skills/` 下写死 `~/Documents/New` 的文件（「现仓库闭环缺口审计」#1：101 个；减去「事实源入口」已改的两个编排 skill 目录）全部改为指向事实源入口，缺省值与回退路径一并去掉。

- 只改指针与「从哪读事实」的指令句；方法正文不动（方法层留用）。
- 例子：已标「仅供理解，禁止引用到输出」的例子是教学支架，正文不因来自 New 而重写；但凡是让 agent **去读** New 的句子一律改指入口。若某例子写着会被当成现行事实的产品参数，改成不含具体参数的通用说法，不从新源补数字。
- 文件所有权：本票不碰 `skills/marketing-orchestrator/**`、`skills/lead-generation/**`（归「台账拆两线」与编排循环票）。
- 量大：可按目录分批；可派 subagent 执行，主会话逐批抽查 diff。

入口路径与指针写法（「事实源入口」关票时写入，2026-10-14）：

- 入口：`docs/fact-sources.md`（仓库根相对路径）。台账键 `product_context` 保留，值已改为 `docs/fact-sources.md`。仓外路径只住在入口里，skill 里不写。
- 标准指针句（「从哪读事实」那一句整句换成它）：
  > 产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理；原文不拷进本仓库。
- 引用台账的闸门句：把 `（缺省/默认 ~/Documents/New/CONTEXT.md；把 ~ 展开为主目录…）` 换成 `（事实源入口 docs/fact-sources.md）`，再接「按其指路取证」。凡是「需要参数再读 …/fact-base/」的分句一律删掉，参数从哪查由入口决定。英文句同理：`ledger product_context (= docs/fact-sources.md)`。
- 特例（「台账拆两线」关票时更正，2026-10-14）：「缺 `product_context` 则写入 …」在 `marketing-init` 步骤 3（和它的 description 与清单），改为写入 `docs/fact-sources.md`。`marketing-profile` 里的指针模板 `source: …/CONTEXT.md` 改为 `source: docs/fact-sources.md`；「用户若要改事实，改 …」改为「事实以线上站点与新站仓库为准，不改本仓库」。
- 台账已拆（2026-10-14）：skill 里的台账路径已统一改为 `state/marketing-status.md`（marketing-*）或 `state/lead-status.md`（lead-*），`state/status.md` 已删除。闸门句现在长这样：「读台账 `state/lead-status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；…）」。本票整句换成标准指针句即可，台账路径可以随之去掉；只为读 `phase`、`method_skill`、`output_dir` 的台账引用不要动。`marketing-init`、`marketing-playbook-standards` 同时提到两张台账，属正常。
- 参照：两个编排 skill 及其 `references/` 已按这个写法改完，可对照 diff。
- 实数：本票开工时 `grep -rl "Documents/New" skills` 是 96 个文件，不是 99 个。

## 完成标准

- `grep -rl "Documents/New" skills | wc -l` = 0。
- `evals/` 现有校验脚本全绿；随机抽 5 个 skill 读一遍，指针读得通、无残留回退。
- 不打开 `~/Documents/New` 的任何文件。

## Resolution

（2026-10-14）`skills/` 下 96 个文件（排除两个编排 skill 目录）全部改指事实源入口 `docs/fact-sources.md`，149 处旧路径清零。分三批：

1. **正则批（90 个文件）**：五类句式。
   - 闸门句和输入句「读台账 … 的 `product_context`（缺省/默认 旧路径；…）」连同后面「需要参数再读 …」整句换成标准指针句；紧跟其后的「读不到则停」改为「入口读不到则停」。
   - 默认节「产品事实只读 `product_context`（需要参数再读 …）」换成标准指针句。
   - 两份 methodology 里的输入清单两行合成一行，指向入口。
   - 英文 description 里的 `ledger product_context (default …)` 改为 `the fact-source entry docs/fact-sources.md`。
2. **手改（9 个文件）**：
   - `marketing-profile`：指路三步改为「入口 → 三方」；指针模板改为 `source: docs/fact-sources.md`、`sources_opened`、`status: readable | partial | missing`；「改事实」改为以线上站点与新站仓库为准。
   - `marketing-init`：`product_context` 缺失、为空或值不对，一律写成入口。
   - 另外七个文件：`lead-data-validation`、`lead-interview` 及其 `skill-seeds`、`lead-buyer-psychology/nine-scenarios`、`lead-product-knowledge` 及其 `family-classifier`、`marketing-eval`。
3. **统一说明句**：7 处例子说明「无对应 New/竞品材料可借」改为「无对应事实源材料可借」。

刻意保留两类：
- 4 处例子出处说明（`marketing-psychology`、`marketing-copywriting`、`lead-warm-email-transform`、`marketing-email-outreach`）说的是「例子形状借自 New」。它们不是读取指令，按本票规则不重写。
- 交付物模板的 `source: 台账 product_context` 和清单里「已读 `product_context`」。这个键的值就是入口，不是回退。

核验：
- `grep -rl "Documents/New" skills | wc -l` = 0；「需要参数再读」「fact-base」「缺省/默认 `~`」残留也是 0。
- `evals/validate_project.py`、`validate_deliverables.py` 全绿；68 条 WARN 改前改后数量一样，都是早就有的 workbook 提示。
- 随机抽 5 个（seed 20261014）读改过的段落：`marketing-seo-audit`、`lead-magnet-gen`、`lead-linkedin-pain-solution`、`marketing-paid-advertising`、`marketing-visual-content`。指针都读得通，没有残留的缺省值或回退。
- 没打开过旧目录里的任何文件。
