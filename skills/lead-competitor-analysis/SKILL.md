---
name: lead-competitor-analysis
description: >
  Use when analyzing competitors, researching competitor positioning, mapping a
  competitive landscape, finding market gaps, competitor profiling, positioning
  strategy, competitive analysis, differentiation, 竞品分析, 竞争分析, 竞品定位,
  市场空白, or 差异化机会 in a B2B lead run. Map observed positioning strategies
  to representative companies with overview, audience, and selling points; then
  name uncovered spaces, underperforming claims, and unmet needs checked against
  ICP pain. Read the ledger product_context (default ~/Documents/New/CONTEXT.md)
  and approved ICP; invent no companies or domains. Not for marketing-tree
  battle cards, USP extraction, market-size reports, or phase navigation.
---

# 竞品定位（策略×公司 + 市场空白）

把该利基里真实出现的定位策略，映射到可核验代表公司，再对照 ICP 痛点标出空白与可执行差异化。写入 `deliverables/lead/04-market/`。

## 步骤

1. **输入**。读台账 `state/status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录）。共用规则若存在则读 `skills/marketing-playbook-standards/SKILL.md`。硬依赖：存在且已批准则读 `deliverables/lead/01-icp/icp-analysis.md`；缺失且无 `user_waiver` → 停并写缺口，打开 `skills/lead-icp-analysis/SKILL.md`（存在则按其做）。有则读：`deliverables/lead/02-companies/target-companies.md`、`deliverables/lead/02-companies/distributors-analysis.md`（或同目录 `distributors.xlsx`）。记下品类、利基、目标市场、已知对手、ICP 痛点。品类或利基仍缺：先看用户本轮；仍缺则停并只要这两项。需要结构化补问时打开 `skills/lead-interview/SKILL.md`，不在本文件另写问卷。完成：能指出品类、利基、买家痛点各依据哪几条；原文不拷进本仓库；用户本公司不进竞品表。

2. **发现定位**。用网页搜索查证该利基的公开竞品与定位用语。需要原文时抓取指定 URL。搜索不可用则停止并写缺口，不编造。查询形状见下方「默认」。对照 `references/positioning-types.md` 给观察到的策略打标签；菜单上没有的按公开材料实际用语新增，不把八类当必须凑齐。完成：每条策略能指回至少一次搜索或已抓取页；未观察到的类型不进表。

3. **代表公司**。每个已观察策略选 2 家可核验代表公司，抓取官网（首页；概览不足再抓 About 或等价页），写 Company Overview、Target Audience、Key Selling Points。口号与证据分开记。多域名并行时 dispatch a subagent, else do it inline。完成：每家有可访问域名或已标 unverified；未核验的不编 Overview。某策略只有 1 家可核验 → 不编第二家，记为可能弱势策略。某策略公开玩家 ≥5 → 代表仍写 2 家，另记拥挤。目标 6 策略 × 2 家；搜不到 6 个真实策略则按实际数量交付并写缺口，不拿无关公司凑行。

4. **空白**。三类分开写，不混：无人占据的定位组合；已占位但执行弱（站点、内容、响应等可观察弱点）；未满足需求——必须对照 ICP 痛点，ICP 没提的不记为机会。完成：至少 3 个空白，或明示搜完后不足 3 个及原因；每个空白有 ICP 痛点交叉引用。

5. **建议与落盘**。每条建议指向一个空白 + 用户已陈述能力。能力未陈述的标待补，不发明产线或预算。按下方模板写入 `deliverables/lead/04-market/competitor-positioning.md` 与 `deliverables/lead/04-market/competitor-comparison.xlsx`。完成：主报告含三节必填；表每行有 `data_source`；教学例子原文零出现。

## 默认

- 产出只进 `deliverables/lead/04-market/`。不要用本 skill 写营销树战斗卡、USP 七步或市场规模报告。战役闸门与审批走 `skills/lead-generation/SKILL.md`，本文件不重复六维。
- 查证用网页搜索；需要原文时抓取指定 URL 的正文。概念型最低：至少 5 次网页搜索；每家代表公司抓取官网验证域名。关键词量、权威分、月流量：仅当用户已配置研究工具并导出时解析；未配置则用搜索结果量作粗热度，不编造流量或份额。
- 数字、证书、营收、成立年份只来自：产品上下文、用户本轮、搜索结果或已抓取正文。交付物写 URL 与访问日期。
- 策略与分析用中文；表列名 English snake_case；公司名不翻译；卖点摘录保持页面原文语言。
- 硬依赖 `lead-icp-analysis`；软依赖公司调研（有则读，不阻塞）。分销商名单若存在，只作发现线索，不替代官网核验。
- 写不了 xlsx 时，同目录写 `competitor-positioning.csv` 与 `market-gaps.csv`，列名与 sheet 一致，并在主报告注明。

查询形状（花括号是字段，不抄进交付物）：

```
"{product_name}" competitors {market}
"{product_category}" manufacturer positioning
{competitor_domain}/about
"{competitor_name}" target audience
"{competitor_name}" reviews complaints
```

## 写法

- 先观察再贴标签：定位类型来自公开页实际用语，不是先选类型再找公司。
- 首页标语记为主张；证书、年限、测试、可核验记录才当证据。二者不写进同一句冒充事实。
- 空白只在「公开材料确实未主张」且「买家在乎」时成立。
- 每策略 2 家是代表画像，不是市场玩家上限。拥挤要记数量；稀缺不要补假公司。
- 建议写成「空白是什么 → 用已有哪项能力填 → 下一步做什么」，不写空泛「加强品牌」。
- 综合官网，不要整段抄 About。中型与利基玩家也要搜，不只最大几家。
- 公司块形状见 `references/positioning-types.md`。

## 产出

主文件 `deliverables/lead/04-market/competitor-positioning.md`：

```markdown
# 竞品定位 — {品类} × {市场}

