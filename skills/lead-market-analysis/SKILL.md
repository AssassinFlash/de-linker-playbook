---
name: lead-market-analysis
description: >
  Use when the user asks for market research, market analysis, market size,
  CAGR, SWOT analysis, market forecast, market overview, market entry, market
  opportunity, market trends, 市场分析, 市场调研, 市场规模, 市场趋势, or
  市场进入策略. Write a ten-section B2B market intelligence report covering
  size and CAGR, landscape, buyer behavior, trends, evidenced SWOT, risks,
  financial projections, timed recommendations, and appendices. Read ledger
  product_context and approved competitor analysis; invent no market numbers.
  Output under deliverables/lead/04-market/. Not for ICP research, contact
  discovery, or outreach copy.
---

# 市场分析（10 板块）

把产品利基的公开市场证据与已批准竞品材料，写成 10 板块情报报告，写入 `deliverables/lead/04-market/`。缺来源就写缺口，不编造规模或增长率。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。

2. **输入与闸门**。读台账 `state/lead-status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录）。记下品类/利基、目标市场、用途（内部决策 / 投资人 / 销售支持，未指定则内部决策）。硬依赖：`deliverables/lead/04-market/competitor-positioning.md` 与 `competitor-comparison.xlsx` 的 frontmatter `status` 为 `approved` 或 `approved_with_concerns`，或台账已记 `user_waiver`。软依赖（有则读，不阻塞）：`deliverables/lead/01-icp/icp-analysis.md`、`deliverables/lead/02-companies/` 下目标公司 / 分销商 / 零售商文件。硬依赖未满足：停，打开 `skills/lead-competitor-analysis/SKILL.md`（存在则按其做）；该文件也不存在则只报缺口，不自造竞品表。产品上下文仍不够圈定利基或市场时，打开 `skills/lead-interview/SKILL.md`（存在则按其做），不在本文件另写问卷。范围默认 10 板块全做；访谈或用户本轮明确收窄时，只做点名板块，并在摘要列出跳过的板块名与原因。完成：能指出利基、目标市场、竞品文件状态各依据哪几条；原文不拷进本仓库。

3. **采集规模与增长**。用网页搜索查证当前规模、近 3–5 年历史增速、未来 3–5 年展望、CAGR。需要原文时抓取指定 URL。规模与 CAGR 各至少两个独立来源交叉；来源相差超过约 30% 时写区间并解释差异，不挑一个当唯一真值。查证次数对齐 `skills/lead-generation/references/search-protocol.md` 的数据型最低要求（覆盖规模 / CAGR / 统计，至少 8 次网页搜索）；有用结果不够则报告实际次数与缺口，不用训练记忆填数。搜索不可用则停止并写缺口。完成：规模与 CAGR 各有 ≥2 条带来源名、年份、时间窗的记录，或已标「未在来源出现」。

4. **采集格局、买家、趋势与风险**。对照已批准竞品表，用网页搜索查证份额、集中度、进入壁垒；买家决策周期与渠道偏好；技术 / 监管 / 贸易政策（含关税、反倾销检索）。有 ICP 或渠道名单则用来核对买家与渠道段落，不另造公司。用户已配置市场探索或流量工具时，由其导出后再解析；未配置则不做流量份额估算。多页抓取需要隔离时 dispatch a subagent, else do it inline。完成：格局、买家、趋势、监管四块各有摘录或显式缺口；每条证据有 URL 与访问日期。

5. **SWOT、风险、财务**。按 `references/ten-sections-detail.md` 写四类 SWOT（每条有证据与 High/Medium/Low 影响）、三类风险（市场 / 竞争 / 监管，各含概率、影响、缓解）、1–5 年市场预测。我方收入或盈亏平衡：仅当产品上下文有量、价或成本；否则标缺口，只做市场层预测。估算必须标「估算」并写推理。完成：SWOT 四类均非空；每条风险有缓解；预测有方法说明；无出处数字为零。

6. **建议与摘要**。建议按影响×可行性排序；每条含做什么、为何（指回本报告发现）、怎么做、何时、由哪个角色负责（用产品上下文里的职能，不编人名）。实施分 0–3 个月、3–6 个月、6–12 个月。最后写执行摘要（放报告最前）：规模、关键趋势、主要机会、主要风险、首要建议；可独立阅读。完成：摘要不依赖后文才能读懂；每条建议有时间线。

7. **落盘**。写入下方路径与模板。策略与分析用简体中文；表列名 English snake_case；公司名不翻译。文末必须有搜索日志。完成：主报告 10 板块齐全，或收窄范围内板块齐全且摘要列出跳过项；工作簿三表每行有 `source` 或 `data_source`；教学支架原文零出现。

## 默认

- 产出只进 `deliverables/lead/04-market/`。进度只认台账。战役闸门与审批走 `skills/lead-generation/SKILL.md`；验证—审查—写入见 `skills/lead-generation/references/orchestration-protocol.md`。营销树基础/竞品走 `skills/marketing-foundation/SKILL.md` 与 `skills/marketing-competitor-intelligence/SKILL.md`，不混写。
- 查证用网页搜索；需要原文时抓取指定 URL。缺搜索则停止并写缺口，不编造。
- 数字只来自：产品上下文、用户本轮、搜索结果或已抓取正文。交付物写来源名、URL、年份、访问日期。
- 金额默认 USD，来源是其他币种时保留原币并注明。历史值与预测值必须带时间标记，不混写。
- 早于「当前公历年 − 2」的数据必须标注年份与陈旧；不是自动丢弃。
- 不重做竞品定位；竞争格局以已批准竞品文件为骨架，本 skill 只补份额、集中度与进入壁垒。
- 单文件、无并行机会的工作 inline 做完，不 dispatch。

## 写法

- SWOT 每条必须能指回摘录、证书、数字或已抓取页；空泛优劣不算完成。
- CAGR 必须写清起止年与来源；只写「增长很快」不算完成。
- 建议必须能执行（动作 + 时间 + 角色），不写无主语的方向口号。
- 收窄范围时，未做板块写「本轮范围外」，不把空白写成「无风险 / 无机会」。
- 附录列完整来源（URL、访问日期）与方法；用表支撑正文，不强制生成图片文件。

## 产出

主文件 `deliverables/lead/04-market/market-analysis.md`。表 `deliverables/lead/04-market/market-data.xlsx`（三 sheet）。板块字段见 `references/ten-sections-detail.md`。

```markdown
# 市场分析 — {利基} × {市场}

