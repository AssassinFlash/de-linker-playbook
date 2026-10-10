# 站点架构与结构化数据

- domain: de-linker.com
- platform: WordPress + WooCommerce（产品上下文：WooCommerce Store API、`/product/<slug>/`；线上 HTML 含 WooCommerce 类名）
- source: 台账 product_context（不粘贴原文）
- accessed: 2026-10-10

## 现状评估

本站是面向安装商、承包商与 EPC 的德国贸易供货站，品类为光伏混合逆变器、LFP 电池与成套储能，目标市场为德国及欧洲贸易伙伴。依据：产品上下文中的域名与 WooCommerce 路径；首页 H1「Linking Value. Serving You.」与页脚「Linker Technology GmbH, Steinfeldstraße 3, 39179 Barleben」（https://de-linker.com/，2026-10-10）。

**URL 树（先清单后设计）**

- `robots.txt` 禁止 `/wp-admin/`、购物车加购查询与 WooCommerce 上传目录；Sitemap 指向 `https://de-linker.com/sitemaps.xml` 与 `https://de-linker.com/de-sitemap.xml`。请求 `/sitemap.xml` 会落到 `sitemaps.xml`。来源：https://de-linker.com/robots.txt。
- 英文索引含 4 个子图：`post-sitemap1.xml`、`page-sitemap1.xml`、`product-sitemap1.xml`、`product_cat-sitemap1.xml`。来源：https://de-linker.com/sitemaps.xml。
- 页面 loc 25 条（含 `/cart/`、`/my-account/`）；文章 loc 11 条（含 `/blog/`）；产品分类 loc 10 条；产品 loc 105 条。来源：各子 sitemap，2026-10-10。
- 产品上下文写明 Store API 约 224 个 SKU。sitemap 产品数少于该口径，差额记入缺口，不把 224 当作可索引 URL 数。
- 固定路由（已抓取，不得改造嵌套产品路径）：
  - 产品：`/product/{slug}/`（德文 `/de/produkt/{slug}/`）
  - 分类：`/product-category/{handle}/`，子分类最多一层，如 `/product-category/commercial-storage/all-in-one-systems/`
  - 目录枢纽：`/products/`（不是默认 `/shop/`）
  - 方案：`/solution/`、`/solution/residential-storage|commercial-storage|utility-storage/`
  - 语言：`hreflang` 英德对，德文前缀 `/de/`
- 主导航（首页渲染）：Products（Home Storage / Commercial Storage 及子项 / Inverters / EMS & Monitoring / EV Chargers / Accessories）· Solutions（Residential / Commercial & Industrial / Utility-Scale）· Plan with Linker（Advisor / Planner / Site Detail）· Services · For Partners（Installers / EPCs）· About（About / Blog / FAQ & Documents）。主 CTA：Contact Linker、Request a System Quote、Trade Portal。来源：https://de-linker.com/。
- 页脚主体：Solutions / Services / Plan with Linker / Account / Contact；法律页 Imprint、Privacy、Terms of Sale、Refund & Returns。销售邮箱 `sales@de-linker.com`。

**现有 schema 审计（existing / missing / duplicate / client-side）**

