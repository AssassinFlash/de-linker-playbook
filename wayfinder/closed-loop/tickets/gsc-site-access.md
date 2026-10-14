---
wayfinder: task
status: open
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

## 进展（执行中，2026-10-14）

- **载体：Site Kit by Google**（用户裁定：用官方插件，这类接入不写代码；先写的 mu 插件方案已撤回、未合并）。只连 Search Console，不连 Analytics。
- 新站票 AssassinFlash/de-linker#145（正文已改为 Site Kit 版），分支 `t145/search-console`（规格 `docs/specs/145-search-console.md`、研究 `docs/research/2026-10-14/search-console-carrier.md`），工作树 `~/Documents/de-linker-worktrees/de-linker-t145`。
- 本地参照实例 t110 装 Site Kit 1.189.0：未连接时前台只多 `generator` meta 与 `//www.googletagmanager.com` 的 dns-prefetch，无脚本无 Cookie；首页 EN/DE × 1440/390 像素差 0。
- 线上尚未安装：agent 的生产 SSH 被权限拦下，待用户放行，或用户在后台「插件 → 安装插件」自己装（清单第 2 步）。
- 操作者清单（Site Kit 版）：vault `deliverables/marketing/00-system/gsc-owner-checklist.md`。
- 余下：线上安装并读回 → 操作者按清单连接、加委托所有者、提交站点地图 → 按 Site Kit 实际用的验证方式（虚拟 HTML 文件或 meta）写回归断言（`just cutover verify` + `tests/e2e` chrome 套件）→ PR → CI → 合并 → `just cutover verify` 对线上 → 验收记录 → 关票。

## 交接

- 所选载体若是 Site Kit，把「Site Kit 已装、版本、配置位置」写进「同意横幅与 GA4 选型调研」与「GA4 与同意横幅站点接入」两票正文。
