---
name: marketing-seo-audit
description: >
  Use when the user needs SEO audit, keyword research, technical SEO, site
  analysis, on-page audit, schema audit, AI SEO audit, AI-search visibility,
  competitor SEO gap analysis, programmatic SEO planning, B2B manufacturing
  SEO, B2B manufacturing search strategy, 关键词研究, or SEO审计. Read the
  ledger product_context (default ~/Documents/New/CONTEXT.md); collect crawl,
  SERP, schema, and AI-visibility evidence; prioritize technical, content,
  and schema actions; write them to deliverables/marketing/02-seo/. Invent no
  volumes or ranks; never paste skill examples into the output. Not for
  site-architecture-only work, post-audit content calendars, or phase
  navigation.
---

# SEO 审计

根据已读产品上下文与可验证抓取/搜索证据，找出搜索可见度缺口，排成技术、内容、schema 与 AI 可见度动作，落到 `deliverables/marketing/02-seo/`。缺证据就写缺口，不编造检索量或排名。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化。
2. **输入**。读台账 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`）。把 `~` 展开为用户主目录，不要把 `~` 当相对路径。需要参数再读同目录 `fact-base/`。已有定位、竞品、定价稿则读 `deliverables/marketing/01-foundation/`；已有站点架构稿则读 `deliverables/marketing/02-seo/site-and-schema.md`。完成：能指出品类、目标市场、站点 URL、目标站点技术栈各依据哪几条；原文不拷进本仓库。站点 URL、品类或目标市场缺到无法开审则停并写缺口，不编造公司、市场、价格、流量或对手事实。只做架构/schema 规划或只要内容日历时，停并改走对应 skill（文件存在时），不在本文件硬做。
3. **收集**。用网页搜索查证；需要原文时抓取指定 URL 的正文。覆盖：站点清单与关键页、robots/sitemap、≥20 条 SERP 查询、关键词证据、≥3 个竞品域名、首页+产品/列表页+内容页的 schema、≥5 条 AI 回答可见度查询。多域名或多页并行时 dispatch a subagent, else do it inline。搜索不可用则停止并写缺口。查询意图、记录字段与数据门：读 `references/methodology.md`。完成：页面清单已得；关键词 ≥50 且每条有 `source`；竞品 ≥3 家有可访问域名；schema 与 AI 查询已记结果或显式缺口。
4. **分析**。分开写、不要混：技术（可抓取/索引/性能/URL）、关键词意图与优先级、竞品差距、内容缺口、页内要素、AI 可见度、schema 与内链。按业务影响、工作量、买家意图、对上游架构的依赖排 P0/P1/P2。量表、表结构与页类型：读 `references/methodology.md`。完成：每条建议能指回收集里的 URL 或查询串；High+P0 有具体页 URL 与可执行修复步骤。
5. **落盘**。写入下方路径与模板。策略与分析用简体中文；面客句子、URL、schema 字段名、文件名按产品上下文（本仓库文件名保持英文）。完成：主稿含指定 8 节且非空；表或 JSON 达最低行数、每行 `source` 非空；文末 5–10 条可验证断言；教学支架原文零出现。

## 默认

- 本 skill 产出进 `deliverables/marketing/02-seo/`。不要用它做纯站点架构规划或审计后的内容日历。
- 目标渠道与目标站点技术栈以产品上下文为准，不在本文件写死平台。平台锁死的 URL 形态不要建议改掉。
- 检索量、CPC、排名、可见度分数只来自：产品上下文、用户本轮提供（含其导出的搜索控制台/分析数据）、已搜索或已抓取的公开页。没有数字就写「未在来源出现」，禁止估计后当事实。
- 抓取未见 JSON-LD 不得写成「无 schema」；标「需用富结果测试复核」。
- 表格式交付物每行有 `source` 或 `evidence`。终稿禁止占位 URL 与 `[TODO]` 类占位串。
- 上游竞品稿缺失时，在本审计内用网页搜索查证至少 3 个可访问竞品域名，或打开 `skills/marketing-competitor-intelligence/SKILL.md`（文件存在时）按其步骤补名单。需要隔离时 dispatch a subagent, else do it inline。不要回跳编排器。

## 写法

- 先过收集门再分析。门未过：只写缺口，不下结论。
- 关键词按 Informational / Commercial / Transactional 分组，并映射目标页；A/P0 必须能对应品类营收路径。
- 技术问题写到操作步骤（哪条 URL、改什么、怎么验证），不写空泛「加强 SEO」。
- 内容缺口每条绑定一条收集阶段的目标词与漏斗阶段。
- B2B 页内审计看规格、起订量、交期、贸易条款、认证，不套用注册或免费试用口吻。

## 产出

主文件 `deliverables/marketing/02-seo/seo-audit.md`：

```markdown
# SEO 审计

