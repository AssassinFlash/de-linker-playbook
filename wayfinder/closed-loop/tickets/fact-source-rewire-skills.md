---
wayfinder: task
status: open
assignee:
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
- 特例：`marketing-profile` 里「缺 `product_context` 则写入 …」改为写入 `docs/fact-sources.md`。它的指针模板 `source: …/CONTEXT.md` 改为 `source: docs/fact-sources.md`。「用户若要改事实，改 …」改为「事实以线上站点与新站仓库为准，不改本仓库」。
- 参照：两个编排 skill 及其 `references/` 已按这个写法改完，可对照 diff。
- 实数：本票开工时 `grep -rl "Documents/New" skills` 是 96 个文件，不是 99 个。

## 完成标准

- `grep -rl "Documents/New" skills | wc -l` = 0。
- `evals/` 现有校验脚本全绿；随机抽 5 个 skill 读一遍，指针读得通、无残留回退。
- 不打开 `~/Documents/New` 的任何文件。