| 页面 | existing | missing | duplicate | client-side |
| --- | --- | --- | --- | --- |
| 首页 https://de-linker.com/ | `WebSite`、`Organization`（legalName Linker Technology GmbH，Barleben 地址，电话与 `sales@de-linker.com`） | `WebSite.potentialAction`（站内搜索）；`Organization.sameAs`；邮箱已在 ContactPoint | 两段独立 script，靠 `@id` `#website` / `#organization` 互指，未见重复类型冲突 | 服务端 `<script type="application/ld+json">`，非客户端注入 |
| 产品 https://de-linker.com/product/goodwe-esa-gw10k-eha-g20-10-kw-single-phase-power-module/ | `Product` + `Brand` + `manufacturer` Organization（品牌名 GoodWe）+ `Offer`（仅 `url` + `InStock`，无价格） | `BreadcrumbList`；`material`；MOQ / 交期 `additionalProperty`；与页上一致的价格字段（页上为贸易净价/询价，价格标缺口） | 未见第二份 Product | 服务端 JSON-LD |
| 产品 https://de-linker.com/product/ecoflow-ocean-2-battery-8-0-kwh-ef-bd-8-s2/ | 同上结构；`description` 含 LiFePO4，但 schema 无 `material` | 同上 | 未见重复 Product | 服务端 JSON-LD |
| 列表 https://de-linker.com/product-category/home-storage/ 等 | 仅 `BreadcrumbList` | `ItemList` 或 CollectionPage | 无 | 服务端 |
| 目录枢纽 https://de-linker.com/products/ | `CollectionPage` + `BreadcrumbList` | `ItemList` | 无 | 服务端 |
| 联系 https://de-linker.com/contact/ | `ContactPage`/`WebPage` + 内嵌 `Organization` | `LocalBusiness`（有实体地址但未标营业点类型） | Organization 与首页 `#organization` 未用同一 `@id` | 服务端 |
| About https://de-linker.com/about/ | `AboutPage`/`WebPage` + Organization | 与首页 Organization `@id` 对齐 | 无 | 服务端 |
| FAQ 下载 https://de-linker.com/faq-download/ | `CollectionPage` | 不标 `FAQPage`（该页是资料库而非页内问答） | 无 | 服务端 |
| 方案/角色页 `/solution/*`、`/for-installer/`、`/for-epc/`、`/services-support/` | 无 JSON-LD | `WebPage` + `BreadcrumbList`；有页内问答时再评估 FAQPage | 无 | 无脚本 |

抽查：`https://de-linker.com/product/goodwe-gw10k-et/` 在 2026-10-10 被 301 到 `/product-category/inverters/`。产品上下文 SKU 清单里该 permalink 仍在。保留 URL 规划必须覆盖这类失效产品路径。

**竞品结构对照**

1. Memodo（https://www.memodo.de/photovoltaik/，2026-10-10）：一级按品类切分——Solarmodule、Wechselrichter、Heimspeicher、Gewerbespeicher、Energiemanagementsysteme、Ladestationen、Unterkonstruktion、Wärmepumpen、Zubehör；品牌作为二级文件夹（`/photovoltaik/module/{brand}/`）；知识放 `/m/photovoltaik-wissen/heimspeicher/`。产品 URL 为 `/{slug}/{numeric-id}`（例：https://www.memodo.de/goodwe-bat112/13739）。Heimspeicher 列表：https://www.memodo.de/photovoltaik/heimspeicher/。该产品页服务端 HTML 无 `application/ld+json`，标「需服务端或实渲染核验」。
2. Krannich Solar Shop（https://shop.krannich-solar.com/en-de，2026-10-10）：一级按品类——Solar Modules、Inverters、Residential Storages、Inverter & Storage Sets、Commercial Storages、EMS、Mounting Systems、E-Mobility、Accessories。产品 URL `/{Name}/{numeric-id}`。列表页有 `BreadcrumbList` + 空壳 `Organization`。产品页有完整 `Product`（sku/mpn/image/description，电芯化学 LFP 写在描述中）。价格 CTA 为 Request price（登录后可见）。例：https://shop.krannich-solar.com/en-de/SigenStor-20.0-Energy-Controller-15.0-TP/0165154 、https://shop.krannich-solar.com/en-de/Residential-Storage。

对照结论：两家都以「住宅储能 / 工商业储能」并列品类，品牌与套装是第二轴或筛选，价格可登录墙。Linker 已有 Home Storage 与 Commercial Storage 分类，且产品路径扁平、价格走贸易门户——推荐架构只落 WooCommerce 固定路由，不把登录墙后的净价写进 Offer.price，不按最宽竞品菜单铺空栏目（模块、支架、热泵本站无货）。

## 推荐站点架构

平台约束先行（https://woocommerce.com/document/permalinks ，2026-10-10）：商品路径扁平，所有 SKU 同级 `/product/{slug}/`；层级做在 `product-category` 与标签，不伪造 `/product-category/.../product-slug`。分类可嵌套一层，本站已用于 Commercial Storage 与 Accessories 子类。

