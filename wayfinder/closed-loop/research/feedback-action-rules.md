# 反馈分级行动规则

访问日：2026-10-14。本文在 `wayfinder/feasibility/research/feedback-ladder-practice.md` 上扩展，不重做那份底子。等待窗口只用下面列出的 Google Search Central 现行文档。底子里若复述过活动纪要中的内部抓取小时数，那些小时数不作为本文的期限。

外展对象均已事先同意。同意只说明可以发信，不提供客户认知，也不提供回复率或间隔。

## 结论

冷启动里可以立刻执行的下一步只有三类：网站侧有文档写明的技术阻断，按该状态写明的修法修掉；邮件传输层的永久失败停掉该地址，暂时失败交给传输重试；页面上已经违反 Google 标题或摘要清单的缺陷，按清单改那一处。收录后零展示、点击率、回复率、跟进次数、跟进间隔、询盘个数，以及何时把决策从 L0–L1 上移到按比率改页或改序列，都无通用阈值。两家外发厂商的数据都显示第一封之后仍有相当比例的回复，所以无回复不构成停在第一封的理由，也不构成改写序列的理由；两套封数建议互相冲突，不能合成一个次数。个位数询盘的记账边界是 0–9，这是「个位数」的字面尽头，业界没有公布这条线。

## 怎么读这些表

- **事实**带 URL，访问日都是 2026-10-14。
- **推断**是用已引用的数字做的算术，对方没有把它定成阈值。
- **〔未证实〕**是这次没查到。不写成事实，也不留给口头确认。
- **无通用阈值**表示没有可脱离行业判断使用的统一数字。旁边写的是常见做法和它的局限。
- 级别用仓库术语：L0 已执行，L1 已到达（收录或有展示；邮件送达），L2 有互动（搜索点击；邮件真人回复），L3 有转化（询盘）。冷启动阶段的决策停在 L0–L1。这些级别本身来自仓库 `CONTEXT.md`，不是外部标准。
- 承接 skill 是本仓库 `skills/<name>/SKILL.md` 的 frontmatter `name`。**无**表示这一行的动作是等待、记账或停手，不调用方法 skill。skill 正文里的天数表、九封模板、三封 Hook/Proof/Nudge 都不是外部阈值。
- 厂商页标了利益相关。他们的比例不能平均，也不能当成德国 B2B 光伏储能的目标。

一条登记 URL，或一条登记外展序列，是归因锚点。看这一条动作成不成功，只数挂在这个锚点上的询盘。没挂上锚点的询盘仍计入北极星，不计入这一条的成败。北极星「任一入口、不去重」是仓库术语。外展回信怎样对齐成询盘，不在本文，见 `wayfinder/closed-loop/tickets/l3-inquiry-source.md`。

## 网页

小站（约 500 页或更少）大概不需要拿整份 Page indexing 报告判断成败。重要页用 `site:` 和 URL Inspection。[索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) 写明：未收录可以是正常情况，例如预期中的 robots.txt、noindex、重复 URL，或已删除且没有替代页的 404；重复页和替代页不应被收录；目标不是 100% 收录；重要页应当被收录。表里的 Source 为 Google 或 Website，大体上只能修 Source 为 Website 的问题。优先处理验证状态为 failed 或 not started、且 Source 为 Website 的项。

