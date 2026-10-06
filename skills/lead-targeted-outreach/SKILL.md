---
name: lead-targeted-outreach
description: >
  Use when writing emails for a specific company, personalized outreach
  sequence, company-specific cold email, targeted outreach, follow-up for
  a researched prospect, 定向开发邮件, 定向邮件序列, 针对性冷邮件, or
  定向外展. Turn approved targeted-research into a default 3-email
  sequence (Hook, Proof, Nudge) or an extended multi-angle sequence for
  one named prospect. Distinct from batch ICP cold email. Read the ledger
  product_context and deliverables/lead/07-targeted/research.md; invent no
  company facts, case studies, or testimonials. Write copy under
  deliverables/lead/07-targeted/; send only if an outbound tool is already
  configured. Not for batch cold email, contact harvesting, or the
  research pass itself.
---

# 定向外展（单公司个性化邮件序列）

根据已批准的定向调研，为一家已点名公司写个性化冷邮件序列，写入 `deliverables/lead/07-targeted/outreach.md`。缺情报标缺口，不编造；未配置外发工具则只产文案不发送。

## 步骤

1. **输入**。读 `skills/marketing-playbook-standards/SKILL.md`（存在则读）。读台账 `state/status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录）。硬依赖：`deliverables/lead/07-targeted/research.md` 已批准，或台账有 `user_waiver`；未满足则停，宣布打开 `skills/lead-targeted-research/SKILL.md`，不自造调研、不写通用开发信。存在则读：`deliverables/lead/05-usp/usp-strategy.md`、`deliverables/lead/01-icp/icp-analysis.md`、该公司在 `deliverables/lead/03-contacts/` 的行。从用户本轮取出公司名；与 `research.md` 不一致则停，先做对应该公司的调研。产品、收件角色或成功标准仍不清：打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则把缺口写入台账，不自造访谈清单。完成：能说出公司名、调研文件、将引用的情报各依据哪几条；原文不拷进本仓库。点名多家时先做第一家，其余见默认。

2. **定模式、角色与角度**。模式：用户点名封数或点名角度 → extended；否则 default（3 封）。收件角色按序取：本轮消息 → 该公司联系人行 → 调研里的买家信号 → 在采购 / 指定人 / 运营 / 负责人里选最贴近的一档并标明「角色未在上下文出现，暂用」。角色优先事项若调研已覆盖，不再另搜。未覆盖时用网页搜索查证该角色在该行业的公开决策标准，至多一轮；需要原文则抓取指定 URL。搜索不可用则跳过角色补搜并写缺口，不编造角色心理。default 三封弧：Hook → Proof → Nudge。Proof 只在产品上下文或调研里有可核验用例、社会证明或能力证据时使用；否则改用 `references/multi-angle-strategies.md` 的 `industry_insight` 或 `value_add`，并在策略概述写明替换。extended：用户选定的角度不重复；未选则按该文件推荐顺序补齐；`breakup_nudge` 只能作末封。角度所需证据（用例、数字、证言、竞品名、可寄出的资料）在上下文或调研里找不到 → 换角或减封，不编材料。完成：模式、封数、每封角度、收件角色均已写下；每封能预指出将引用的那条调研情报。

3. **起草**。按「写法」写每一封：Purpose、Subject、Body、CTA，并标注 `research_insight`（调研章节 + 一句摘录）。default 正文 ≤150 词，extended ≤180 词（英文按空格分词；上限不是目标）。策略叙事可作 Hook 开场材料，不整段粘贴。主句只使用价值匹配为 strong 或 moderate 的维；产品解决不了的痛点不写进邮件。完成：每封一词上限内、一个 CTA、首句关于对方；每封有调研引用；教学支架原文零出现。

4. **落盘**。按下方模板写入 `deliverables/lead/07-targeted/outreach.md`。节奏写具体 Day 偏移，取 `references/multi-angle-strategies.md` 默认表，时区取调研总部；调研没有时区则写「时区未在调研出现」。无 Excel。完成：文件非空；序列与节奏都在；未发信（或用户已配置外发工具且本轮明确要求发送时，在报告记录工具名，仍把文案留在本文件）。验证—审查—审批走 `skills/lead-generation/references/orchestration-protocol.md`，本 skill 不代替审批。

5. **出门检查**。对照「清单」。完成：个性化测试通过（换一家公司则整封站不住）；空证据已换角或标缺口；没有用模型记忆填的公司细节。

## 默认

- 产品事实只读台账 `product_context`（需要参数再读 `~/Documents/New/fact-base/`），不在本仓库另存档案。
- 一家目标 inline 做完。用户点名多家：每家一份报告；需要隔离时 dispatch a subagent, else do it inline。批量无调研的开发信走 `skills/lead-cold-email-gen/SKILL.md`（文件存在时）。
- 查证用网页搜索；需要原文时抓取指定 URL。不并列搜索引擎菜单。不为「最佳实践」或回复率凑查询；方法已在本文件。
- 外发工具、联系人/邮箱发现服务：仅当用户已配置（付费项须先告知并获准）。未配置则只产文案、邮箱标「联系人待补」，不编造地址、不发送。
- 同一家重跑：覆盖 `outreach.md`，旧版交编排协议归档。换一家且用户要保留旧稿：写 `outreach-<slug>.md`，并在报告开头注明当前目标。
- 分析用本轮语言；面客正文用买家语言（缺省英语），同一封不混用。公司名不翻译。
- 产出只进 `deliverables/lead/07-targeted/`。

## 写法

- 个性化测试：把公司名换成另一家，这封应读不通。只插入公司名不算个性化。
- 序列推进：每封提供新信息或新角度，不把同一推销换词重说。default 弧是 Hook → Proof → Nudge；extended 按 `references/multi-angle-strategies.md` 由软到硬再到收束。
- 首句写对方处境（优先事项、新闻、痛点、变化），不写我方公司或产品名。
- 每封一个 CTA；探询、要一页纸、要样品、要对比，不写注册 / 免费试用。
- 语气：同行对同行。短句、国际英语、无俚语、无文化梗、无 ALL CAPS 主题、无附件（正文只说可以另寄）。
- 数字、案例、证言、证书、可寄出的资料：产品上下文或已抓取页里有才写。没有则换角或写「未在上下文出现」，禁止补造。
- 主题行：好奇或相关，指向对方处境，不写标题党。

### default 三封

1. **Hook**：主题扣调研里的一条具体处境。三段以内：个性化洞察 → 一条对得上的问题（接价值匹配）→ 低压 CTA。
2. **Proof**：一句话收回挑战 → 可核验的用例或证明 → 一个资源或通话 CTA。无证明则按步骤 2 换角。
3. **Nudge**：承认时机可能不对 → 一句核心收益 → 最后一次 CTA（可寄一页纸或样品）。

extended 九角的目的、结构、选用与节奏见 `references/multi-angle-strategies.md`。

## 产出

主文件 `deliverables/lead/07-targeted/outreach.md`。无表。策略段落用本轮语言；Subject / Body / CTA 用买家语言。

```markdown
# Targeted Outreach — {company_name}

