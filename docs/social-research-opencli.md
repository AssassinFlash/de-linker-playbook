# OpenCLI 公开社媒补充取证

Apify 仍是外部研究主入口。OpenCLI 是第二取证路径：Apify 已经给出检索基线后，用它读取平台内的公开帖子、主页和评论，补足搜索摘要里看不到的真实语言、角色关系和平台语境。

OpenCLI 不绕过平台额度、登录墙、robots、服务条款或反爬限制。它复用操作者已经登录的 Chrome profile；不得把 cookie、密码、私信或完整联系人数据写进仓库、日志或对话。

## 什么时候用

- 需要看 LinkedIn、Facebook、TikTok、Instagram、Reddit 的公开原帖或评论，而不是只看搜索摘要。
- Apify 已跑过基线，仍需补平台内的安装商、供应商、渠道商或下游用户语言。
- 需要区分“直接买家自述、供应商观察、营销展示、下游压力、规则限制”，而不是把一句帖子直接当行业事实。

公开社媒用于研究与教学，不用于批量抓人、采集私信或把平台当免费联系人数据库。

## 会话与登录

1. 先跑 `opencli doctor`。
2. 用 `opencli auth status --site linkedin,facebook,tiktok,instagram,reddit,youtube,twitter` 检查登录态。Bluesky 走公开 API，不需要登录。
3. OpenCLI 绑定的是 Chrome profile。登录态不对时，先比较 Chrome 各 profile 的 cookie 更新时间，再在正确 profile 登录一次；后续会话直接复用该 profile。
4. 平台专用命令返回 429、404、空数组或跳转到登录页时，记录状态并检查路由、profile、限频和页面是否仍公开；改用同一 OpenCLI 的通用浏览器读取页面。

## 只读路径

### LinkedIn

- 公开内容搜索：用 `opencli browser open` 打开 `https://www.linkedin.com/search/results/content/?keywords=<query>`，再 `opencli browser extract`。
- 已知公司或个人：用 `opencli linkedin company`、`profile`、`posts` 等只读命令。
- `people-search` 会消耗 LinkedIn 的 Commercial Use Limit。先靠公开公司页、内容帖和官网缩小范围，确认是目标 ICP 后再查具体人员。

### Facebook

- 页面和小组发现：`opencli facebook search "<query>" --limit 10`。
- 小组内搜索：用通用浏览器打开 `https://www.facebook.com/groups/<id>/search/?q=<query>`。
- 帖子正文与评论：标准页面只显示动态流时，用 `https://mbasic.facebook.com/groups/<id>/posts/<post_id>/`，再 `opencli browser extract`。

### TikTok

- 视频发现：`opencli tiktok search "<query>" --limit 10`。
- 用户与视频列表：`opencli tiktok profile`、`user`。
- 需要评论时用通用浏览器打开视频页，点击评论入口后提取；营销视频只能证明市场表达，不能单独证明采购痛点。

### Instagram

- 优先用通用浏览器打开已知公开帖子、Reel 或 hashtag 页面，再读取正文和评论。
- 专用 `profile`、`user`、`search` 命令遇到 `/users/info` 429 或搜索 404 时，改用页面读取；不把接口失败当成“没有内容”。

### Reddit

- 搜索：`opencli reddit search "<query>" --limit 10`。
- 帖子与评论：`opencli reddit read <post-id> --limit 25 --depth 2`。
- Reddit 的公开自述通常比营销帖更接近真实工作问题，但仍要标地区、身份和样本边界。

### YouTube

- 视频发现：`opencli youtube search "<query>" --limit 10 --upload year`。
- 单条内容：`opencli youtube video <url>` 看标题、描述和时间戳；`transcript` 读字幕；`comments` 读评论。
- 字幕地址可能返回空响应；继续看视频描述和评论，不把字幕失败当成没有内容。
- 区分安装商自己的教育内容、供应商访谈和媒体评论；评论里的下游声音不能直接写成安装商采购痛点。

### X / Twitter

