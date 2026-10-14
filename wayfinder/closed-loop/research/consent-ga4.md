# 同意横幅与 GA4 选型

调研日：2026-10-14。只读。没有改 de-linker.com，没有装插件，没有改 de-linker 仓库。

推荐组合：Complianz 免费版做横幅和事先阻断，加上 WP Consent API，加上 Site Kit 作为以后的 GA4（以及仍未接入的 GSC）载体。Site Kit 里打开 Consent Mode，默认全部 `denied`；不要再打开 Complianz 自己的 Google Consent Mode。Complianz 的 Script Center 在访客对 statistics 作出同意之前，挡住 `googletagmanager.com`、`google-analytics.com`、`googleads.g.doubleclick.net`，以及一旦启用就挡住 Site Kit 的 Google Tag Gateway 第一方脚本。内联的 consent default 和 Site Kit 本地的 consent-mode 脚本不要挡。这样落到 Google 定义的 Basic：同意前不向 Google 传数据，拒绝的访客也不发 cookieless ping。第一层放同等的接受和拒绝。横幅英文先写，德文按 Sie 体另写，走对抗文案评审，并记入变更台账。

理由有四条。第一，DSK《数字服务提供者指南》1.2 边号 (36)、(121)、(122) 要求：需要同意的终端访问必须发生在同意之后；横幅还在时，不加载需要同意的进一步脚本和第三方内容。Google 对 Advanced 的定义是页面一打开就加载标签，拒绝期间仍发送带时间戳、User Agent、Referrer 的 ping。这和上述边号对不上，所以不采用 Advanced。第二，Site Kit 官方文档把 Complianz、Cookiebot、CookieYes 列为通过 WP Consent API 对接的 CMP，并写明 Consent Mode 由 Site Kit 管，再开 CMP 自己的 Consent Mode 可能冲突。Complianz 免费版 readme 把 Script Center、脚本阻断、WP Consent API 放在 Premium 标题之前，FAQ 写明免费版包含脚本阻断且没有同意记录条数上限；Google Consent Mode 本身列在 Premium，本组合不依赖那一项。第三，GSC 站点接入票仍是 `status: open`，线上没有 Site Kit，也没有 GA4。选 Site Kit 是为了让以后的 GSC 和 GA4 共用一个载体，不是接收一份已经完成的交接。第四，Basic 拿不到 GA4 的行为建模。既有可行性结论把 GSC（不依赖同意横幅）当作 L1/L2 主路径，GA4 是补充，这个缺口可以接受。

最接近的备选是 CookieYes 免费版：它写明 Consent Mode v2 的 Basic 和 Advanced、WP Consent API、Polylang，Site Kit 也点了名。不把它放在第一位，是因为它的扫描、日志和处理在 CookieYes 云上，免费档是每月 5,000 次页面浏览、每次扫描 100 页、每月 5 次扫描，去掉 “Powered by CookieYes” 要付费。Cookiebot 免费档最多 50 个 subpages，本站仅产品 sitemap 就有 210 条 URL。Real Cookie Banner 的 Google Consent Mode 在其营销页上标为 PRO，wordpress.org 的说明和 FAQ 没有出现 WP Consent API。

## 1. 德国法对分析类 Cookie 要求什么

现行法名是《电信与数字服务数据保护与隐私法》（TDDDG）。§25 第 1 款：在终端用户的终端设备上存储信息，或访问已经存储在那里的信息，只有在终端用户基于清楚、全面的信息作出同意后才允许；告知和同意依条例 (EU) 2016/679（GDPR）作出。第 2 款只有两类例外：存储或访问的唯一目的是通过公共电信网传送消息，或者存储或访问对于提供用户明确请求的数字服务是绝对必要的。

来源：<https://www.gesetze-im-internet.de/ttdsg/__25.html>

DSK 指南边号 (4)、(5) 写明：该条自 2021-12-01 起先以 TTDSG §25 实施；引入《数字服务法》的修改把 “Telemedien” 换成 “digitale Dienste”，法律简称为 TDDDG；《数字服务法》于 2024-05-14 生效，TMG 同时废止。边号 (6) 写明新 §25 在内容上与原 TTDSG §25 相同。这补上了既有笔记里「改名生效日未查证」的那一项。

来源：<https://www.datenschutzkonferenz-online.de/media/oh/OH_Digitale_Dienste.pdf>（下文称 DSK OH 1.2；本地核对的是该 PDF 的文本）。目录页：<https://www.datenschutzkonferenz-online.de/orientierungshilfen.html>。第 108 次会议于 2024-11-06 通过该文本、用以替换 2021 年电信媒体指南 1.1：<https://www.datenschutzkonferenz-online.de/media/pr/Protokoll_108_DSK.pdf>。

GDPR 条文的欧盟官方公报页本次打开时返回 HTTP 202（WAF challenge），正文没有取到。下面涉及 GDPR 的句子，以 DSK 的转述和已打开的判决、监管新闻稿为准，不引用二次转载站。

### 分析不是一揽子免同意

边号 (87)–(89)：监管机构故意不对「Reichweitenmessung」作一律免同意的判断。单纯把某页的计数加一、用不含个人数据的日志计次、或本站自己的简单计数像素，和第三方用设备、用户 ID、停留、入口出口、下载等做的 Reichweitenanalyse 不是一回事。边号 (90) 写明，连简单的访问计数是否属于用户明确请求的服务，也取决于具体目的。边号 (109) 写明，跟踪场景里 Art. 6(1)(f) 只在少数配置下成立。边号 (111)：第三方即使只为自己的目的处理 IP 地址，Art. 6(1)(f) 通常也不能作为把该数据交给它的依据。

