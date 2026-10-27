# SEO 审计方法

读本文件前先确认 `SKILL.md` 已判定本 skill 适用。此处是查询意图、记录字段、分析量表、表结构与可验证断言。

目录：

- [收集](#收集)
- [分析](#分析)
- [交付](#交付)
- [衔接](#衔接)
- [反模式](#反模式)
- [质量](#质量)

品类、目标市场、产地、目标站点技术栈一律取产品上下文对应字段，不在本文件填值。

## 收集

用 Apify 搜索查证；需要原文时抓取指定 URL 的正文。默认先搜再抓。用户已配置网页采集服务时，才用它抓公开页或动态页。Apify 修复与替代取证后仍不可得：停止并写缺口，不编造。多页并行时 dispatch a subagent, else do it inline。

### 站点清单与关键页

记录整站 URL 清单与页数。至少抓：

- 首页：导航、主句、行动按钮
- 产品列表或集合路径（以目标站点技术栈为准）：结构、产品标识、筛选
- 关于 / 联系：公司信息、认证、产地（仅上下文或页面已出现的）
- `/robots.txt`：抓取限制、sitemap 位置
- `/sitemap.xml`：已列 URL、lastmod（有则记）

每页记录：URL、title、meta description、H1、字数、图片数、内链数、canonical。

### SERP 与关键词

至少 20 条查询写入来源栏。查询意图（用上下文的品类 / 目标市场 / 产地替换，不在本文件填值）：

1. 品类 + manufacturer
2. custom + 品类 + supplier
3. 品类 + wholesale B2B
4. 品类 + 目标市场
5. 品类 + 单价或公开价
6. 品类 vs 上下文中的替代方案（每种替代各查一次）
7. 品类 + 产地 + buy / supplier
8. B2B + 品类 + buyer guide
9. 品类 + industrial supplier + content 或 SEO
10. 目标市场 + procurement + 品类
11. best + 品类 + manufacturer
12. where to buy + custom + 品类

每条记录：第 1 页域名、SERP 功能（购物、图片、视频、相关提问）、本站是否可见、来源 URL、访问日期。

关键词表至少 50 行。检索量、CPC、竞争度只填有来源的数字；没有则该列写「未在来源出现」，禁止估计。`source` 写查询串或工具/页面 URL。

### AI 回答可见度

至少 5 条查询，覆盖品牌、核心商业、对比、地域四类中的至少三类。在可访问的 AI 回答界面（搜索引擎 AI 摘要、对话式搜索）上测；界面不可用则只记网页 SERP，并在缺口写明未测界面。

记录：本域是否出现、竞品是否出现、被引用 URL、查询、界面、日期。可见度分数只允许从这些逐条记录推导（出现次数 / 已测次数），禁止主观打分。

### Schema

至少抓 3 类页：

- 首页：Organization、WebSite、LocalBusiness
- 产品或列表页：Product、AggregateOffer、BreadcrumbList
- FAQ 或指南页：FAQPage

客户端注入的 JSON-LD 可能不出现在抓取正文。抓取未见标记时记「未在抓取正文出现，需富结果测试复核」，不得写成「无 schema」。

### 竞品

至少 3 个可访问竞品域名，抓首页以外的产品页或列表页、内容/FAQ 页。记录 title/meta 模式、产品页内容深度、URL 形态、已见到的 schema 类型、内链模式。每条有抓取 URL。

上游 `deliverables/marketing/01-foundation/` 已有竞品稿则先用其已核验域名，仍要补 SEO 向抓取，不把定位稿句子当 SERP 事实。

### 收集门

未满足则不准进入分析结论（只写缺口）：

- [ ] 本站页面清单（抓取 + sitemap，能说明来源）
- [ ] ≥50 条关键词，每条有 `source`
- [ ] ≥20 条 SERP 查询含第 1 页结果
- [ ] ≥3 个竞品站点有页内数据与来源 URL
- [ ] ≥5 条 AI 可见度查询已测或已写未测界面缺口
- [ ] 首页 + 产品/列表 + 内容页的 schema 记录已完成（含「未见、待复核」）

## 分析

### 技术

**可抓取**

- robots 是否误挡
- sitemap 是否可访问
- 产品页是否在首页 3 次点击内
- 筛选/标签是否制造重复；canonical 是否在

**索引**

- `site:` 计数与期望页数
- 孤儿页、抓取错误

**体验（仅就抓取能见的风险写，不编造实验室分数）**

- 最大内容绘制：过大主图/产品图
- 布局偏移：缺尺寸、延迟加载
- 交互：第三方脚本、聊天插件

**URL**

- 标识是否可读（关键词化短标识 vs 无语义编号）
- 小写、连字符、URL 中不放日期
- 遵守目标站点技术栈锁死的路径形态，不建议改平台不允许改的层级

### 关键词与意图

| 意图 | 漏斗 | 页类型 |
| --- | --- | --- |
| Informational | 访问 | 博客、指南、术语 |
| Commercial | 询盘 | 列表、对比 |
| Transactional | 询盘 → 样品 | 产品页、联系页 |
| 长尾具体 | 样品 → 订单 | 产品页、案例 |

分级：

- **A（P0）**：核心商业词，直接对应品类营收路径，且有收集证据
- **B（P1）**：支撑列表或内容的次要词
- **C（P2）**：长尾或可程序化变体

两页抢同一主词标自相残杀。三类意图都不得缺；缺的写缺口并补收集，不拿 C 级词冒充 A 级。

### 竞品差距

对每家已抓竞品写：title 模式与词位、产品页平均深度、schema 类型、SERP 上他们有而本站无的词、他们有而本站无的内容主题。结论必须指回抓取 URL 或 SERP 查询。

### 内容缺口

从 SERP 与 AI 引用页归纳缺失形态（有证据才列）：

- 材料/规格对照
- 目标市场高意图场景页
- 竞品在排的市场/地理页
- 相对替代方案或采购路径的对比页
- 询盘前真实问句的 FAQ

每条绑定收集阶段的目标词、建议路径形状、漏斗阶段。

### 页内

至少 3 个产品页、2 个列表/集合页：

- title：唯一、词前置、约 ≤60 字符
- meta：含行动、约 ≤160 字符
- H1：每页一个，对应当页意图
- 图片 alt：描述性，不用文件名
- 深度：规格、起订量、交期、贸易条款、认证（上下文或页面已有才写）
- 一页一个主词，无自相残杀

### Schema 与架构

| 页类型 | 优先类型 |
| --- | --- |
| 首页 | Organization、WebSite、LocalBusiness |
| 产品页 | Product、AggregateOffer、BreadcrumbList |
| 列表页 | BreadcrumbList、ItemList |
| FAQ/指南 | FAQPage |
| 案例页 | ImageObject、Article |
| 联系页 | LocalBusiness |

每页至少 2 条内链，无孤儿页。架构建议对照目标站点技术栈约束，不与上游 `site-and-schema.md` 唱反调；若冲突，引用上游并写需确认项。

## 交付

全部写到 `deliverables/marketing/02-seo/`。策略与分析用简体中文。面客句子、URL、schema 字段名、文件名按产品上下文；本仓库文件名保持英文。每条建议引用收集阶段的 URL 或查询串。

### 主稿八节

`seo-audit.md` 必须含：

1. **执行摘要** — 至多 3 条发现，影响只能写已有证据能支撑的范围
2. **技术 SEO 审计报告** — 表：问题（具体 URL）、影响 High/Medium/Low、证据、修复步骤、优先级 P0/P1/P2
3. **关键词策略** — ≥50 词，含意图、优先级、目标页
4. **竞品 SEO 差距分析** — 逐家，带来源 URL
5. **内容机会分析** — 缺失主题 + 目标词 + 意图
6. **AI 搜索可见度诊断** — 由逐条查询推导的可见度与引用缺口
7. **Schema 与架构建议** — 按页类型 + URL 修复
8. **行动计划** — P0 / P1 / P2，每条引用收集数据

另写来源表、缺口、可验证断言、下一步。

### 表

`seo-audit-data.xlsx`：可从仓库 `templates/seo-audit-data.xlsx` 复制后填。不能写表时改同目录 `seo-audit-data.json`，四个数组名与下列 sheet 对应。最低行数：Keywords 50、Technical Issues 10、Competitor SEO 3、AI Visibility 10。每行 `source` 非空。

**Keywords**

```
keyword, search_volume, cpc_usd, competition, difficulty, current_rank,
serp_features, intent, priority, target_page, source
```

`search_volume` / `cpc_usd` / `difficulty` / `current_rank` 无来源则填「未在来源出现」。`competition` 仅用 Low/Medium/High 或「未在来源出现」。`intent` 仅用 Informational/Commercial/Transactional。`priority` 用 A/B/C 或 P0/P1/P2。

**Technical Issues**

```
page_url, issue_type, severity, description, fix_recommendation, priority, source
```

`issue_type`：Crawlability / Index / Performance / On-page / Schema。`severity`：High/Medium/Low。

**Competitor SEO**

```
competitor, domain, page_1_keywords, title_pattern, content_depth,
schema_present, notes, source
```

`domain` 必须是已打开过的根域，禁止占位名。

**AI Visibility**

```
query, ai_surface, appears, citation_url, competitor_appears, notes, source
```

`ai_surface` 写实际使用的界面名；未测的界面不要冒充已测。`appears` / `competitor_appears` 用 Y/N。`source` 为查询 + 日期。

### 执行附件

写到 `deliverables/marketing/02-seo/execution/`，每件非空：

- `keyword-master-list.md` — 全词表：intent、priority、target_page
- `technical-audit-checklist.md` — 逐项修复步骤与验证方法
- `page-seo-templates.md` — 按页类型的 title/H1/meta 形状（交付物模板，不是 skill 教学例子）
- `content-gap-priorities.md` — 缺页/主题、目标词、漏斗、预估影响（影响须能回溯证据）
- `competitor-seo-data.md` — 逐家词与结构记录
- `ai-visibility-audit.md` — 逐查询记录
- `schema-implementation-checklist.md` — 类型、目标页、验证步骤（含富结果测试）

## 衔接

需要隔离时 dispatch a subagent, else do it inline。不要回跳 `skills/marketing-orchestrator/SKILL.md`。

- 竞品名单不足：打开 `skills/marketing-competitor-intelligence/SKILL.md`（文件存在时），或在本审计内补满 ≥3 个可访问域名
- 用户要内容日历：打开 `skills/marketing-content-strategy/SKILL.md`（文件存在时）；本审计只交 `content-gap-priorities.md`
- 用户要独立 GEO 方案：打开 `skills/marketing-ai-seo/SKILL.md`（文件存在时）
- 用户要 JSON-LD 片段或架构地图：打开 `skills/marketing-site-and-schema/SKILL.md`（文件存在时）
- 用户要程序化落地页矩阵：打开 `skills/marketing-programmatic-seo/SKILL.md`（文件存在时）；本审计只把可程序化变体标为 C/P2

文件不存在则在缺口写明，并完成本审计最低门，不阻塞主稿。

## 反模式

1. 猜测检索量或排名。
2. 仅凭抓取断定无 schema。
3. 建议不绑品类与目标市场的证据。
4. 竞品少于 3 个仍写差距结论。
5. 使用超过 12 个月且无日期的第三方词数据却不标记。
6. 无关键词或 SERP 证据仍推荐新内容。
7. 主观 AI 可见度分数。
8. 占位 URL 或 `[competitor-url]` / `[keyword]` / `[TODO]` / `[placeholder]`。
9. 忽略目标站点技术栈的 URL 约束。
10. 表或建议无 `source`。

## 质量

出门前核：

- [ ] ≥50 词，每条有真实 `source`
- [ ] 页面清单来自抓取与 sitemap
- [ ] ≥3 家竞品有页内数据与来源 URL
- [ ] ≥20 条 SERP 含第 1 页与功能记录
- [ ] ≥5 条 AI 查询已记录结果或未测缺口
- [ ] schema 覆盖首页、产品/列表、内容/FAQ，并区分抓取所见与待富结果测试
- [ ] 技术表已 P0/P1/P2，修复步骤具体到 URL
- [ ] 内容缺口 ≥5 条，各有目标词与漏斗
- [ ] 含针对目标站点技术栈的建议（canonical、sitemap、标识命名）
- [ ] 表或 JSON 四个集合达最低行数
- [ ] 主稿在 `deliverables/marketing/02-seo/seo-audit.md`
- [ ] 7 个执行附件非空
- [ ] 无占位串；教学例子原文未进入交付物

可验证断言（写入主稿，供验收，不是评测夹具）：

1. `deliverables/marketing/02-seo/seo-audit.md` 存在且含全部 8 个必需节
2. 表或 JSON：Keywords ≥50、Technical Issues ≥10、Competitor SEO ≥3、AI Visibility ≥10
3. 凡带 `source` 的格子均非空，且为真实 URL 或可识别查询串
4. 至少 5 个 A/P0 核心商业词，各有 `target_page`
5. High + P0 技术问题 ≥3，各含页面 URL 与可执行修复步骤；站点极干净则写「未达到 3 条，已列全部已见表项」并列出证据，不编造问题
6. AI 查询 ≥5，覆盖品牌 / 核心商业 / 对比 / 地域中至少三类
7. schema 结论覆盖三类页，并区分抓取与待复核
8. 内容缺口 ≥5，各有目标词与漏斗
9. `execution/` 下 7 个附件均非空
10. 全文 0 个占位串
