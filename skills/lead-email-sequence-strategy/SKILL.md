---
name: lead-email-sequence-strategy
description: >
  Use when organizing already-written lead emails into a campaign
  plan, sending order, email strategy, 邮件策略, 发送计划, 邮件编排,
  A/B testing plan, cold vs warm variants, or follow-up timing,
  including phase 6 of this repo's lead run. Only sequence existing
  lead-group assets (cold, warm, follow-up, lead-magnet drafts);
  assign per-ICP order, cadence, A/B tests, and stop conditions;
  write a config guide for the user's configured outbound or
  sequence tool; if none is configured, produce the plan only and do
  not send. Not for writing the emails themselves, marketing-phase
  nurture systems, finding contacts, drip setup from scratch, or
  phase navigation.
---

# 邮件活动编排

把已经写好的冷邮件、暖化稿、跟进序列和引流素材，编成按 ICP 分组的统一发送策略，落到 `deliverables/lead/06-outreach/email-strategy.md`。本文件只编排 lead 组已有成稿资产，不代写邮件，不做营销获客阶段的名单研究或生命周期培育。未配置外发/序列工具则只产计划，不发送。

## 步骤

1. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。共用规则若存在则读 `skills/marketing-playbook-standards/SKILL.md`。硬依赖（须已批准，或有 `user_waiver`）：`deliverables/lead/06-outreach/cold-emails.md`、`deliverables/lead/06-outreach/followup-sequence.md`。软依赖存在则读：`deliverables/lead/06-outreach/warm-emails.md`、`deliverables/lead/06-outreach/lead-magnet.md`、`deliverables/lead/01-icp/icp-analysis.md`、`deliverables/lead/03-contacts/contacts.xlsx`。资产是否齐、ICP 段数、外发工具名仍不清时，打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则把缺口写入台账，不自造访谈。完成：能指出首封、跟进、ICP 各依据哪份文件；原文不拷进本仓库。硬依赖未满足且无 `user_waiver` → 停，不编邮件凑序列。

2. **资产盘点**。把已读邮件逐封列入清单：`asset_id, type, icp_name, strategy_name, source_path, human_review`。`type` 只取 `cold` / `warm` / `followup` / `lead_magnet`。跟进按策略名对齐（Friendly Reminder、Additional Value、Direct Yes/No、Social Proof、Limited-Time Incentive、Feedback Request、Previous Interaction、Breakup、New Angle），对不上的仍入表，`strategy_name` 写原文标题。缺哪封记哪封，不补写。完成：上游文件里每封信都有一行；无主的资产标 `unassigned`。

3. **节拍查证**。用网页搜索查证当年 B2B 跟进节拍做法；用户点名了外发/序列工具时，再搜该工具的序列设置要点（停发、延迟、追踪）。需要原文则抓取指定 URL。完成：来源表有 URL 与访问日期，或已记录搜索不可用。搜索不可用 → 不写行业打开率/回复率，节拍改用「写法」默认骨架并标明「默认模板，非本轮测得最优」，不编造基准。

4. **按 ICP 填槽**。每个 ICP 单独一条序列，互不混装。按「写法」默认骨架把 `asset_id` 填进日槽；无对应资产的槽位删掉或标缺口，不发明替稿。跟进稿未按 ICP 拆分时：首封按 ICP 分配，跟进骨架共用，并在缺口写明「要分写时打开 `skills/lead-followup-sequence/SKILL.md`（文件存在时）」。完成：每个 ICP 有一张槽位表（日偏移、策略、`asset_id`、是否附件）；未使用的资产有原因。

5. **A/B 与停发**。有暖化稿且该 ICP 联系人足够拆成两列独立收件人 → 默认测「暖化首封 vs 冷首封」，指标为回复率。缺变体或不够拆 → 只跑默认首封（有暖化用暖化），A/B 写入缺口，不编 50/50。第二测「跟进里强 CTA vs 弱 CTA」仅当两封现稿 CTA 确实不同；不改写 CTA。停发：回复、退订、退信，三者任一即整列停止。有打开追踪时，首封从未打开的不发带附件的价值信。完成：每个 ICP 写明跑哪一测或为何延期；停发三条写进策略。

