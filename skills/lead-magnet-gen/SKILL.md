---
name: lead-magnet-gen
description: >
  Use when creating lead magnets, buyer guides, sourcing checklists, vendor
  scorecards, quizzes, templates, gated content, downloadable PDFs, cost
  breakdown explainers, 引流磁铁, 引流素材, 获客工具, 内容资产, or 买家指南,
  including phase 6 outreach of this repo's lead run. Read the ledger
  product_context and upstream ICP or USP files when present; recommend
  three of six formats (Mistake Guide, Checklist, Scorecard, Quiz, Template,
  Explainer); then write the magnet plus a low-pressure follow-up script
  under deliverables/lead/06-outreach/. Invent no statistics, case studies,
  or certifications. Not for cold-email sequences, LinkedIn posts, SEO
  articles, or phase navigation.
---

# 引流磁铁

按六种格式之一写出可发送的买家教育内容，并配一条低压跟进脚本，落到 `deliverables/lead/06-outreach/`。方法是澄清输入 → 三选一格式 → 成稿 → 跟进脚本。缺证据标缺口，不编造。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。

2. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。存在则读：`deliverables/lead/01-icp/icp-analysis.md`（编排硬依赖）、`deliverables/lead/05-usp/usp-strategy.md`、产品知识稿（`deliverables/lead/05-usp/product-knowledge.md` 或 `deliverables/lead/10-sales/product-knowledge.md`，以磁盘已有为准）。用户本轮给出的品类、买家类型、痛点、已有物料（规格表、目录、报价模板）或指定格式一并用。核心三项：品类、买家类型、至少一条痛点。缺核心：先看本轮消息；仍缺则打开 `skills/lead-interview/SKILL.md`（存在则按其做），否则停并只要这三项。不要在本文件另写问卷。ICP 缺失：不编画像；买家与痛点改从产品上下文或本轮取，交付物注明「ICP 未在上游出现」。原文不拷进本仓库。完成：能指出品类、买家、痛点各依据哪几条。

3. **查证**。用网页搜索查证该类买家在该品类上的 sourcing 痛点、常见错误、公开指南或清单形态。需要原文则抓取指定 URL 的正文。搜索日志格式见 `skills/lead-generation/references/search-protocol.md`。搜索不可用则停止并写缺口，不编造统计、法规、认证或案例。完成：每条将写入磁铁的行业判断有 URL 或摘录，或已标「未在来源出现」；`## 搜索日志` 有行。

4. **选格式**。读 `references/format-pool.md`。按买家处境从封闭六种里建议 3 个，每个一句理由。用户已点名且在池内 → 用该格式，不必再建议。用户未选：本轮能问则只问一句选哪个；用户已说直接做、或本轮不能问 → 取建议第 1，交付物写明「格式未经用户确认」。禁止自造第 7 种。完成：一种格式、一句理由；做过建议则建议列表非空。

5. **成稿**。按该格式骨架写：标题、导语（约 100–150 词，对买家痛点说话、不写卖方能力清单）、主体、低压 CTA、可选署名。紧接着写跟进脚本（邮件或 LinkedIn 可用）：分享资源，不约会议。条数按 `references/format-pool.md` 的目标来；证据不够则少写并标缺口，不拿跨品类空话凑数。数字、证书、案例、产地：产品上下文或本轮查证有才写。面客语种以产品上下文为准，缺省英语；分析与理由跟本轮语言。完成：主体符合该格式（清单有条目、计分卡有计分逻辑、测验有题与解读等）；CTA 只提供按规格/MOQ/项目改一版，不约电话；跟进稿无编造的社会证明；署名字段上下文没有则省略或 `[待补充]`。

6. **落盘**。写入 `deliverables/lead/06-outreach/lead-magnet.md`。只产文案，AI 不代发；审稿到 `operator_ok` 后由操作者亲手发。完成：文件非空；含格式理由、磁铁正文、跟进脚本、待填字段、PDF 排版建议、搜索日志、缺口；教学支架原文零出现。

## 默认

- 产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理；不在本仓库另存档案。
- 产地、供应地、目标市场以产品上下文为准，不预设某一出口国。
- 查证用网页搜索；需要原文时抓取指定 URL。搜索不可用则停止并写缺口。不并列多引擎菜单。
- 单文件 inline 做完；需要隔离时 dispatch a subagent, else do it inline。
- 六种格式是封闭池：Mistake Guide、Checklist、Scorecard、Quiz、Template、Explainer。
- USP 只在有证据时自然嵌入，不把磁铁写成宣传册。买家即使不向你下单，内容仍应有用。
- 合规、标准、认证：未在上下文或已抓取页确认的，标「须与合规团队核实」，不写成已持有。
- 冷邮件、跟进序列、邮件策略：各走对应 `lead-*` skill（文件存在时）。本文件只产磁铁与跟进脚本。
- 产出只进 `deliverables/lead/06-outreach/`。