- source: 台账 product_context（不粘贴原文）
- competitor_source: deliverables/lead/04-market/competitor-positioning.md
- accessed:
- scope: all_10 | 列出的板块
- purpose: 内部决策 | 投资人 | 销售支持

## 1. 执行摘要

## 2. 市场概览

## 3. 竞争格局

## 4. 消费者行为

## 5. 趋势与机会

## 6. SWOT

## 7. 风险分析

## 8. 财务预测

## 9. 建议

## 10. 附录

## 搜索日志
| # | Capability | Query/URL | Results | Useful | Notes |
|---|------------|-----------|---------|--------|-------|
| 1 | web_search |  |  |  |  |
Total: N calls, M useful
```

`market-data.xlsx` 三 sheet（列名一字不改）：

- 市场数据汇总：`metric, value, source, year, category, notes`
- SWOT矩阵：`type, description, evidence, impact_level, data_source`
- 风险矩阵：`risk_type, description, probability, impact, mitigation, data_source`

写不出工作簿时，同目录写 `market-metrics.csv`、`swot-matrix.csv`、`risk-matrix.csv`，列名与上表一致，并在主报告附录注明。

## 例子

> 仅供理解，禁止引用到输出。

格局：输入写「欧洲批发都是网店」→ 成稿应改成同一批发层里的两种实现（公开目录+价格登录墙 vs 宣传站+登录后交易门户），并写清注册是一次人工核验、核验后自助下单；不要并成一个渠道格，也不要照抄各站注册页或价格门原句。竞品名只标结构（例如某德系店目录公开、价在墙后）。

规模：输入写单一 TAM、或把货架深度当市场规模 → 成稿应改成来源 A / 来源 B 的区间与口径差（品类、地理、渠道层），不平均成假精确值，不用过时货架计数填规模。CAGR 写起止年与来源名。

机会：输入写「工商业增长快」→ 成稿应改成公开容量分段下的中间带——对大型专商太小、对住宅侧小商太大，空白是「谁报价这一档」，证据来自买家侧来源；不要把住宅自发自用经济套到这一档，不要粘论坛用户名或原帖。

买家：输入写「在意质量与交期」→ 成稿应改成这一档先要负荷数据与电价条款能否成立；电网与许可若被渠道材料标成关键路径，就写入决策周期。不编周期天数，不把库存灯号或时效承诺写成我方卖点。

跨境：输入写「欧洲统一市场」、或把德语制度名译进别国摘要 → 成稿应按市场分开钱的说法、资格门、并网登记用语；同一货架层在不同语言店是不同名词，不要压成一个英文伞名，也不要进口美式公用事业词当本地卡点。缺某国来源就标缺口。

SWOT：输入写「品质较好」或「我们更专业」→ 成稿应改成可指回摘录的观察（认证自某年来源页持有；或在位者把门放在注册一次、对照我方是否每笔人工），对照来源页的行业口径。不要空泛优劣，不要把竞品口号当证据。

建议：输入写「应该做欧洲站」→ 成稿应改成动作+时间窗+职能，指回本报告的格局 / 中间带 / 跨境发现；先补哪国资格门与口径，而不是先开译站。

## 易错

- 未读竞品批准件就开写格局，或把竞品分析重做一遍。
- 先写执行摘要再找数据。
- 单源 CAGR 或规模仍写成定论。
- 无出处统计，或把模型记忆当行业报告。
- SWOT / 风险没有证据或没有缓解。
- 预测不写方法，或把历史值抄成展望。
- 建议没有时间线或负责角色。
- 默默跳过板块，却自称 10 板块齐全。
- 把教学例子原文写入交付物。

## 清单

- [ ] 已读共用规则与 `product_context`；硬依赖已批准或已记 user_waiver
- [ ] 10 板块齐全，或收窄范围已在摘要列明
- [ ] 规模与 CAGR 各 ≥2 源（或已标缺口）；数字均有来源名 + 年份
- [ ] SWOT 每条有证据；风险每条有概率、影响、缓解
- [ ] 财务预测有 1–5 年时间窗与方法；估算已标「估算」
- [ ] 建议含时间线与角色；执行摘要最后写、放最前、可独立读
- [ ] `market-analysis.md` 与 `market-data.xlsx`（或等价 CSV）在 `deliverables/lead/04-market/`
- [ ] 搜索日志有查询、URL、日期；例子原文未进入交付物