6. **工具配置**。用户已配置外发/序列工具 → 按「产出」配置清单写成可粘贴步骤（每 ICP 一活动、延迟与槽位表一致、追踪、停发）。仅当用户已配置且本轮明确要求发送时，才用该工具按本策略配置；否则只写指南，不发送。未配置 → `tool: not_configured`，计划照写，不假装已建活动。联系人文件缺失 → 标「联系人待补」，活动不可执行。完成：配置节非空；发送与否与工具状态一致。

7. **落盘**。写入 `deliverables/lead/06-outreach/email-strategy.md`。策略/分析用中文；表列名 English snake_case；公司名不翻译。验证—审查—审批走 `skills/lead-generation/references/orchestration-protocol.md`，本 skill 不代替审批。完成：主文件非空；下方断言满足；教学支架原文零出现。

## 默认

- 产品事实只产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。，不在本仓库另存档案。
- 查证用网页搜索；需要原文时抓取指定 URL。不并列搜索引擎菜单。搜索不可用则不编造基准。
- 外发/序列工具：仅当用户已配置；付费项须先告知并获准。未配置则只产文案与计划，不发送。
- 进度只认台账。产出只进 `deliverables/lead/06-outreach/`。
- 写邮件走 `skills/lead-cold-email-gen/SKILL.md`、`skills/lead-warm-email-transform/SKILL.md`、`skills/lead-followup-sequence/SKILL.md`、`skills/lead-magnet-gen/SKILL.md`（文件存在时）。本文件只编排 lead 组已写成稿，不重写正文。营销获客阶段的名单与生命周期培育走 `marketing-email-outreach`。暖化稿在序列中的优先级按本文件「暖化优先」，不以 `lead-warm-email-transform` 另排。
- 单文件编排 inline 做完。多 ICP 且需隔离盘点时 dispatch a subagent, else do it inline。
- 数字、打开率、回复率、退订率：来源表或用户本轮有才写。没有就写「未在来源出现」，禁止补造。
- 限时折扣/激励槽：产品上下文确有、仍有效的报价才用；否则跳过，不编优惠。跟进成稿里的策略 5 仍盘点入表，与「激励默认不进骨架」不冲突。

## 写法

**一 ICP 一活动。** 不同画像不同首封与痛点，混装无法看哪条序列在工作。

**暖化优先。** 该 ICP 有暖化稿则暖化作默认 Day 0；冷稿作 A/B 或无暖化时的回退。

**默认骨架（日偏移相对首封）。** ICP 或产品上下文写了更长采购周期则按比例拉长，并标明依据；未写则用下表，且标「默认模板」。

| 日偏移 | 策略 | 资产 | 规则 |
| --- | --- | --- | --- |
| 0 | First touch | 暖化默认；冷稿为变体 | 同一收件人只收一封首封 |
| 1–2 | Friendly Reminder | 跟进对应稿 | |
| 3–5 | Additional Value | 跟进对应稿；有引流素材可作附件 | 有打开追踪且首封未打开 → 不带附件 |
| 7 | Direct Yes/No **或** Social Proof | 两封现稿里只取一封 | 同一收件人同一天不发两封；另一封可作 A/B，不可并列 |
| 10 | Feedback Request | 跟进对应稿 | |
| 14 | Previous Interaction | 跟进对应稿 | 仅当该联系人或暖化稿确有过往互动；否则整槽跳过 |
| 17 | Breakup | 跟进对应稿 | 只收尾、不夹推销 |
| 21+ | New Angle | 跟进对应稿 | 仅在决裂后仍无回复时发 |

槽位随上游实有资产增减，不按「必须九封」凑数。Limited-Time Incentive 默认不进骨架：`lead-followup-sequence` 策略 5 仍列入资产清单，默认 `skip_reason` 写「激励默认不进骨架」；产品上下文确有、仍有效的报价才进槽。

**节拍。** 默认日表是给工具填的延迟，不要另写一套互斥的「3 / 7 / 15 天」计划。更快易像骚扰，更慢易断档；拉长须能指回 ICP 或查证来源。

**停发与分支。** 回复 / 退订 / 退信 → 该收件人整列停。不要对谁都把骨架走完。决裂必须干净。

