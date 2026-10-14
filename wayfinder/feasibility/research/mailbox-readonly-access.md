---
wayfinder: research
ticket: mailbox-readonly-access
checked: 2026-10-14
mailbox: chester@de-linker.com
---

# 只读邮箱接入

## 结论摘要

`chester@de-linker.com` 的收信托管在腾讯企业邮。2026-10-14 向权威 DNS `dns23.hichina.com` 与 `dns24.hichina.com` 查到：MX 为 `5 mxbiz1.qq.com`、`10 mxbiz2.qq.com`，SPF 为 `v=spf1 include:spf.mail.qq.com ~all`，`mail.de-linker.com` CNAME 到 `exmail.qq.com`，`_dmarc.de-linker.com` 返回 NXDOMAIN。
Gmail API 的 `gmail.readonly` 与 Microsoft Graph 的 `Mail.Read` 只读各自托管的邮箱。本域 MX 与 Google 文档中的 `smtp.google.com`（2023 年前的 aspmx 记录仍有效）以及 Microsoft 365 管理中心要求配置的 MX 都不相同，这两个 API 现在读不到这只邮箱。
这只邮箱的只读路径是 IMAP：`imap.exmail.qq.com` 端口 993、SSL。先在网页邮箱打开 IMAP；开了安全登录就用客户端专用密码。打开文件夹用 EXAMINE，取正文用 BODY.PEEK。企业微信「获取收件箱邮件」只读应用收件箱，不包括成员的已发送。
L0 外展不能单靠这只邮箱认定。站点发信走 Hostinger 的 `mail()`，团队通知的 To 默认是 `sales@de-linker.com`，不会进入 chester@ 的已发送。执行登记仍是 L0 的唯一来源；邮箱只适合核对已发送夹里、发件人是 chester@ 的信。
L2 用外展那封的 Message-ID 对齐回复的 `In-Reply-To` / `References`，并排除 `Auto-Submitted: auto-replied`。只看主题前缀 Re: / AW: / 回复 不稳定。
L3 的形式发票申请通知和联系表单通知写给团队邮箱（默认 sales@）。盲抄名单是 Woo 选项，代码默认是空的，线上值本次未读到。直接来信没有稳定结构。每日摘要列出未处理询盘，它本身不是一封新询盘。
没有开源项目实现这套 L0 / L2 / L3。可参照的是自带读取代码的 ImapFlow（`readOnly` 走 EXAMINE）、imap_tools、Himalaya，以及 GitHub 的 email_reply_parser（只拆回复正文）。本次没有登录这只邮箱。

识别规则是根据下面的协议和本站发信代码作出的推断，不是在这只邮箱里跑出来的分类结果。

## 查证的事实

### 1. 公开 DNS（2026-10-14）

查询对象是权威服务器，不是公共递归解析器。`dig @dns23.hichina.com` 与 `dig @dns24.hichina.com` 对 MX 和 apex TXT 的回答一致。系统递归解析器对 TXT 多次超时，权威查询没有超时。SOA 的序列号在两次查询间不一致（见过 `2026082509` 与 `2026082617`），MX 与 SPF 的内容没有变。

| 记录 | 结果 |
|---|---|
| NS | `dns23.hichina.com`、`dns24.hichina.com` |
| MX | `5 mxbiz1.qq.com`、`10 mxbiz2.qq.com`（TTL 600） |
| TXT | `v=spf1 include:spf.mail.qq.com ~all`（TTL 600） |
| `_dmarc.de-linker.com` TXT | 权威回答 `NXDOMAIN`，没有 DMARC 记录 |
| `mail.de-linker.com` | CNAME `exmail.qq.com` |
| `smtp` / `imap` / `pop` / `webmail` / `autodiscover` / `autoconfig` | 在 `dns23.hichina.com` 上没有 CNAME，也没有 A |
| `de-linker.com` 与 `www` 的 A | `46.202.156.7` |

`46.202.156.7` 落在 RIPE 的 `46.202.152.0 - 46.202.159.255`，netname `HOSTINGER-HOSTING`，country `DE`，org `ORG-HIL18-RIPE`。这是网站地址的网段，不是 MX。

来源：本次对上述权威 NS 的直接查询；RIPE 对象见 <https://rest.db.ripe.net/search.json?query-string=46.202.156.7>。

