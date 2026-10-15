---
wayfinder: task
status: open
assignee:
step: 5
blocked_by: [consent-ga4-research, gsc-site-access]
---

# GA4 与同意横幅站点接入

## Question

（agent 在新站仓库执行；操作者建 GA4 资源并验收）按「同意横幅与 GA4 选型调研」的推荐，在线上站点装好同意横幅与 GA4。

- 操作者清单：`所有者账号` 建 GA4 账号 + 媒体资源 + 网站数据流（时区 Europe/Berlin、币种按站点），取衡量 ID 交 agent；`日常账号` 加账号层管理员；服务账号加查看者（供后续读数）。
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
