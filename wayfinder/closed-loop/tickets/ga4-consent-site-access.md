---
wayfinder: task
status: closed
assignee: Codex 会话 01a152c8-81b1-7bf1-8521-f55ce229ff7f 2026-10-19
step: 5
blocked_by: [consent-ga4-research, gsc-site-access]
---

# GA4 与同意横幅站点接入

## Question

（agent 在新站仓库执行；操作者建 GA4 资源并验收）按「同意横幅与 GA4 选型调研」的推荐，在线上站点装好同意横幅与 GA4。

- 操作者清单：`所有者账号` 建 GA4 账号 + 媒体资源 + 网站数据流（时区 Europe/Berlin、币种按站点），取衡量 ID 交 agent；`日常账号` 加账号层管理员；服务账号加媒体资源管理员（用户 2026-10-19 当场裁定，供后续任务）。
- 新站仓库按其 `AGENTS.md` 规矩：开票、规格、PR、CI、验收三件套（含 1440 / 390 × EN / DE 视觉验收）；横幅文案 EN 先行、DE 独立撰写，走对抗评审；横幅作为裁定过的变更进变更台账，其余像素零差异。
- 验收：拒绝前无 GA4 请求、无 `sbjs_*` Cookie（浏览器网络面板 / Tag Assistant 证据）；接受后 GA4 实时报告可见自己的访问；撤回可用。

## 调研交接（「同意横幅与 GA4 选型调研」关票时写入）

- 依据：`wayfinder/closed-loop/research/consent-ga4.md`。推荐组合与理由在其开头；坑在第 5 节，逐条过。
- 组合：Complianz 免费版 + WP Consent API + Site Kit；Site Kit 开 Consent Mode，Complianz 自己的 Consent Mode 不开；Script Center 在 statistics 同意前挡 `googletagmanager.com`、`google-analytics.com`、`googleads.g.doubleclick.net`（及 Tag Gateway 第一方 URL，若启用），不挡 Site Kit 内联 consent default 与本地 consent-mode JS → Basic。`ad_user_data` / `ad_personalization` 只跟 marketing，不随分析打开。
- **必须在本地 / 评审站实测、未经实证不得上线的**：Script Center 能否在执行前挡住 Site Kit 已入队的 `gtag.js`；放行后 dataLayer 里排队的 consent update 是否生效；LiteSpeed 延迟 / 合并 JS 是否打乱「default → 横幅 → 放行」顺序（`wait_for_update` 仅 500 ms）；Tag Gateway 默认开关（Complianz changelog 声称已支持 Tag Gateway URL，仍要实测）；Complianz 免费版能否按 Polylang 为 EN / DE 各存一套横幅文案（readme 只写 WPML）。任一项不成立 → 按调研第 4 节的后备（仓库插件里把脚本推迟到同意后，不走 Code Snippets），或回到 CookieYes 备选，理由记入新站仓库规格。
- 横幅第一层：同等的接受与拒绝；按 DSK 边号 (119)(120) 写目的、欧洲经济区外处理、逐一点名接收方；撤回与同意一样容易；保留旧横幅文本与流程说明（边号 (85)）。
- **线上现状**：首页已在无横幅情况下加载 WooCommerce 订单归因（Sourcebuster，`sbjs_*`），按 DSK 边号 (80) 不属绝对必要。本票须把它纳入横幅管理（WP Consent API 对应类别），并在验收里证明拒绝前不写 `sbjs_*`。**优先纳入横幅管理而不是关掉**：订单来源是询盘归因的首选候选（见地图 Not yet specified「询盘归因到动作」），验收还要证明同意后它照常记录。
- 「GSC 站点接入」已选 Site Kit 作载体并装好（见下节），本票直接复用，不再安装。

## 站点接入交接（「GSC 站点接入」关票时写入）

- **Site Kit 已装（2026-10-14，「GSC 站点接入」写入）**：线上 Site Kit by Google **1.189.0**，WP-CLI 从 wordpress.org 原生安装；由后台**用户 1（唯一管理员）**的会话、用 `所有者账号` 连接。只连了 Search Console（资源 `https://de-linker.com/`，验证方式 = Site Kit 虚拟 HTML 文件 `/google<令牌>.html`）；**Analytics 未连**，欢迎页的 Analytics 勾与「匿名使用数据」勾都未勾；仪表盘目标选了「Sell products」（只影响卡片）。
- **配置位置**：后台 Site Kit → Settings → Connected Services（Search Console 在此，不可断开）；接 GA4 时在同处「Connect more services → Analytics」，或仪表盘上的「Set up Analytics」。选项在 `googlesitekit_*`（`googlesitekit_search-console_settings` = `{"propertyID":"https://de-linker.com/","ownerID":1}`），验证令牌在用户 1 的用户选项 `wp_googlesitekit_site_verification_file`。
- **不要动的**：不删用户 1、不在 Site Kit 里 Reset / Disconnect，否则 GSC 验证会掉；新站 `just cutover verify` 的 `search-console` 段与 e2e「Site Kit by Google is still active」会报错（规格 `docs/specs/145-search-console.md`）。
- **前台现状**：Site Kit 未连 Analytics 时每页已多一行 `<link rel='dns-prefetch' href='//www.googletagmanager.com'>`（只是 DNS 预解析提示，不向 Google 发请求、不写 Cookie）与 generator meta。横幅验收「拒绝前无 GA4 请求」时把这行算在已知现状里，不当作违规请求。