## 写法

- 视角永远是「买家需要知道什么」，不是「工厂有多好」。
- 可复制进邮件，或改成一页 PDF；不用依赖外部工具的复杂排版。
- CTA 公式：`[对方可回复的动作] + [按对方规格/MOQ/项目定制]`。不用约会议、注册、免费试用。
- 跟进主题用磁铁标题；正文说明这是针对哪条痛点的材料，问要不要一份，并提供改一版。禁止写「很多买家都觉得有用」之类无来源社会证明。
- 同一稿不混用两种面客语种。品类名一篇一译并锁定。
- 专家买家不从零解释基础术语；新进口商不堆只有工程师能用的缩写。以买家类型为准。

## 产出

目录：`deliverables/lead/06-outreach/`

主文件 `lead-magnet.md`：

```markdown
# Lead Magnet — {品类} × {买家类型} × {格式}

- source: 台账 product_context（不粘贴原文）
- accessed:
- format:
- format_confirmed_by_user: yes / no
- buyer_language:

## 输入摘要
Product / Buyer Type / Pain Points / Existing Materials / Desired Format

## 格式理由
建议过的 3 个（若有）与入选理由

## Lead Magnet Content
### TITLE
### INTRODUCTION
### MAIN CONTENT
### CTA
### SIGNATURE
（上下文无署名信息则整节省略）

## Follow-Up Message Script
Subject:
Body:

## 待填字段
须按具体产品或订单填写的占位，用 `[待补充]`，面客段禁止残留未解释占位符充数

## PDF 排版建议
一页可扫：标题、导语、主体、CTA；不用多栏或必须依赖外部组件的版式

## 搜索日志
| 查询或 URL | 日期 | 结论 |

## 缺口
```

断言（未满足则不算全量完成）：

- 格式在六种池内，且有理由
- 导语对买家痛点说话，不含卖方能力清单
- 主体结构与所选格式一致
- CTA 低压、可回复、提供定制
- 跟进脚本非空、不约会议、无编造社会证明
- 含数字或认证的句子有来源，或 `[待补充]` / 「未在上下文出现」
- 教学支架原文零出现

## 例子

> 仅供理解，禁止引用到输出。

输入写「帮买家少踩坑」。选题先对同档批发店 FAQ 的问句分桶，不要对厂家诊断页。批发侧买家问句成簇的是交易桶：订货与付款、发货与到货、到货损伤与退货、保修找谁办；厂家页把问句铺成标题索引、答句藏在工单后，问句多、当场答句少，那是路由密度不是磁铁。一稿只锁一桶，再从封闭六种里选一种骨架。

成稿应改成该品类、该买家角色下这一桶里可核验的具体错误与后果（到货核验落在哪张凭证、质保对家是厂家还是批发接口）。没有来源就少写条目并标缺口，不写「七个行业通用秘诀」，也不把别人店里的时限、免运门槛、退货费率写进磁铁当承诺。CTA 用「需要按你们规格改一版就回复」，不用「约个电话」。跟进信不写「很多买家都觉得有用」。第一单是备线不是换商：内容在对方不下单时仍要能用；身份停在批发接口，不写成制造商或备件库。不要把本节句子粘进交付物。

## 易错

- 没读产品上下文或上游痛点就发明行业错误清单。
- 把教学例子或模型记忆当事实、统计或案例。
- 用宣传口吻写教育内容，或在磁铁里硬推销。
- 跨品类空话凑满目标条数。
- CTA 约会议或要对方承诺下单。
- 跟进稿编造「很多买家使用」。
- 把产地锁成某一出口国，而不看产品上下文。
- 自造第 7 种格式，或不写理由直接成稿。
- 把本文件当成开发信或 LinkedIn 帖生成器。
- AI 代发（不论是否配置外发工具、用户是否要求）。
- 终稿面客段用未解释占位符冒充已核实内容。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 品类、买家类型、痛点有依据；ICP 缺失已标明
- [ ] 行业判断有来源或已标缺口；搜索不可用已停
- [ ] 格式在六种池内，有理由；建议过则列出 3 个
- [ ] 主体与格式骨架一致；条数未用空话凑
- [ ] 导语对买家痛点说话；CTA 低压可回复
- [ ] 跟进脚本非空、不约会议、无编造社会证明
- [ ] 数字与认证未编造；合规未确认已标核实
- [ ] 文件在 `deliverables/lead/06-outreach/lead-magnet.md`；未发送
- [ ] 教学例子原文未进入交付物
