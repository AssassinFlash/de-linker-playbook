---
name: marketing-site-and-schema
description: >
  Use when the user asks for site architecture, sitemap, navigation, URL
  structure, schema markup, structured data, JSON-LD, information
  architecture, breadcrumbs, 网站架构, 站点结构, 结构化数据, or a B2B
  website IA and Schema.org plan, including phase 2 SEO work. Read the
  ledger product_context; crawl the live site plus robots, sitemap, and
  at least two competitor URL trees; map taxonomy, URLs, internal links,
  inquiry paths, and JSON-LD by page type to the target site stack named
  in context; write the strategy document and blueprint workbook under
  deliverables/marketing/02-seo/. Invent no URLs or schema facts. Not for
  keyword-only audits, conversion copy, paid ads, or phase navigation.
---

# 站点架构与结构化数据

根据已读产品上下文与已抓取站点证据，设计信息架构、URL、导航、内链与 Schema.org 标注，落到 `deliverables/marketing/02-seo/`。先抓后设计；缺证据写缺口，不编造。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化。
2. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。存在则读 `deliverables/marketing/01-foundation/` 的定位与竞品稿，以及 `deliverables/marketing/02-seo/` 的审计与程序化页面矩阵。完成：能指出品类、目标市场、买家角色、站点域名、目标站点技术栈各依据哪几条；原文不拷进本仓库。域名或技术栈未在上下文出现则用网页搜索查证公司站点；仍缺则停并写缺口，不编造 URL 或平台。
3. **收集**。用网页搜索查证；需要原文时抓取指定 URL 的正文（含动态页）。默认先搜再抓。本站：URL 树、首页导航与页脚、目录/筛选、关于与联系、`/robots.txt`、`/sitemap.xml`、渲染 HTML 里的 `application/ld+json`。竞品：至少 2 个域名的 URL 分类、至少 1 个产品页或列表页的 schema。多域名并行时 dispatch a subagent, else do it inline。搜索不可用则停止并写缺口。查询清单与数据门：读 `references/methodology.md`。完成：本站清单、现有 schema 审计、≥2 竞品结构、≥1 竞品 schema、平台路由约束均已记录；客户端注入的 JSON-LD 标「需服务端或实渲染核验」。
4. **分析**。先记目标站点技术栈的固定路由，再设计 2–4 级分类、URL、导航与询盘、内链、按页 schema。不得违反平台路由。薄页或近重复页不标为可索引。字段表、JSON-LD 骨架、工作表列：读 `references/methodology.md`。完成：无孤立页；每个产品映射到 ≥2 个列表/分类；每条架构建议能回溯步骤 3 的 URL 或查询。
5. **落盘**。写入下方路径。策略与分析用简体中文；URL、schema 字段、handle 用英文。完成：主文档含且仅含 7 个指定章节；工作簿四表各 ≥20 行且 `source` 非空，或已写等价 JSON 并标明未能出表的原因；教学支架原文零出现；文末可验证断言成立。

## 默认

- 产品事实只读 `product_context`，不在本仓库另存档案。
- 目标渠道与目标站点技术栈以产品上下文为准，不预设某一电商或建站平台。
- 查证默认一条能力：用网页搜索查证。需要原文时抓取指定 URL。用户已配置网页采集服务时，才用它抓取公开页。缺搜索则停并写缺口，不编造。
- 未完成收集数据门不得进入分析。
- 终稿禁止 `[YOUR_...]`、纯数字 ID 路径、未声明 template 的占位 URL。未确定值用双花括号字段名并标明 template，或写「未在上下文出现」。
- 表每行有 `source` 或 `evidence`。JSON 若写，须含 `site.pages[]` 与 `schema.implementations[]`。

## 写法

- 先全站清单后设计，禁止凭记忆画信息架构。
- 分类 2–4 级：品类 → 应用或行业 → 属性 → 规格。标签前缀与筛选项同步（`type:` / `application:` / `attribute:` / `market:`）。
- URL：小写、连字符、商业路径不含日期、handle 描述性。
- 每类主要页面指向一个主行动（询价 / 样品 / 目录），表单字段服务项目型采购，不用注册试用口吻。
- 内链：无孤立页；产品 ↔ 案例 ↔ 指南 ↔ FAQ 成簇；枢纽页链到辐条页。
- 多 schema 同页用 `@graph`，不重复平台已输出的类型。产品 JSON-LD 含制造属性：`material`、MOQ、交期、`manufacturer`。
- 插入点写主题模板 head 或等价位置（以目标站点技术栈为准），并给出 Rich Results Test 与 Schema.org Validator 验证路径。

## 产出

主文件：