推断：GA4 的 JavaScript 会在终端上存储或读取分析用存储，并按 Google 自己的产品目的接收测量数据，不能放进 §25(2) 第 2 项。既有笔记的同一推断仍然成立。来源除上列边号外，见 Google 对 `analytics_storage` 的说明：<https://developers.google.com/tag-platform/security/concepts/consent-mode>。

### 事先阻断

边号 (36)：同意的意思表示必须在需要同意的终端访问之前已经作出。第一次打开网站就把 Cookie 写上、然后再问，不允许。边号 (121)：横幅显示期间，先不加载可能访问终端或处理个人数据、且需要同意的进一步脚本，尤其不加载需要同意的外来服务器内容。Impressum 和隐私政策必须仍能打开。边号 (122)：只有用户作出主动行为（打勾或点击按钮）之后，才可以存储或读取，并开始需要同意的处理。

### 拒绝与接受同级

边号 (58)、(59)：把拒绝放到第二层、因而比同意多点击，影响自愿性。横幅挡住内容、用户不能直接忽略时，选项必须同等。边号 (124)、(125)：第一层的拒绝按钮不是在任何版式下都强制；只有用户必须操作才能继续浏览时才强制。横幅不挡住内容、用户不必操作时，第一层拒绝可以没有。常见横幅经常已经满足「必须有第一层拒绝」的条件。小屏幕上也不能挡住内容。边号 (134)–(137)：一旦提供拒绝，它必须在大小、颜色、对比和字体上能被认出是同等选项。示例文案是 “Einwilligung erteilen” 旁边的 “Weiter ohne Einwilligung”。写着 “Einstellungen oder Ablehnen”、点进去才到第二层的按钮不够。边号 (130)：仅颜色不同，不自动否定自愿性。边号 (118)：选项不得预先打勾。

法院比边号 (124) 的窄例外更严，本站按「第一层同等接受和拒绝」做。

- 科隆高等法院 2024-01-19，6 U 80/23：第一层是 “Akzeptieren” 和 “Einstellungen”，外加 “Akzeptieren & Schließen” 和关闭符号，没有同等拒绝。法院认为这不是 §25(1) TTDSG 结合 GDPR Art. 4 Nr. 11 所要求的自愿且充分告知的同意。全文：<https://nrwe.justiz.nrw.de/olgs/koeln/j2024/6_U_80_23_Urteil_20240119.html>
- 下萨克森州数据保护专员 2025-05-20 新闻稿：汉诺威行政法院 2025-03-19（10 A 5385/22）确认其观点。有 “Alle akzeptieren” 时，第一层必须有清晰可见的 “Alles ablehnen”；否则如此取得的同意无效，违反 TDDDG 和 GDPR。新闻稿没有写 Google Tag Manager。来源：<https://www.lfd.niedersachsen.de/startseite/infothek/presseinformationen/urteil-zu-manipulativem-cookie-banner-alles-ablehnen-schaltflache-ist-ein-muss-241960.html>
- 联邦最高法院 2020-05-28，I ZR 7/16，新闻稿 067/2020：预先打勾允许 Cookie，不是有效同意。新闻稿引欧盟法院 2019-10-01，C-673/17，Planet49。新闻稿：<https://www.bundesgerichtshof.de/SharedDocs/Pressemitteilungen/DE/2020/2020067.html>。判决全文和 EUR-Lex 上的 Planet49 本次没有打开。
- 欧洲数据保护委员会 Cookie Banner Taskforce 报告（2023-01-18）：需要同意的 Cookie 不得在用户作出肯定行为之前设置；绝大多数监管机构把「有同意按钮、却在任何一层都没有拒绝按钮」视为违规。来源：<https://www.edpb.europa.eu/system/files/2023-01/edpb_20230118_report_cookie_banner_taskforce_en.pdf>

### 可撤回

边号 (126)：撤回必须和作出同意一样容易，GDPR Art. 7(3) 第 4 句。边号 (37) 还要求告知：撤回不影响撤回前已经发生的存储或访问的合法性（Art. 7(3) 第 3 句）。

### 记录

边号 (84)、(85)：履行 §25(1) 第 2 句、Art. 7(1) 和 Art. 5(2) 的举证责任，不需要长期 UID Cookie。通常只要能说明用了什么流程取得同意，并把结果存在一个不含 UID、也不含多余信息的 Cookie 里。应保留已被替换的横幅文本和配置。推断：按访客保存商业化「同意档案」超过 DSK 写明的最低限度。没有同意档案产品，不等于自动不合规；没有流程说明、也没有保留旧横幅文本，则对不上 (85)。

### 第一层要写什么

边号 (119)：第一层通常要有具体目的；若建立个人画像并和其他网站的数据合并成更大的使用画像，要写明；若在欧洲经济区外处理，要写明；要写明数据交给多少个控制者。边号 (120)：第三方必须逐一点名。“Partner” 或「可能与其他数据合并」不够。至少要给出该第三方自己提供的目的说明。

### 语言 Cookie、购物车、管辖

边号 (81)：语言或背景色偏好不需要 UID。存一个不识别人的值，例如 `language: de`，即可。这不是对 Polylang 插件的裁定。`pll_language` 是否落入 §25(2) 第 2 项，是推断。Polylang 自己的 Cookie 说明本次没有打开。

边号 (80)：购物车或支付 Cookie，通常要等用户真的把商品放进购物车或开始支付，才算绝对必要。只浏览商店时，不必提前启用。

公开首页 JSON-LD 的 `addressRegion` 是 Sachsen-Anhalt（本次不抄街道、邮编、电话、邮箱）。萨克森-安哈尔特州数据保护专员的职责页写明，她向设在该州的企业提供咨询。来源：<https://datenschutz.sachsen-anhalt.de/landesbeauftragte/aufgaben>，机构首页 <https://datenschutz.sachsen-anhalt.de>。联邦专员的地址目录指向同一机构：<https://www.bfdi.bund.de/SharedDocs/Adressen/EN/LfD/Sachsen-Anhalt.html>。

