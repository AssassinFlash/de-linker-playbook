# Google 渠道接入路径

调研日期：2026-10-14。回答 [`../tickets/google-channel-access.md`](../tickets/google-channel-access.md) 的 Question。没有用本站凭据调用这三套 API，也没有改仓库里的其他文件。

术语按 [`CONTEXT.md`](../../../CONTEXT.md)：L0 来自执行登记，L1 是收录/展示或邮件送达，L2 是搜索点击或邮件回复，L3 是询盘。北极星是询盘，不按 GA4 转化来定义。

## 结论摘要

最小已验证路径是：一个 Google Cloud 项目、一把服务账号 JSON 密钥、三处各自的产品授权，再加一个仓内 Python 脚本。脚本用官方客户端读 Google 表格里的执行登记，向 Search Console 的 Search Analytics 取展示和点击，用 URL Inspection 抽查收录，把结果追加回同一张表。搜索侧的 L1/L2 由此闭合，不在访客终端写 Cookie。L3 仍是站点询盘，不由 GA4 产生。GA4 Data API 可以挂在同一把密钥上，但德国站点要先有同意横幅；Consent Mode v2 是交给 Google 的信号，不是横幅的替代。无 Cookie 统计能换掉的是站内浏览，换不掉 Search Console。Looker Studio 对这三套数据都有原生连接器，点选即可看图，不负责写反馈分级。`AminForou/mcp-gsc` 自带可运行的 Search Console 调用代码，它是 MCP 服务器，不作为「任何 harness 能跑」的那条路径。

## 怎么读

- **事实**：下面带 URL 的句子，来自本次打开的官方文档、法律文本、厂商页面、GitHub 仓库或 WordPress.org API。
- **推断**：单独标出。推断不是来源没写的事实。
- **未查证**：本次没有打开到能支持该句的一手页面，不补数字、不补结论。

「已验证」按 [`../map.md`](../map.md)：有人用它跑出过数据，或自带数据接入代码。本次没有亲自打通 de-linker 的账号，所以「已验证」指方案自带可执行的接入代码，不是指本站已经跑出数。

## 最小路径

**推断（由下面三节的事实拼成，本身没有一份 Google 文档把它写成「反馈回流」）：**

1. 建一个 Cloud 项目，启用 Search Console API、Google Analytics Data API、Google Sheets API。三套 API 各自有启用步骤，不是启用一个就覆盖另外两个。
2. 建一个服务账号，下载 JSON 密钥，放到仓库外，用环境变量把路径交给脚本。密钥不进 git。
3. 人工完成一次产品授权：Search Console 资源里把服务账号邮箱加成用户；GA4 媒体资源里授予该邮箱；把那张 Google 表格共享给该邮箱。Cloud 项目的 IAM 角色不等于这三处授权。
4. 仓内一个 Python 脚本，依赖官方客户端：GA4 用 `google-analytics-data`（快速入门样例在 GitHub），Search Console 与 Sheets 用 `google-api-python-client` 调 REST。任何能执行 `python` 的 harness 都跑同一条命令。
5. 脚本每次做四件事：读执行登记（L0，人已经写好）；按其中的 URL 查 Search Analytics，展示写入 L1、点击写入 L2；对登记里尚未确认收录的 URL 做 URL Inspection；把结果追加到表格。询盘列留给站点订单、表单和邮箱，不从 GA4 填。
6. 日程用系统定时任务跑这个脚本。GSC 的定稿数据通常晚 2–3 天，不必在人点击发布的同一分钟去拉。

账号权限、配额和坑见下三节。Looker Studio 不在这条写入路径里。

## Search Console

### 事实：三套接口分别做什么

Search Console API 提供 Search Analytics、Sitemaps、Sites、URL Inspection。Search Analytics 查点击、展示、点击率和排名；Sitemaps 列出、提交、读取、删除站点地图；URL Inspection 查看某个 URL 在 Google 索引里的状态。

来源：<https://developers.google.com/webmaster-tools/v1/api_reference_index>