- company:
- domain:
- recipient_role:
- recipient_email:
- mode: default | extended
- source: 台账 product_context（不粘贴原文）
- research_source: deliverables/lead/07-targeted/research.md
- usp_source:
- accessed:
- sent: no

## 邮件策略概述

## 收件人分析

## 邮件序列

### Email {n} — {angle}

- purpose:
- research_insight:
- subject:
- body:
- cta:
- word_count:

## 发送节奏建议

| email | day_offset | thread | send_window |
| --- | --- | --- | --- |

## 来源

| 声明 | URL 或调研章节 | 访问日期 | 摘录 |
| --- | --- | --- | --- |

## 可验证断言

## 缺口

## 下一步
```

断言（未满足则不算全量完成）：

- 每封 `research_insight` 非空，且能在 `research.md` 或本轮用户材料中指回
- default 正好 3 封且弧为 Hook → Proof → Nudge（Proof 已按规则替换的，概述里写明）
- extended 各封角度不重复；`breakup_nudge` 若出现必为末封
- 每封一个 CTA；`word_count` 不超过该模式上限
- 含数字或案例的句子有来源，或已标「未在上下文出现」
- `recipient_email` 有值或为「联系人待补」
- `sent` 为 `no`，除非用户已配置外发工具且本轮要求发送
- 教学支架原文零出现

## 例子

> 仅供理解，禁止引用到输出。

调研写该公司某年宣布迁产线。第一句应点这条公开动作，不要写祝对方安好，也不要以我方工厂介绍开场。没有写入上下文的客户结果，就不要编「同类公司节省了某个百分比」。不要把本节句子粘进交付物。

## 易错

- 调研文件缺失或不是这家公司仍开写。
- 把批量 ICP 开发信模板套上公司名，冒充定向。
- 编造案例、证言、ROI 或未持有的资料作为 Value Add。
- 首句介绍我方公司；一封里多个 CTA。
- 把产品解决不了的痛点写进承诺。
- 为凑查询去搜回复率或「冷邮件最佳实践」。
- 未配置外发工具却声称已发送，或编造收件邮箱。
- 把教学例子原文写入交付物。
- 终稿残留未解释占位符。

## 清单

- [ ] 已读共用规则、`product_context` 与已批准 `research.md`（或 user_waiver）；目标是一家公司
- [ ] 模式、角色、每封角度已定；缺证据的角已替换或减封
- [ ] 每封有调研引用、一个 CTA、首句关于对方；字数未超上限
- [ ] 个性化测试通过；序列在推进，不是同一推销重说
- [ ] 节奏含 Day 偏移；时区有依据或已标缺口
- [ ] 邮箱待补或可回溯；未配置外发则未发送
- [ ] 文件在 `deliverables/lead/07-targeted/outreach.md`（或已注明的 `outreach-<slug>.md`）
- [ ] 教学例子原文未进入交付物
- [ ] 工具只写能力；多家时为 dispatch a subagent, else do it inline
