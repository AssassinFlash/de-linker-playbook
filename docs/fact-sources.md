# 事实源入口

本仓库的产品事实、公司事实、对外说法和竞品事实都不在仓库里。唯一入口就是本文件：所有 skill 与台账只指向这里，再由这里指到三方。本仓库只指路，不拷贝（指路不复制）。

读路径时把 `~` 展开为用户主目录，不要把 `~` 当相对路径。仓外路径只写在本文件里；换一台机器时，只改本文件。

## 三个源

### 1. 线上站点：对外现状

`https://de-linker.com/`，只读。英文在根路径，德文在 `/de/` 下。

| 要看什么 | 去哪 |
|---|---|
| 站上有哪些页 | 站点地图索引 `https://de-linker.com/sitemaps.xml`（文章、页面、产品、产品分类四张子图） |
| 产品与产品分类 | `/products/` 和各产品页；德文同路径加 `/de/` |
| 产品参数（机器可读） | `https://de-linker.com/wp-json/linker/v1/engineering-feed`：每个已发布产品的型号、品牌、系列、品类、用途、相数、关键数值；每个数值带 `citation`（我们托管的数据手册 URL + 页码） |
| 数据手册原件 | 产品页与 feed 里的 `documents`，都是本站托管的 PDF（`/wp-content/uploads/…`） |
| 工具 | Solution Configurator `/solution-configurator/`（德文 `/de/loesungskonfigurator/`）；Genie 嵌在产品、询盘、账户各入口 |
| 联系与询盘入口 | `/contact/`；询盘以形式发票申请提交（见新站仓库规格 11） |

### 2. 新站仓库：规格与业主裁定

`~/Documents/de-linker`，私有、只读。营销、获客任务不改这个仓库；站点接入的改动按它自己的 `AGENTS.md` 走，与本仓库无关。

按这个顺序读，读到够用就停：

1. `AGENTS.md`：§1 这是什么（公司、站点、客户类型、两个工具）；§2 业主裁定（按日期，是事实）；§3 用词（产品词、询盘四状态、德文 Sie 体与禁用句式）。
2. `docs/specs/README.md`，再读要用的那份规格：
   - `7-selection-facts.md`：产品事实契约（哪些键、从哪来、`unknown` 怎么算）
   - `8-engineering-data.md`、`8-decisions.md`：工程数据与逐件决定
   - `11-commerce.md`：商务链与询盘
   - `13-genie.md`、`14-solution-configurator.md`、`19-tool-pages.md`：两个工具与工具页
   - `9-i18n.md`、`82-domain-language.md`：双语与域语言
   - `74-daily-digest.md`：询盘每日摘要
   - `17-cutover.md`、`145-search-console.md`：上线管线与 Search Console
3. 数据目录：
   - `plugins/linker-commerce/data/`：兼容合同 `compatibility.json`、工程覆盖层 `engineering-overlay.json`、经营政策 `operating-policies.json`
   - `plugins/linker-i18n/data/`：德文术语表 `glossary-de.json`、德文禁词 `banned-de.json`
   - `plugins/linker-tools/data/legacy-redirects.json`：旧地址跳转
   - `docs/faq/`：逐产品 FAQ（问题、EN/DE 答案、手册引用、评审记录）

### 3. 竞品调研：市场与对手

在私有 vault 里，路径 `deliverables/marketing/00-research/`（`deliverables/` 是软链）。公开克隆里这是断链，等于这个源不存在。

- `competitor-study-2026-10-01/`：先读 `README.md`。里面有 12 家同类供货商画像与综合分析（`competitors/`）、邮件/网站/项目三方比对与核查（`comparison/`）、定位邮件条目（`email-positioning-statements.md`）、随邮件附来的几份产品数据手册 PDF。涉及网站的条目抓取于 2026-09-30，早于新站上线，引用前对照线上站点。
- `industry-research-2026-09-20/`：先读 `README.md`。32 份：制造商 01–08、批发商 09–12、买家画像 13–18、链上摩擦 19–22、论坛/FAQ/电价/工具/案例/采购 23–28、跨市场 32。**29–31 号写的是重构前的旧站，可能已过期**，涉及本公司的一律以线上站点与新站仓库为准。

## 什么问题查哪个源

| 问题 | 先查 | 再查 |
|---|---|---|
| 某产品的参数（功率、容量、相数、电压、兼容） | 线上 engineering-feed 或产品页上的值，顺着 `citation` 打开托管数据手册那一页 | 新站仓库规格 7、8 与 `compatibility.json` |
| 卖什么、不卖什么、产品分类 | 线上 `/products/` 与产品分类站点地图 | 新站仓库 `AGENTS.md` §2 |
| 买家是谁 | 新站仓库 `AGENTS.md` §1 | 行业调研 13–18（市场画像，不是客户名单） |
| 对外怎么说（措辞、用词、禁词、语气） | 线上页面现行文案；新站仓库 `AGENTS.md` §3 | `glossary-de.json`、`banned-de.json`、规格 82；单个产品的问答看 `docs/faq/` |
| 公司承诺（回复时限、形式发票有效期、库存怎么说、贸易条款） | 新站仓库 `AGENTS.md` §2 | `operating-policies.json` |
| 询盘怎么进来、有哪些状态 | 新站仓库 `AGENTS.md` §3 与规格 11、74 | 线上 `/contact/` 与产品页的询盘入口 |
| 工具能做什么 | 线上工具页 | 新站仓库 `AGENTS.md` §1 与规格 13、14、19 |
| 站点结构、URL、哪些页已上线 | 线上站点地图与实际页面 | 新站仓库规格 17、`legacy-redirects.json` |
| 某竞品的事实（产品、价格、渠道、话术） | 竞品调研 `competitors/` 与 `comparison/verification.md` | 行业调研 01–12；要引用就打开对方现网核对 |
| 市场、电价、并网、买家摩擦 | 行业调研 19–28、32 | — |
| 本公司的定位主张 | 线上页面现行文案 | 竞品调研 `email-positioning-statements.md` 只算候选主张，线上或新站裁定里找不到对应的标〔未证实〕 |

## 冲突时谁为准

1. **产品参数**：以我们托管的数据手册为准（新站仓库业主裁定）。页面值、feed 值、调研里的数字与手册冲突，取手册；手册取不到，标〔未证实〕，不写这个数。随邮件附来的那几份 PDF 只是副本，以站上托管的版本为准。
2. **对外现状**（页面上现在写什么、哪些 URL 存在、哪些功能已上线）：以线上站点为准。新站仓库里有规格但线上还没有的，不写成已上线。
3. **规格、裁定、用词、承诺**：以新站仓库为准。`AGENTS.md` §2 按日期，新裁定覆盖旧裁定；数据文件或规格与 §2 冲突，以 §2 为准。
4. **竞品调研**只管市场与对手，不作本公司事实。它写到本公司的地方（含 29–31 号、`comparison/site-positioning.md`）与线上或新站仓库冲突，以后两者为准。
5. **查不到**：标〔未证实〕，按没有处理。没有可以询问的人。

## 读的规矩

- 三个源都只读。原文不拷进本仓库；交付物只写来源（URL，或「新站仓库 `<文件>` §<节>」，或 vault 路径）。
- 公开仓库只写路径和角色名（所有者账号、日常账号、服务账号、团队邮箱），不写真实邮箱、账号或表格 ID。
- 旧的产品资料目录已过期，不是事实源，不读。

## skill 怎么引用本入口

skill 里写一句指针，不写仓外路径，不写缺省值或回退路径：

> 产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理；原文不拷进本仓库。

台账键 `product_context` 的值就是 `docs/fact-sources.md`。