保留既有可索引 URL（供 301，禁止无证据改 handle）：

- `/`、`/products/`、`/product-category/home-storage/`、`/product-category/commercial-storage/` 及其两个子类、`/product-category/inverters/`、`/product-category/ems-monitoring/`、`/product-category/ev-chargers/`、`/product-category/accessories/` 及其两个子类
- `/solution/` 与三个应用页、`/for-installer/`、`/for-epc/`、`/about/`、`/contact/`、`/faq-download/`、`/services-support/`、`/blog/` 及 10 篇指南
- 德文 `/de/` 对等路径（`/de/loesung/heimspeicher/` 等）只作语言替身，不另做一套英文 IA

信息架构（2–4 级，映射到已存在 handle，不新造未核验 slug）：

```
L1 品类（WooCommerce product-category，可索引）
  home-storage
  commercial-storage
    L2 属性/形态：all-in-one-systems · battery-systems
  inverters
  ems-monitoring
  ev-chargers
  accessories
    L2 属性：meters-current-transformers · backup-power
L2 应用（WordPress 页面 /solution/*，可索引枢纽，不替代分类）
  residential-storage · commercial-storage · utility-storage
L3 属性（WooCommerce 标签/筛选，薄组合 noindex）
  phase · voltage-class · backup · chemistry
L4 规格（仅 PDP 区块与 JSON-LD additionalProperty）
```

主导航建议（与线上一致，只收紧交叉）：Products 走 L1 分类；Solutions 走应用页；不要把 Utility 画成可加购分类（线上写明 quoted per project）。Inverters 保持独立 L1（线上已是一级），通过标签 `application:residential` / `application:commercial` 交叉进两个应用枢纽，避免把全部逆变器堆进单一「储能」列表。

URL 规则：小写、连字符、无日期、无纯数字 ID。竞品 Memodo/Krannich 的数字 ID 路径不套用。未确定的新列表用 template `https://de-linker.com/product-category/{{handle}}/`，禁止未声明占位。

index / noindex：

- index：首页、`/products/`、10 个分类、3 个方案、角色页、About、Contact、FAQ 下载、Services、Blog 文章、sitemap 中的产品 PDP
- noindex 或登录墙：`/cart/`、`/my-account/`、`/compare-products/`、`/quote-configurator/`、`/proforma-request/`、筛选参数页（`?filter_*`）、空标签组合
- 失效产品（如 `/product/goodwe-gw10k-et/`）→ 301 到所属分类或替代 SKU，不留软 404

每个产品至少进 2 个列表：例如 ESA 功率模块 ∈ `inverters` + `home-storage`；BAT 机柜 ∈ `commercial-storage/battery-systems` + `commercial-storage`；电表 ∈ `accessories/meters-current-transformers` + `accessories`。Utility 容器级仅挂 `/solution/utility-storage/`，不新建无货分类。

## 产品分类与标签规范

| 级 | 前缀 | 值（取自线上分类名/方案名，不编造） | 筛选项同步 | 列表 URL |
| --- | --- | --- | --- | --- |
| L1 | `type:` | `type:home-storage` `type:commercial-storage` `type:inverter` `type:ems` `type:ev-charger` `type:accessory` | Products 菜单与 `/products/` 品牌+品类筛选 | `/product-category/{{handle}}/` |
| L2 应用 | `application:` | `application:residential` `application:commercial` `application:utility` | Solutions 菜单；分类页侧栏 | `/solution/{{handle}}/` |
| L3 | `attribute:` | `attribute:single-phase` `attribute:three-phase` `attribute:hv` `attribute:lv` `attribute:all-in-one` `attribute:backup` `attribute:lfp` | 分类筛选；薄页 noindex + canonical 回父分类 | 标签 URL 仅在 WooCommerce 产出后登记，未创建则「未在上下文出现」 |
| L4 | 规格 | kW / kWh / IP / 备份 kVA | 仅 PDP，不单独索引 | `/product/{slug}/` |
| 市场 | `market:` | `market:de` `market:eu` | 不单独做国家落地页（无证据） | 不新建 `/markets/` |