### 向美国传输

边号 (113)、(114) 及脚注 58：2023-07-10 的欧盟—美国数据隐私框架充足性决定已经存在，因此对已获认证的接收方可以走 GDPR Art. 45。Schrems II（C-311/18）描述的是该决定之前的标准。脚注写的是决定本身，没有点名 GA4 的合同主体是否仍在认证名单上。名单页本次没有打开。见文末〔未证实〕。

## 2. Consent Mode v2：Basic、Advanced、不替代横幅、数据缺口

Google 的开发者文档写明：网站或应用上的同意由使用方负责取得，可以用横幅、自建方案或 CMP。来源：<https://developers.google.com/tag-platform/security/concepts/consent-mode>。

GA4 帮助写明原句：Consent mode does not provide a consent banner or widget. Rather, it interacts with it. 既有笔记「Consent Mode 不替代横幅」与这句一致，本次按 Google 自己的页面复核，结论不变。来源：<https://support.google.com/analytics/answer/9976101>

同一概念页对两种实现的定义：

- Basic：在用户与横幅交互之前阻止 Google 标签加载。交互前不向 Google 传输任何数据，包括同意状态。用户拒绝时，完全没有数据，标签不触发。Ads 的转化建模此时用的是通用模型。
- Advanced：用户一打开页面就加载标签。默认可以是 denied。拒绝期间，标签发送不带 Cookie 的测量。这套实现能做广告主专用模型，而不是通用模型。

Ping 可以包含：浏览器被动加上的头信息，其中点名 Timestamp、User Agent、Referrer；URL 里是否出现过广告点击信息（例如 GCLID / DCLID）；同意状态的布尔值；每次页面加载生成的随机数。来源同上概念页。

v2 在存储类参数之外使用 `ad_user_data` 和 `ad_personalization`。概念页列出的类型还有 `ad_storage`、`analytics_storage`、`functionality_storage`、`personalization_storage`、`security_storage`。`analytics_storage` 控制分析用存储，例如访问时长。

GA4 帮助对缺口的原话：若用「挡住 Google 标签，直到对话框出现且用户同意」来实现 Consent Mode，就得不到 Consent Mode 的全部好处，例如用户拒绝时，媒体资源里没有建模数据去填观察值的空缺。Advanced 在拒绝时发送 cookieless ping，GA4 用这些 ping 做行为建模和转化建模。`analytics_storage=denied` 时不设置、不访问、不读取 Analytics Cookie；若另外设置了 user_id 或自定义维度，它们仍会送出。来源：<https://support.google.com/analytics/answer/9976101>

行为建模的资格写在另一页，而且把 Advanced 写成前提：Consent Mode 必须全站开启；网页上的实现必须在同意对话框出现之前就加载标签，并且无论用户是否同意都加载（advanced implementation）。另外，媒体资源要在至少 7 天里每天有至少 1,000 个 `analytics_storage=denied` 的事件，并且在此前 28 天中至少 7 天、每天至少 1,000 名用户发送 `analytics_storage=granted` 的事件。达到这些外部条件也不保证合格。来源：<https://support.google.com/analytics/answer/11161109>

推断：本站若按第 1 节采用 Basic，拒绝的访客在 GA4 里没有事件，也达不到上述建模资格。同意的访客仍有观察值。既有渠道笔记把 GSC 作为不依赖横幅的 L1/L2 主路径、GA4 作为补充，因此这个缺口不改变选型。来源：`wayfinder/feasibility/research/google-channel-access.md` 关于 GSC 与 GA4 分工的既有结论；建模资格来自上列 Google 帮助页。

汉堡数据保护专员「建议使用 Basic Consent Mode」只出现在二次博客。本次没有在 `datenschutz-hamburg.de` 打开到这样的页面。见〔未证实〕。DSK OH 1.2 没有出现 “Consent Mode” 这几个字。

Site Kit 文档对「打开 Consent Mode、访客拒绝」的描述是：标签把拒绝告诉 Google，不存 Cookie，GA4 用转化建模和行为建模填空。这是 Advanced 的效果，除非 CMP 把外部脚本挡住。来源：<https://sitekit.withgoogle.com/documentation/using-site-kit/consent-mode/>

## 3. 免费 CMP

安装数是 WordPress.org Plugin API 在 2026-10-14 返回的 `active_installs` 分档，不是精确安装数，也不是德国市场份额。接口：`https://api.wordpress.org/plugins/info/1.2/?action=plugin_information&request[slug]=<slug>`。

本站约束（新站 `AGENTS.md`，票内已引用）：不买付费插件；不用 Code Snippets；EN/DE 走 Polylang；德语 Sie；客户可见文案走对抗评审；横幅是裁定过的变更，进变更台账；LiteSpeed；WordPress + WooCommerce。公开 sitemap 于 2026-10-14 的 URL 条数：`page-sitemap1.xml` 49，`post-sitemap1.xml` 22，`product-sitemap1.xml` 210，`product_cat-sitemap1.xml` 20。索引：<https://de-linker.com/sitemaps.xml>。

### Complianz（`complianz-gdpr`）

7.5.6，更新 2026-10-13 7:32am GMT，活跃安装 1,000,000。readme：<https://plugins.svn.wordpress.org/complianz-gdpr/trunk/readme.txt>

免费功能列表（出现在 `== Premium Features ==` 之前）包含 Script Center（按类别或服务控制脚本、iframe 和插件）、Proof of Consent、WP Consent API 的完整集成、对德国 TTDSG/DSGVO 的分区规则。FAQ 写明：Complianz Free 包含可用的横幅、自动扫描、脚本阻断、隐私政策生成器，以及 GDPR、CCPA、ePrivacy；没有同意记录条数上限；免费版用于单一站点。Premium 增加多站点、A/B、TCF 等。