下面这些 `_domainkey` 名字在 `dns23.hichina.com` 上既没有 TXT 也没有 CNAME：`qq`、`mail`、`exmail`、`dkim`、`default`、`google`、`selector1`、`selector2`、`k1`、`s1`、`s2`、`qcloud`、`tencent`、`s2024`、`s2025`、`mxbiz1`、`mxbiz2`、`biz`、`mailer`、`hostinger`、`spf`。本次没有枚举全部可能的 selector。`include:spf.mail.qq.com` 没有展开：向 `mail.qq.com` 的 NS 做递归查询超时。

### 2. 为什么 Gmail API 和 Graph 现在接不上

Google Workspace 当前要加的 MX 值是 `smtp.google.com`。2023 年前开通的域名可以继续用以 `aspmx` 开头的旧 MX，邮件正常就不必改。来源：<https://knowledge.workspace.google.com/admin/domains/set-up-mx-records-for-google-workspace>（由 <https://support.google.com/a/answer/140034> 打开）。

Microsoft 365 的邮箱 MX 在管理中心「Add DNS records」页复制，各租户不同。已有别家 MX 时，要删掉它，或把它的优先级调得低于 Microsoft 365，新邮件才会进 Microsoft 365。来源：<https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider>。

本域两条 MX 都是 `mxbiz*.qq.com`。与上面两份文档要求的记录不同。

### 3. 腾讯企业邮 IMAP：最小步骤与坑

官方帮助（企业微信帮助中心，页面标题「IMAP是什么？IMAP和POP有什么区别？」）给出的配置：

- 收信：`imap.exmail.qq.com`，SSL，端口 993
- 发信：`smtp.exmail.qq.com`，SSL，端口 465
- 账户名和邮件地址都填完整邮箱地址
- 密码填企业邮箱密码；已经开启安全登录时，改用客户端专用密码

来源：<https://open.work.weixin.qq.com/help2/pc/19887>。该页把「如何获取客户端专用密码」链到 <https://open.work.weixin.qq.com/help2/pc/19902>。本次没有再打开 19902 的正文。

同一帮助中心的 Foxmail 设置页写明：用电脑网页版登录，进入【设置 → 收发信设置/客户端设置 → 开启服务】，打开 IMAP 或 POP3 之后，客户端才能配置。安全登录开启后要生成授权码。来源：<https://open.work.weixin.qq.com/help2/pc/19880>。

同页列出的协议限制：IMAP 当时不支持删除文件夹和重命名文件夹；文件夹名里的特殊符号（例子是全角空格）会让部分手机收信失败。

只读的协议要求不在腾讯这篇帮助里，在 IMAP4rev2：

- `EXAMINE` 与 `SELECT` 返回相同，但邮箱以只读打开。不允许修改邮箱的永久状态，包括每用户状态。成功时标记响应必须以 `[READ-ONLY]` 开头。来源：RFC 9051 §6.3.3，<https://www.rfc-editor.org/rfc/rfc9051>。
- `FETCH BODY[<section>]` 会隐含设置 `\Seen`。`BODY.PEEK[<section>]` 是不设置 `\Seen` 的替代形式。来源：RFC 9051 对这两项 fetch 项的定义，同一 URL。

最小步骤（把上面几份原文按顺序排起来）：

1. 用网页邮箱为 `chester@de-linker.com` 打开 IMAP。
2. 若该账号开了安全登录，在网页里取客户端专用密码，不要把网页登录密码写进脚本。
3. TLS 连接 `imap.exmail.qq.com:993`，用户名用完整地址。
4. `LIST` 出文件夹后，对收件箱和已发送夹发 `EXAMINE`，取信用 `BODY.PEEK`。
5. 只读脚本不要配置 SMTP。`smtp.exmail.qq.com:465` 是发信，本次任务不需要。

已核对的坑：

- 官方给出的凭据是完整的客户端密码或授权码。本次没有看到「只读专用密码」的官方说明。`EXAMINE` 是客户端选择；拿着这组凭据的程序仍然可以 `SELECT` 并改旗标。
- 文件夹名含特殊符号时，部分客户端收信失败（官方原文如上）。
- 本次没有登录，已发送夹的实际名字、是否广告 `IDLE`、是否广告 `SPECIAL-USE \Sent`，都未查证。