命名：标签与筛选项同一前缀同一值。Home Storage 的 H1 已是「Home Storage」，不要再混未核验的 Heimspeicher slug 到英文站。德文站沿用已核验 `/de/produkt-kategorie/` 对等路径（以德文 sitemap 为准），不在同一语言站混用。

套装：线上 Commercial Storage 子类 All-in-One Systems 已存在，可保留为 L2 列表，不编造未出现的套装 URL。

## 询盘转化路径

线上主行动已经是询价/门户，不是注册试用。联系页表单字段（https://de-linker.com/contact/，2026-10-10）：问题正文；意图（A question / Product guidance / Price & availability / Product documents / Discuss a project / Support for an order / Work with Linker）；Name；Reply email；Company（可选）；隐私同意。页上写明无需账号。页脚另有 `sales@de-linker.com`、`chester@de-linker.com`。

| 页面类型 | 主行动 | 去向 | 表单字段（项目采购） |
| --- | --- | --- | --- |
| 首页 | Request a System Quote | `/contact/?intent=offer` | 沿用意图=Discuss a project / Price；补项目类型、数量、目的国、时间（页上尚未出现，记缺口） |
| 分类 / `/products/` | 筛选后询价 | 同 Contact intent=offer，预填分类名 | 数量、目的国、贸易条款 |
| PDP | 询价（价格未进 schema） | Contact 带 `kind=product` 与 source URL（首页已用该模式） | 型号（预填）、数量、目的国、交期、参考图上传（上传未在联系页出现） |
| 方案页 | Request a project | `/contact/` 或 Planner | 应用类型、负荷/备份需求、时间 |
| Utility 方案 | 项目报价，不进购物车 | Contact / 人工 | 容量、并网点、时间；与线上「quoted per project」一致 |
| 角色页 Installer / EPC | 选型与供货对话 | Contact + `/linker-planner/` | 现场/项目字段 |
| 资料 | 下载目录（已无账号墙） | `/faq-download/` | 证书按订单索取（页上原文）；不要改成门控注册 |
| 复购伙伴 | Trade Portal | `/my-account/` | 登录后净价；该面 noindex |

即时通讯：页上未见 WhatsApp 链，不编造。桌面字段控制在 5–7 个：意图、姓名、邮箱、公司、项目类型、数量、目的国。不要用免费试用口吻。

终端访客：方案 FAQ 问「Does Linker install for end customers?」——若页内已回答，把终端入口写成转安装商，不混进贸易目录（需在方案页核验答句后再标 FAQPage）。

## 内链策略

规则：无孤立页；产品 ↔ 方案 ↔ 指南 ↔ 资料成簇；枢纽链辐条。

- 枢纽：`/products/` → 10 个分类；`/solution/` → 三个应用页；`/blog/` → 10 篇指南；`/faq-download/` → 资料。
- 分类 → 其下 PDP；PDP 面包屑 Home > Products > {Category} > {Product}（产品页目前缺 BreadcrumbList，P0 补）。
- 每个 PDP 至少链：所属两个分类、对应 `/solution/*`、一篇相关指南、FAQ 下载。例：ESA 模块 → `/product-category/inverters/` + `/product-category/home-storage/` + `/solution/residential-storage/` + `/installer-checklist-inverter-battery-pairing/`。
- 指南 → 至少一个产品或分类。已有文章 handle：`hybrid-inverter-vs-ac-coupled-storage`、`ci-storage-peak-shaving-backup-scalability`、`residential-storage-backup-self-consumption`、`size-battery-storage-residential-backup`、`installer-checklist-inverter-battery-pairing` 等（post-sitemap）。
- 角色页 `/for-installer/`、`/for-epc/` 链回方案与分类，避免学院/工具页孤立（Advisor / Planner / Design Canvas 从主导航与页脚互链）。
- 近重复：Home Storage 分类 vs Residential Solution——前者 index 商品，后者 index 应用叙事，互相链但 canonical 各指自身。