Google Consent Mode 写在 Premium 列表里。另一条 FAQ「Does Complianz support Google Consent Mode v2?」只回答 Yes，没有写免费还是付费。两处并存，本调研不把 v2 信号算进免费版。推荐组合用 Site Kit 发信号，正好避开这一项。changelog 有 “Updated Google Site Kit integration” 和去掉 Consent Mode v2 的 BETA 标记，同样没有写档位。

Polylang：changelog 有一条 “translatable URLs in polylang”。横幅字符串的记载是 WPML（`wpml-config.xml`、字符串注册修复）。免费版能否按 Polylang 语言各存一套横幅文案，见〔未证实〕。官方对比页 <https://complianz.io/complianz-free-vs-premium/> 本次返回 HTTP 404，档位以这份 readme 为准。

自托管、FAQ 没有页面浏览封顶。这是推荐它的原因。

### CookieYes（`cookie-law-info`）

3.5.7，更新 2026-10-14 5:53am GMT，活跃安装 1,000,000。readme：<https://plugins.svn.wordpress.org/cookie-law-info/trunk/readme.txt>。定价：<https://www.cookieyes.com/pricing/>

免费计划写明包含横幅、自动阻断、扫描器、政策生成器、同意日志、Google Consent Mode v2。功能列表写 “Google Consent Mode v2 (Advanced and Basic)”。WP Consent API：是。Polylang、WPML、TranslatePress：是。同意数据存在欧盟数据中心，并提 Data Processing Agreement。扫描、日志和处理在 CookieYes 云上，不进 WordPress 数据库。

定价页免费档：每月 5,000 次页面浏览，每次扫描 100 页，每月 5 次扫描，Cookie auto-blocking 为 Yes。readme 把提高页面浏览上限、去掉 “Powered by CookieYes” 放在付费能力里。超过 5,000 次之后横幅和阻断是否继续工作，定价页和 readme 都没有写，见〔未证实〕。

Site Kit 文档点名 CookieYes。它是文档最齐的备选。不放第一，是因为云处理、页面浏览档和品牌锁定。

### Real Cookie Banner（`real-cookie-banner`）

5.3.10，更新 2026-10-08 6:53am GMT，活跃安装 100,000。插件页 FAQ：<https://wordpress.org/plugins/real-cookie-banner/>。营销页：<https://devowl.io/wordpress-real-cookie-banner/>

FAQ：核心功能免费，可以建无限的服务和 content blocker；大多数服务模板和 content blocker 模板只在 PRO。PRO 差异列表写明包括：对不安全第三国处理的同意、同意统计、高级可视化 content blocker、设计预设、TCF、地理限制、Google Tag Manager 与 Matomo Tag Manager 支持、跨站转发同意、大量模板。营销页把带星号的功能标为仅 PRO，其中有 “Google Consent Mode*”。wordpress.org 的说明和 FAQ 文本里没有 WP Consent API，也没有 Site Kit。多语言支持 WPML、Polylang、TranslatePress、Weglot 的那句在已提取的营销页段落里没有星号。

免费版不能当作 Site Kit 的对接路径：WP Consent API 未见记载，Consent Mode 在营销页上是 PRO。付费版被「不买付费插件」排除。

### Cookie Notice / Cookie Compliance（`cookie-notice`）

3.1.16，更新 2026-10-13 5:31pm GMT，活跃安装 800,000。readme：<https://plugins.svn.wordpress.org/cookie-notice/trunk/readme.txt>

Banner Only 不需要账号，FAQ 写明它不包含自动脚本阻断、目的分类和同意记录存储。Connected 模式（免费或付费）才加上自动阻断、目的分类、同意记录、Google Consent Mode、多语言横幅。WP Consent API 的注册可以不登录账号，以便 Site Kit、WooCommerce 跟随横幅；阻断需要 Cookie Compliance 账号。访客横幅来自 `cdn.hu-manity.co/hu-banner.min.js`，同意记录由浏览器直接发给 Hu-manity.co。readme 的隐私节写处理地点为欧盟、AWS Ireland。

changelog：免费档的真实额度是每月 1,000 次访问。免费档达到月访问上限后，Autoblocking 会暂停，下个周期再恢复。这是合规失效，不推荐。

### GDPR Cookie Compliance / Moove（`gdpr-cookie-compliance`）

5.2.2，更新 2026-10-08 9:55am GMT，活跃安装 300,000。readme：<https://plugins.svn.wordpress.org/gdpr-cookie-compliance/trunk/readme.txt>

免费要点：数据存在网站本地；接受、拒绝、关闭、设置；可决定脚本默认加载还是同意后才加载；Google Consent Mode v2；文案、logo、颜色可改；Polylang、WPML、TranslatePress。Premium 列表明确包含 Google Site Kit integration、同意日志、地理定位、iframe blocker、Cookie 声明、按语言使用不同脚本。changelog 有一句：Consent Mode v2 下，GA4 的 cookieless ping 在同意前发送。WP Consent API 出现在 changelog，不在 Premium 列表里。

免费版的 Site Kit 路径不成立：官方把 Site Kit 集成放在 Premium，且其 Consent Mode 按 changelog 会在同意前发 ping。

### Cookiebot by Usercentrics（`cookiebot`）

4.7.5，更新 2026-10-08 11:48am GMT，活跃安装 100,000。readme：<https://plugins.svn.wordpress.org/cookiebot/trunk/readme.txt>

事先阻断、Google 认证、Consent Mode v2、WP Consent API 都有记载。免费计划：“Start free with up to 1 domain and 50 subpages”。changelog 有 WooCommerce 附加逻辑，在同意前阻断 Order Attribution / SourceBuster。定价页 <https://www.cookiebot.com/en/pricing/> 本次 HTTP 403。Polylang 在已读的 readme 段落里没有出现。