企业微信服务端另有一个读信接口，读的不是成员邮箱。文档原文：「由于用户可向应用所绑定的邮箱回复邮件，故支持应用获取**应用收件箱**的邮件列表。」请求是 `POST https://qyapi.weixin.qq.com/cgi-bin/exmail/app/get_mail_list?access_token=ACCESS_TOKEN`，按时间范围分页返回 `mail_id`。来源：<https://developer.work.weixin.qq.com/document/path/97369>。它不提供成员已发送夹，不能用来认定 L0。

### 4. Gmail API `gmail.readonly`：最小步骤与坑

只在邮箱改由 Google 托管之后才用得上。当前 MX 不满足第 2 节的条件。

范围表把 `https://www.googleapis.com/auth/gmail.readonly` 放在 Restricted scopes 下，说明文字是 “View your email messages and settings.”。同表里的 `https://www.googleapis.com/auth/gmail.metadata` 只能看标签和头，看不到正文。Restricted 的定义是：这类范围访问面宽，要做 restricted scope 的 OAuth 应用验证。来源：<https://developers.google.com/workspace/gmail/api/auth/scopes>。

OAuth 同意屏幕若是外部用户类型且发布状态为 Testing，刷新令牌 7 天过期，除非请求的范围只是姓名、邮箱和用户资料。每个 Google 账号、每个 OAuth 客户端还有 100 个刷新令牌的上限。来源：<https://developers.google.com/identity/protocols/oauth2>。

系统标签 `SENT` 不能手工贴上。它自动出现在：用 `drafts.send` 或 `messages.send` 发出的信、用 `messages.insert` 插入且 From 是该用户的信、以及用户在 Gmail 网页里发出的信。来源：<https://developers.google.com/workspace/gmail/api/guides/labels>。

增量同步要保存最近一封的 `historyId`，之后做部分同步；第一次必须全量同步。来源：<https://developers.google.com/workspace/gmail/api/guides/sync>。

最小步骤（托管改到 Google 之后）：

1. 把 MX 改成 Google 文档要求的值，并等收信切过去。
2. 建 Cloud 项目，打开 Gmail API，配置 OAuth 同意屏幕。
3. 只请求 `https://www.googleapis.com/auth/gmail.readonly`。
4. 用该用户走一次同意，保存刷新令牌。Testing 状态要在 7 天内重新同意，或把应用送去验证。
5. 全量拉信，记下 `historyId`；已发出的信看系统标签 `SENT`。

已核对的坑：restricted 验证、Testing 令牌 7 天、`gmail.metadata` 没有正文、`SENT` 只覆盖经 Gmail 发出或按上面规则插入的信。本次没有把 `users.messages.list` 的查询语法页面整页抓下来，查询串不在这里展开。

### 5. Microsoft Graph `Mail.Read`：最小步骤与坑

只在邮箱改由该租户的 Exchange Online 托管之后才用得上。当前 MX 不满足第 2 节的条件。

权限参考（2026-10-14 抓取的英文页）：

| 权限 | 应用权限 | 委托权限 |
|---|---|---|
| `Mail.Read` | 标识 `810c84a8-4a9e-49e6-bf7d-12d183f40d01`。无登录用户，读组织内全部邮箱。管理员同意：要 | 标识 `570282fd-fa5c-430d-a7fd-fc8dc98a9dca`。读登录用户自己的邮箱。管理员同意：不要 |
| `Mail.ReadBasic` | 读全部邮箱的基本属性，不含 body、previewBody、附件和扩展属性 | 同上，限于登录用户 |
| `IMAP.AccessAsUser.All` | 无 | 标识 `652390e4-393a-48de-9484-05f9b1212954`。显示名 “Read and write access to mailboxes via IMAP.” 管理员同意：不要 |

`Mail.Read` 的委托权限可用于个人 Microsoft 账号。应用权限即使已经授予，管理员仍可以用 application access policy 把应用限制到指定邮箱，而不是整个组织。来源：<https://learn.microsoft.com/en-us/graph/permissions-reference>。策略页本身：<https://learn.microsoft.com/en-us/graph/auth-limit-mailbox-access>。

`IMAP.AccessAsUser.All` 是读写，不是只读，而且只出现在委托权限一列。它是 Outlook IMAP 的 OAuth 范围，不是 Graph 的 `Mail.Read`。