## Schema 实施方案

插入点：WordPress 主题 `wp_head` 或等价 JSON-LD 打印；产品补充用 WooCommerce `woocommerce_structured_data_product` 过滤器扩字段，**不**再输出第二份 `@type: Product`。同页多种类型用 `@graph`，并与首页已有 `#organization` / `#website` `@id` 对齐。验证：https://search.google.com/test/rich-results 与 https://validator.schema.org/ 。参考：https://schema.org/Product 、https://contentgecko.io/blog/woocommerce-structured-data 、https://woocommerce.com/document/permalinks 。

| 页面 | 类型 | 动作 |
| --- | --- | --- |
| 首页 | 已有 Organization + WebSite | 补 `sameAs`（未在上下文出现则留空）；可选 `SearchAction` 指向 `/products/#search-box` |
| PDP | 已有 Product + Offer | `@graph` 增 BreadcrumbList；`material` 有事实则填（电池描述已见 LiFePO4）；`additionalProperty` 增加 MOQ、Lead Time（值未在上下文出现则不输出该 PropertyValue）；`manufacturer` 保持品牌制造商，**不要**把 Linker Organization 写成制造商；Offer 不写公开价，价格字段标缺口；`InStock` 仅当页上可见供货状态时保留 |
| 分类 | BreadcrumbList | 可选 ItemList（仅首屏有稳定顺序的卡片）；薄筛选页不标 |
| `/products/` | CollectionPage | 保持；不要当单一堆货 ItemList 输出全部 105 URL |
| Contact / About | 已有 | Contact 可加 `LocalBusiness` 仅当确认展厅/仓库对公开放（页上有 Barleben 地址，开放时间未出现） |
| FAQ 下载 | CollectionPage | **不**标 FAQPage |
| 方案/角色 | 无 | 先 WebPage + BreadcrumbList；仅当问答都在本页且答句有密度时再 FAQPage |
| 指南 | 无 | `Article` + BreadcrumbList |
| 全站可索引页 | — | BreadcrumbList |

产品 JSON-LD 骨架（有事实填事实；template 已声明）：

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Product",
      "name": "{{PRODUCT_NAME}}",
      "sku": "{{SKU}}",
      "description": "{{DESCRIPTION}}",
      "image": "{{IMAGE_URL}}",
      "brand": { "@type": "Brand", "name": "{{BRAND}}" },
      "manufacturer": {
        "@type": "Organization",
        "name": "{{BRAND}}"
      },
      "material": "{{MATERIAL}}",
      "offers": {
        "@type": "Offer",
        "url": "{{PRODUCT_URL}}",
        "availability": "{{AVAILABILITY_URL}}",
        "priceCurrency": "EUR"
      },
      "additionalProperty": [
        { "@type": "PropertyValue", "name": "MOQ", "value": "{{MOQ}}" },
        { "@type": "PropertyValue", "name": "Lead Time", "value": "{{LEAD_TIME}}" }
      ]
    }
  ]
}
```

实填例（来自已抓产品页，非 template）：`name` GoodWe ESA GW10K-EHA-G20 (10 kW single-phase power module)；`sku` DLK-GOODWE-GW10KEHAG20；`brand`/`manufacturer` GoodWe；Offer 无价格。电池页描述含 LiFePO4，可将 `material` 标为 LiFePO4。`{{MOQ}}`、`{{LEAD_TIME}}` 未在产品上下文与该两页 JSON-LD 出现，禁止编造。`price` 不填。

WooCommerce 默认会输出基础 Product/Offer（https://contentgecko.io/blog/woocommerce-structured-data）。本站产品 JSON-LD 已存在，实施时只扩字段，禁止重复类型。

## 行动计划

**P0**

1. 产品页补 BreadcrumbList，与分类页已有面包屑同一结构。验证 Rich Results Test。
2. 产品 JSON-LD：有描述依据的 `material`；`manufacturer` 保持品牌；Offer 与页上询价一致、不写净价。
3. 失效 PDP（抽查 `/product/goodwe-gw10k-et/`）建 301 表，对照产品上下文 224 vs sitemap 105 的差额。
4. 联系表在 `intent=offer` 时增加项目类型、数量、目的国（仍无需注册）。

**P1**

5. 方案/角色/指南补 WebPage + BreadcrumbList；核验页内 FAQ 密度后再决定 FAQPage。
6. 标签前缀 `type:` / `application:` / `attribute:` / `market:` 与 `/products/` 筛选对齐；每个 SKU 映射 ≥2 个分类。
7. Organization `@id` 在 Contact/About 复用首页 `#organization`。
8. 德文 `de-sitemap.xml` 与英文子图做一次 URL 对账（hreflang）。