- source: 台账 product_context（不粘贴原文）
- accessed:
- strategies_n:
- companies_n:
- gaps_n:

## 竞品定位策略分析

### {策略名}
- 拥挤度：代表 2 家 / 可观察玩家约 N
- 代表公司：按公司块填写

## 市场定位空白分析

### 无人占据
### 执行偏弱
### 未满足需求（对照 ICP）

## 差异化建议

| 空白 | 已陈述能力 | 建议动作 | priority |
| --- | --- | --- | --- |

## 缺口

## 搜索日志
| # | Capability | Query/URL | Results | Useful | Notes |
|---|------------|-----------|---------|--------|-------|
```

同目录表 `competitor-comparison.xlsx`：

- Sheet 竞品定位：`positioning_strategy, company_name, domain, target_audience, key_selling_points, market_position, data_source`（目标 12 行；不足则与缺口栏一致）
- Sheet 市场空白：`gap_description, current_status, opportunity, recommended_action, priority`（目标 3 行）

## 例子

> 仅供理解，禁止引用到输出。

口号不是证据：把「行业领先质量」记为主张；把可核验的认证年份或召回记录记为证据，不把两句写成同一事实。

空白必须买家在乎：公开页没人做某种装饰包装，不算机会；ICP 把加急样品列为前三痛点、而公开材料无人承诺加急样品，才写入未满足需求。

不凑数：诚实搜索后只观察到 4 种定位，就交付 4×代表公司，并在缺口写「未凑满 6 策略」，不编第 5、6 家公司。

## 易错

- 未读 ICP 就标「买家在乎的空白」。
- 用模型记忆填公司名或域名，而不是已抓取页。
- 把「我没听过」当成「市场不存在」，却未搜索。
- 只写「他们主打质量」，没有摘录或证据。
- 把用户本公司写进竞品表。
- 建议超出已陈述能力。
- 把本 skill 当营销树战斗卡或 USP 七步管线。
- 把 skill 例子原文写入交付物。

## 清单

- [ ] 已读 `product_context`；ICP 已批准或已记录 `user_waiver`
- [ ] 定位类型来自观察，不是菜单配额
- [ ] 每家代表公司有可访问域名或 unverified；无编造 Overview
- [ ] 空白对照过 ICP 痛点；建议绑定已陈述能力
- [ ] 主报告含三节必填；表每行有 `data_source`
- [ ] 搜索日志有 URL 与日期；例子原文未进入交付物
- [ ] 文件在 `deliverables/lead/04-market/competitor-positioning.md` 与 `competitor-comparison.xlsx`（或已注明的 csv 降级）
