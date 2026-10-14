---
wayfinder: task
status: open
assignee:
step: 1
blocked_by: [base-table-build, ledger-split]
---

# 执行登记流程

## Question

（AFK）落地 `CONTEXT.md`「执行登记」：操作者在对话里说一句（哪个渠道、发布 / 更新了什么）→ AI 查证 → AI 写进底表执行登记表。L0 的唯一来源，也是归因锚。

- 写成一个正典 skill（`skills/<name>/SKILL.md`，跨 harness，触发词含「我发了」「上线了」「更新了」「发出去了」等），并在 `AGENTS.md` 指路；两条线共用。
- 查证：网页 → 抓线上 URL，确认 200、内容与口述相符（标题 / 关键句），记录查证时间；其他渠道（LinkedIn 等）→ 能公开访问就抓，不能就记「操作者口述，未查证」并说明原因。**邮件**的查证（在已发送里）要 IMAP，归「邮箱 IMAP 回流」票补上；本票先记「待邮箱接入后查证」。
- 写入走「建底表」定下的脚本层（追加一行，带编号；重复登记要能识别）。
- 两张台账（「台账拆两线」定的文件）不记执行登记，只在需要时引用编号。

## 站点侧改动也是执行（用户 2026-10-14：站点优化与接入并行）

- 新站仓库里影响收录或可见内容的改动（robots、noindex、canonical、站点地图、URL / 301、标题 / 描述、正文）上线后同样要登记，否则反馈接不回原因。登记来源可以是新站仓库已合并的 PR（链接作为查证证据），不必等操作者口述。
- 本票落地时补登：从「GSC 站点接入」上线那天起、新站仓库已合并且影响上述内容的 PR，逐条补进执行登记（标「补登」）。
- 改 URL 的登记要同时记旧 URL 与新 URL，保证 GSC 数据能接回。

- 台账文件（「台账拆两线」关票时写入，2026-10-14）：营销 `state/marketing-status.md`、获客 `state/lead-status.md`；旧的 `state/status.md` 已删除。两张共用键：YAML `phase`、`phase_name`、`next`、`method_skill`、`output_dir`、`product_context`（值 `docs/fact-sources.md`，`evals/validate_project.py` 会检查），同样的键再列一遍在「当前」表里，另有「阶段」「已完成」「回写」各节。获客台账另有「审批与过期」表（交付物、方法 skill、status、review_date、review_score、stale_reason、stale_date；frontmatter 为准，本表是索引）和「豁免（user_waiver）」表（日期、方法 skill、跳过的硬依赖、用户原话）。营销台账没有这两张表（只拆不改）。执行登记不进任何一张；需要引用时只写编号。

## 完成标准

- 演练：对一个线上真实页面口述一次「更新了 X」→ 底表多出一行、查证列为真；对一个不存在的 URL 口述 → 查证失败、不写入或写入标「查证失败」（本票定其一）。

## 交接

- 执行登记编号格式与查证列，写进「GSC 数据回流」「邮箱 IMAP 回流」「营销编排改循环」三票正文。
