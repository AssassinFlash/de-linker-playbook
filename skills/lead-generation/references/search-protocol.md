# 搜索协议

所有获客方法 skill 共用：先查证再写名单。训练记忆不能充当公司名、域名、员工数、市场规模、CAGR、联系人或竞品定价的来源。需要外部研究时，Apify 是强制主入口；故障修复与替代路径见 `docs/apify.md`。需要平台原帖和评论补充 Apify 基线时，按 `docs/social-research-opencli.md`。

## 目录

- [核心规则](#核心规则)
- [默认能力与替代路径](#默认能力与替代路径)
- [按 skill 类型的最低查证](#按-skill-类型的最低查证)
- [查询模板](#查询模板)
- [来源标注](#来源标注)
- [故障与替代路径](#故障与替代路径)
- [搜索日志](#搜索日志)
- [结果是否有用](#结果是否有用)

## 核心规则

产出公司、市场、联系人、竞品数字之前，必须留下真实查证记录。搜索先走 Apify；失败时先修复，不得首次失败就 fallback、降低深度或宣布找不到。Apify 基线之后，公开社媒原帖与评论用 OpenCLI 补证，并保持完整供应链角色边界。

## 默认能力与替代路径

默认主路径是 Apify；替代工具只在 Apify 路径已诊断、记录后使用。

| 需要 | 做法 |
| --- | --- |
| 查证事实、名单、痛点、趋势 | 用 `apify/rag-web-browser` 或已核验的 Apify 搜索 Actor |
| 需要页面原文、验证域名可达 | 用 `apify/rag-web-browser` 抓取指定 URL；大批量页面用 `apify/website-content-crawler` |
| 动态页、登录后才能看 | 先用 Playwright/raw-http 等不同 Actor 配置；仍受限再组合 Computer Use、网站 API 或人工接手并记录原因 |
| 公开社媒原帖与评论 | Apify 基线之后，按 `docs/social-research-opencli.md` 用 OpenCLI 读取；一次一个小查询，遇 429/404 记录后走同一工具的通用页面读取 |
| 联系人/邮箱 | 用联系人/邮箱发现服务（仅当用户已配置）；否则交付物标「联系人待补」 |
| 大规模公开页采集 | 用 Apify Website Content Crawler 或合适的公开页采集 Actor |
| 关键词量/难度 | 用用户已配置的关键词研究工具（用户导出，本侧解析）；未配置则用搜索自动补全与结果量作粗热度 |

Apify Token 已由操作者预付费并按月轮换；Apify 研究质量优先，不因剩余额度缩研究，也不需要每次运行前单独审批。新 Actor 仍先小批量验证 schema、字段和噪声，确认后再扩大日期范围或 `maxItems`。其他付费服务仍须取得授权。

## 按 skill 类型的最低查证

| 类型 | 最低要求 |
| --- | --- |
| 概念型（ICP、竞品定位） | 目标 5 次 Apify 搜索；关键判断再用 Apify 抓取原文 |
| 名单型（公司、分销商、零售商） | 发现用 Apify；每家必须抓取验证域名；搜不够就报告实际数量，不补假公司 |
| 联系人 | 先用 Apify 查公开页；已配置发现服务才批量补邮箱；否则标「联系人待补」 |
| 数据型（市场） | 目标 8 次 Apify 搜索覆盖规模/CAGR/统计；CAGR 与规模至少两源交叉验证 |
| 内容生成（冷邮件等 outreach 文案） | 目标 3 次 Apify 搜索：冷邮件 best practices、主题行写法/打开率、行业邮件模板各至少 1 次；搜到的模板原文禁止写入交付物，只提炼结构与语气模式 |

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

### 内容生成 / 冷邮件

```
B2B cold email best practices {year}
cold email subject line open rate B2B
"{product_category}" cold email template B2B
"{icp_industry}" buyer pain points sourcing {product_category}
```

搜到的模板只用于提炼模式，原文不进入交付物。

## 来源标注

每条来自搜索的事实必须带：

- `data_source`：查询或 URL
- `retrieved_date`：YYYY-MM-DD
- `confidence`：high（交叉验证）/ medium（单源）/ low（估算，须标明）

## 故障与替代路径

- Apify 不可用 → 按 `docs/apify.md` 依次修 token、Actor、参数、Dataset、请求格式、权限、网络、抓取规则、输出解析、timeout 和 rate limit。
- 目标页不可抓 → 换关键词、页面、数据源、Actor、抓取方式或请求参数；再组合 Scrapling、Scrapy、Crawl4AI、Firecrawl、Computer Use、网站 API、sitemap、feed 或源码。
- 社媒专用命令返回 429、404、空数组或登录跳转 → 记录命令、时间、角色和状态；检查 profile、路由与限频，再用 `opencli browser open/extract` 读公开页面，不能写成“没有数据”。
- 只有充分调查后仍不可得，才写缺口；不能用「Apify 与替代取证仍不可得」直接替代「没有数据」。
- 联系人发现服务未配置 → 标「联系人待补」，不编造邮箱。
- 已配置能力失败 → 记入阻塞日志；替代路径仍是取证，不是跳过研究。

## 搜索日志

每次方法 skill 产出必须含：

```markdown
## 搜索日志
| # | Capability | Query/URL | Results | Useful | Notes |
|---|------------|-----------|---------|--------|-------|
| 1 | apify_search | "{positioning_term} {market}" |  |  | actor=...; run=...; dataset=... |
Total: N calls, M useful
```

每次 Apify 搜索或抓取尽量记录 Actor slug、run ID、dataset ID；OpenCLI 记录平台、命令、查询或 URL、链路角色、登录/限频状态。修复和替代路径另记 `## 阻塞与升级日志`。

调研若要进入获客教学或跨会话复用，把可复用判断拆成 `knowledge/knowledge-base.json` 的证据卡：一条一个判断，带来源、角色、类型、摘录和置信度。原始长文继续留在 `research/`，知识库不复制全文。

阻塞时追加 `## 阻塞与升级日志`（模板见 `manual-intervention-protocol.md`）。

## 结果是否有用

有用：含目标实体（公司、人、统计），来源可追溯（官网、行业出版物、政府数据、公开职业页），能填入某个必填字段。

噪声：泛泛软文、内容农场、目录站或交易平台列表页。
