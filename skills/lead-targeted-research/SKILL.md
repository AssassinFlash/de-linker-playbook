---
name: lead-targeted-research
description: >
  Use when researching a specific named company, doing a company deep dive,
  prospect background check, single-company analysis, prospect intelligence,
  targeted research, value mapping for one target, 客户背调, 定向调研,
  单个公司调研, or 价值匹配. Run a six-source public-intelligence pass on
  one already identified prospect, then map findings to product USPs for a
  Value Alignment Summary, Custom Opportunity Framing, and Strategic
  Narrative. Distinct from lead-company-research, which builds batch
  prospect lists. Read the ledger product_context and the approved USP
  file; invent no intelligence when a source is empty. Not for batch
  company lists, contact harvesting, or sending outreach.
---

# 定向客户调研（单公司深调与价值映射）

对已点名的一家目标公司做六源公开情报，再与已批准 USP 做双向价值映射，写入 `deliverables/lead/07-targeted/research.md`。一家一份报告；不发信。

## 步骤

1. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。硬依赖：`deliverables/lead/05-usp/usp-strategy.md` 已批准，或台账有 `user_waiver`；未满足则停，宣布打开 `skills/lead-usp-extraction/SKILL.md`，不自造 USP。存在则读 `deliverables/lead/01-icp/icp-analysis.md`、`deliverables/lead/02-companies/target-companies.md`、`deliverables/lead/04-market/competitor-positioning.md`。从用户本轮取出**一家**公司名或官网；只有 URL 则先抓取再取公司名；只有名称则用网页搜索查证官网再抓取验证。未点名且上下文不够：打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则只问公司名与域名一次，然后停。完成：能说出公司名、已验证或已标缺口的域名、本轮要用的 USP 各依据哪几条；原文不拷进本仓库。点名多家时先做第一家，其余见默认。

2. **六源搜集**。按 `references/six-source-intelligence.md` 依次查：官网、LinkedIn 公司页、新闻、新闻稿、评价与反馈、投资者或行业报告。默认用网页搜索查证；需要原文时抓取指定 URL。官网至少抓能打开的首页；About / 产品或服务页能打开则抓，路径不存在则改抓等价页并记缺口。每个源记一条：有发现（URL、访问日期、摘录）或「无相关结果」。搜索不可用则停止并写缺口。完成：六源都有记录；留下的每条情报能指回 URL 与日期。

3. **合成情报**。写出四个组件，分析用本轮语言（缺省中文）：客户背景（商业模式、服务市场、体量、竞争位置，须综合而非抄 About）；当前优先事项或增长动作（招聘、新闻稿、新闻、LinkedIn 活动作证据）；痛点（经营 / 市场 / 供应链，须这家公司特有；有 ICP 则交叉验证，对不上的不升格为痛点）；变化或转型（数字化、合规、自动化、供应商多元化、市场扩张等）。完成：四节都有正文或明示缺口；每条主张有来源与年份或日期；旧材料不得写成当前事实。

4. **价值映射**。读 `references/value-mapping-framework.md`。用已批准 USP 与产品上下文里能指回的能力，对照步骤 3 的优先事项、痛点、变化，填六维：Operational Fit、Strategic Alignment、Pain Point Resolution、Cost/Efficiency、Compliance/Certification、Supply Chain。每维 Strength 为 Strong / Moderate / Weak / None。完成：六维都有；Strong 必须同时有公司侧证据 URL 与一条具体 USP；无数字写「未在来源出现」，不编 ROI 或证书。

5. **机会与叙事**。写 2–3 条个性化使用场景，每条引用步骤 2–4 的具体证据。再写战略叙事：**正好三句**，买家语言（缺省英语），以对方正在做的事开头，可作后续冷邮件开场，本 skill 不发送。完成：场景 2–3 条且互不重复；叙事三句、对方世界在前、能回溯证据；无对齐的维不写进主句。

6. **落盘**。按下方模板写入 `deliverables/lead/07-targeted/research.md`。无 Excel。完成：文件非空；七个组件都在；搜索日志非空；教学例子原文零出现。

7. **出门检查**。对照清单与 `## 清单`。完成：六源都已尝试；痛点非行业套话；价值匹配双向且有证据；叙事三句且对方在前；空源已写明，没有用模型记忆填的格子。

## 默认

- 共用规则若存在则读 `skills/marketing-playbook-standards/SKILL.md`。
- 查证用网页搜索；需要原文时抓取指定 URL（含动态页）。搜索或抓取不可用、登录墙、验证码：停止并写缺口，不编造。
- 一家目标 inline 做完。用户点名多家：每家一份报告；需要隔离时 dispatch a subagent, else do it inline。不要把多家合成一份名单（名单走 `skills/lead-company-research/SKILL.md`）。
- 六源不是等权：优先近期信号；某源空白是合法结果。宁缺有来源的组件，不凑满七个猜测。
- 价值映射在本会话用已取证情报与 USP 合成，不另开一轮搜索让引擎代写对齐。
- 数字、人数、营收、证书、评价只来自：产品上下文、用户本轮、搜索结果或已抓取正文。交付物写 URL 与访问日期。
- 分析用本轮语言；战略叙事与场景里的面客句用买家语言。公司名不翻译。
- 下游个性化外展走 `skills/lead-targeted-outreach/SKILL.md`（文件存在时）；本 skill 只产情报与叙事，不发信。
- 同一家重跑：覆盖 `research.md`，旧版交编排协议归档。换一家且用户要保留旧报告：写 `research-<slug>.md`，并在报告开头注明当前目标。