## 完成标准

- 上述三条验收证据齐，新站仓库验收记录链接写进 Resolution。

## 审稿交接（「操作者审稿」关票时写入，2026-10-15）

- 同意横幅的 EN / DE 文案是对外文字：新站仓库的对抗评审照走，另外上线前要按本仓库 `docs/feedback-rules.md` 第 10 节给操作者审稿，按意见改到操作者说「可以了」再进 PR。两道互不替代：对抗评审查合规与表述，审稿是操作者看行不行、想不想改。

## 2026-10-19 重新认领

用户要求从头做，取代旧施工会话；新站原撤案票已重开，当前分支与证据链接在本轮完成时回填。

- Google 账号角色沿用地图：所有者账号持有，日常账号共同管理。
- **权限裁定**：用户原话“都是管理员权限，我不想因为权限分太细导致后续任务无法执行”。按本次待执行授权的原范围落实：日常账号为账号层管理员，服务账号由媒体资源查看者改为媒体资源管理员。
- 所有者已亲自接受德国条款，专属 GA4 账号、媒体资源、网站数据流已创建并浏览器读回；ID 只进私有 vault `marketing/00-system/ga4-owner-checklist.md`。站点标签尚未连接。

## Resolution · 2026-10-19

- 已完成。用户改定 **CookieYes**，并明确要求本地与线上同步；英德文案与外观经过对抗评审和操作者多轮实看，最终批准“可以了，英德两版一起上线”。原调研中的 Complianz 组合由本轮实现取代，不再执行其 Script Center 步骤。
- 新站实现 [GA4 与 CookieYes 接入](https://github.com/AssassinFlash/de-linker/pull/358)，两个 CI 检查通过后合并为 `21020e094ac5011d63363e91691aa6eb68b174d0`。Spec、Standards 独立复核完成；原生 CookieYes 3.5.7 + WP Consent API 2.1.0 + Site Kit 1.189.0，无付费服务、无 Code Snippets。
- 生产部署 `20261019T082705433994Z-21020e09` 已完成原生 `resume-deploy` 验证与归档；维护已关闭。Search Console 插件、原资源与所有者用户 1 保留，虚拟验证文件 HTTP 200。首页、产品、询盘、账号英德路线及既有重定向回归通过。
- 先发布 CookieYes 与解析前阻断，再在所有者账号下完成 Site Kit 连接。用户已当场确认其额外请求的两项权限。GA4 专属账号、媒体资源、网站数据流和共同管理员均已读回，真实值只在私有 vault 清单。保留期 14 个月，Google Signals、用户提供数据和广告个性化关闭。
- **真实生产验收 7 组通过**：EN/DE × 1440/390 首次与拒绝后没有 Google 追踪请求、`_ga`、`sbjs_*`；分析、来源、双用途可分别生效；撤回后清 Cookie，下一德语页没有后续 Google 追踪请求。测量传输未拦截、未绕过 CSP。三个 Ads 同意信号在默认及全部更新后均保持 denied。GA4 实时报告已实际看到 1 位活跃用户及首页 `page_view`、`session_start` 等事件。
- 本地实例 `c201_20261019`（9156）同步相同代码、双语配置、隐私政策、永久页脚撤回入口与 WindPress 原生缓存；隔离环境不向生产 GA4 写夹具。本地 9 项真实插件浏览器测试、全仓 `just test`、静态检查均通过。1440/390 × EN/DE Computer Use 验收及本地变更前后非授权区域零像素差异记录在新站 `docs/acceptance/2026-10-19/201-consent/`。生产截图也已保存；生产与本地 3/4 全页完全相同，英语手机页仅既有语言胶囊区域有像素差异，细节如实记入私有验收，不声称线上四页全部零差异。
- 最终线上证据与账号交接：私有 vault `marketing/00-system/ga4-owner-checklist.md` 末节；`marketing/00-system/evidence/2026-10-19-ga4/` 的 `site-kit-connected.png`、`realtime-accepted-visit.png`、`live/network-cookies.json`、`live-visual/`。PR 内验收 README 是合并前截面，本 Resolution 与私有清单补齐生产完成状态。
- 执行登记四行已查证：`E-20261019-01`、`E-20261019-02`（全站首页 EN/DE），`E-20261019-03`、`E-20261019-04`（隐私政策 EN/DE）。后续「GA4 进看板」已直接写入 Basic 模式、用途及资源指针交接；未在本会话提前执行后续票。