**P2**

9. 分类 ItemList 仅用于稳定排序的短列表；筛选薄页 noindex。
10. LocalBusiness 仅在确认对公地址可访问后添加。
11. `sameAs` 与 SearchAction 等增强字段，值未出现则不写。

执行附件：工作簿 `site-schema-blueprint.xlsx`；等价 JSON `site-schema-blueprint.json`；JSON-LD 片段见本章。未另写 sitemap-structure 等附件。

## 来源

| 声明 | URL 或查询 | 访问日期 | 摘录 |
| --- | --- | --- | --- |
| 本站域名、贸易定位、H1、导航、页脚地址 | https://de-linker.com/ | 2026-10-10 | H1 Linking Value. Serving You.；导航 Home Storage / Commercial Storage；页脚 Linker Technology GmbH, Steinfeldstraße 3, 39179 Barleben |
| robots 与 sitemap 入口 | https://de-linker.com/robots.txt | 2026-10-10 | Sitemap: https://de-linker.com/sitemaps.xml ；https://de-linker.com/de-sitemap.xml |
| 英文 sitemap 索引 | https://de-linker.com/sitemaps.xml | 2026-10-10 | post / page / product / product_cat 四个子图 |
| 分类 URL 清单 | https://de-linker.com/product_cat-sitemap1.xml | 2026-10-10 | 10 条 product-category loc，含 home-storage 与 commercial-storage 子类 |
| 产品 URL 数量 | https://de-linker.com/product-sitemap1.xml | 2026-10-10 | 105 条 `/product/` loc |
| 首页 WebSite + Organization JSON-LD | https://de-linker.com/ | 2026-10-10 | legalName Linker Technology GmbH；address Barleben；email sales@de-linker.com |
| 产品 Product+Offer | https://de-linker.com/product/goodwe-esa-gw10k-eha-g20-10-kw-single-phase-power-module/ | 2026-10-10 | sku DLK-GOODWE-GW10KEHAG20；manufacturer GoodWe；Offer 无 price |
| 电池描述含 LiFePO4 | https://de-linker.com/product/ecoflow-ocean-2-battery-8-0-kwh-ef-bd-8-s2/ | 2026-10-10 | description: 8.03 kWh nominal LiFePO4 battery module |
| 联系页表单与 schema | https://de-linker.com/contact/ | 2026-10-10 | 意图枚举含 Price & availability、Discuss a project；ContactPage JSON-LD |
| FAQ 下载非 FAQPage | https://de-linker.com/faq-download/ | 2026-10-10 | CollectionPage；H1 Technical documentation and trade rules on file |
| Memodo 品类树 | https://www.memodo.de/photovoltaik/ ；https://www.memodo.de/photovoltaik/heimspeicher/ | 2026-10-10 | Heimspeicher / Gewerbespeicher / Wechselrichter 等一级分类 |
| Memodo 产品 URL 形态 | https://www.memodo.de/goodwe-bat112/13739 | 2026-10-10 | H1 GoodWe BAT112；服务端无 ld+json |
| Krannich 一级品类 | https://shop.krannich-solar.com/en-de | 2026-10-10 | Residential Storages、Commercial Storages、Inverters 等 |
| Krannich Product schema | https://shop.krannich-solar.com/en-de/SigenStor-20.0-Energy-Controller-15.0-TP/0165154 | 2026-10-10 | @type Product；sku 0165154；描述含 Cell chemistry: LFP |
| WooCommerce 固定路由 | https://woocommerce.com/document/permalinks | 2026-10-10 | 默认 product 与 product-category 基座；商品可不嵌套分类 |
| WooCommerce Product JSON-LD 行为 | https://contentgecko.io/blog/woocommerce-structured-data | 2026-10-10 | 核心输出 name/image/sku/offers；制造属性需扩展 |
| Schema.org Product / additionalProperty | https://schema.org/Product | 2026-10-10 | additionalProperty 为 PropertyValue |
| B2B 制造站 IA（应用+产品线） | https://www.nopio.com/blog/b2b-website-design | 2026-10-10 | 产品页要规格与文档；能力与应用路径分开 |
| 产品上下文 SKU 规模与路径 | 台账 product_context（~/Documents/New/CONTEXT.md） | 2026-10-10 | WooCommerce Store API 规模与 `/product/<slug>/`；原文未复制 |