50 个 subpages 盖不住本站 sitemap：页面加文章已是 71，产品 URL 210。免费档不够。付费被约束排除。

### WPConsent（`wpconsent-cookies-banner-privacy-suite`）

1.2.0，更新 2026-10-08 11:29am GMT，活跃安装 200,000。readme：<https://plugins.svn.wordpress.org/wpconsent-cookies-banner-privacy-suite/trunk/readme.txt>

自托管，写明没有页面浏览封顶，同意记录在自己的数据库。免费列表包含：对 Google Analytics、Google Ads 等的自动脚本阻断；YouTube、Vimeo、Google Maps、reCAPTCHA 的内容阻断；Google Consent Mode v2；WP Consent API。FAQ 写：标签在 consent-denied 状态下继续工作，以便收到建模转化，且同意前不设 Cookie。另一句写：横幅里的每条文案都可以在后台翻译；自动翻译多语言站点是 Pro。readme 没有出现 Polylang，也没有出现 Site Kit。Pro 列表包含地理定位和 IAB TCF。

它是自托管方向上最接近 Complianz 的另一个免费插件。不放第一，因为 Site Kit 的具名伙伴列表里没有它，而且它把自己的 Consent Mode 写成拒绝期间仍向 Google 提供建模数据，也就是 Advanced。能否关掉它自己的 Consent Mode、只留脚本阻断、改由 Site Kit 发信号，readme 没有写。

### CookieAdmin（`cookieadmin`）

1.2.6，更新 2026-10-12 1:38pm GMT，活跃安装 400,000。readme：<https://plugins.svn.wordpress.org/cookieadmin/trunk/readme.txt>。首页：<https://cookieadmin.net>

Pro 列表包含：Google Consent Mode v2、内容阻断、Polylang、WPML、同意日志、多语言（含 German Formal）。免费列表是可定制表单、基础扫描、分类、GDPR 与美国州法、接受全部或拒绝全部。changelog 里有未标 Pro 的 “Block Scripts” 修复，所以免费版可能带一个脚本阻断开关；内容阻断和 Consent Mode v2 仍写在 Pro。德语正式体和 Polylang 都在付费侧。不推荐。

### iubenda（`iubenda-cookie-law-solution`）

3.13.5，更新 2026-09-01 8:22am GMT，活跃安装 200,000。readme：<https://plugins.svn.wordpress.org/iubenda-cookie-law-solution/trunk/readme.txt>

readme 写了 Google Consent Mode 的 Basic 和 Advanced、WP Consent API，changelog 写了 Polylang。免费档的域名、页面或流量上限在这份 readme 里没有出现。见〔未证实〕。不进入推荐。

### CCM19 Integration（`ccm19-integration`）

1.1.11，更新 2026-04-21 12:14pm GMT，活跃安装 5,000。readme：<https://plugins.svn.wordpress.org/ccm19-integration/trunk/readme.txt>

插件自己写明：它只是把 CCM19 嵌进 WordPress，CCM19 需要购买、租赁，或在 <https://www.ccm19.de> 注册免费账号，再把后台代码贴进插件。免费账号的限额本次没有打开。它不是一套自包含的免费横幅。

### 其余目录条目

同一次 API 还看到，但 readme 没有逐项核对，因此下表功能列标〔未证实〕，不进入推荐：

- Beautiful Cookie Banner（`beautiful-and-responsive-cookie-consent`）4.9.2，更新 2026-08-21，活跃安装 40,000。
- CookieHub（`cookiehub`）1.2.4，更新 2026-08-24，活跃安装 3,000。
- Klaro Consent Manager（`klaro-consent-manager`）1.1.7，更新 2019-05-11，活跃安装 200。2019 年后无更新，不作为候选。

WP Consent API（`wp-consent-api`）2.1.0，更新 2026-09-15，活跃安装 200,000。它不是横幅。readme 写明第三方脚本的阻断留在 CMP 里，不放进这个插件。来源：<https://plugins.svn.wordpress.org/wp-consent-api/trunk/readme.txt>

Borlabs Cookie 的目录 slug `borlabs-cookie` 在既有笔记的同日 API 调用中返回 404，不在目录里。付费与否以其销售页为准；该页本次没有打开。不买付费插件的约束已经把它排除在推荐之外。

### 对比