URL Inspection 的总判有三档：[单页检查](https://support.google.com/webmasters/answer/12482179?hl=en)。「URL is on Google」表示已收录且没有问题，但工具不保证出现在搜索结果里。「URL is on Google, but has issues」表示已收录，增强项可能受影响，页面仍可以出现。「URL is not on Google」要展开 Page indexing 看原因。Live test 不检测重复页和规范网址选择。最后抓取日期为空、且状态是 Google 还没发现该 URL 时，做一次 Test live URL，再 Request indexing。同一 URL 反复提交不会更快，单条提交有配额；抓取可从数日到数周，请求抓取不保证收录。[请求重抓](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl)。

| 级别 | 信号 | 条件 | 动作 | 承接 skill | 来源 | 适用前提 |
| --- | --- | --- | --- | --- | --- | --- |
| L0 | 执行登记已有这条 URL，URL Inspection 尚未给出到达证据 | 底表只有执行记录，没有下面任一收录状态 | 不改标题、不改正文、不改信息架构。打开 URL Inspection，按下一行的状态名行事 | 无 | 仓库术语：`CONTEXT.md`「执行登记」。状态含义见本表其余行的 Google 文档 | 执行登记是 L0 的唯一来源。这一行只防止在没有状态名时动手 |
| L0 | Server error (5xx) | 请求该 URL 时服务器返回 500 级错误 | 修服务器错误。修完后用 Test live URL 确认，再 Request indexing 一次 | marketing-seo-audit | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) | 冷启动同样修。这是网站侧阻断 |
| L0 | Redirect error | 重定向链过长、循环、最终 URL 超长，或链中有坏的或空的 URL | 用 Lighthouse 一类调试工具看清链条并修掉。确认 live test 通过后 Request indexing 一次 | marketing-seo-audit | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) | 单条错误的重定向用本行。整站 URL 结构设计用下面的规范网址行 |
| L0 | URL blocked by robots.txt，且执行登记要求这页被收录 | robots.txt 挡住了 Googlebot；页面本应被收录 | 去掉这条阻挡。robots.txt 不能保证不被收录；若目的是不收录，应去掉阻挡并改用 noindex | marketing-seo-audit | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) | 阻挡是有意的：动作改为记账，承接 skill 无 |
| L0 | URL marked noindex，且执行登记要求这页被收录 | 抓取时遇到 noindex | 去掉 noindex。Live test 已不再检出 noindex 时，Request indexing 一次。指令还在就先删指令，不要先提交 | marketing-seo-audit | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) | noindex 是有意的：记账，承接 skill 无 |
| L0 | Soft 404 | 页面像「未找到」，但 HTTP 状态不是 404 | 这页若已删除：改成真正的 404。这页若应存在：补上真实内容，使它不再像软 404。用 live test 的 View tested page 看 Google 渲染结果 | marketing-seo-audit | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) | 冷启动只修这个状态。不因此做点击率改写 |
| L0 | Blocked due to unauthorized request (401) | Googlebot 收到 401 | 取消该页的授权要求，或允许已验证身份的 Googlebot。可用无痕窗口核对 | marketing-seo-audit | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) | 页面本就不应公开：记账，承接 skill 无 |
| L0 | Blocked due to access forbidden (403) | 服务器对不带凭证的 Googlebot 返回 403。Googlebot 从不提交凭证，页面不会被收录 | 若本应收录：允许未登录访问，或在核验身份后放行 Googlebot | marketing-seo-audit | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) | 本就不应公开：记账，承接 skill 无 |
| L0 | URL blocked due to other 4xx issue | 其他 4xx，不属于上面已列的类型 | 用 URL Inspection 查这一次的具体状态并修网站侧原因。修完再请求一次收录 | marketing-seo-audit | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) | 没有具体状态名之前不改文案 |
| L0 | Not found (404)，登记 URL 本应在线 | 请求返回 404，执行登记仍把这页当作在线页 | 恢复该页，或做 301 到新地址。Google 会继续尝试一段时间；无法要求它永久忘记一个 URL | marketing-seo-audit | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) | 已删除且没有替代页：404 可以是正常结果，记账，不请求收录，承接 skill 无 |
| L0 | Page with redirect | 非规范 URL 跳转到别处，这个 URL 本身不会被收录。目标页是否收录另说 | 检查目标页。登记的是跳转前的 URL：把锚点改到目标，或修掉错误的跳转。Live test 会跟着跳转走，索引视图则针对被检查的那个 URL | 错误跳转：marketing-seo-audit。跳转是有意的：无 | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) | 有意跳转且目标已是锚点：只记账 |
| L0 | Crawled - currently not indexed | Google 抓过，尚未收录。将来可能收录，也可能不收录 | 不重新提交这个 URL。冷启动不因此改写正文 | 无 | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) | 官方动作是不必再提交。把「未收录」理解成必须改稿，是推断，本行不执行 |
| L0 | Discovered - currently not indexed | Google 已发现、尚未抓取。通常是预计抓取会压垮站点，所以改期。最后抓取日期因此为空 | 不反复 Request indexing。检查是否误挡 robots、站点是否顶不住抓取；新站外链很少时，检查站点地图是否让这页能被发现 | 技术阻断：marketing-seo-audit。要补的是站点地图或内链结构：marketing-site-and-schema | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en)；[站点地图](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)；[请求重抓](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl) | 空的最后抓取日期在这个状态名下表示尚未抓，不表示 Google 从未发现。站点地图不保证抓取或收录，也不提高排名 |
| L0 | 最后抓取日期为空，且 Google 尚未发现该 URL | 总判不是 Discovered。工具显示还没找到这页 | Test live URL 一次，再 Request indexing 一次。然后等待 | 无 | [单页检查](https://support.google.com/webmasters/answer/12482179?hl=en)；[请求重抓](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl) | 与上一行分开。重复提交不会更快 |
| L0 | 新页或新站仍在官方等待窗口内 | 页或站是新的；或刚请求过抓取。多数站点新页至少要数日才会被注意到，不应期待当天抓取（新闻站除外）。多数站点的检查和收录是三天或更久。索引报告对新页或新站写的是大约一周；新内容可以是数日。已知 URL 之后，部分站点要数周才抓到。抓取 FAQ：不能预测何时或是否抓取、收录；站点太新是未收录最常见的原因 | 窗口内只等待、只记账。不改稿，不在同一天反复提交未改过的站点地图，不期待站点地图里每个 URL 都被立刻抓取 | 无 | [抓取排错](https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors)；[索引报告](https://support.google.com/webmasters/answer/7440203?hl=en)；[抓取 FAQ](https://developers.google.com/search/help/crawling-index-faq)；[请求重抓](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl) | 这些是官方时钟，不是「零展示即异常」的天数。页面即使被抓到，若没有足够的价值或用户需求，仍可能不出现在结果里 |
| L0 | Alternate page with proper canonical tag | 页面正确指向已收录的规范页（AMP 或移动/桌面替代） | 不做事 | 无 | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) | Search Console 不检测语言替代页 |
| L0 | 登记 URL 是重复页，Google 选中的规范网址是干净 URL | 登记 URL 带参数、www 差异或尾部斜线一类副本；Google 选了另一个规范网址。Duplicate without user-selected canonical 本身不是错误 | 不改页。展示、点击和排名数据记在 Google 选中的规范网址上，改去读那个 URL | 无 | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en)；[展示与点击](https://support.google.com/webmasters/answer/7042828?hl=en) | 副本上的零展示，先核对是不是数据记到了规范网址 |
| L0 | 登记 URL 本应是规范网址，Google 选了另一个 | Duplicate, Google chose different canonical than user，或 Google 选错了规范网址。另一个 URL 不是有意的移动版或 AMP | 把规范信号对齐，使登记 URL 与 Google 使用的规范网址相同。先在 URL Inspection 对照 Google-selected canonical 和 User-declared canonical | marketing-site-and-schema | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en)；[单页检查](https://support.google.com/webmasters/answer/12482179?hl=en) | 用户声明的规范页若和当前页并不相似，Google 不会选它。声明错了就改声明，而不是反复提交 |
| L1 | Page is indexed，或总判 URL is on Google | 收录成功 | 记 L1。收录不保证出现在搜索结果里。操作者自己搜不到：仍记已收录、有资格出现。到 google.com 的搜索框查修剪后的 URL，才能核对是否出现；不要把地址栏粘贴当成这个测试 | 无 | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en)；[单页检查](https://support.google.com/webmasters/answer/12482179?hl=en) | 结果随时间、地点、设备和个人历史变化。个人搜索看不到，不启动改页 |
| L1 | URL is on Google, but has issues | 已收录，增强或体验项有问题 | 记 L1。不把这一档当成未收录。冷启动不因此改页 | 无 | [单页检查](https://support.google.com/webmasters/answer/12482179?hl=en) | 结构化数据、移动可用性、HTTPS 留在记录里。它们不构成上移到按比率改稿 |
| L1 | Indexed, though blocked by robots.txt | 尽管 robots.txt 阻挡，页面仍被收录。摘要会很有限。别人的链接仍可能让它被收录 | 本应收录：更新 robots.txt 放行。本应不收录：去掉 robots 阻挡，改用 noindex | marketing-seo-audit | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) | 警告不阻止收录 |
| L1 | Page indexed without content | 已在索引中，但 Google 读不到内容。可能是对 Google 做了伪装，或格式不可索引。不是 robots.txt | 用 URL Inspection 的 Coverage 看具体原因并修可读性 | marketing-seo-audit | [索引报告](https://support.google.com/webmasters/answer/7440203?hl=en) | 冷启动修这个技术状态，不据此改营销角度 |
| L1 | 已收录，展示仍为 0 | 锚点是 Google 选中的规范网址；界面上的展示是实数 0，不是 `~` 或 `-`；官方等待窗口已过 | 继续记账。无通用阈值规定「收录后多少天零展示算异常」。窗口过后仍不把站点判成偏离轨道，不改稿 | 无 | [抓取 FAQ](https://developers.google.com/search/help/crawling-index-faq)；[展示与点击](https://support.google.com/webmasters/answer/7042828?hl=en)；[搜索效果概览](https://support.google.com/webmasters/answer/7576553?hl=en) | 已收录仍可能不出现在某一次搜索里。导出的 0 可能来自界面上的 `~` 或 `-`，那种读数按「没有读数」记账 |
| L1 | 读数不能用来触发改页 | 要用 Search Console 判断这一条 URL | 看 Pages 维度（按页汇总），不用全站汇总的点击率或平均排名。点线的初步数据（通常是今天，有时是昨天，数小时内会变）不拿来判断。界面上的 `~` 或 `-` 导出后会变成 0，导出的 0 不单独当成真实零 | 无 | [关于效果数据](https://support.google.com/webmasters/answer/17011364?hl=en)；[搜索效果概览](https://support.google.com/webmasters/answer/7576553?hl=en)；[展示与点击](https://support.google.com/webmasters/answer/7042828?hl=en) | 全站汇总把同一次搜索里的多个 URL 算成一次展示，并取最高排名，点击率和平均排名会更好看。展示是用户看到或可能看到链接；轮播或折叠块通常要滚到或展开才计数。点击率 = 点击 ÷ 展示 |
| L0 或 L1 | 标题或 meta description 命中 Google 写明的缺陷 | 页面本身可见：标题空了一半、过时、与页面不符、堆砌关键词、全站或一组页面共用套话、标题语言或书写系统与正文不一致、主标题在页面上无法辨认；或 meta description 是关键词串、各页相同、没有概括该页。不需要展示量或点击率 | 只改这些缺陷。Google 可能改写标题；标题来源重新抓取可从数日到数周。摘要主要来自页面正文，meta description 在它比正文更能说明页面时才会被用到 | marketing-copy-editing | [标题链接](https://developers.google.com/search/docs/appearance/title-link)；[摘要](https://developers.google.com/search/docs/appearance/snippet) | 标题和 meta description 都没有通用长度上限，结果按设备宽度截断。不设字数配额，不设点击率配额。本行不是 `marketing-copywriting`（那是起草新文案库），也不是 `lead-seo-content-edit`（那是改已批准的获客文章草稿） |
| L1 | 有展示、无点击，标题和摘要没有命中上一行的缺陷 | 新 URL，没有可对比的上一时段 | 记账。无通用阈值规定多少展示或多少点击率才允许改标题。不设点击率百分比 | 无 | [展示与点击](https://support.google.com/webmasters/answer/7042828?hl=en)；[流量下降](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) | 德国或能源类关键词的位置–点击率曲线〔未证实〕，不使用 |
| L2 | 有点击、询盘事件还没被证实在记 | 能看到点击，但询盘事件是否记入尚未核对 | 先核对询盘事件是否真的被记录。核对完成前不改页 | marketing-measurement | 动作依据是仓库证据闸：未证实的计数不拿来判页面。skill 范围见 `skills/marketing-measurement/SKILL.md` | 该 skill 写的是度量与事件字典，不是改页。单个跟踪故障不是它的完整阶段任务；这里只用它核对事件是否存在 |
| L2 | 有点击、无询盘，事件已经在记 | 这一条登记 URL 上的询盘为 0–9 | 只把行记入底表。不改页，不给渠道排名 | 无 | 0–9 的说明见本文「询盘」。点击定义见 [展示与点击](https://support.google.com/webmasters/answer/7042828?hl=en) | 表单当场报错不属于本行，见询盘节 |
| L2 | 已有对比期，展示稳住，点击下降 | 同一页能比较两个时段；展示基本不变，点击下降 | 检查标题和摘要是否命中缺陷清单，或别的站点是否用了更醒目的富结果。命中缺陷清单才改那一处 | 命中缺陷：marketing-copy-editing。未命中：无 | [流量下降](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) | 新 URL 没有上一时段，本行不触发。这是内容缺陷检查，不是冷启动上移，也不是点击率配额 |

## 邮件

硬退和软退按 SMTP 状态码，不按某家发送工具的营销用语。

[RFC 5321](https://www.rfc-editor.org/rfc/rfc5321) §4.2.1：4yz 是暂时失败，客户端应当重试；若原样重试、对方也没有新的实现，仍可能成功。5yz 是永久失败，客户端不应重复同一请求；人可以在真正的改变之后再发起，例如改了拼写或账户状态。§4.5.4.1：一次失败后发送方必须延迟再试；重试间隔一般应当至少 30 分钟；一直重试到送出或发送方放弃；放弃时间一般至少要 4–5 天；这些参数必须可配置。这是传输重试，不是销售跟进的间隔。

[RFC 3463](https://www.rfc-editor.org/rfc/rfc3463)：2.X.X 成功；4.X.X 持续的暂时失败，以后再发可能成功；5.X.X 永久失败，原样重发不太可能成功，消息或目的地必须改变。X.1.1 是目的邮箱不存在（@ 左侧），只用于永久失败。X.1.2 是目的系统（@ 右侧），只用于永久失败。X.1.3 是地址语法，只用于永久失败。X.2.2 邮箱已满，应当用作持续的暂时失败，即使用户看到的类别数字是 5。

[Gmail 发件人准则](https://support.google.com/mail/answer/81126?hl=en) 针对发往个人 Gmail 的邮件。自 2024-02-01 起，每天向 Gmail 账户发送超过 5,000 封的发件人要满足该页的额外要求，其中包括 Postmaster Tools 垃圾率低于 0.3%，以及营销和订阅邮件的一键退订。同一页的后续建议是把垃圾率保持在 0.10% 以下，并避免达到 0.30% 或更高。退信或延迟开始出现时，先降低发送量，直到 SMTP 错误率下降，再缓慢加回。Google 不跟踪打开率，也不能核实第三方的打开率；打开率低不一定是送达或垃圾分类的信号。

本站事先同意的少量一对一名单，达不到每天 5,000 封的一键退订触发线。一键退订头因此不是本表的发送闸门。收件人本人拒绝或退订，这条线程仍然停止。

| 级别 | 信号 | 条件 | 动作 | 承接 skill | 来源 | 适用前提 |
| --- | --- | --- | --- | --- | --- | --- |
| L0 | 邮件已写入执行登记，尚无送达或退信 | 只有发出记录 | 不改文案。等待传输结果，再按下面的状态码行事 | 无 | 仓库术语：`CONTEXT.md`「执行登记」 | 打开率不作为等待结束的信号 |
| L1 | 送达，无退信 | 传输成功，没有 4yz 或 5yz | 记 L1 | 无 | [RFC 5321](https://www.rfc-editor.org/rfc/rfc5321) 的 2yz 完成；[RFC 3463](https://www.rfc-editor.org/rfc/rfc3463) 的 2.X.X | 送达不是回复，也不是询盘 |
| 未到 L1 | 永久失败 | 5yz，或增强码 5.1.1、5.1.2、5.1.3。没有「邮箱已满」的 X.2.2 或同等说明 | 停这个地址。不原样重发 | 无 | [RFC 5321](https://www.rfc-editor.org/rfc/rfc5321) §4.2.1 与 §4.2.5；[RFC 3463](https://www.rfc-editor.org/rfc/rfc3463) | 停手本身不调用找人 skill |
| 未到 L1 | 同一位已同意的人，邮箱被判永久不存在，仍要联系此人 | 上一行已经成立，且要找的是同一个人的另一个邮箱 | 只为这个人查找公开邮箱。找不到就不编地址。查找工具未配置时，把该行标成联系人待补。新地址在发出前做联系人与域名核对 | 查找：lead-contact-discovery。发出前核对：lead-data-validation | 永久失败的定义见上一行的 RFC。skill 范围见各自 `SKILL.md` | 不因此去找另一家公司。`lead-data-validation` 是发出前的名单核对，不是退信处理器 |
| 未到 L1 | 暂时失败，含邮箱已满 | 4yz，或增强码 X.2.2，或退信写明邮箱已满 | 不手动连发同一封销售信。交给发信系统重试：间隔至少按 30 分钟量级延迟，放弃窗口一般至少 4–5 天。窗口用尽后按最终状态码重分类 | 无 | [RFC 5321](https://www.rfc-editor.org/rfc/rfc5321) §4.2.1、§4.5.4.1；[RFC 3463](https://www.rfc-editor.org/rfc/rfc3463) X.2.2 | 这不是销售跟进的天数。服务器若把邮箱已满发成类别 5，仍按暂时失败 |
| 未到 L1 | 一批地址开始退信或被延迟 | 不是单个地址的 5.1.1，而是发送量上去后错误率升高 | 降低发送量，直到 SMTP 错误率下降，再缓慢加回。多次退信的收件人从列表中移除 | 无 | [Gmail 发件人准则](https://support.google.com/mail/answer/81126?hl=en) | 「多次退信就自动退订」是邮件列表指导。它不授权对 5yz 继续原样重试 |
| 未到 L1 | 5.7.26，或 421 4.7.0、550 5.7.1 一类 IP 或认证拒绝 | 拒绝原因是认证、PTR 或发信 IP 信誉，不是收件人邮箱不存在 | 修 SPF、DKIM、DMARC 或发信 IP。不改销售文案，不换一家新公司的联系人 | 无 | [Gmail 发件人准则](https://support.google.com/mail/answer/81126?hl=en) | 该页建议所有发件人设置 SPF、DKIM、DMARC。每天超过 5,000 封才进入额外要求 |
| L1 | Postmaster 垃圾率达到 0.30% 或更高 | 能看到该域的 Postmaster 垃圾率 | 先降量并检查列表。不把垃圾率当成改文案的理由 | 无 | [Gmail 发件人准则](https://support.google.com/mail/answer/81126?hl=en) | 每天超过 5,000 封的要求是低于 0.3%；同一页建议保持低于 0.10%，并避免 0.30% 或更高。少量一对一发信时 Postmaster 有没有读数〔未证实〕。没有读数就不编一个垃圾率 |
| L1 | 打开率低或打开率为 0 | 任何打开率数字 | 不动作。不用打开率判断送达、垃圾分类或是否跟进 | 无 | [Gmail 发件人准则](https://support.google.com/mail/answer/81126?hl=en) | Google 不跟踪打开率 |
| L1 | 无真人回复，登记里还有未发出的计划内下一封 | 无永久退信，无人拒绝或退订，计划里还有下一封 | 发出那一封。不因为回复率为 0 或发送量小而改写序列。间隔用登记里已经写下的日期。登记没写日期：不新造天数表 | 下一封文案还没写完：lead-followup-sequence，只补这一封。文案已齐、只差排序：lead-email-sequence-strategy | [Belkins 跟进统计](https://belkins.io/blog/sales-follow-up-statistics)；[Instantly 2026 基准](https://instantly.ai/cold-email-benchmark-report-2026) | 两家都支持不要停在第 1 封，见冷启动节。无通用次数，无通用间隔。`lead-followup-sequence` 的九封模板和内部 Day 网格不是封数，也不是间隔。`lead-cold-email-gen` 只写第一封。回复率为 0 不触发 `lead-warm-email-transform` |
| L1 | 无真人回复，登记里没有计划封数，也没有下一封 | 同上，但计划是空的 | 不新指定第几封，不新指定隔几天。记账 | 无 | 同上 | 常见做法是 Belkins 的 3–5 封和 Instantly 的 4–7 封。二者冲突，本行不代选。德国 B2B 的封数和间隔〔未证实〕 |
| L1 | 计划封数已经用完 | 登记中的最后一封已发出，仍无真人回复 | 停止这条序列并记账。不因为回复率为 0 再追加 | 无 | 封数无通用值，见冷启动节 | 停，是因为计划用完，不是因为某个回复率达标 |
| 不计 L2 | 自动回复，含休假通知 | [RFC 3834](https://www.rfc-editor.org/rfc/rfc3834) 把休假通知定义为告诉发件人邮件在一段时间内不太会被阅读。自动回复应带 `Auto-Submitted: auto-replied`。Belkins 的回复率排除自动回复和退信通知 | 不记 L2。不改写序列。不把休假通知当成「隔几天再发一封」的期限 | 无 | [RFC 3834](https://www.rfc-editor.org/rfc/rfc3834)；[Belkins 回复率](https://belkins.io/blog/cold-email-response-rates) | 休假程序自己不对同一发件人在数日内重复回复，建议默认 7 天。这是自动回复程序的默认，不是销售序列的间隔。休假结束后隔多久发下一封〔未证实〕 |
| 未到 L1 | 改址通知 | RFC 3834 的 change-of-address：原地址已废弃，应改用另一个地址 | 停旧地址。通知里给出了新地址：记下它，发出前做核对。不把对方刚提供的地址再拿去「发现联系人」 | 发出前核对：lead-data-validation | [RFC 3834](https://www.rfc-editor.org/rfc/rfc3834) | 通知没给新地址：只停旧地址，承接 skill 无 |
| L2 | 真人回复，要求报价、规格、价格或样品 | 回复正文里有这类请求 | 停冷序列。记 L2。按报价路径写回复 | lead-service-quotation | 回复是真人回复，故为 L2（仓库术语）。skill 范围见 `skills/lead-service-quotation/SKILL.md` | 不把这封回信自动记成询盘。`lead-service-first-contact` 是首次接触计划，`lead-service-first-order` 是下单之后 |
| L2 | 真人回复，只有反对 | 价格、起订量、质量或现有供应商等反对，且没有报价、规格、价格或样品请求 | 停冷序列。记 L2 | lead-service-objection | 同上，skill 为 `lead-service-objection` | 同一封里已经有报价请求：走上一行 |
| L2 | 真人回复，明确拒绝或退订 | 对方不要再收，或使用了退订 | 停这条线程。不再写后续邮件 | 无 | 对方的拒绝。列表场景下的退订途径见 [Gmail 发件人准则](https://support.google.com/mail/answer/81126?hl=en) | 事先同意不覆盖事后拒绝。每天未过 5,000 封时，不把一键退订头当成发送闸门 |
| L2 | 其他真人回复 | 不属于报价、反对、拒绝或退订 | 停冷序列。记 L2。不把回复本身记成询盘 | 无 | 仓库术语的 L2。不映射到询盘流程 skill | 不用 `marketing-inquiry-flow`、`lead-service-first-contact` 或 `lead-service-first-order` |

零回复在小样本里很常见。这是推断，不是阈值。Belkins 把 2025 年回复率定义为唯一回复数除以发出数，排除自动回复和退信通知：7,530,489 封，34,393 个被跟踪的回复，平均 0.45%。按这个 0.45% 做独立重复试验，一次都不回复的概率约为：50 封 0.798，100 封 0.637，200 封 0.406，500 封 0.105，1000 封 0.011。计算用的是他们写出的 0.45%，不是他们公布的停手线。Instantly 的 3.43% 是另一种口径和另一个总体，不代入这个概率。

[三倍法则](https://en.wikipedia.org/wiki/Rule_of_three_(statistics))：若 n 次里事件出现 0 次，0 到 3/n 是发生率的 95% 置信区间；n 大于 30 时，这是对更精细检验的一个好近似。该页由 (1−p)^n = 0.05 推到边界约 3/n。因此 3/30 = 0.10，3/50 = 0.06，3/100 = 0.03，3/300 = 0.01。零回复不能据此把序列判成失败。n 不大于 30 时，连这个近似都不要用。维基条目引用了 Hanley 与 Lippman-Hand，JAMA 1983，249(13):1743–5，PMID 6827763；论文摘要这次没有取到，不引用摘要原句。

## 询盘

| 级别 | 信号 | 条件 | 动作 | 承接 skill | 来源 | 适用前提 |
| --- | --- | --- | --- | --- | --- | --- |
| L3 | 一个锚点上的询盘为 0–9 | 锚点是一条登记 URL，或一条登记外展序列。计入的是已经挂到这个锚点上的询盘，含 0 也含 9 | 写下这一行。不改页，不改序列，不给渠道排名 | 无 | 0–9 是「个位数」的字面尽头。业界没有公布这条起改线。零事件不能判失败的统计依据见 [三倍法则](https://en.wikipedia.org/wiki/Rule_of_three_(statistics)) | 9 不是行业截止值。n=9 时 3/n 的近似超出该页写的 n>30 范围，所以不用 3/n 论证这条字面边界。未归因的询盘仍计入北极星，不计入这个锚点 |
| L3 | 一个锚点上的询盘大于 9 | 同上，计数已经离开个位数 | 仍然只记账。超过 9 之后从哪一个数开始允许按询盘改页或改序列，无通用阈值 | 无 | 没有这样的通用数字。广告模型的量级见下一行，不能搬过来 | 不把维基的 n>30 当成业务起改线。n>30 只说明 3/n 这个近似从那里开始比较好 |
| L3 | 有人用广告归因模型的建议量当作改页依据 | 看到「200 次转化、30 天内 2,000 次广告互动」 | 不改自然搜索页，不改邮件序列。该建议只用于数据驱动归因模型本身 | 无 | [数据驱动归因](https://support.google.com/google-ads/answer/6394265?hl=en) | 所有转化动作不论量级都可以用该模型；数据少时模型仍能运行，数据多时分析更准。这是广告路径的模型建议，不是自然流量或邮件询盘的起改线，也不表示满 200 个询盘就要改页 |
| L2 | 表单当场报错 | 提交时页面给出可见错误，或提交没有完成。这是故障，不是比率 | 修这个表单或着陆页上的故障 | marketing-landing-page | 故障不需要样本量。skill 范围含询盘表单与着陆页审计，见 `skills/marketing-landing-page/SKILL.md` | 不因此启动整阶段转化项目。`marketing-cro` 是阶段协调，不承接这一处故障。`marketing-inquiry-flow` 是提交之后到报价的路径。`marketing-funnel-optimization` 要先有已批准的 05-cro 交付物 |
| L3 | 询盘事件尚未被证实在记 | 要拿询盘数判断页面或序列之前 | 先核对事件是否记录。核对前不改页、不改序列 | marketing-measurement | 与网页节同一行。未核实的计数不用于判断 | 口径对齐不在本文 |

## 冷启动 → 上移

上移指：离开「只修技术阻断、送达和退信」，改成按点击率、回复率、询盘率或排名改页、改序列。

| 级别 | 信号 | 条件 | 动作 | 承接 skill | 来源 | 适用前提 |
| --- | --- | --- | --- | --- | --- | --- |
| 上移 | 用日历或询盘个数把决策级别往上抬 | 任何「第 N 天」「第 N 个询盘」「进了前 10」 | 不抬。无通用阈值，也没有通用时间窗。技术阻断、送达、永久退信和暂时退信，不随日历改变。标题缺陷清单命中时按网页节改那一处，那不是上移 | 无 | 官方时钟没有异常天数：[抓取 FAQ](https://developers.google.com/search/help/crawling-index-faq)。排名绝对值不是成功标准：[流量下降](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) | 个位数询盘期间，不把该锚点上移到按比率改页或改序列。超过 9 之后，按比率改动仍无通用阈值 |
| 上移 | 名次小幅波动，或还没有对比期 | 例如从第 2 到第 4。新 URL 没有上一时段 | 不改。小幅波动任何时候都会发生，页面已经表现好时避免激进修改。绝对名次少作为焦点；对已有流量的站点，展示和点击才是成功度量 | 无 | [流量下降](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) | 大幅掉出前列（文档举例：从前 10 掉到大约第 29）才对全站做自查。有的改动数日见效，有的要数月；一般等数周再看排名影响，且不保证有影响。16 个月和 3 个月对比是给已有历史的下降诊断，不是冷启动配额。中等站点改 URL 后，Google 注意到变化可能要数周 |
| 上移 | 把「数日到数周」当成零展示的异常期限 | 页面已收录，展示仍少 | 继续等待和记账。常见做法是 Google 自己的时钟：新页多数站点至少数日，常见三天或更久；新页或新站大约一周；抓取可到数周；不保证何时收录或是否收录 | 无 | [抓取排错](https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors)；[索引报告](https://support.google.com/webmasters/answer/7440203?hl=en)；[请求重抓](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl)；[抓取 FAQ](https://developers.google.com/search/help/crawling-index-faq) | 局限：这些句子说的是抓取和收录的时间，没有说收录后第几天零展示算异常 |
| 上移 | 数月没进前 10，想据此改稿 | 用站外研究判断新页是不是太慢 | 不把「约 6 个月」写成期限。只记账 | 无 | [Ahrefs 2025](https://ahrefs.com/blog/how-long-does-it-take-to-rank-in-google-and-how-old-are-top-ranking-pages/) | 见下面的常见做法。该研究支持「好几个月没进前 10，不能据此判偏离轨道」。它不支持一个改稿截止日期 |
| 上移 | 用回复率或零回复改写序列、或停在第 1 封 | 发送量仍小，或回复数为 0 | 不改写。计划内还有下一封就发下一封。封数和间隔无通用值 | 计划内下一封的文案：lead-followup-sequence。没有计划：无 | [Belkins 跟进统计](https://belkins.io/blog/sales-follow-up-statistics)；[Instantly 2026 基准](https://instantly.ai/cold-email-benchmark-report-2026) | 两套常见做法和局限见下。不平均 |
| 上移 | 用广告转化量级决定自然搜索或邮件何时可调 | 引用 200 次转化或 2,000 次互动 | 不转移。模型建议留在广告归因里 | 无 | [数据驱动归因](https://support.google.com/google-ads/answer/6394265?hl=en) | 数据少时模型仍能运行 |

常见做法和局限：

Ahrefs 在该文中的样本（利益相关：Ahrefs 销售 SEO 工具）：2023 年 9 月爬虫见到的 100 万个随机 URL，一年内进入前 10 的占 1.74%，98.26% 没有，低于他们自己 2017 年研究的 5.7%。另滤一批 2023 年 10 月创建的 200 万个随机 URL，只要非空英文内容，一年内进前 10 的占 6.11%，作者说这个数可能更公平。在确实进了前 10 的页面里，40.82% 是在 1 个月内进去的。Google 前 10 的页面中 72.9% 超过 3 年（2017 年为 59%）。排名第 1 的页面平均 5 年（2017 年为 2 年）。前 10 里不满 1 年的页面占 13.7%（2017 年为 22%），作者写明其中一部分差异可能来自抽样。高搜索量词比低搜索量词更慢。作者建议：大约 6 个月后若仍不在前 10，可以考虑更新内容，此后机会很低，除非做些改变。局限：这不是 Google 的阈值；分母是随机 URL，不是一个认真运营的 B2B 站；把它收成截止日期，会和「大多数页面从未进前 10」这个结果相撞。本文不采用这 6 个月。也没有德国搜索结果的时间线。

Belkins 跟进页（作者 Michael Maximoff，页面标注 Updated 2026-06-26；利益相关：Belkins 销售托管外展）。邮件样本是 2025 年 12 个月的 7,530,489 封。第 1 步的单步回复率 0.59%；第 2 到第 6 步合计占全部回复的 58.6%，第 1 封占 41.4%。第 3 步单独约到的会面多于第 1 步和第 2 步之和；第 1–2 步合计占邮件来源会面的 46.4%，第 3–5 步合计占 53.5%。从第 3 步起，约会率稳定在 0.2%，为第 1–2 步的两倍。他们的建议是跑 3–5 步，把第 3 封写成不同角度，并写明第 5 步之后邮件收益下降很快。该页没有天数间隔。同一页的 LinkedIn 和电话数字不用于本站的邮件规则。样本是净新冷邮件，不是已同意的光伏名单。

Instantly 基准（页面文内 Updated January 12, 2026；HTML 标注 Last Published Fri Oct 09 2026；利益相关：Instantly 销售发送工具）。总体回复率 3.43%，定义为全部回复（含跟进产生的回复）除以发出数。上四分位 5.5%。精英档超过 10%，且是发件人里的前 10%。首触回复率是回复了第一封的线索占比。FAQ：4–7 封是较理想的序列长度；58% 的回复出现在第 1 步，第 2–4 步再贡献 42%；建议至少 4 封。同一页也写剩余跟进贡献 42% 的回复。样本描述是数十亿次冷邮件互动、数千个活跃工作区、服务 70 万家以上企业。没有比「数十亿」更精确的发出数。退信率低于 2% 是该页的厂商建议，本文的硬退和软退仍以 RFC 为准。

两套不能平均：回复率定义不同（唯一回复、排除自动回复和退信，对比全部回复含跟进），总体也不同（0.45% 对 3.43%）。合流后的可执行含义只有：不要因为无回复停在第 1 封；不要把 58.6%、42%、3–5 或 4–7 当成配额；不要因为小样本零回复去改写序列。

Belkins 回复率页（Margaret Lee，Updated 2026-06-26）同一 7,530,489 封，平均 0.45%。分母已从「打开的人」改成「全部发出」。该页没有 Germany、German、Deutschland 或 solar。建筑、金融服务、医疗、法律落在 0.56%–0.60%，是他们数据里较高的行业桶，不是光伏，也不是德国，更不是目标。波兰 1.43% 来自 46,000 封，不外推。周日 0.57% 的分母只有 21,615 封，周一超过 160 万封，他们自己写明周日百分比很吵。早上 8:00–12:00 的 0.54% 是他们的发送时段结果。这些都不写成发信时刻或目标回复率。

## 〔未证实〕

这次没有查到，不写成规则：

- 德国、德语区或光伏储能 B2B 的跟进间隔、跟进次数、回复率。Belkins 2026 回复率页没有德国，也没有太阳能。
- 收录之后，连续多少天零展示算异常。官方文档只有抓取和收录的「数日到数周」，并写明不保证。
- 有展示、无点击，且标题和摘要没有命中缺陷清单时，最低展示量或点击率下限。
- 询盘超过 9 之后，从哪一个数开始可以按询盘改页或改序列。
- 休假自动回复之后，隔多久发下一封销售邮件。RFC 3834 的 7 天是自动回复程序的默认。
- 每天远低于 5,000 封时，Postmaster Tools 是否给得出可用的垃圾率。
- Search Console 是否因隐私隐藏稀有查询、同时仍把它们计入合计。这次打开的[搜索效果概览](https://support.google.com/webmasters/answer/7576553?hl=en)和[关于效果数据](https://support.google.com/webmasters/answer/17011364?hl=en)没有这句话。概览只写明：查询可以出现在表里，但个人再搜时不一定看到本站，因为结果随时间、地点、设备和近期历史变化。
- GA4 关键事件的最低样本量。
- 德国可见度或排名时间线，包括 SISTRIX 一类工具的曲线。
- 德国或能源类关键词的位置–点击率曲线。
- 正向回复率（相对全部回复）的可用基准。Belkins 页用的是他们定义的回复率，不是正向回复率。
- Hanley 与 Lippman-Hand 1983 年 JAMA 论文的摘要原句。维基条目和书目信息已核对，PubMed 摘要这次没有取回。

不采用、以免被当成阈值的数字：Ahrefs 作者的约 6 个月；Belkins 的 3–5 封与 Instantly 的 4–7 封，二者都不作为配额；Instantly 的退信率 2%；两家的星期和钟点；广告模型的 200 与 2,000；维基的 n>30。

## 来源

| 来源 | 支撑什么 | 访问日 | 利益相关 |
| --- | --- | --- | --- |
| https://support.google.com/webmasters/answer/7440203?hl=en | 索引原因、Source=Website、约 500 页以下可不用整份报告、新页大约一周、100% 不是目标、各未收录状态的动作 | 2026-10-14 | 否 |
| https://support.google.com/webmasters/answer/12482179?hl=en | URL Inspection 三档总判、不保证出现在结果里、最后抓取为空时的一次请求、live test 不覆盖重复与规范网址 | 2026-10-14 | 否 |
| https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl | 抓取可从数日到数周；重复请求不会更快；有配额；不保证收录。页脚 Last updated 2025-12-10 UTC | 2026-10-14 | 否 |
| https://developers.google.com/search/help/crawling-index-faq | 不能预测何时或是否抓取、收录；站点地图不保证收录或提高排名；未收录最常见原因是太新。Last updated 2025-12-10 UTC | 2026-10-14 | 否 |
| https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors | 多数站点新页至少数日；多数站点三天或更久；抓到了仍可能因价值或需求不足而不展示；不要同一天反复提交未改站点地图。Last updated 2025-12-18 UTC | 2026-10-14 | 否 |
| https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview | 新站外链少时可能需要站点地图；约 500 页或更少且内链完整时可能不需要；站点地图不保证抓取或收录。Last updated 2025-12-10 UTC | 2026-10-14 | 否 |
| https://developers.google.com/search/docs/appearance/title-link | 标题缺陷清单；没有长度上限；Google 可能改写；重新处理可从数日到数周。Last updated 2025-12-10 UTC | 2026-10-14 | 否 |
| https://developers.google.com/search/docs/appearance/snippet | 摘要主要来自正文；meta description 的用法；各页应有独特描述；没有长度上限。Last updated 2026-04-20 UTC | 2026-10-14 | 否 |
| https://support.google.com/webmasters/answer/7042828?hl=en | 展示、点击、点击率、排名的定义；数据记在 Google 选中的规范网址上 | 2026-10-14 | 否 |
| https://support.google.com/webmasters/answer/7576553?hl=en | 图按全站汇总、Pages 表按页汇总；点线初步数据；`~` 与 `-` 导出为 0；查询出现在表里不等于个人搜索看得到 | 2026-10-14 | 否 |
| https://support.google.com/webmasters/answer/17011364?hl=en | 全站汇总会使点击率和平均排名更好看；初步数据通常是今天、有时是昨天，数小时内可能变 | 2026-10-14 | 否 |
| https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops | 展示稳住而点击下降时检查标题和摘要；避免对表现好的页面做激进修改；绝对名次少作为焦点；数周观察与不保证。Last updated 2025-12-10 UTC | 2026-10-14 | 否 |
| https://support.google.com/google-ads/answer/6394265?hl=en | 数据驱动归因：不限量级都可用；建议 30 天内至少 200 次转化和 2,000 次广告互动，数据少时仍能运行 | 2026-10-14 | 否。该建议不转移到自然搜索或邮件 |
| https://support.google.com/mail/answer/81126?hl=en | 垃圾率 0.3% 与 0.10%；每天 5,000 封的额外要求；退信时降量；不跟踪打开率；退订途径 | 2026-10-14 | 否 |
| https://www.rfc-editor.org/rfc/rfc5321 | 4yz 与 5yz；至少 30 分钟量级的重试延迟；放弃时间一般至少 4–5 天 | 2026-10-14 | 否 |
| https://www.rfc-editor.org/rfc/rfc3463 | 4.X.X 与 5.X.X；X.1.1、X.1.2、X.1.3；X.2.2 邮箱已满应为暂时失败 | 2026-10-14 | 否 |
| https://www.rfc-editor.org/rfc/rfc3834 | 休假通知与改址通知的定义；`Auto-Submitted: auto-replied`；回复程序的 7 天默认 | 2026-10-14 | 否 |
| https://belkins.io/blog/sales-follow-up-statistics | 7,530,489 封；第 2–6 步占回复 58.6%；建议 3–5 步；该页没有天数间隔。Updated 2026-06-26 | 2026-10-14 | 是。Belkins 销售托管外展 |
| https://belkins.io/blog/cold-email-response-rates | 回复率定义与 0.45%（34,393 / 7,530,489）；无德国、无太阳能；行业桶与周日小样本。Updated 2026-06-26 | 2026-10-14 | 是。同上 |
| https://instantly.ai/cold-email-benchmark-report-2026 | 3.43%、5.5%、精英档超过 10%；4–7 封与至少 4 封；第 1 步 58%、第 2–4 步 42%。文内 Updated January 12, 2026 | 2026-10-14 | 是。Instantly 销售发送工具 |
| https://ahrefs.com/blog/how-long-does-it-take-to-rank-in-google-and-how-old-are-top-ranking-pages/ | 1.74%、6.11%、40.82%、72.9%、平均第 1 名 5 年、13.7%；作者的约 6 个月建议，本文不采用 | 2026-10-14 | 是。Ahrefs 销售 SEO 工具 |
| https://en.wikipedia.org/wiki/Rule_of_three_(statistics) | 零事件时 0 到 3/n 的 95% 区间；n>30 时近似较好；推导式。不作为业务起改线 | 2026-10-14 | 否 |
| 本仓库 `skills/*/SKILL.md` | 只支撑「承接 skill」列的名字和职责边界 | 2026-10-14 | 否。不是外部阈值 |