## 缺口

- 上游 `deliverables/marketing/01-foundation/` 定位稿、竞品稿与 `02-seo/seo-audit.md`、`programmatic-seo.md` 均为空（仅 .gitkeep）。本文件按烟测继续，未编造已批准审计结论。
- 产品上下文是文案工程词汇表，未单列 ICP 文件；买家角色取自线上 For Installers / For EPCs 与首页副文案。
- Store API 约 224 SKU vs 产品 sitemap 105 URL；哪些 SKU 有意不出索引未在上下文说明。
- `/product/goodwe-gw10k-et/` 已 301 到分类，全量失效 permalink 表未做。
- 产品 JSON-LD 无价格、无 MOQ、无交期；贸易净价在门户后，未抓登录后页面。
- Memodo 产品页服务端无 JSON-LD，竞品 schema 仅完整摘录 Krannich 一条。
- 方案页是否有足够密度的页内 FAQ 未逐条核验，故未标 FAQPage。
- 搜索摘录里部分营销页曾出现 Munich hub 表述，与首页/页脚/About meta 的 Barleben 不一致；结构化数据地址以已抓页脚为准，Munich 不写入 Organization。
- 联系表缺少数量、目的国、贸易条款、参考图上传。
- 开放时间、sameAs 社交 URL、站内 SearchAction 目标未在上下文出现。
- 德文分类基座的精确 path 未逐条与英文 10 个分类对账（仅确认产品为 `/de/produkt/{slug}/`）。
- 模板工作表列名为「Shopify Insertion Point」，与方法要求的 `insertion_point` 及「不以某一电商平台为默认」冲突；本交付在该列填写 WordPress/WooCommerce 插入点，不采用 Shopify 路由。

## 可验证断言

1. 本文含且仅含七个必需章节（现状评估至行动计划），另附来源、缺口、可验证断言；每条架构建议可回溯收集阶段 URL 或查询。
2. `site-schema-blueprint.xlsx` 的 Page Inventory ≥20 行，Source 列非空。
3. Proposed Structure ≥20 行，Priority 仅为 P0/P1/P2。
4. Schema Mapping ≥20 行，产品行 Required Properties 含 material 与 manufacturer（MOQ/交期标缺口）。
5. Internal Links ≥20 行，Link Type 仅 nav / related / breadcrumb / hub。
6. 竞品引用 Memodo 与 Krannich 的具体 URL（见来源表）。
7. schema 审计覆盖首页、产品、联系页，并记录 existing / missing / duplicate / client-side。
8. JSON-LD 骨架含 material、MOQ、交期、manufacturer；MOQ/交期值为声明过的 `{{MOQ}}` / `{{LEAD_TIME}}` template；无未声明 `[YOUR_...]`。
9. 产品 URL 模式为 `/product/{slug}/`，不含纯数字 ID 或日期路径。
10. 终稿无 `item-123`、`page-1` 类通用 URL；未把教学例子原文写入本文。