URL Inspection 的方法是 `POST https://searchconsole.googleapis.com/v1/urlInspection/index:inspect`，请求体含 `inspectionUrl`、`siteUrl`、可选 `languageCode`。文档写明：目前只返回 Google 索引中那一版的状态，不能用它测试线上 URL 能不能被索引。范围是 `webmasters` 或 `webmasters.readonly`。返回里有 `indexStatusResult.verdict`（`PASS` / `FAIL` 等）、`coverageState`、`lastCrawlTime`、规范网址。

来源：<https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect>，<https://developers.google.com/webmaster-tools/v1/urlInspection.index/UrlInspectionResult>

Indexing API 是另一套接口。它只接受带 `JobPosting`，或嵌在 `VideoObject` 里的 `BroadcastEvent` 的页面，用来通知抓取或移除。默认配额只够开通测试，更大用量要另行申请。普通营销页不能用它代替 URL Inspection，也不能用它「请求编入索引」。

来源：<https://developers.google.com/search/apis/indexing-api/v3/quickstart>（页面标注更新于 2026-07-16）

### 事实：授权

Search Analytics 的范围是 `https://www.googleapis.com/auth/webmasters.readonly` 或 `https://www.googleapis.com/auth/webmasters`。资源标识：网址前缀资源用 `http://www.example.com/` 这种形式，网域资源用 `sc-domain:example.com`。

来源：<https://developers.google.com/webmaster-tools/v1/searchanalytics/query>（页面内容在 2026-08-11 的文档版本中含 `dataState`）

授权指南写明，私有用户数据走 OAuth 2.0，凭证类型包括服务账号。该页没有逐步写出「把服务账号邮箱加进 Search Console」。

来源：<https://developers.google.com/webmaster-tools/v1/how-tos/authorizing>

Search Console 的用户等级是 Owner、Full、Restricted。Full 可以查看全部数据并做一部分操作；Restricted 对多数数据有查看权。权限表把 Performance、URL Inspection、Submit sitemap 列成不同功能；URL Inspection 一行在 Restricted 下写着 “Fetch only”。本次抓取没有还原勾选图标，因此不能从该表断定 Restricted 能否提交站点地图。

来源：<https://support.google.com/webmasters/answer/7687615>

Indexing API 的前提文档写的是另一套产品，但它证明了同一件事：服务账号要作为站点用户加进去，邮箱在密钥 JSON 的 `client_email` 里，形如 `name@project.iam.gserviceaccount.com`，由已验证所有者加为委托所有者。

来源：<https://developers.google.com/search/apis/indexing-api/v3/prereqs>

`AminForou/mcp-gsc` 的 README 写的 Search Console API 做法是：启用 API，下载服务账号 JSON，在资源的 Users and permissions 里把该邮箱加成 Full。OAuth 桌面客户端是另一条路，第一次要浏览器登录。

来源：<https://github.com/AminForou/mcp-gsc/blob/main/README.md>

**推断：** 读展示和点击、做 URL Inspection，用 `webmasters.readonly` 加上资源用户身份就够。要提交站点地图，按 mcp-gsc 已写出的做法把邮箱加成 Full，不把 Restricted 当成已证实够用。

### 事实：配额

限额页（标注更新于 2025-08-28）把配额分成三档。

Search Analytics 还有单独的负载配额：10 分钟一档的短期负载，1 天一档的长期负载。超限错误都叫 quota exceeded。按网页或查询词分组、过滤，以及拉很长的日期区间，负载更贵。页面对 QPS 的数字是：

- 同一站点 1,200 次/分钟
- 同一用户 1,200 次/分钟
- 同一项目 40,000 次/分钟，30,000,000 次/天

URL Inspection：

- 同一站点 2,000 次/天，600 次/分钟
- 同一项目 10,000,000 次/天，15,000 次/分钟

其余资源（限额页没有再单列 Sitemaps 或 Sites）：同一用户 20 次/秒、200 次/分钟；同一项目 100,000,000 次/天。

来源：<https://developers.google.com/webmaster-tools/limits>

另有数据行数上限，不是上面的调用次数：单次响应最多 25,000 行；每个搜索类型、每个站点、每天最多露出 50,000 行（按点击排序）。官方建议每天拉一天的数据，并用 `startRow` 翻页，直到返回 0 行。

来源：<https://developers.google.com/webmaster-tools/v1/how-tos/all-your-data>

