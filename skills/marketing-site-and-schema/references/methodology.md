# 站点架构与结构化数据方法

读本文件前先确认 `SKILL.md` 已判定本 skill 适用。查询清单、数据门、平台约束、分类与 URL 模式、schema 对照、工作表列、执行附件与可验证断言以本文为准。

## 目录

- [输入](#输入)
- [收集](#收集)
- [分析](#分析)
- [交付](#交付)
- [反模式](#反模式)
- [质量闸门](#质量闸门)
- [可验证断言](#可验证断言)

## 输入

先读台账 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；需要参数再读同目录 `fact-base/`）。存在则读，不复制进本仓库：

- `deliverables/marketing/01-foundation/product-positioning.md`
- `deliverables/marketing/01-foundation/competitor-analysis.md`
- `deliverables/marketing/02-seo/seo-audit.md`
- `deliverables/marketing/02-seo/programmatic-seo.md`

分析前核对（缺则写入缺口，不编造）：

1. 要审计的站点 URL
2. 目标站点技术栈（以产品上下文为准）
3. 目录规模：SKU、变体或系列数量
4. 优先买家类型
5. 必须保留的既有 URL（供 301 规划）

## 收集

默认一条能力：用网页搜索查证。需要原文时抓取指定 URL 的正文（含动态页）。用户已配置网页采集服务时，才用它抓取公开页。搜索不可用则停止并写缺口，不编造、不并列多引擎菜单。多域名并行时 dispatch a subagent, else do it inline。每条记下 URL、访问日期、摘录。

### 本站

| 能力 | 目标 | 记录 |
| --- | --- | --- |
| 抓取站点 URL 清单 | 产品上下文中的域名 | 全站页面与 URL 树 |
| 抓取指定 URL | 首页 | 导航、页脚、主 CTA |
| 抓取指定 URL | 目录/列表或等价路径 | 分类、筛选、产品卡片 |
| 抓取指定 URL | 关于、联系、FAQ | 信任信号、表单、已有 schema |
| 抓取指定 URL | `/robots.txt` | 禁止抓取路径、规则 |
| 抓取指定 URL | `/sitemap.xml` | 页面清单与索引范围 |

在渲染 HTML 中查找 `application/ld+json`。客户端注入的 JSON-LD 可能对爬虫不可见；这些页标「需服务端或实渲染核验」。

### 竞品结构

| 能力 | 目标 | 记录 |
| --- | --- | --- |
| 抓取站点 URL 清单 | 竞品域名 1 | URL 分类与列表层级 |
| 抓取站点 URL 清单 | 竞品域名 2 | 同上 |
| 抓取指定 URL | 竞品产品页 | schema 类型、title/H1、内容深度 |
| 抓取指定 URL | 竞品列表页 | 筛选、内链、面包屑 |

### 最佳实践查询

把产品上下文的品类与目标站点技术栈代入，不写死某一建站平台名：

1. B2B 制造网站信息架构
2. 目标站点技术栈的 B2B 站点结构（以产品上下文的平台字段为准）
3. B2B 供应商 JSON-LD
4. 供应商信息架构案例
5. 制造产品 Schema.org 实现

### 数据门

未齐下列项不得进入分析：

- [ ] 本站全页清单来自 URL 树与 `sitemap.xml`
- [ ] 首页、产品或列表页、联系页已做 schema 审计
- [ ] ≥2 个竞品站点结构已映射
- [ ] ≥1 个竞品 schema 已摘录
- [ ] 目标站点技术栈的 URL 约束已记录

## 分析

### 平台约束

先从已抓取 URL 与平台公开文档记录固定路由，再设计分类。常见约束类型（选用与目标站点技术栈匹配的一行，不把某一平台当默认）：

| 约束类型 | 典型路径形态 | 设计含义 |
| --- | --- | --- |
| 商品路径扁平 | 所有 SKU 同级；列表靠标签或集合页分层 | 层级做在列表 + 标签，不伪造嵌套产品路径 |
| 分类可嵌套 | 分类基座可改 | 可把应用/行业做成分类或子分类 |
| 完全自定义 | 任意模式 | 必须核验路由与 canonical |

不要推荐违反固定路由的结构。

### 分类

按目录规模与买家意图建 2–4 级：

```
L1: 品类（列表 / 分类）
  L2: 应用或行业（列表 + 标签）
    L3: 属性 / 变体（标签或子列表）
      L4: 规格 / 尺寸（变体或详情块）
```

每个产品带齐相关标签。命名约定（值取产品上下文字段，不在 skill 里填）：

| 前缀 | 形态 |
| --- | --- |
| `type:` | `type:` + 品类字段 |
| `application:` | `application:` + 应用字段 |
| `attribute:` | `attribute:` + 属性字段 |
| `market:` | `market:` + 目标市场字段 |

筛选项与此前缀同步。

### URL

| 页面类型 | 模式 | 说明 |
| --- | --- | --- |
| 列表（品类） | `/{catalog}/{handle}` 或平台等价路径 | handle 描述性 |
| 列表（应用） | `/{catalog}/{application}` | 与品类列表交叉，薄页不索引 |
| 产品 | `/{product}/{handle}` | 禁止纯数字 ID、禁止日期 |
| 静态页 | `/{pages}/{slug}` 或平台静态路径 | about、工厂参观、联系 |
| 项目 / 案例 | `/{case-studies}/{slug}` 或博客子路径 | 链回至少 1 个产品 |
| 资料 / 指南 | `/{guides}/{slug}` 或资源博客 | 枢纽链到辐条 |
| 市场页 | `/{markets}/{market}` 或静态市场页 | 关键词来自产品上下文 |

规则：小写、连字符、商业 URL 不含日期、不用 ID-only handle、层级不超过 4 级。

### 导航与询盘

每类主要页面指向一个主行动：

| 行动 | 触发 | 去向 |
| --- | --- | --- |
| 询价 | 产品/列表主 CTA | 联系页，含项目字段 |
| 即时通讯询盘 | 浮钮 + 产品页 | 以目标市场为准的即时通讯链接，预填品名 |
| 索样 | 产品页次 CTA | 索样页 |
| 下载目录 | 资料区 | 门控 PDF 表单 |

询盘字段：项目类型、数量、目的国、时间、贸易条款、参考图上传。桌面 5–7 字段；不用注册或免费试用口吻。

### 内链

- 无孤立页：每个产品属于 ≥2 个列表；每个案例链到 ≥1 个产品。
- 主题簇：产品 → 相关项目 → 材料指南 → FAQ → 相关产品。
- 枢纽-辐条：品类列表、应用列表、资料枢纽链到辐条页。

### Schema 对照

| 页面 | 类型 | 用途 |
| --- | --- | --- |
| 首页 | `Organization`、`WebSite` | 品牌实体、站点搜索框 |
| 产品 | `Product` + `AggregateOffer` 或 `Offer` | 富结果、规格可见 |
| 列表 | `ItemList` 或 `BreadcrumbList` | 导航清晰 |
| 关于 / 联系 | `Organization` + `LocalBusiness`（有展厅/工厂时） | 信任 |
| FAQ | `FAQPage` | SERP / 答案资格 |
| 项目 / 案例 | `ImageObject`、`Article` | 作品可见 |
| 面包屑 | `BreadcrumbList` | 每个可索引页 |

同页多种类型用 `@graph`，不重复平台已输出的类型。

产品 JSON-LD 骨架（有事实填事实；未确定标明 template 或「未在上下文出现」）：

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{{PRODUCT_NAME}}",
  "description": "",
  "image": "",
  "brand": { "@type": "Brand", "name": "{{BRAND}}" },
  "manufacturer": {
    "@type": "Organization",
    "name": "{{BRAND}}",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "{{ORIGIN}}"
    }
  },
  "material": "{{MATERIAL}}",
  "color": "{{FINISH}}",
  "offers": {
    "@type": "AggregateOffer",
    "lowPrice": "",
    "highPrice": "",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  },
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "MOQ", "value": "{{MOQ}}" },
    { "@type": "PropertyValue", "name": "Lead Time", "value": "{{LEAD_TIME}}" }
  ]
}
```

`{{ORIGIN}}`、`{{MATERIAL}}` 取产品上下文对应字段，不在本文填值。

### 审计记录

对每个已审页面记下：已有类型、缺失必填属性、重复或冲突 schema、是否客户端注入。

## 交付

路径根：`deliverables/marketing/02-seo/`。每条推荐引用收集阶段的 source URL 或查询。

### 策略文档七章

`site-and-schema.md` 含且仅含：

1. 现状评估 — 页面清单、现有 schema、竞品结构对照
2. 推荐站点架构 — 分类层级、URL 映射、导航
3. 产品分类与标签规范 — L1–L4、标签命名、筛选
4. 询盘转化路径 — CTA 图与表单字段
5. 内链策略 — 枢纽-辐条与主题簇规则
6. Schema 实施方案 — 按页类型、JSON-LD 插入方法、验证步骤
7. 行动计划 — P0 / P1 / P2，指向执行附件

### 工作簿

`site-schema-blueprint.xlsx`，可从 `templates/site-schema-blueprint.xlsx` 复制。不能写表时写同目录 `site-schema-blueprint.json`，并符合 `schemas/site-schema-blueprint.schema.json`。

| 工作表 | 列 | 最低行数 |
| --- | --- | --- |
| Page Inventory | `url`, `page_type`, `title`, `meta_description`, `h1`, `current_schema`, `issues`, `source` | 20 |
| Proposed Structure | `page_type`, `url_pattern`, `example_url`, `parent_hub`, `priority`, `index_strategy`, `content_source`, `source` | 20 |
| Schema Mapping | `page_type`, `schema_types`, `required_properties`, `insertion_point`, `validation_url`, `priority`, `source` | 20 |
| Internal Links | `from_url`, `to_url`, `anchor_text`, `link_type`, `source` | 20 |

`priority` 仅 P0 / P1 / P2。`link_type` 仅 nav / related / breadcrumb / hub。`source` 每行非空。Schema Mapping 的 `required_properties` 对产品行须含 `material`、MOQ、交期、`manufacturer` 中至少两项。

JSON 形状（可选，与表等价）：

```json
{
  "site": {
    "domain": "",
    "platform": "",
    "audit_source": "url-tree + sitemap.xml",
    "pages": [
      {
        "url": "",
        "page_type": "collection",
        "proposed_url": "",
        "taxonomy_level": 1,
        "priority": "P0",
        "index": true,
        "source": ""
      }
    ]
  },
  "schema": {
    "audit_date": "",
    "implementations": [
      {
        "page_type": "product",
        "schema_types": ["Product", "AggregateOffer"],
        "insertion_point": "theme-head",
        "priority": "P0",
        "source": ""
      }
    ]
  }
}
```

`platform` 填目标站点技术栈，不写死某一建站品牌。`insertion_point` 写主题模板 head 或等价位置。

### 执行附件

按需写入同目录：

- `sitemap-structure.md` — URL 地图：标题、父枢纽、列表归属
- `navigation-spec.md` — 顶栏、巨型菜单、页脚、面包屑、移动导航
- `platform-collections.md` — 分类/列表创建清单：handle、排序、筛选
- `page-wireframes.md` — 首页、产品页、列表页、联系页内容块
- `schema-code-snippets.md` — 可复制 JSON-LD：Organization、Product、FAQPage、BreadcrumbList、LocalBusiness、WebSite
- `page-schema-map.md` — 页面类型 ↔ schema 类型
- `redirect-map.md` — 重构所需 301
- `validation-checklist.md` — Rich Results Test 与 Schema.org Validator 步骤

## 反模式

1. 未抓本站就设计架构。
2. 推荐结构违反目标站点技术栈的固定路由。
3. 制造孤立页。
4. JSON-LD 输出 `[YOUR_...]` 且未声明 template。
5. 重复平台已有 schema，不用 `@graph` 补充。
6. 薄页或近重复页标为可索引。
7. 通用 URL 如 `/products/item-123`。
8. 跳过竞品 schema 就推荐类型。

## 质量闸门

- 本站已用 URL 树与 sitemap 清单化
- ≥2 个竞品结构带 source URL
- 首页、产品或列表、联系页 schema 已审计
- 目标站点技术栈 URL 约束已记录
- 无孤立页；产品映射 ≥2 个列表
- 主要页面类型已定义询盘 CTA 与字段
- JSON-LD 含制造属性或已标缺口
- 每行有 `source`；无未声明占位 URL
- 工作簿四表各 ≥20 行，或 JSON 等价且已说明未能出表的原因

## 可验证断言

1. `site-and-schema.md` 含且仅含 7 个必需章节，每条建议下方有来源。
2. Page Inventory ≥20 行，`source` 100% 非空。
3. Proposed Structure ≥20 行，`priority` 仅为 P0/P1/P2。
4. Schema Mapping ≥20 行，产品行 `required_properties` 含 material、MOQ、交期、manufacturer 中至少两项。
5. Internal Links ≥20 行，`link_type` 在 {nav, related, breadcrumb, hub} 内。
6. 至少引用 2 个竞品域名及具体 source URL。
7. schema 审计覆盖首页、产品或列表、联系页，每类记录 existing / missing / duplicate / client-side。
8. JSON-LD 同时出现 material、MOQ、交期、manufacturer，且未使用未声明的 `[YOUR_...]`。
9. 产品 URL 模式为描述性 handle，不含纯数字 ID 或日期路径。
10. 终稿无未标明 template 的 `[YOUR_...]`，也无 `item-123`、`page-1` 类通用 URL。