最小步骤（托管改到 Microsoft 365 之后）：

1. 按管理中心的值改 MX，并处理旧 MX。
2. 在 Entra 应用里只加委托权限 `Mail.Read`，由 `chester@` 的用户同意。这样读到的是登录用户自己的邮箱，不需要管理员同意。
3. 若必须用应用权限（没有用户登录），加 `Mail.Read` 的应用权限，做管理员同意，再用 application access policy 收窄到这一个邮箱。
4. 要正文就用 `Mail.Read`。`Mail.ReadBasic` 明确不含 body。

已核对的坑：应用权限默认是全部邮箱；`Mail.ReadBasic` 没有正文；IMAP 的 OAuth 范围是读写。`GET /me/messages` 那一页本次打开时要求登录，查询参数（包括是否默认返回 `In-Reply-To`）未在本次抓取里核对，不在这里写死。

### 6. 本站实际把哪类信送到哪

事实源是 `~/Documents/de-linker`（地图规定的产品仓库）。下面路径都在该仓库，不是公开 URL。

站点发信走 Hostinger 的 PHP `mail()`，限额写的是 10 封/分钟、100 封/24 小时，四个站共用。来源：`AGENTS.md`（「邮件：Hostinger `mail()`……」）。网站 A 记录所在网段与 Hostinger 的 RIPE 对象一致，见第 1 节。From 地址不是插件写死的。WooCommerce 用自己的发件人选项；2026-10-09 的验收样本是 `From: Linker <sales@de-linker.com>`，例如 `docs/acceptance/2026-10-09/11/mail/en-20261009-153147-a983954a.eml`。同一天的站内调研记录过当时的选项 `woocommerce_email_from_address=sales@de-linker.com`（`docs/research/2026-10-09/mail-root-cause.md`）。本次没有再读生产数据库，不能把今天的选项值写成已核对。

团队通知的收件人：

- To = `linker_commerce_team_to`，空则默认 `sales@de-linker.com`。来源：`plugins/linker-commerce/includes/Settings/Options.php` 的 `DEFAULT_TEAM_TO`。
- Bcc = `linker_commerce_team_bcc`。空字符串解析后是空列表，并会去掉与 To 重复的地址。同一文件的 `team_bcc()`。
- 新询盘、每日摘要、新客户、VAT 变更都走这个 To + Bcc。联系表单的团队信同样。来源：`includes/Mail/TeamEmail.php`、`includes/Contact/Emails/TeamMessageEmail.php`。
- `chester@de-linker.com` 在代码里是测试模式的默认改写地址（`includes/Mail/TestMode.php` 的 `DEFAULT_TO`），测试开关打开时投递被改到这一地址。它不是生产 To，也不是生产 Bcc 的默认值。

会进团队邮箱的主题（站点默认语言；德语在 `languages/linker-commerce-de_DE_formal.po`）：

| 邮件 | 类 | 英文默认主题 | 德语 |
|---|---|---|---|
| 新询盘（形式发票申请进入 `inquiry-received`） | `Inquiry/Emails/NewInquiryEmail.php` | `New inquiry #{order_number} from {company}` | `Neue Anfrage #{order_number} von {company}` |
| 联系表单 | `Contact/Emails/TeamMessageEmail.php` | `New message from {name}` | `Neue Nachricht von {name}` |
| 每日摘要 | `Digest/DigestEmail.php` | `Daily digest, {date}` | `Tagesübersicht, {date}` |
| 新客户 | `Registration/Emails/NewCustomerEmail.php` | `New customer: {company}` | `Neuer Kunde: {company}` |
| VAT 变更 | `Registration/Emails/VatReviewEmail.php` | `VAT check changed: {company}` | `USt-IdNr.-Prüfung geändert: {company}` |

新询盘的触发钩子是 `woocommerce_order_status_pending_to_` + `inquiry-received` + `_notification`。团队信的 Reply-To 是下单客户。正文英文模板有句子 `New inquiry %1$s from %2$s (%3$s).`，并带后台链接。来源：`includes/Inquiry/Emails/NewInquiryEmail.php`、`templates/emails/linker-new-inquiry.php`。

联系表单团队信的 Reply-To 是访客，正文有 “sent a message through the contact form”。来源：`includes/Contact/Emails/TeamMessageEmail.php`、`templates/emails/linker-contact-team.php`。