### 事实：延迟、保留、冷启动能拿到什么

`dataState` 省略或为 `final` 时只返回已定稿数据；`all` 包含仍在处理的新数据；`hourly_all` 给小时拆分。请求近期数据时，响应里的 `metadata` 会标出仍不完整的日期或小时，时区是 America/Los_Angeles。

来源：<https://developers.google.com/webmaster-tools/v1/searchanalytics/query>

效果报告：收集到的数据通常 2–3 天后可见；最近约 2 天可能仍是初步数据；除 24 小时视图外，按日的数据以太平洋时间切日。

来源：<https://support.google.com/webmasters/answer/7576553>，以及效果报告的数据说明页 <https://support.google.com/webmasters/answer/17011364>

Google 在 GA4 的 Search Console「Queries」说明里写明：Search Console 保留最近 16 个月的数据，因此 Analytics 里的对应报表也最多 16 个月；Search Console 收集之后 48 小时，Search Console 和 Analytics 都能看到。若先建网站数据流再完成站点验证，数据从验证完成时起算；若先验证再建数据流，从建数据流当天起算。

来源：<https://support.google.com/analytics/answer/13682862>

新站：Search Console 帮助写明，新创建的站点或新加入 Search Console 的站点，生成数据最多要一周。添加资源本身不影响网站在搜索里的表现。数据从有人把资源加进账号开始收集，验证前也会收集。平台资源的说明写明，刚添加时图表可以是空的，处理需要几天，只显示收集开始之后的日子。

来源：<https://support.google.com/webmasters/answer/96568>，<https://support.google.com/webmasters/answer/34592>，<https://support.google.com/webmasters/answer/17148418>

Search Analytics 在没有数据的日子不会返回该日的行；`startRow` 超过结果数时，响应成功且行数为 0。按网页和查询词分组时，系统会为了算得动而丢掉一部分行，所以明细查询的点击数可以小于只按国家、设备汇总的数字。

来源：<https://developers.google.com/webmaster-tools/v1/api_reference_index>，<https://developers.google.com/webmaster-tools/v1/how-tos/all-your-data>

**推断：** 零展示的冷启动站点上，Search Analytics 的正常结果是空行，不是接口坏了。站点地图提交和 URL Inspection 不依赖已经有人搜索过。L1「已收录」可以先靠 Inspection 的 `verdict`；L1「有展示」和 L2「有点击」要等搜索侧真的出现，而且定稿数要按 2–3 天的滞后读。品牌词过滤器另有一句「低展示量的站点不可用」，所以冷启动不要依赖它。

来源中的品牌词限制：<https://support.google.com/webmasters/answer/17011259>

**未查证：** 从未被抓取的 URL，Inspection 返回的 `coverageState` 英文字符串本次没有抓到样例。按查询词隐藏低频查询的隐私阈值，本次打开的限额页和「取全部数据」页没有写出单独数字；能引用的是上面的「分组越细，行越少」。

### 事实：现成实现

`AminForou/mcp-gsc`（GitHub API，2026-10-14）：1,918 star，252 fork，15 个 open issue，MIT，默认分支 `main`，`pushed_at` 为 2026-09-15。`pyproject.toml` 里包名 `mcp-search-console`，版本 0.4.1，分类为 Development Status :: 4 - Beta，依赖 `google-api-python-client`、`google-auth`、`mcp[cli]>=1.3.0,<2.0.0`，要求 Python ≥ 3.11。

来源：<https://github.com/AminForou/mcp-gsc>，<https://github.com/AminForou/mcp-gsc/blob/main/pyproject.toml>，<https://api.github.com/repos/AminForou/mcp-gsc>

README 列出的工具覆盖资源列表、Search Analytics、时段对比、单 URL 与最多 10 个 URL 的 Inspection、站点地图的列出和提交。破坏性操作（加删资源、删除站点地图）默认关闭。环境变量 `GSC_DATA_STATE` 默认 `all`，`final` 只要定稿。0.4.x 的更新说明记录了使用者报来的超时、排序和富媒体结果字段错误，并在 2026 年 9 月的版本里修过。

来源：<https://github.com/AminForou/mcp-gsc/blob/main/README.md>