| 插件 | 版本 / 更新 / 安装分档 | Consent Mode v2 | WP Consent API | Site Kit 具名联动 | Polylang | 事先阻断 | 免费档能否覆盖本站 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Complianz | 7.5.6 / 2026-10-13 / 1,000,000 | readme 把功能放在 Premium；FAQ 只说支持，未写档位 | 免费列表有 | Site Kit 文档点名 | 仅见 URL 翻译 changelog；横幅字符串是 WPML。〔未证实〕 | 免费 FAQ 与 Script Center 写有 | 自托管，FAQ 无记录条数上限，无页面浏览封顶记载。v2 信号不靠它 |
| CookieYes | 3.5.7 / 2026-10-14 / 1,000,000 | 免费，Basic 与 Advanced | 有 | Site Kit 文档点名 | 有 | 免费，自动阻断 | 云日志；5,000 次页面浏览 / 月，100 页 / 次扫描。超限行为〔未证实〕。去品牌付费 |
| Real Cookie Banner | 5.3.10 / 2026-10-08 / 100,000 | 营销页标 PRO | 说明与 FAQ 未见 | 未见 | 营销页多语言句未标星号 | 免费可建 content blocker；多数模板 PRO | 不作为 Site Kit 路径 |
| Cookie Notice | 3.1.16 / 2026-10-13 / 800,000 | Connected 各档有；Banner Only 无 | 可不登录即注册 | readme 点名 Site Kit 会跟随 API | Connected 才有多语言横幅 | Connected 才有；免费档每月 1,000 次访问后暂停 | 不够 |
| Moove | 5.2.2 / 2026-10-08 / 300,000 | 免费功能列表有；changelog 为同意前 ping | changelog 有，未进 Premium 列表 | Site Kit 集成在 Premium | 免费列表有 | 免费可指定脚本同意后加载；iframe 阻断在 Premium | Site Kit 路径要付费 |
| Cookiebot | 4.7.5 / 2026-10-08 / 100,000 | 有 | 有 | Site Kit 文档点名 | 已读段落未见 | 有，含 SourceBuster 附加 | 免费最多 50 个 subpages，低于本站 URL 数 |
| WPConsent | 1.2.0 / 2026-10-08 / 200,000 | 免费；文案是拒绝期间仍供建模 | 免费 | 未见 | 未见插件名；自动多语言翻译是 Pro | 免费列表写自动阻断 GA | 自托管、无页面浏览封顶。默认是 Advanced |
| CookieAdmin | 1.2.6 / 2026-10-12 / 400,000 | Pro | 未见 | 未见 | Pro，含 German Formal | 内容阻断在 Pro；changelog 另有未标 Pro 的 Block Scripts | 不够 |
| iubenda | 3.13.5 / 2026-09-01 / 200,000 | readme 写 Basic 与 Advanced | 有 | 未见 | changelog 有 | 有事先阻断的表述 | 免费限额〔未证实〕 |
| CCM19 Integration | 1.1.11 / 2026-04-21 / 5,000 | 插件不实现 | 插件不实现 | 未见 | 插件不实现 | 取决于外部 CCM19 | 要另购或另注册；免费账号限额〔未证实〕 |

## 4. GA4 载体：Site Kit，还是仓库里自己输出 gtag

线上状态（2026-10-14 保存的首页 HTML，337,316 字节，最终 URL `https://de-linker.com/`）：没有 `gtag`、`GTM-`、`google-site-kit`、`googletagmanager`、`consent`。有 `sourcebuster`、`pll_cookie`、`woocommerce`、`seopress`。`/de/` 返回 200。响应头在同一次会话里是 `server: LiteSpeed`、`x-powered-by: PHP/8.3.35`。账户盘点写明 Google 侧当时没有 GSC 资源、没有 GA4、Site Kit 未安装。GSC 接入票仍是 open。来源：<https://de-linker.com/>；`wayfinder/feasibility/tickets/google-account-inventory.md`；`wayfinder/closed-loop/tickets/gsc-site-access.md`。

Site Kit by Google 1.189.0，更新 2026-10-05 9:57pm GMT，活跃安装 5,000,000。首页 <https://sitekit.withgoogle.com>。

官方 Consent Mode 页：Consent Mode 不是横幅。要让它正常工作，必须安装并配置 WP Consent API 和一个同意插件；Site Kit 会提示安装 WP Consent API。CMP 若自带 Consent Mode，在 Site Kit 已启用时不要再用，以免冲突。具名、通过 WP Consent API 原生协作的插件包括 Complianz、Cookiebot CMP by Usercentrics、CookieYes。来源：<https://sitekit.withgoogle.com/documentation/using-site-kit/consent-mode/>

插件源码（wordpress.org 的 1.189.0 包内 `includes/Core/Consent_Mode/Consent_Mode.php`，与 GitHub 上核对过的同名文件一致）把默认值设为：

`ad_personalization`、`ad_storage`、`ad_user_data`、`analytics_storage`、`functionality_storage`、`security_storage`、`personalization_storage` 全部 `denied`，`wait_for_update` 为 500 毫秒。类别映射：`statistics` → `analytics_storage`；`marketing` → `ad_storage`、`ad_user_data`、`ad_personalization`。内联片段只定义 `dataLayer` / `gtag()` 并写入 `gtag('consent','default', …)`，片段 id 为 `google_gtagjs-js-consent-mode-data-layer`。它自己不请求 `gtag.js`。

`includes/Core/Tags/GTag.php` 的 `enqueue_gtag_script()` 在存在 tag 时注册并入队脚本。默认 URL 是 `https://www.googletagmanager.com/gtag/js?id=` 加上 tag id，async。这段入队不读取同意状态。Google Tag Gateway 开启时，同一文件改为走第一方 “hat” 脚本（`maybe_print_hat_script()`，注释写明 first party tag hat，仅在 `is_google_tag_gateway_active()` 为真时输出）。该开关的默认值本次没有读到。构建后的 consent-mode JS 会在 `wp_has_consent` / `wp_listen_for_consent_change` 上把类别更新为 granted 或 denied。它不阻止 Google 脚本加载。

推断：只打开 Site Kit Consent Mode、不挡外部脚本，就是 Google 的 Advanced。要得到 Basic，CMP 必须在 statistics 同意前阻止上述 Google 域名上的脚本执行，同时不阻止内联 default 和本地 consent-mode JS。同意之后，`gtag()` 的实现是 `dataLayer.push`，因此 default 和随后的 update 可以先留在队列里，等脚本放行再执行。这是从上述源码推的，没有在本站执行过。

不启用 Consent Mode 时，Site Kit 文档写：已连接 Analytics 或 Ads 的话，欧洲经济区、瑞士和英国的跟踪会被挡住。因此「为了少传数据而关掉 Site Kit 的 Consent Mode」会让同意之后的欧洲访客也不进 GA4。本组合是打开 Consent Mode，再用 CMP 把加载推迟到同意之后。

仓库插件直接输出 gtag 是后备，不是第一选择。GSC 票还没选载体，Site Kit 同时能接 Search Console 和 Analytics，并且已经按 WP Consent API 的 statistics / marketing 发 v2 默认值。自己写的插件要重做这套 default、update 和「同意前不请求 gtag.js」。Code Snippets 不在允许范围内；若以后实证 Script Center 挡不住 Site Kit 的入队，再在仓库插件里把脚本放到同意之后，仍不走 Code Snippets。不另加 GTM 容器来加载 GA4。下萨克森新闻稿没有写 GTM 本身必须事先同意；二次资料里的这一句见〔未证实〕。GTM 容器仍是额外的第三方脚本，本站没有它也能由 Site Kit 加载 gtag。

