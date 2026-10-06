# 搜索协议

所有获客方法 skill 共用：先查证再写名单。训练记忆不能充当公司名、域名、员工数、市场规模、CAGR、联系人或竞品定价的来源。

## 目录

- [核心规则](#核心规则)
- [默认能力与逃逸](#默认能力与逃逸)
- [按 skill 类型的最低查证](#按-skill-类型的最低查证)
- [查询模板](#查询模板)
- [来源标注](#来源标注)
- [降级](#降级)
- [搜索日志](#搜索日志)
- [结果是否有用](#结果是否有用)

## 核心规则

产出公司、市场、联系人、竞品数字之前，必须留下真实查证记录。搜索不可用 → 停止并写缺口，不编造。

## 默认能力与逃逸

默认一条能力 + 一个逃逸，不并列引擎菜单。

| 需要 | 做法 |
| --- | --- |
| 查证事实、名单、痛点、趋势 | 用网页搜索查证 |
| 需要页面原文、验证域名可达 | 抓取指定 URL 的正文 |
| 动态页、登录后才能看 | 抓取指定 URL 的正文（含动态页）；失败则按 `manual-intervention-protocol.md` 请用户接手 |
| 联系人/邮箱 | 用联系人/邮箱发现服务（仅当用户已配置）；否则交付物标「联系人待补」 |
| 大规模公开页采集 | 用网页采集服务抓取公开页（仅当用户已配置）；付费前告知并获准 |
| 关键词量/难度 | 用用户已配置的关键词研究工具（用户导出，本侧解析）；未配置则用搜索自动补全与结果量作粗热度 |

付费能力使用前必须告知预估费用。用户未批准 → 保留已有结果并标缺口。

## 按 skill 类型的最低查证

| 类型 | 最低要求 |
| --- | --- |
| 概念型（ICP、竞品定位） | 目标 5 次网页搜索；关键判断再抓取原文 |
| 名单型（公司、分销商、零售商） | 发现用网页搜索；每家必须抓取验证域名；搜不够就报告实际数量，不补假公司 |
| 联系人 | 先网页搜索公开页；已配置发现服务才批量补邮箱；否则标「联系人待补」 |
| 数据型（市场） | 目标 8 次网页搜索覆盖规模/CAGR/统计；CAGR 与规模至少两源交叉验证 |

交付前检查：交付物含 `## 搜索日志`；次数达到上表目标，不足时日志写明尝试与缺口（记 CONCERN），禁止空搜凑数或编造来源（编造直接 FAIL）。无日志则数据准确性直接 FAIL。存在阻塞但无 `## 阻塞与升级日志` → Actionability 至少 CONCERN。

不要用「只搜不抓、从未打开过公司站」结束名单型任务。

## 查询模板

花括号是字段，不是要抄进交付物的句子。品类、市场、定位词取产品上下文与已批准 ICP，不在本协议填值。

### ICP / 买家画像

```
"{product_name}" buyers {market}
"{industry}" procurement challenges {year}
"{industry}" pain points supply chain
"{industry}" purchasing department structure
B2B buyers of {product_category} procurement decision process
```

### 公司发现

```
"{positioning_term}" {market}
"{industry}" distributor {country}
"{product_category} {company_type} {region}"
```

每条候选必须抓取域名确认可访问。排除目录站、交易平台列表页，不把列表页当成目标公司。

### 分销商 / 零售商

```
"{product_category}" distributor {country}
"{product_category}" wholesaler {region}
"{product_category}" retail brand {country}
{domain}/become-a-supplier OR /partnerships
```

员工数约束（方法 skill 若要求小于 200）：用公开资料交叉，缺则标缺口，不编造。

### 市场分析

```
"{product_niche}" market size {year} filetype:pdf
"{product_niche}" global market size CAGR forecast
"{industry}" market report competitive landscape
"{product_niche}" trends and opportunities
```

### 竞品

```
"{product_name}" competitors {market}
"{product_category}" manufacturer positioning
{competitor_domain}/about
"{competitor_name}" reviews complaints
"{competitor_name}" market share
```

## 来源标注

每条来自搜索的事实必须带：

- `data_source`：查询或 URL
- `retrieved_date`：YYYY-MM-DD
- `confidence`：high（交叉验证）/ medium（单源）/ low（估算，须标明）

## 降级

- 网页搜索不可用 → 停止并写缺口，不编造。
- 抓取失败（反爬、登录、验证码）→ 换查询或按人工接手协议续跑，不把训练记忆填进字段。
- 联系人发现服务未配置 → 标「联系人待补」，不编造邮箱。
- 已配置能力失败 → 记入阻塞日志，降回网页搜索 + 抓取原文。

## 搜索日志

每次方法 skill 产出必须含：

```markdown
## 搜索日志
| # | Capability | Query/URL | Results | Useful | Notes |
|---|------------|-----------|---------|--------|-------|
| 1 | web_search | "{positioning_term} {market}" |  |  |  |
Total: N calls, M useful
```

阻塞时追加 `## 阻塞与升级日志`（模板见 `manual-intervention-protocol.md`）。

## 结果是否有用

有用：含目标实体（公司、人、统计），来源可追溯（官网、行业出版物、政府数据、公开职业页），能填入某个必填字段。

噪声：泛泛软文、内容农场、目录站或交易平台列表页。
