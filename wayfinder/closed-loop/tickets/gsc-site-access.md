---
wayfinder: task
status: closed
assignee: claude-code 7cbbae73 (2026-10-14)
step: 1
blocked_by: []
---

# GSC 站点接入

## Question

（agent 在新站仓库 `~/Documents/de-linker` 执行；操作者只在 GSC 后台点所有者才能点的几下并验收）让 `https://de-linker.com/` 成为已验证的 GSC 网址前缀资源，并提交站点地图。

- **新站仓库的规矩优先**：按 `~/Documents/de-linker/AGENTS.md` 走（在那边开票、新会话、`just up`、分支 → PR → CI 绿 → 合并、管线 本地 → 评审站 → 线上；不买付费插件；不走 Code Snippets；代码只进仓库插件或 mu-plugin）。本票在 playbook 侧只记结果与链接。
- **验证载体由本票按证据定**：Site Kit（免费，后续 GA4 / Consent Mode 可复用，但会多一个第三方插件，经切换工具 `wp plugin install` 装）vs 仓库插件输出 `google-site-verification` meta vs 根目录 HTML 文件。考虑：后续「GA4 与同意横幅站点接入」是否复用同一载体；像素零差异门（head 里的 meta 不改像素）；缓存（LiteSpeed）清理。决定与理由写进新站仓库的规格 / 变更记录。
- 操作者清单：用 `所有者账号` 在 GSC 建网址前缀资源 `https://de-linker.com/`，取验证码交给 agent；上线后点「验证」；把 `日常账号` 加为**委托所有者**；在 GSC 提交站点地图（地址以线上实际为准，查 `robots.txt` / SEOPress）。
- 验证码不是密钥，但真实账号信息只写 vault。

## 调研交接（「同意横幅与 GA4 选型调研」关票时写入）

- 该调研推荐以后 GA4 用 **Site Kit** 作载体（它按 WP Consent API 发 Consent Mode v2 默认值，Site Kit 文档点名 Complianz 等 CMP 联动），并建议 GSC 与 GA4 共用这一载体。选载体时把这一条当作证据之一；若仍选 meta / HTML 文件，写明理由，以免 GA4 那票再装 Site Kit 时与已有验证冲突。详见 `wayfinder/closed-loop/research/consent-ga4.md` 第 4 节。
- 注意：Site Kit 只要连了 Analytics 就会无条件入队 `gtag.js`。本票只连 Search Console，不连 Analytics，直到「GA4 与同意横幅站点接入」装好横幅。

## 防冲掉（用户 2026-10-14：站点优化与接入并行）

- 新站会在本票之后继续优化与部署。验证载体必须在新站仓库内、随正常部署发布，并在新站的回归检查里加一条断言（线上 / 评审站首页仍输出 GSC 验证；若用 Site Kit，则插件在且已连接 Search Console），让后续任何 PR 冲掉验证时 CI 或回归先报错。在新站仓库的规格里写明「这是数据回流的前提，不得移除」。

## 完成标准

- GSC 显示资源已验证；站点地图状态「成功」（截图或操作者口述 + agent 用线上 HTML 复核 meta / 文件存在）。
- 新站仓库对应 PR 已合并、已上线，验收记录在其 `docs/acceptance/` 下；本票 Resolution 链接它。

## Resolution

2026-10-14 完成：`https://de-linker.com/` 是已验证的 GSC 网址前缀资源，站点地图 `sitemaps.xml` 状态「成功」。

- **载体 = Site Kit by Google 1.189.0**（用户裁定：用官方插件，这类接入不写代码；先写的仓库 mu 插件方案撤回未合并）。偏离本票「防冲掉」里「载体在新站仓库内、随正常部署发布」一句：Site Kit 不在仓库里，由 WP-CLI 从 wordpress.org 装在线上；部署不删仓库外插件，防冲掉改由回归检查兜住（见下）。
- **只连 Search Console**：Analytics 与匿名使用数据都未勾；OAuth 范围只有 profile/email、siteverification、webmasters。验证方式 = Site Kit 虚拟 HTML 文件；连接者 = 后台用户 1（唯一管理员）。
- **GSC**：`所有者账号` = 验证所有者，`日常账号` = 委托所有者（它早已是 Google 账号）。
- **回归**：新站 `just cutover verify` 新增 `search-console` 段，对生产主机断「Site Kit 启用、已连 `https://de-linker.com/`、验证文件可取」，任一不成立退出码 1；评审站 e2e `specs/search-console.spec.ts` 断插件在。新站规格写明「数据回流的前提，不得移除」，并写明不得删用户 1、不得 Reset / Disconnect。
- **新站记录**：票 AssassinFlash/de-linker#145（已关），PR #146 squash 合并为 `96d70ad`；验收记录 `~/Documents/de-linker/docs/acceptance/2026-10-14/145/README.md`；规格 `docs/specs/145-search-console.md`；研究 `docs/research/2026-10-14/search-console-carrier.md`。前台只多 generator meta 与 `googletagmanager.com` dns-prefetch，首页 EN/DE × 1440/390 像素差 0。
- **私有**：真实账号、操作清单与 GSC 用户截图在 vault `deliverables/marketing/00-system/`（`gsc-owner-checklist.md`、`evidence/2026-10-14-gsc-users-owners.jpg`）。
- **后续票已写入**：「GA4 与同意横幅站点接入」「同意横幅与 GA4 选型调研」（Site Kit 版本、配置位置、不要动的、dns-prefetch 现状）、「GSC 数据回流」（资源、站点地图、加服务账号的路径、数据起点）。
- 新站 mu 插件 `linker-site-guards.php`、`linker-engine-pin.php` 未纳入 PHPCS/PHPStan 的覆盖缺口：本票试修时触及安全守卫文件被权限拦下而撤回，未修，留给用户决定。

## 交接

- 所选载体若是 Site Kit，把「Site Kit 已装、版本、配置位置」写进「同意横幅与 GA4 选型调研」与「GA4 与同意横幅站点接入」两票正文。（已写入，2026-10-14）