**推断：** 按地图里的标准，它「自带数据接入代码」，Search Console 这一段可以当已验证的调用样例。它不适合当 playbook 的接入本体：入口是 MCP，文档按 Claude Desktop、Cursor、Codex、Gemini CLI 配置，五家兼容目标并不都靠 MCP。脚本应借用同一套官方 Python 客户端和同一套授权，而不是把 MCP 服务器当成唯一跑法。本次没有执行这个服务器。

GA4 官方快速入门页另外链了一份 Google 自己的 Analytics MCP：<https://github.com/googleanalytics/google-analytics-mcp>。本次没有读该仓库的 README，不把它算进「可直接用」的结论。

## GA4 Data API

### 事实：授权与官方样例

Data API 快速入门（页面内容在 2026-10-09 一代文档中）写明可用用户账号或服务账号，并演示 `runReport`。抓取到的「开始之前」是用户账号标签：`gcloud auth application-default login`，范围含 `https://www.googleapis.com/auth/analytics.readonly`，然后在 Analytics 界面授予该账号对媒体资源的访问。样例使用 `google.analytics.data_v1beta.BetaAnalyticsDataClient`，注释写明默认构造函数读取 `GOOGLE_APPLICATION_CREDENTIALS`。Python 样例文件：<https://github.com/googleanalytics/python-docs-samples/blob/main/google-analytics-data/quickstart.py>。

来源：<https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart>

**未查证：** 服务账号标签下的逐步点击本次没有单独抓到。快速入门没有写明最低角色是 Viewer 还是别的角色，只要求在界面授予访问。修改数据保留期的说明另要求 Editor：<https://support.google.com/analytics/answer/7667196>。

**推断：** 服务账号邮箱要在 GA4 媒体资源的访问管理里单独加上。只在 Cloud 项目里启用 Data API，读不到报表。

### 事实：配额

限额页标注更新于 2026-10-13。类别是 Core、Realtime、Funnel、Chat。普通 `runReport` 走 Core。标准媒体资源：

- Core 令牌：每媒体资源每天 200,000，每小时 40,000，每项目每媒体资源每小时 14,000
- 并发请求：每媒体资源 10
- 每项目每媒体资源每小时服务端错误：10

360 的 Core 令牌大约是标准档的 10 倍，并发 50。多数请求不超过 10 个令牌；行数、维度、过滤、日期长度、高基数字段会加价。请求体加 `"returnPropertyQuota": true` 可在响应里看到消耗和剩余。任一桶剩余为 0，随后请求返回 `429 RESOURCE_EXHAUSTED`。日配额在太平洋时间午夜刷新。

来源：<https://developers.google.com/analytics/devguides/reporting/data/v1/quotas>

2023 年的博客仍写着更小的「每项目每媒体资源每小时 1,250」。以 2026-10-13 的限额页为准。

来源（旧文，不采用其中的数字）：<https://developers.google.com/analytics/blog/2023/data-api-quota-management>

**推断：** 一天拉一次、按登记 URL 过滤的报表，远低于标准档配额。配额不是这条路径的约束。

### 事实：延迟与保留

标准媒体资源的典型处理：实时为数分钟，日内约 2–6 小时，日处理约 12 小时。Data API 查询不在 Analytics 360 报表 SLA 的覆盖范围内，帮助页把它标成 best effort。

来源：<https://support.google.com/analytics/answer/12233314>

数据保留控制的是用户级和事件级数据。标准媒体资源的用户级保留是 2 个月或 14 个月；其余事件数据同样是 2 或 14 个月，26/38/50 个月只给 360。帮助页写明：这项设置不影响标准汇总报表（含主要和次要维度），只影响探索和漏斗报表。Large 与 XL 媒体资源的事件级保留会被压到 2 个月。

来源：<https://support.google.com/analytics/answer/7667196>

**未查证：** Data API 的 `runReport` 是否完全不受 2/14 个月保留期影响。帮助页说的是界面上的标准汇总报表，没有点名 Data API。零事件的新媒体资源会返回空行还是错误，本次没有调用，不编。

### 事实：德国法与 Consent Mode