每日摘要每天 09:00 Europe/Berlin 发给同一个团队邮箱。第②块是仍处于 `wc-inquiry-received`、且创建早于发送时刻减 86400 秒的询盘。来源：`docs/specs/74-daily-digest.md`。

团队信的语言是站点默认语言，不是客户当时的语言（`TeamEmail` 调用 `LocaleSwitch::site_default()`）。语言规格写的是 en 为默认、无前缀，de 为 `/de/`。来源：`docs/specs/9-i18n.md`。2026-10-09 那封德语测试客户的团队信主题仍是英文 `New inquiry #59 from Solarbau Beispiel GmbH`（`docs/acceptance/2026-10-09/11/mail/de-20261009-153305-079230d5.eml`）。

给客户的确认信主题是 `Your inquiry #{order_number} has been received` / `Ihre Anfrage … ist eingegangen`，收件人是客户，不是团队。来源：`includes/Inquiry/Emails/InquiryReceivedEmail.php` 与上面那批 `.eml`。

联系表单的线上地址，2026-10-14 的 HTTP 状态：`https://de-linker.com/contact/` 为 200，`https://de-linker.com/de/kontakt/` 为 200，`https://de-linker.com/kontakt/` 与 `https://de-linker.com/de/contact/` 为 404。插件把表单挂在 `/contact/`（`includes/Contact/Form.php`）。

RFC 5322 写明：准备发送时，一种实现会把 `Bcc:` 行删掉，但 Bcc 里的人仍然收到一份。另一种实现给 To/Cc 的副本删掉 Bcc 行，给 Bcc 收件人另一份仍带 Bcc 行。用哪一种由实现决定。来源：RFC 5322 §3.6.3，<https://www.rfc-editor.org/rfc/rfc5322>。因此不能假定 chester@ 收到的副本上还看得到 `Bcc:` 头。

回复的标准字段：每封信都应有 `Message-ID`；回复应带 `In-Reply-To` 和 `References`，里面是一个或多个消息标识。来源：RFC 5322 §3.6.4，同一 URL。

自动回复应带 `Auto-Submitted: auto-replied`。来源：RFC 3834 §3.1.7 与 §5，<https://www.rfc-editor.org/rfc/rfc3834>。

### 7. 可参照的开源实现

「已验证」按地图的标准：有人用它跑出过数据，或仓库自带数据接入代码。下面四个都抓了作者自己的 README 或 API 文档。没有一个包含本站的 L0 / L2 / L3 主题规则。

| 项目 | 它实际做什么 | 和本票的关系 | 来源 |
|---|---|---|---|
| ImapFlow | Node.js IMAP 客户端。`getMailboxLock(path, options)` 与 `mailboxOpen` 的 `readOnly: true` 使用 IMAP `EXAMINE` 而不是 `SELECT`。README 写明它是 EmailEngine 的 IMAP 引擎 | 只读打开邮箱的直接参照。README 示例本身没有传 `readOnly`，调用方要自己加上 | <https://github.com/postalsys/imapflow> 的 README；<https://imapflow.com/docs/api/imapflow-client> |
| imap_tools | Python IMAP。`fetch` 的 `mark_seen` 默认 `True`，会把信标成已读 | 自带读取代码。默认值与只读目标相反，要用 `mark_seen=False` | <https://github.com/ikvk/imap_tools> 的 `README.rst` |
| Himalaya | 邮件 CLI，后端包含 IMAP，也包含 Gmail REST 与 Microsoft Graph | 自带三种后端的读取代码。Gmail / Graph 两个后端对当前这只邮箱不适用 | <https://github.com/pimalaya/himalaya> 的 README |
| email_reply_parser | 从纯文本邮件里拆出回复正文。README 写明 GitHub 用它显示由邮件回复生成的评论 | 有生产使用记录。它不判断这封是不是外展的回复，也不认识询盘通知 | <https://github.com/github/email_reply_parser> 的 README |

## 推断

下面每条都依赖上一节的事实，但没有在 `chester@de-linker.com` 里用真实信件验证过。