## 写法

- 每条价值匹配用「具体 USP → 具体需求 → 研究证据」；「我们产品很好」不算对齐。某维对不上就写 None。
- 痛点必须能指回这家公司的公开信号。行业套话（成本压力、供应链挑战）单独出现即未完成。
- 战略叙事先写对方优先事项，再写可见缺口，最后才点能力；能力句必须能回溯步骤 4 的 Strong 或 Moderate。
- 把对方营销主张与经营现实分开写。只有官网口号、无第三方或行为证据的，标为自称。
- 使用场景必须引用步骤 2–4 已记录的情报，不另发明业务线。

## 产出

主文件 `deliverables/lead/07-targeted/research.md`。分析段落用本轮语言；战略叙事用买家语言。

```markdown
# Targeted Research — {company_name}

- company:
- domain:
- source: 台账 product_context（不粘贴原文）
- usp_source: deliverables/lead/05-usp/usp-strategy.md
- accessed:

## 客户背景

## 当前优先事项

## 痛点分析

## 变化领域

## 价值匹配

| dimension | prospect_need | evidence_url | usp_match | strength |
|-----------|---------------|--------------|-----------|----------|
| operational_fit |  |  |  |  |
| strategic_alignment |  |  |  |  |
| pain_point_resolution |  |  |  |  |
| cost_efficiency |  |  |  |  |
| compliance_match |  |  |  |  |
| supply_chain |  |  |  |  |

- primary_angles:
- secondary_angles:
- gaps:

## 机会框架

## 战略叙事

## 空源与缺口

## 搜索日志
| # | Capability | Query/URL | Results | Useful | Notes |
|---|------------|-----------|---------|--------|-------|
```

`strength` 取值：`strong` / `moderate` / `weak` / `none`。列名 English snake_case。

## 例子

> 仅供理解，禁止引用到输出。

形状借自批发竞品单公司深调（双站拆分、注册墙取证、同源数字对照、空源不猜）。只借方法，不把竞品原句、型号、价格或规模数字写入交付物。点名公司若只有手册站、没有贸易店，双站与价门步骤收成空源，不编造门户。

输入把公司站口号与贸易店导航糊成一段 About。成稿应改成：公司站（定位、分支、新闻稿）与贸易店（品类树、注册资格、匿名可见范围）分源记录；混站不算客户背景。不要把口号写成经营现实。结构对照：公司站 + shop 子域是一套 CMS 与声音；手册站 + 全登录门户是另一套——先判再取官网源能看见的那一层。

输入写「他们有阶梯价、库存很满」。成稿应改成：匿名能核验的进官网源（品类、货号可见、价位槽被门挡住）；门后净价、库存、账期、支付记空源，不编。注册页公开的资格（贸易证明、行业下拉、审批后再发凭证）可当「卖给谁」的证据；未解释字段标未知，不猜。

输入从 LinkedIn 与旧通稿各摘一个人数，合成「当前体量」。成稿应改成：列表对照并标日期，不静默取平均；登录墙后的人数不写已核实。公开评价样本很薄时，不要写成「客户普遍好评」。痛点必须落到该公司一条带日期的公开信号，不要写「他们有成本压力」。奖项只保留对方写明的测评维度，不升格为质量证明。

价值匹配写成「某条已批准 USP 对应其某项已取证需求，因为某 URL 某日原文」；双向都空则该维 `none`。战略叙事三句：先写对方正在推进的事，再写可见缺口，最后才点能力；不要以供应商自称开头。

## 易错

- 未读已批准 USP 就做映射，或临场编造卖点。
- 把 `lead-company-research` 的批量名单当成深调，或把多家公司写进同一份 `research.md` 冒充一份报告。
- 把官网 About 改写一遍当作客户背景。
- 空源用模型记忆填满；或为凑查询次数重复无信息搜索。
- 六源等权，把无新闻、无年报的公司硬写成「战略级扩张」。
- 价值匹配对任何公司都成立（高质量、交期稳定）。
- 战略叙事以我方产品开头，或超过三句。
- 把登录墙后的人数、营收写成已核实事实。
- 把本报告当成已发送的定向开发信。
- 把己方公司（产品上下文里的卖方）当作目标客户。

## 清单

- [ ] 已读 `product_context` 与已批准 USP；目标是一家已点名公司
- [ ] 六源均已尝试；空源已写明；每条留下的情报有 URL 与日期
- [ ] 客户背景有综合，不是 About 改写
- [ ] 痛点针对这家公司；有 ICP 则已交叉
- [ ] 价值匹配六维齐全；Strong 双向有证据；无数字未编造
- [ ] 使用场景 2–3 条；战略叙事正好三句且对方在前
- [ ] 搜索日志非空；例子原文未进入交付物
- [ ] 文件在 `deliverables/lead/07-targeted/research.md`（或已注明的 `research-<slug>.md`）；未发信