与所选 CMP 的配合：安装 WP Consent API 和 Complianz；Site Kit 连接 Analytics 并打开 Consent Mode；Complianz 里不要启用它自己的 Google Consent Mode（该项在 Premium，且 Site Kit 警告冲突）。Script Center 把统计类脚本按 statistics 拦截，营销类按 marketing 拦截。GA4 只应跟随 statistics。`ad_user_data` 和 `ad_personalization` 跟随 marketing，留给以后若使用 Ads 标签时，而不是默认随分析一起打开。

## 5. 推荐组合、理由、已知坑

组合与理由已写在开头。实施时横幅第一层使用同等的接受和拒绝，目的、欧洲经济区外处理和接收方按边号 (119)、(120) 写清，并提供与同意同样容易到达的撤回入口。文案不在本笔记里起草。

### 已知坑

1. Site Kit 在有 tag 时就会入队 `gtag/js`，Consent Mode 的内联片段不负责阻断。CMP 没拦住这个 URL，线上就是 Advanced，同意前会发出含 User Agent 和 Referrer 的 ping。
2. 同时打开 Site Kit 的 Consent Mode 和 CMP 自己的 Consent Mode，Site Kit 文档写明可能冲突。Complianz 的该项又在 Premium，免费站点上不应出现第二套片段。
3. `wait_for_update` 只有 500 毫秒。LiteSpeed 若延迟或合并 JS，CMP 的 update 可能晚于这个窗口。Cookie Notice 的 changelog 写过：LiteSpeed Cache、WP Rocket 等的 Delay JavaScript 会让横幅变晚、Cookie 在同意前加载；他们后来把自己的脚本排除出合并。这是另一家插件的修复记录，说明缓存优化会打乱「先 default、再横幅、再放行」的顺序。Complianz 和 Site Kit 是否已对 LiteSpeed 做同样排除，本次没有在它们的文档里核到。
4. Google Tag Gateway 开启后，测量脚本可以不走 `googletagmanager.com`。只按这个域名做拦截，会漏掉第一方 URL。默认是否开启，见〔未证实〕。在阻断规则覆盖该 URL 之前不要打开。
5. 整页缓存不能把「已同意」写进给所有访客的 HTML。脚本标签若无条件出现在缓存的 HTML 里，阻断必须在脚本执行前完成。
6. WooCommerce 订单归因已经在公开首页加载 Sourcebuster，早于任何 GA4。官方文档列出的 Cookie 包括 `sbjs_session`（本会话页浏览和当前路径，30 分钟）、`sbjs_udata`（文档原文写访客 user agent 的信息，例如 IP、浏览器和设备类型，会话）、以及 `sbjs_first`、`sbjs_current`、`sbjs_first_add`、`sbjs_current_add`、`sbjs_migrations`。可在 WooCommerce → Settings → Advanced → Features → Order Attribution 关闭。文档写明与 WP Consent API 兼容，以便接入 CMP。装上 API 之后默认落在哪个类别，文档没有写。来源：<https://woocommerce.com/document/order-attribution-tracking/>
7. 边号 (80)：浏览商品页不等于已经请求购物车功能。功能型 Woo Cookie 和归因 Cookie 要分开看。归因这组不是结账所绝对必要的。
8. Complianz 的横幅字符串文档是 WPML。本站是 Polylang。英文和德文 Sie 必须各自能改，不能靠机器翻译交差。这条在插件里是否现成，见〔未证实〕。
9. Basic 下，拒绝访客没有 GA4 事件，行为建模的官方资格也达不到。不要为了补上建模改回 Advanced。
10. 横幅是客户可见的新界面，按新站约束进变更台账，并走对抗文案评审。
11. CookieYes 的云日志、5,000 次页面浏览和 “Powered by” 锁定，Cookie Notice 在 1,000 次访问后暂停阻断，Cookiebot 的 50 个 subpages，都是免费档看起来能用、对本站不够的例子。
12. DSK (84)、(85) 不要求按访客的商业同意档案。把「没有 Records of Consent 付费模块」直接写成违法，超过了已读的指南。反过来，不保留旧横幅文本和流程说明，对不上 (85)。

## 〔未证实〕

- Google 作为 GA4 接收方当前是否仍列在 <https://www.dataprivacyframework.gov/list>。DSK 只确认 2023-07-10 的充足性决定存在。
- 汉堡监管机构是否建议 Basic Consent Mode。没有打开到官方页。
- 汉诺威行政法院 10 A 5385/22 是否另行认定 Google Tag Manager 本身必须事先同意。已打开的州监管新闻稿没有这句。判决全文本次没有打开。
- GDPR 官方公报正文、欧盟法院 Planet49 全文、BGH I ZR 7/16 判决全文。EUR-Lex 返回 HTTP 202。新闻稿和 DSK 转述已用，不把未打开的页面当来源。
- Complianz 免费版 Script Center 能否在脚本执行前拦住 Site Kit 已经入队的 `gtag.js`，以及 Google Tag Gateway 的第一方 URL。没有在本站或测试站执行。
- 脚本被挡住期间，dataLayer 里排队的 consent update 会不会在放行后按预期生效。源码推断见第 4 节，没有执行。
- Site Kit 的 Google Tag Gateway 默认是开还是关。
- Complianz 免费版能否用 Polylang 为 EN 和 DE 各存一套横幅文案。readme 只明确 WPML，外加一条 Polylang URL 翻译。
- Complianz FAQ 所说的 Consent Mode v2 是否属于免费版。Premium 列表和 FAQ 互相不解释。
- CookieYes 超过每月 5,000 次页面浏览后，横幅和自动阻断是否继续。云处理的具体国家（readme 只写欧盟数据中心）没有再细化。
- iubenda 免费档的页面、域名或流量上限。
- CCM19 免费账号的限额。
- WPConsent 能否关闭自己的 Consent Mode、只做阻断，并和 Site Kit 的信号共存。readme 未写 Site Kit。
- CookieAdmin 免费版的 Block Scripts 能否覆盖 Site Kit。内容阻断和 Consent Mode 写在 Pro。
- Woo 订单归因在检测到 WP Consent API 后默认对应 statistics 还是 marketing，以及未同意时是否已经停止入队。当前线上是在没有 CMP 的情况下加载的。
- Polylang 的语言 Cookie 是否被其官方文档声明为 §25(2) 所绝对必要。DSK (81) 只谈到非识别性的语言值。
- Complianz、Site Kit 对 LiteSpeed 延迟合并 JS 的官方排除规则。
- Borlabs 的标价页。目录中不存在；推荐已因「不买付费插件」排除，标价不影响结论。
- Beautiful Cookie Banner、CookieHub 的 Consent Mode、WP Consent API、Site Kit、Polylang 和阻断能力。只核了安装分档和更新时间。