现行法名是《电信与数字服务数据保护与隐私法》（TDDDG）。§25 第 1 款：在终端用户的终端设备上存储信息，或访问已经存储在该设备上的信息，只有在终端用户基于清楚、全面的信息作出同意后才允许；告知和同意依 GDPR 作出。第 2 款的例外只有两类：仅为通过公共电信网传送消息，或存储/访问对于提供用户明确要求的数字服务是绝对必要的。

来源：<https://www.gesetze-im-internet.de/ttdsg/__25.html>

§26 允许建立经认可的同意管理服务，并授权联邦政府用条例规定细节。配套条例 EinwV 已公布。

来源：<https://www.gesetze-im-internet.de/ttdsg/__26.html>，<https://www.gesetze-im-internet.de/einwv/BJNR0200B0025.html>

**未查证：** TTDSG 改名为 TDDDG 的生效日。本次只确认现行文本的名称是 TDDDG。第 108 次数据保护会议的记录写明，引入《数字服务法》的修改法把「Telemedien」换成了「digitale Dienste」，并于 2024-11-06 的文本通过了《数字服务提供者指南》1.2 版，用以替换 2021 年电信媒体指南 1.1 版。1.2 版 PDF 正文本次没有取到。

来源：<https://www.datenschutzkonferenz-online.de/media/pr/Protokoll_108_DSK.pdf>

1.1 版（2022-11-30）对「覆盖面测量」的写法是：监管机构故意不说覆盖面测量可以一律不经同意，因为这个词太宽；是否可以不经同意，最多只能针对一套写明的配置和目的来判断。

来源：<https://www.datenschutzkonferenz-online.de/media/oh/20221130_OH_Telemedien_2021_Version_1_1.pdf>

Google 的 Consent Mode 不是这条法律的文本。Google Ads 帮助写明：要继续把适用的代码/SDK 用于衡量、广告个性化和再营销，必须向欧洲经济区用户取得对个人数据使用的同意，并把同意信号传给 Google。v2 增加的参数是 `ad_user_data` 和 `ad_personalization`。GA4 帮助写明：与 Google Ads 等广告产品共用 Analytics 数据时，若不处理，2024 年 3 月起受众只包含欧洲经济区以外的用户；广告衡量看 `ad_user_data`，广告个性化看 `ad_personalization`。

来源：<https://support.google.com/google-ads/answer/13695607>，<https://support.google.com/analytics/answer/14275483>

参数说明：`analytics_storage` 控制分析用的存储（例如访问时长）。`analytics_storage=denied` 时不读写第一方分析 Cookie 或应用标识。该页写明示意图不是法律意见。

来源：<https://developers.google.com/tag-platform/security/concepts/consent-mode>，<https://support.google.com/analytics/answer/13802165>

**推断：** 在德国站点上安装 GA4 的 JavaScript，属于 §25 的终端访问，不能靠「统计对我们有用」落进绝对必要例外。同意横幅是法定前提，Consent Mode 是横幅结果要传给 Google 的格式。默认值应为拒绝，用户作出同意后再改为授予。地图里记录的「站点尚无同意横幅、尚无 GA4」如果仍然成立，Data API 会没有站内事件可读。本次没有重核线上站点。

**未查证：** 已有多少家服务按 EinwV 被正式认可。Google 认证 CMP 名单本次没有逐条对到下面的 WordPress 插件。加载 `gtag.js` 本身是否在任何德国判决里被单独认定，本次没有打开判决书。

### 事实：WordPress 上能看到的同意插件

2026-10-14 调用 WordPress.org Plugin API（`active_installs`）。返回值是目录公布的分档，不是精确安装数，也不是德国市场份额：

| 插件 | slug | API 返回的 active_installs |
| --- | --- | --- |
| Complianz | `complianz-gdpr` | 1,000,000 |
| CookieYes | `cookie-law-info` | 1,000,000 |
| Cookie Notice（Cookie Compliance） | `cookie-notice` | 800,000 |
| iubenda | `iubenda-cookie-law-solution` | 200,000 |
| WP Consent API | `wp-consent-api` | 200,000 |
| Real Cookie Banner | `real-cookie-banner` | 100,000 |
| Cookiebot by Usercentrics | `cookiebot` | 100,000 |
| Site Kit by Google | `google-site-kit` | 5,000,000 |

`borlabs-cookie` 返回 404，不在这个目录里。