- `deliverables/marketing/02-seo/site-and-schema.md`
- `deliverables/marketing/02-seo/site-schema-blueprint.xlsx`（从 `templates/site-schema-blueprint.xlsx` 复制后填；不能写表时改同目录 `site-schema-blueprint.json`）
- 可选：`deliverables/marketing/02-seo/site-schema-blueprint.json`

```markdown
# 站点架构与结构化数据

- domain:
- platform: 目标站点技术栈（以产品上下文为准）
- source: 台账 product_context（不粘贴原文）
- accessed:

## 现状评估

## 推荐站点架构

## 产品分类与标签规范

## 询盘转化路径

## 内链策略

## Schema 实施方案

## 行动计划

## 来源

| 声明 | URL 或查询 | 访问日期 | 摘录 |
| --- | --- | --- | --- |

## 缺口

## 可验证断言
```

工作表（列名与最低行数见 `references/methodology.md`）：Page Inventory、Proposed Structure、Schema Mapping、Internal Links。Schema Mapping 的插入点列名为 `insertion_point`。

执行附件按需同目录：`sitemap-structure.md`、`navigation-spec.md`、`platform-collections.md`、`page-wireframes.md`、`schema-code-snippets.md`、`page-schema-map.md`、`redirect-map.md`、`validation-checklist.md`。规格见 `references/methodology.md`。

## 例子

> 仅供理解，禁止引用到输出。

对标抓到两种公开面：目录可浏览、价格登录后可见；或手册站与下单门户分域。现状评估应分条记下两种及各自 URL，推荐架构按上下文技术栈只选一种落地；不要把登录墙后的目录画成可索引页，也不写「全面升级信息架构」。

输入写竞品主导航按行业词分品类（Heimspeicher / Gewerbespeicher 并列），第二轴是品牌文件夹，应用（耦合、户内户外）是筛选项。成稿应改成 2–4 级：品类 → 应用或行业 → 属性，标签前缀与筛选项同步，每个产品映射 ≥2 个列表；不要用单一「储能」列表堆货，也不要按最宽竞品 mega-menu 硬铺空栏目。套装若在对标里是一级栏目，可单列列表，不编造未出现的套装 URL。URL 用小写连字符行业词 handle（如 `/home-storage/`、`/commercial-storage/`），不要日期、纯 ID，也不要同一语言站混用未核验外文 slug。

输入写知识/学院/工具在主导航与店并列。内链应改成产品 ↔ 指南 ↔ FAQ 成簇，学院页不得孤立。询盘主行动写成询价 / 样品 / 目录，表单收项目采购字段；不要写成注册试用。终端访客有入口则写成转给安装商的路由，不要混进贸易目录。

输入写站点 FAQ 是账号/订货/货运问、产品页 FAQ 是安装配套卡点。成稿应分层：产品页只放订货疑虑与临门一脚，店级采购发货退货进站点 FAQ，升档问不进产品页。批发现场回答交易问，技术与保修对口方写制造商并标缺口；不要把制造商症状题搬进本站 FAQPage。问答都在本页且答句有密度才标 FAQPage；只有题干、点进知识库的页面写成路由器，不标 FAQPage。

抓到首页没有 Organization JSON-LD、产品页只有 Offer、价格在页上是询价或登录可见。建议写成「首页补 Organization + WebSite；产品页用 @graph 补 Product，Offer 与页上一致、价格字段标缺口」；不写公开价，不把库存状态写进 schema 当卖点，也不把本站 Organization 写成制造商。不要把本节句子写入交付物。

## 易错

- 未完成数据门就画架构。
- 把客户端注入的 JSON-LD 当成已对爬虫生效。
- 用单一列表堆全部产品，造成孤立页或无主题簇。
- URL 含日期、纯 ID、大写或下划线，或层级超过 4 级。
- 只给产品页写 schema，忽略首页 Organization / WebSite、联系页 LocalBusiness、FAQPage。
- 筛选项与标签前缀不同步。
- 近重复列表全部设为 indexable，不指定 canonical 或 noindex。
- JSON-LD 留未声明的 `[YOUR_...]` 或 `item-123`。
- 推荐结构违反目标站点技术栈的固定路由。
- 把教学例子原文写入交付物。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 本站已用 URL 树 + sitemap 清单化；首页、产品或列表、联系页已做 schema 审计
- [ ] ≥2 个竞品结构带 source URL；≥1 个竞品 schema 已摘录
- [ ] 目标站点技术栈路由约束已记录；分类无孤立页；产品映射 ≥2 个列表
- [ ] 询盘 CTA 与表单字段覆盖主要页面类型
- [ ] 产品 JSON-LD 含 material、MOQ、交期、manufacturer 中至少两项实填或已标缺口
- [ ] 主文档 7 章与工作簿（或等价 JSON）在 `deliverables/marketing/02-seo/`；每行 `source` 非空
- [ ] 无未声明占位符；教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