## 来源

| 来源 | URL | 用于 |
| --- | --- | --- |
| TDDDG §25 | <https://www.gesetze-im-internet.de/ttdsg/__25.html> | 同意与绝对必要例外 |
| DSK OH 1.2 PDF | <https://www.datenschutzkonferenz-online.de/media/oh/OH_Digitale_Dienste.pdf> | 边号 (4)–(6)、(36)、(37)、(58)、(59)、(80)、(81)、(84)–(92)、(109)、(111)、(113)、(114)、(118)–(126)、(130)、(134)–(137) |
| DSK 指南目录 | <https://www.datenschutzkonferenz-online.de/orientierungshilfen.html> | 1.2 的公布位置 |
| 第 108 次 DSK 会议记录 | <https://www.datenschutzkonferenz-online.de/media/pr/Protokoll_108_DSK.pdf> | 2024-11-06 通过 1.2 |
| 科隆高院 6 U 80/23 | <https://nrwe.justiz.nrw.de/olgs/koeln/j2024/6_U_80_23_Urteil_20240119.html> | 第一层无同等拒绝则同意无效 |
| 下萨克森州数据保护专员新闻稿 | <https://www.lfd.niedersachsen.de/startseite/infothek/presseinformationen/urteil-zu-manipulativem-cookie-banner-alles-ablehnen-schaltflache-ist-ein-muss-241960.html> | VG Hannover 2025-03-19，10 A 5385/22 |
| BGH 新闻稿 067/2020 | <https://www.bundesgerichtshof.de/SharedDocs/Pressemitteilungen/DE/2020/2020067.html> | 预先打勾不是有效同意；引 Planet49 |
| EDPB Cookie Banner Taskforce | <https://www.edpb.europa.eu/system/files/2023-01/edpb_20230118_report_cookie_banner_taskforce_en.pdf> | 有接受无拒绝；同意前不得设置 |
| 萨克森-安哈尔特州数据保护专员 | <https://datenschutz.sachsen-anhalt.de/landesbeauftragte/aufgaben> | 对该州企业的咨询职责 |
| BfDI 地址目录 | <https://www.bfdi.bund.de/SharedDocs/Adressen/EN/LfD/Sachsen-Anhalt.html> | 机构名称与首页 |
| Consent Mode 概念 | <https://developers.google.com/tag-platform/security/concepts/consent-mode> | Basic / Advanced、ping 内容、使用方负责取得同意 |
| GA4 Consent Mode | <https://support.google.com/analytics/answer/9976101> | 不提供横幅；挡住标签就没有建模填空 |
| GA4 行为建模资格 | <https://support.google.com/analytics/answer/11161109> | 必须 Advanced，以及 1,000 事件 / 1,000 用户门槛 |
| Site Kit Consent Mode 文档 | <https://sitekit.withgoogle.com/documentation/using-site-kit/consent-mode/> | 需要 WP Consent API 和 CMP；不要双开；点名三家 CMP |
| Site Kit 1.189.0 源码 | Plugin API slug `google-site-kit`；包内 `Consent_Mode.php`、`GTag.php` | 默认 denied；无条件入队 gtag.js；Tag Gateway |
| WordPress.org Plugin API | `https://api.wordpress.org/plugins/info/1.2/?action=plugin_information&request[slug]=<slug>` | 2026-10-14 的版本、更新时间、安装分档 |
| 各插件 trunk readme | `https://plugins.svn.wordpress.org/<slug>/trunk/readme.txt` | 上表各 slug |
| Real Cookie Banner 插件页与营销页 | <https://wordpress.org/plugins/real-cookie-banner/> ，<https://devowl.io/wordpress-real-cookie-banner/> | 免费核心与 PRO 星号 |
| CookieYes 定价 | <https://www.cookieyes.com/pricing/> | 5,000 次页面浏览、100 页扫描 |
| Woo 订单归因 | <https://woocommerce.com/document/order-attribution-tracking/> | Cookie 名称与 WP Consent API |
| 本站首页与 sitemap | <https://de-linker.com/> ，<https://de-linker.com/sitemaps.xml> | 无 GA4；URL 条数 |
| 既有渠道笔记 | `wayfinder/feasibility/research/google-channel-access.md` | GSC 为主、GA4 为补充；本次复核 Consent Mode 与 §25 |
| 账户盘点与 GSC 票 | `wayfinder/feasibility/tickets/google-account-inventory.md` ，`wayfinder/closed-loop/tickets/gsc-site-access.md` | Site Kit 未装；GSC 票仍 open |