来源：`https://api.wordpress.org/plugins/info/1.2/?action=plugin_information&request[slug]=<slug>`，本次对上表 slug 各请求一次。

Site Kit 是 Google 发布的插件，名称写的是 Analytics、Search Console、AdSense、Speed。它是在 WordPress 里连接产品的界面，不是同意横幅，也不是往表格追加反馈行的脚本。

**未查证：** Site Kit 当前版本是否会自行发出 Consent Mode v2 信号。Borlabs Cookie 的安装量。哪一款是德国安装商站点的主流，目录全球分档回答不了。

**推断：** 若以后要上 GA4，WordPress 侧的常见拼法是一个同意插件加上 WP Consent API，让别的插件读取同一份同意状态。选型不是本票要定的实现。

### 事实：无 Cookie 替代

Plausible 的数据政策写明：不用 Cookie，不生成持久访客标识，不跨设备、跨站、跨应用跟踪；用当日盐、站点域名、IP 和 User-Agent 做哈希，盐每 24 小时轮换并删除；访客数据在欧盟处理，法律实体在爱沙尼亚；源代码在 GitHub。同一站点写明，使用 Plausible 不需要为分析展示 Cookie 横幅或为跟踪收集同意，并建议把具体问题交给自己的律师。

来源：<https://plausible.io/data-policy>，<https://plausible.io/cookieless-web-analytics>

其试用说明列出 Starter、Growth、Business、Enterprise。首页在本次检索摘录里，10k 月页面浏览这一档显示 Starter 每月 $9（1 个站点，数据保留 3 年）、Growth 每月 $14（最多 3 个站点）、Business 每月 $19（最多 10 个站点，数据保留 5 年，Stats API 每小时 600 次，含 Looker Studio 连接器）。30 天试用、不需要信用卡。更高流量档的标价本次没有整表抓下。`/pricing` 返回 404。

来源：<https://plausible.io/>，<https://plausible.io/docs/trial-to-paid>

Matomo 官方 FAQ：关掉 Cookie 不会自动停止跟踪，JavaScript 跟踪仍会跑。它写明，多数欧洲国家的 ePrivacy 国内法要求，在使用落入技术范围的跟踪（含 Cookie 和 JavaScript）之前取得同意，除非落进绝对必要例外；有的法域在不存储访客 ID 等个人数据时，无 Cookie 跟踪可以免同意。FAQ 要求咨询自己的法律顾问。WordPress 里关闭 Cookie 的位置是 Matomo Analytics → Settings → Disable cookies。关闭 Cookie 会降低回访识别的准确度。

来源：<https://matomo.org/faq/general/faq_157/>

Matomo 价格页（本次抓取）：On-Premise 的 Community 为永久免费，用户和 hit 不限，支持方式是论坛。Cloud 在 50,000 hits/月这一档显示每月 22 EUR（不含税），年付 220 EUR；超出部分页面写 5,000 hits 为 2.2 EUR（不含税）。FAQ 写明 Cloud 数据存在德国法兰克福。自建可选服务器位置。价格页同时出现 On-Premise 插件包：Team 275 EUR/月、Business 1,450 EUR/月、Enterprise 3,400 EUR/月；对比表又写 Team「From €230/mo」。两套数字都在同一页，本次不断言哪一个是唯一标价。所有方案的功能列表含 HTTP Analytics API，因此自建版也可以被脚本读取。

来源：<https://matomo.org/pricing/>

**推断：** 这两样能替代的是 GA4 的站内浏览和事件，不能替代 GSC 的展示和点击，也不能替代表格里的执行登记和询盘。Plausible 声称免横幅；Matomo 自己不这么承诺；DSK 1.1 版拒绝给「覆盖面测量」开一揽子免同意。在 1.2 版正文未读到之前，不能把任一产品写成德国监管已经放行。代价除此之外还有：回访和跨会话归因变弱；Plausible 的 Stats API 和 Looker 连接器在首页摘录里属于 Business；Matomo 自建免费但要自己托管，Cloud 从上述 22 EUR 档起。

## Google Sheets

### 事实：追加行、读取、配额、范围