- **批量 X 研究默认走 Apify**，因为用操作者自己的 X 登录态做长查询容易超时、触发 `SearchTimeline` 限流并增加账号风险。OpenCLI 只用于少量补充、已知帖子检查或 Apify 不可用时的临时页面读取。
- 当前优先 Actor：`delicious_zebu/ultimate-x-twitter-advanced-search-scraper`。先小批量检查噪声，再按关键词、精确短语、日期、语言、最低回复/点赞数扩大；需要评论时用 `scraper_one/x-post-replies-scraper` 读取指定帖子回复。
- 搜索：`opencli twitter search "<query>" --product top --limit 10`。
- X 查询可能很慢，复杂查询先用 `OPENCLI_BROWSER_COMMAND_TIMEOUT=120`；仍失败时收窄关键词。
- 遇到 `SearchTimeline` 429，记录会话额度并按提示等待 15–30 分钟；不要连续重试。
- 只读 `search`、`thread`、`tweets` 等命令。关注、点赞、回复、私信等写命令不属于研究流程。

### Bluesky

- 用户发现：`opencli bluesky search "<query>" --limit 10`。
- 已知账号：`opencli bluesky user <handle>`；帖子线程：`opencli bluesky thread <url>`。
- 公开 API 无需登录，但搜索以用户为主，行业帖子可能没有；抽样无结果时记录低产出，不连续扩大抓取。

## 限频与写操作

- 一次只跑一个平台查询，默认 `--limit 10` 或更小；不写循环、不批量翻页、不制造登录账号。
- 遇到限频先停，记录平台、命令、时间、状态和替代路径；恢复后再做小批量。
- 只使用搜索、主页、帖子、评论读取。点赞、关注、评论、发帖、发消息、发连接邀请等写操作不属于研究流程。

## 全链路角色表

研究社媒时先画完整链路，再决定谁进 ICP：

| 链路位置 | 典型角色 | 能帮助理解什么 | ICP 处理 |
| --- | --- | --- | --- |
| 上游 | 制造商、逆变器/储能/组件供应商、技术支持 | 产品能力、故障模式、安装商常见问题、渠道约束 | 供应商观察可作邻近证据，不自动成为买家 |
| 渠道 | 批发商、经销商、分销商 | 库存、信用、交付、保修协调和区域覆盖 | 若本公司直接卖给渠道，才进入对应渠道 ICP |
| 交付 | EPC、安装商、电气承包商、运维商 | 报价、选型、施工、调试、返工、售后与项目风险 | 通常是直接 ICP 候选 |
| 下游 | 业主、工商业终端客户、DIY/prosumer | 价格透明度、许可、并网、监控、漏水、保修期待 | 作为客户的客户和压力来源，不混入直接 B2B ICP |
| 规则闸门 | 电网/DNO、许可机构、认证与标准机构 | 什么可以安装、并网和交付，谁承担合规风险 | 影响采购和决策链，不是独立商业买家 |

供应商、渠道商、安装商和下游用户都值得看；研究的是整条链怎样传导压力，不是把每个角色都硬塞进同一张 ICP 表。只有直接向本公司采购的角色进入主名单，其他角色进入“链路证据”或“下游压力”。

## 证据分级

- **直接买家自述**：安装商、EPC、经销商自己描述项目、供应、采购或风险。
- **邻近观察**：供应商、招聘方、渠道商描述买家常见问题；需要一条直接买家或规则来源复核。
- **营销展示**：公司主页主动发布的产品、速度、库存和施工展示；只证明市场表达。
- **下游压力**：业主、DIY、prosumer 或终端客户的担忧；说明安装商要承担什么，不直接等于安装商采购动机。
- **规则证据**：DNO、证书、许可、标准或平台官方说明。

## 搜索日志

每轮至少在交付物的 `## 搜索日志` 记录：

| # | Platform | Capability | Query / URL | Chain role | Auth / status | Results | Useful | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

- `Capability` 写 `opencli_search`、`opencli_browser`、`opencli_extract` 或具体站点命令。
- `Chain role` 写上游、渠道、交付、下游或规则闸门。
- `Useful` 只数能支撑判断或提出下一问题的结果；广告和重复内容记 0。
- 429、404、登录跳转和替代路径写进 `Notes`，不把失败写成“没有数据”。