- source: 台账 product_context（不粘贴原文）
- site_url:
- stack:
- accessed:

## 执行摘要

## 来源

| 声明 | URL 或查询串 | 访问日期 | 摘录 |
| --- | --- | --- | --- |

## 技术 SEO 审计报告

## 关键词策略

## 竞品 SEO 差距分析

## 内容机会分析

## AI 搜索可见度诊断

## Schema 与架构建议

## 行动计划（P0 / P1 / P2）

## 缺口

## 可验证断言

## 下一步
```

同目录一并写入（列与最低行数见 `references/methodology.md`）：

- `seo-audit-data.xlsx` — 可从 `templates/seo-audit-data.xlsx` 复制后填；不能写表时改同目录 `seo-audit-data.json`
- `execution/keyword-master-list.md`
- `execution/technical-audit-checklist.md`
- `execution/page-seo-templates.md`
- `execution/content-gap-priorities.md`
- `execution/competitor-seo-data.md`
- `execution/ai-visibility-audit.md`
- `execution/schema-implementation-checklist.md`

用户点名独立 GEO 方案、JSON-LD 片段或内容日历时，分别打开 `skills/marketing-ai-seo/SKILL.md`、`skills/marketing-site-and-schema/SKILL.md`、`skills/marketing-content-strategy/SKILL.md`（均须文件存在），不在本审计里另起一套。

## 例子

> 仅供理解，禁止引用到输出。

抓取到产品页 title 只有品牌名、H1 为欢迎语。审计写「title 未含品类主检索词（来源：该页 URL，日期）」，不写「SEO 很差」。导航是自造品类、公开货架却用行业名（家用储能 / 工商业储能一类）时，关键词表与 H1 对齐行业词，并按「品类 × 品牌」两轴核类型列表页；缺页写成内容缺口（目标词=该类型行业名，来源：竞品分类 URL），不把内部标签当主检索词，也不用「补博客」顶替列表页。兼容套装在竞品是一级类、本站没有对应列表时，同样记缺口，不并进品牌墙。

目录可抓、价格登录后才见：技术项写「价格门不等于 robots 挡目录」，不把无价目录判成薄内容。抓取未见 JSON-LD 时写「需用富结果测试复核」，不写「无 schema」。路径大小写会 404 的栈，不建议改掉锁死的 URL 形态。

FAQ 页问句成排、答句点进工单或知识库：AI 可见度写「页上无机器可读答句，查询抽不到答案（来源：该 FAQ URL + AI 查询串）」，不写「FAQ 条数不够」。页上可见问句与 FAQPage 条目对不上时，schema 建议写成对齐可见 FAQ，不写「再堆问句」。店级桶（下单 / 发货 / 账号）与产品页问（接线 / 配组）分目标页；informational 查询映射学院或工具页，产品页不扛百科。不要把本节句子粘进交付物。

## 易错

- 没读产品上下文就按通用 SEO 清单开写。
- 把教学例子或模型记忆当检索量、排名或流量。
- 只交 Markdown，漏掉已承诺的表或执行附件。
- 凭一次抓取断定没有 schema。
- 关键词只堆量不分类、不映射目标页。
- 建议改掉目标站点技术栈锁死的路径层级。
- 竞品只看首页，或用占位域名。
- AI 可见度只测品牌词，或打主观分数。
- 技术问题不给页面级 URL 与验证方法。
- 回跳编排器或未完成收集门就写行动计划。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 页面清单、≥50 词（每条 `source`）、≥20 条 SERP、≥3 家竞品、schema 三类页、≥5 条 AI 查询均已记录或显式缺口
- [ ] 检索量与排名未编造；未见标记未写成「无 schema」
- [ ] 主稿 8 节齐全；建议均能回溯 URL 或查询串；P0 含具体修复步骤
- [ ] 产出在 `deliverables/marketing/02-seo/`；表或 JSON 达最低行数且 `source` 非空
- [ ] 终稿无占位串；教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