1. **L0。** 人手从这只邮箱的网页或 IMAP 客户端发出、并且客户端把副本放进已发送夹的外展，可以在已发送夹里看到，发件人是 `chester@de-linker.com`。站点经 Hostinger `mail()` 发出的信不经过这只邮箱的发信，不会因此出现在它的已发送夹。执行登记是 L0 的定义来源（`CONTEXT.md`）。稳定做法是：登记里记下该封的 Message-ID 或至少日期加收件人，再用已发送夹核对；对不上就以登记为准，不把「已发送夹里多出来的信」自动当成一次外展。已发送夹里还会有人回复客户时自己发出的信，单凭「在已发送夹」区分不了外展和答复。
2. **L2。** 一封来信的 `In-Reply-To` 或 `References` 含有某封已登记外展的 Message-ID，就把它记为那次外展的回复。`Auto-Submitted: auto-replied` 的不算 L2。主题以 Re:、AW:、Aw:、回复、答复 开头，只能当弱提示：客户新写一封、或网关丢掉回复头时，这个前缀会漏，也会把无关的 Re: 算进来。
3. **L3，站点触发的通知。** 在团队邮箱（以及它的盲抄副本）里，同时满足下面几条的，当作形式发票申请通知：主题匹配 `New inquiry #… from …` 或 `Neue Anfrage #… von …`，并且正文有对应的 “New inquiry … from …” / 德语译文。联系表单通知同理，主题 `New message from …` / `Neue Nachricht von …`，正文有 contact form 那句。不要把 `New customer:`、`VAT check changed:`、`Daily digest,` / `Tagesübersicht,` 算进 L3。摘要第②块是已经用新询盘信报过的单子的再次列出，再计一次会重复。
4. **这只 chester@ 邮箱默认收不到第 3 条。** 那些信的 To 默认是 sales@。只有 `linker_commerce_team_bcc` 含有 chester@，或者邮箱里另有转发规则，副本才会出现在 chester@。转发规则不在仓库里。Bcc 头又可能在投递前被去掉，所以不能用「头里有没有 Bcc: chester@」来判断。副本上更稳的标志是主题加正文，外加 To 仍是 sales@、From 是当时的 Woo 发件人。
5. **L3，直接来信。** `CONTEXT.md` 把直接来信算询盘。这类信没有本站模板。排除掉第 3 条的通知、第 2 条的外展回复、以及带 `Auto-Submitted` 的自动回复之后，剩下的来信无法只靠头字段稳定分成「买家询盘」和「其他」。这一档需要人看，或者另定一个明确的发件人/主题规则。本次没有这样的规则。
6. **SPF 与站点发信。** apex TXT 只 `include:spf.mail.qq.com`，软失败是 `~all`。站点发信走 Hostinger `mail()`。本次没有展开这个 include，不能独立判断 Hostinger 的出站地址在不在授权范围里。2026-10-09 的站内笔记写过「SPF 只授权腾讯，Hostinger 不会替它做 DKIM」（`docs/research/2026-10-09/mail-root-cause.md`）。那是先前的结论，不是本次 DNS 复核。

## 仍未解决

- 没有登录 `chester@de-linker.com`。IMAP 是否已在网页里打开、是否开了安全登录、已发送夹的真实名字、`IDLE` 与 `SPECIAL-USE`，都要登录后才能看到。
- 生产库里的 `linker_commerce_team_to`、`linker_commerce_team_bcc`、`woocommerce_email_from_address` 本次没有读。代码默认是 sales@ 加空盲抄；2026-10-09 的样本与当时的选项记录也是 sales@。今天是否仍把 chester@ 抄进去，未知。
- 生产站点的默认语言本次没有读。规格和 2026-10-09 的样本指向团队信主题为英文；若后台改成德语，主题会变成 `.po` 里的德语句。
- DKIM：上面列出的 selector 没有记录。未探测的 selector 仍可能存在。
- `spf.mail.qq.com` 的展开本次超时，Hostinger 出站是否通过 SPF 未复核。
- DMARC 名字是 NXDOMAIN。没有策略记录。
- Graph「列出邮件」页本次被登录墙挡住，`In-Reply-To` 是否要 `$select` 才返回，未核对。
- Gmail `users.messages.list` 的查询语法页本次没有整页抓取。
- 企业微信帮助页 <https://open.work.weixin.qq.com/help2/pc/19902> 只作为 19887 上的链接记下，专用密码的点击步骤没有逐字核对。
- 没有任何开源项目在本站信件上跑通过。上表只说明它们自带读取或拆信代码。
