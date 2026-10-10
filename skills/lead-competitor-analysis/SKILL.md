---
name: lead-competitor-analysis
description: >
  Use when niche positioning strategy map, ICP whitespace, competitor
  positioning strategy, finding market gaps against ICP pain, 利基定位,
  策略地图, 竞品定位, 市场空白, ICP 空白, or 差异化机会 in a B2B lead run.
  Map observed positioning strategies to representative companies with
  overview, audience, and selling points; then name uncovered spaces,
  underperforming claims, and unmet needs checked against ICP pain. Read
  the ledger product_context (default ~/Documents/New/CONTEXT.md) and
  approved ICP; invent no companies or domains. Battle cards, vs pages,
  and channel prices belong to `marketing-competitor-intelligence`. Not
  for USP extraction, market-size reports, or phase navigation.
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

- 产出只进 `deliverables/lead/04-market/`。厂对厂战斗卡、vs 页、渠道价走 `marketing-competitor-intelligence`。不要用本 skill 写 USP 七步或市场规模报告。战役闸门与审批走 `skills/lead-generation/SKILL.md`，本文件不重复六维。
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

画像先填栏目再贴标签：批发对手按「定位主张 → 品类树 IA → 注册墙/价格门 → 工具/学院」四栏核验。输入只写「某光伏批发商、质量领先」→ 成稿应改成四栏可核验画像再打 `positioning_strategy`，而不是把首页口号当 Overview。

双站与实体图不要混行：公司站与贸易店是两份证据；店品牌、集团名、培训中心是同一玩家的不同表面。公司站标语记主张；店侧未登录看不到净价、注册才开交易记门禁。输入把公司站口号抄进 Key Selling Points、或把集团站与本地店拆成两家 → 拆开主张与门禁，实体图合并为一行。

同市场不同语域分开策略：电气全能批发（货号/现货/宽目录语言）与光伏专科批发（系统/应用语言、学院与对比工具）不要并成一条「分销商」。目录公开+价门 与 手册站+门户全墙 是同一贸易门禁策略的两种实现，不要拆成两条定位。

价格门不是空白：多平台对照常见的是目录可浏览、贸易价登录后可见。输入写「没人公开报价所以无人占据」→ 改成拥挤的贸易门禁观察。库存灯号、交期控件只记为「可得性/物流」策略信号，不把对方时效或库存承诺抄成我方卖点。

FAQ 取证看问句分桶与答句密度，不看页脚有没有 FAQ：账号/物流/质保路由 vs 产品诊断分开记。店级薄 FAQ（多半登录与购物车）且产品页无问答，是执行面观察，不要推断「不做售后」或新开一条 Service-oriented。消费端 PDP 问答与贸易店工单入口不是同一层证据；打不开的店标 unverified，不写「无 FAQ」。

空白必须对照 ICP：公开页家用方案中心很厚、工商业中间带（对大玩家太小、对本地店太大）很薄，且已批准 ICP 把该中间带列为痛点 → 可写入未满足需求。公开页没人做装饰包装，不算机会。规划软件四格（仿真/布置/技术经济/下单）里前三格的厂商不进批发竞品表；二阶转售是渠道层——用户自己若已在分销层，不要把该层写进对手表。

口号不是证据：把「全球分销 / 行业领先」记主张；把已抓取页上的成立年份、可核验认证记证据，不写进同一句。三源计数口径冲突时选一个权威源并记下口径，不把几个数字平均成规模。

不凑数：诚实搜索后只观察到专科批发、电气全能、区域物流、培训伙伴等 4 种定位，就交付 4×代表公司，缺口写「未凑满 6 策略」，不编第 5、6 家，也不把用户本公司写进表。竞品原句只作观察，策略名用自己的标签，不整段抄 About。

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