`spreadsheets.values.append` 把值追加到范围内找到的下一行表。调用要给出表格 ID、A1 范围和 `valueInputOption`。范围之一是 `https://www.googleapis.com/auth/spreadsheets`，另外也接受 `drive` 和 `drive.file`。`INSERT_ROWS` 会为新数据插入行。

来源：<https://developers.google.cn/workspace/sheets/api/reference/rest/v4/spreadsheets.values/append>（本次打开的是该中文镜像页；英文对应页是 <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/append>）

限额页（标注更新于 2026-09-03）：

- 读：每项目每分钟 300，每用户每项目每分钟 60
- 写：同样是 300 和 60
- 建议单次载荷不超过 2 MB
- 单次处理超过 180 秒会超时
- 在每分钟配额内，没有每日次数上限
- 服务账号的调用算作一个账号
- 标准用量不另收费；超出配额「计划在 2026 年较晚时候」向 Cloud 账单收费

来源：<https://developers.google.com/workspace/sheets/api/limits>

**未查证：** 该页 2026-09-03 之后，超额收费是否已经开始。服务账号授权指南里「必须把表格共享给服务账号邮箱」这句，本次没有打开到原文。

**推断：** 与 GSC、GA4 相同，只启用 API 不够，还要把表格共享给服务账号邮箱，权限至少要能追加行。`append` 会在给定范围内寻找已有的表再往下写；执行登记若把说明文字放在数据区下面，行可能写错位置。反馈脚本用固定工作表、固定列、`INSERT_ROWS`，比依赖自动找表稳妥。这一句是用法推断，不是限额页的原文。

一天几十行的执行登记和反馈追加，离 60 次/分钟的写配额很远。

## 三套凭据能否共用

**事实（分属三份文档）：**

- Search Console 认 `webmasters` / `webmasters.readonly`，并认服务账号这种 OAuth 凭证。
- GA4 Data API 快速入门使用 `analytics.readonly`，并用 `GOOGLE_APPLICATION_CREDENTIALS` 指向密钥。
- Sheets 的 append 认 `spreadsheets` 等范围；限额页把服务账号视为单一用户。

**推断：** 一个 Cloud 项目里的一把服务账号密钥可以调用这三套 API。令牌请求里带上这三个范围。产品侧仍是三次授权：Search Console 用户、GA4 媒体资源访问、表格共享。不是「一把密钥自动打通三个产品」。用户 OAuth 也能打通，但要浏览器同意，适合有人值守的第一次登录；无人值守的定时脚本用服务账号，避免把刷新令牌绑在某一个人的登录态上。OAuth 同意屏幕处于测试状态时刷新令牌能活多久，本次未查证。

Looker Studio 的连接步骤是登录 Looker Studio 后再点授权，用的是当时登录的用户，不是脚本里的 JSON 密钥。脚本身份和看图身份可以是同一个人的 Google 账号，也可以分开：脚本用服务账号写表，人用自己的账号在 Looker 里打开同一张表。

## Looker Studio

### 事实

Google 提供的连接器列表包含 Google Analytics、Search Console、Google Sheets。

来源：<https://docs.cloud.google.com/looker/docs/studio/available-connectors>（标注更新于 2026-03-16）

Search Console 连接器：创建数据源，选择该连接器，授权，选站点，再选 Site Impression 或 URL Impression，并选搜索类型（web、image、video、news；URL Impression 另有 discover、googleNews）。

来源：<https://docs.cloud.google.com/looker/docs/studio/connect-to-search-console>

Google 表格连接器：一个数据源连接一张工作表中的一个工作表标签，可选自己拥有的或已共享的表格。

来源：<https://docs.cloud.google.com/looker/docs/studio/connect-to-google-sheets>

**推断：** 看图是零开发：没有仓内代码、没有自定义连接器。它不把 L0–L3 写回表格，也不是「据此行动」的规则引擎。反馈分级的记录仍是表格；Looker 只是可选的阅读层。Site Impression 和 URL Impression 要分开选，查询词和落地页不是同一个数据源里的一张表。连接器能回溯多少个月，本次未在该帮助页上核到，不把它说成与 API 的 16 个月相同。

## 和这条闭环的对应

**推断，规则来自仓库术语，数据来自上面对 API 的事实：**

