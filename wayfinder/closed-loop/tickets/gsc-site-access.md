---
wayfinder: task
status: open
assignee:
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

## 完成标准

- GSC 显示资源已验证；站点地图状态「成功」（截图或操作者口述 + agent 用线上 HTML 复核 meta / 文件存在）。
- 新站仓库对应 PR 已合并、已上线，验收记录在其 `docs/acceptance/` 下；本票 Resolution 链接它。

## 交接

- 所选载体若是 Site Kit，把「Site Kit 已装、版本、配置位置」写进「同意横幅与 GA4 选型调研」与「GA4 与同意横幅站点接入」两票正文。