**终审。** 首封、决裂、带数字或附件的跟进、引流素材：配置进工具前标「须人工终审」。

## 产出

主文件 `deliverables/lead/06-outreach/email-strategy.md`：

```markdown
# 邮件发送策略

- source: 台账 product_context（不粘贴原文）
- accessed:
- tool: configured | not_configured
- send_this_run: no | yes（仅当已配置且用户明确要求）

## 摘要

## 来源

| 声明 | URL | 访问日期 | 摘录 |
| --- | --- | --- | --- |

## 邮件资产清单

| asset_id | type | icp_name | strategy_name | source_path | human_review |
| --- | --- | --- | --- | --- | --- |

## ICP 分组策略

每条 ICP：用哪封首封、跟进是否共用、联系人来源或「联系人待补」。

## 发送序列设计

每条 ICP 一张槽位表：day_offset, strategy_name, asset_id, attachment, skip_reason。

## A/B 测试方案

测什么、指标（回复率）、如何拆名单、样本不足则延期。不写编造的基准胜出线。

## 外发/序列工具配置指南

工具名（用户点名则照写，否则 `not_configured`）。每 ICP 一活动；步骤顺序与延迟复制「发送序列设计」；追踪打开/点击/回复（工具无追踪则标明）；停发：reply / unsubscribe / bounce。未配置则本节是粘贴清单，不是「已创建活动」。

## 监控指标

按邮件位置记打开（有追踪时）、按策略记回复、退订、哪条 ICP 更好、A/B 何时才宣布胜者（两变体都有足够回复；否则「样本不足，不宣布胜者」）。不填假目标值。

## 缺口

## 可验证断言

## 下一步
```

断言（未满足则不算全量完成）：

- 每个 ICP 有独立序列，没有混装
- 每个在用槽位有日偏移与 `asset_id`（或已写 skip_reason）
- 资产清单覆盖上游每一封；未使用的有原因
- 停发含回复、退订、退信
- A/B 有一测及指标，或已记录延期原因
- `tool` 与 `send_this_run` 一致：未配置则不发送
- 无编造的打开率、回复率、优惠
- 教学支架原文零出现

## 例子

> 仅供理解，禁止引用到输出。

输入写两份 ICP 的冷邮件、一封暖化、一组跟进，却把安装商与 EPC 采购装进同一活动。成稿应拆成两个活动：安装商序列把 Day 0 当备线开口，不写成换商；EPC 序列按双闸排发送序——商务闸（价、交期、报价有效期）与技术闸（文件包、认证、兼容证据）分槽，技术闸可否决商务闸，故不要用价/交期独占首封、再把技术证据当附件塞给未打开的人。有暖化的 ICP 用暖化作 Day 0、冷稿作 A/B；没有暖化的只用冷稿，不编第二封首封。报价有效期是买方锁一口价的风险工具，不是 Limited-Time Incentive。采购周期更长则拉长默认骨架，不另写一套日表。未配置外发工具则只写 `email-strategy.md`，不发送。不要把本节句子粘进交付物。

## 易错

- 多个 ICP 装进同一个序列活动。
- 硬依赖缺失时编邮件凑槽。
- 把本文件当写手，重写跟进或发明优惠。
- 未配置外发工具却写「已创建活动」或已经发送。
- 编造打开率、回复率或退订上限。
- 决裂信里夹推销。
- 有打开追踪时，对从未打开首封的人发附件。
- 回复后仍继续发。
- 槽位表与工具延迟写成两套互不相干的日表。
- 按「必须九封」或「必须对半拆」凑数。
- 把本文件当成营销获客阶段的名单研究、生命周期培育或从零搭 drip。
- 把教学例子原文写入交付物。

## 清单

- [ ] 已读 `product_context` 与硬依赖；未满足则已停或已有 user_waiver
- [ ] 上游每一封都在资产清单；无补写邮件
- [ ] 每个 ICP 独立序列；槽位有日偏移与资产或 skip_reason
- [ ] 节拍有来源，或已标默认模板；无编造基准
- [ ] A/B 可执行或已延期；停发含回复 / 退订 / 退信
- [ ] 未配置外发工具则只产计划、未发送
- [ ] 文件在 `deliverables/lead/06-outreach/email-strategy.md`；例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