| 信号 | 最小来源 | 不依赖 |
| --- | --- | --- |
| L0 已执行 | 人写入 Google 表格的执行登记 | GSC、GA4 |
| L1 页面被收录 | URL Inspection 的索引结论 | 同意横幅 |
| L1 有展示 | Search Analytics 的 impressions | 同意横幅 |
| L2 搜索点击 | Search Analytics 的 clicks | 同意横幅 |
| L2 邮件回复 | 不在本票；邮箱只读是另一张票 | GA4 |
| L3 询盘 | 站点订单、联系表单、来信 | GA4 |

冷启动阶段 CONTEXT 把决策放在 L0–L1。此阶段 GSC 可能连续多天是空行，Inspection 和站点地图状态是先有的机器可读信号。GA4 在同意率很低的 B2B 德语站上会更稀，而且装标签本身要先过 §25。所以 GA4 是可加的站内补充，不是这条最小回流的必经段。

## 已知坑

1. 资源字符串必须和 Search Console 里的资源完全一致：`sc-domain:` 与带尾斜线的网址前缀不是同一个标识。社区里有人因此在 URL Inspection 收到 `PERMISSION_DENIED`（“You do not own this site, or the inspected URL is not part of this property.”）。这是帮助社区的报告，不是接口规范里的错误码表。来源：<https://support.google.com/webmasters/thread/251807022>
2. 不传 `dataState` 就只有定稿数据，最近 2–3 天看起来像「接口没更新」。
3. 按日数据用太平洋时间。和德国本地日历对不齐时，先改日切，再怀疑丢数。
4. 同时要网页和查询词时，行会被丢掉；单次 25,000 行，每个搜索类型每天 50,000 行。
5. URL Inspection 每天每站点 2,000 次，只查执行登记里的 URL，不扫全站。它看不到线上实时测试。
6. Indexing API 不能用来催普通页面收录。
7. 新资源一周内没有效果数据，是帮助页写过的正常情况。
8. 服务账号没被加进对应产品时，API 会 403。启用 API 只解决「项目能不能调」，不解决「这个身份能不能看这份资源」。
9. Sheets 的 `append` 会自己找表；范围里若有说明行，写入位置会偏。
10. Sheets 超额收费在 2026-09-03 的文档里仍是「计划在年内收取」。每天几十行碰不到配额，但不要把「永远免费」写成文档承诺。
11. JSON 密钥是长期秘密。丢失后按被公开处理，轮换密钥，并从三个产品里去掉旧邮箱。

## 仍未解决

- 本站现在有没有 Search Console 资源、GA4 媒体资源和一张用来登记的表格，所有权在哪个 Google 账号。这属于账号盘点，不是本票。
- 《数字服务提供者指南》1.2 版正文是否仍拒绝「覆盖面测量一律免同意」。1.2 版 PDF 本次没取到。
- Restricted 用户调用 Search Analytics 和提交站点地图时，API 是否与帮助页权限表一致。勾选图标没有还原。
- 服务账号访问某张表格，是否除了 OAuth 范围之外还必须把文件共享给该邮箱。推断是必须，授权指南原文本次未打开。
- OAuth 同意屏幕在测试状态下，刷新令牌的有效期。
- 从未被抓取的 URL，Inspection 的 `coverageState` 原文。
- Data API 在零事件媒体资源上的响应形状，以及它是否受 2/14 个月保留期约束。
- Sheets 超额是否已在 2026-10-14 之前开始计费。
- Plausible 高于 10k 月浏览量的完整价目；Matomo Cloud 高于 50,000 hits 的完整价目；同一价格页上 On-Premise 包月价两套数字以哪套为准。
- EinwV 下是否已有可实际使用的认可同意服务。
- Google 认证 CMP 与 Complianz、CookieYes、Cookiebot、Real Cookie Banner 的对应关系；Borlabs 的安装量；Site Kit 是否自行发送 Consent Mode v2。
- Looker Studio 的 Search Console 连接器能否覆盖 API 的 16 个月，以及查询词与落地页之外还缺哪些 API 字段。
- 本票没有把上述脚本接到 de-linker 的真实资源上跑一次。路径在文档和现成客户端上成立；本站账号未通之前，不能说这条回流已经出数。
