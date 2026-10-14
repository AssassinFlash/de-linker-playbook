---
wayfinder: task
status: closed
assignee: chesterjohn+agent
blocked_by: []
resolved: 2026-10-14
---

# Google 账号现状清点

## Question

（HITL：给用户清单逐项核对）de-linker.com 在 Google 侧现在有什么：GSC 资源（域名资源还是网址前缀、谁是所有者、哪个 Google 账号）、GA4 媒体资源与数据流、Google Workspace（若 chester@ 在 Google）、可用于建 Google Cloud 项目/服务账号的账号。缺什么、谁来开。

产出：现状表写进本票 Resolution（不写任何密钥或 token）。

## 补充（2026-10-14，主模型）

「只读邮箱接入」已查明 chester@de-linker.com 托管在**腾讯企业邮**（不是 Google Workspace），清单里 Workspace 一项不用再核对；其余 GSC / GA4 / 可建 Cloud 项目的 Google 账号照常核对。

## Resolution

> 账号明细（真实邮箱）在私有 vault：`deliverables/marketing/00-system/google-account-inventory.md`。本文件只写角色名。

2026-10-14 与用户逐项核对（HITL）+ 公开 DNS/站点只读核查。**Google 侧数据层为零，从头开**；无 DNS 权限不构成阻塞。

**账号策略（用户定）**：全部 Google 资源由 `所有者账号` 当所有者（Google Ads 已在此账号充值）；`日常账号`（用户日常账号，须先是 Google 账号）加为同级管理角色。跨账号无数据隔离问题：权限挂在资源上；GA4↔Ads、GSC↔Ads 关联只要求操作账号在两侧都有足够权限（GA4 编辑者 + Ads 管理员；GSC 所有者 + Ads 管理员），且仅建立关联时需要。脚本读数一律走 Cloud 服务账号，其邮箱加进 GSC/GA4/表格为用户，与人用哪个账号无关。

**现状表**

| 项 | 现状 | 证据 | 缺什么 → 谁来开 |
|---|---|---|---|
| GSC | 无任何资源；未验证 | 用户确认；apex 无 `google-site-verification` TXT，首页无验证 meta | 建**网址前缀**资源 `https://de-linker.com/`（http/www/https-www 均 301 到此，覆盖全部流量）；验证走 Site Kit 或 meta/HTML 文件 → 用户（所有者账号）在 GSC 点，站点侧部署见下 |
| GSC 网域资源 | 不可行 | DNS 在阿里云万网（`dns23/24.hichina.com`），用户无权限且永久拿不到 | 不做；网址前缀资源足够 |
| GA4 | 无账号/媒体资源/数据流 | 用户确认；首页无 `gtag`/`G-`/`GT-`/`GTM-` | 建 GA4 账号+媒体资源+网站数据流 → 用户；德国同意前提另见「Google 渠道接入路径」 |
| Google Ads | 已有，`所有者账号`，已充值 | 用户确认 | 加 `日常账号` 为管理员；与 GA4/GSC 关联待两侧建好 |
| Google Cloud | 可登录；按「无项目、无组织」处理 | 用户确认 | 建项目 + 服务账号（GSC/GA4 Data/Sheets API 不需结算）→ 用户；本机 gcloud 现登 `本机 gcloud 当前账号`，须切到 所有者账号 |
| Google Workspace | **不存在** | MX = `mxbiz1/2.qq.com`，SPF `include:spf.mail.qq.com`，无 DMARC | chester@ 在腾讯企业邮；邮箱回流走 IMAP 只读，不走 Gmail API |
| Site Kit by Google | 未安装（线上 `wp-content/plugins/google-site-kit/` 404；新站仓库无引用） | curl + grep | 候选：一个插件同时完成 GSC 验证（虚拟 HTML 文件/meta）、GA4 Google tag、Consent Mode 开关；后者需 WP Consent API + 同意管理插件。第三方插件在新站经 cutover 工具 `wp plugin install` 装 |
| 站点部署 | 用户能部署但**不亲自部署**（怕出错） | 用户确认 | 加验证标签/装插件交由下一张地图里的 agent 执行、用户验收 |

下游：仓内脚本调用 GSC API 时资源标识写 `https://de-linker.com/`（带尾斜线），不是 `sc-domain:de-linker.com`（见「Google 渠道接入路径」坑 1）。Site Kit 的 Consent Mode 开关有官方文档（下方来源），可补「Google 渠道接入路径」里「Site Kit 是否发 Consent Mode v2」的未查证项。

角色对照（日常账号 应加的级别）：GSC **所有者**（委托所有者，非「完整用户」）；GA4 **账号层管理员**；Ads **管理员**；Cloud IAM **Owner**；表格**编辑者**。

来源：GA4↔Ads 关联权限 https://support.google.com/analytics/answer/9379420 、https://support.google.com/google-ads/answer/7519537 ；GSC↔Ads https://support.google.com/google-ads/answer/7529561 ；GSC 所有者类型 https://support.google.com/webmasters/answer/7687615 ；网址前缀/网域资源与验证方式 https://support.google.com/webmasters/answer/10432366 、https://support.google.com/webmasters/answer/10431861 、https://support.google.com/webmasters/answer/9008080 ；Site Kit 建资源与验证 https://sitekit.withgoogle.com/documentation/using-site-kit/choosing-a-search-console-property/ 、https://sitekit.withgoogle.com/documentation/troubleshooting/setup/ ；Site Kit 同意模式 https://sitekit.withgoogle.com/documentation/using-site-kit/consent-mode/ 。

不含任何密钥或 token。

