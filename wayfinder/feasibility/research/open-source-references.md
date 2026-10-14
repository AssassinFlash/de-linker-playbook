---
wayfinder: research
created: 2026-10-14
status: complete
feeds: open-source-references
---

# 开源参照全景

检索日 2026-10-14。事实跟在来源后面。标了 **推断** 的句子不是来源里的原话。查不到的写「未查证」。

闭环用 [`CONTEXT.md`](../../../CONTEXT.md) 的分级：L0 已执行，L1 已到达（收录或展示；邮件送达），L2 有互动（搜索点击；邮件回复），L3 询盘。地图里的闭环还要求这些信号自动进 Google 表格，并驱动下一步；发布和发信仍由人点。见 [`wayfinder/feasibility/map.md`](../map.md)。

分档按票面：A 有数据接入代码且有公开结果；B 有数据接入代码、没有公开结果；C 纯 prompt/skill 集。

## 结论摘要

本轮没有找到分档 A 的项目：没有一个同时具备数据接入代码，和公开、非虚构的「执行 → 数据回流 → 驱动下一步」结果。

最接近闭环的是开源 SDR [AgentSDR](https://github.com/Kandid-ai/AgentSDR)（B）：回复进队列、分类、起草下一封并等人批准；演示姓名标明虚构，序列本身按排程发送。

SEO 能读到 L1 展示和 L2 点击的，是 [mcp-gsc](https://github.com/AminForou/mcp-gsc)、[Google 官方 GA4 MCP](https://github.com/googleanalytics/google-analytics-mcp)，以及把 GA4、GSC 和 Sheets 写在一起的 [google-marketing-stack-mcp](https://github.com/generalist-club/google-marketing-stack-mcp)。三者都是人问一次才返回，不写执行登记，不自动排下一步，属 B。

[CoreSpeed](https://corespeed.io/) 是托管连接器，不是开源 agent。官方 SEO 文写了「查数据、改页面、再测」，但案例标明虚构，且没有点名 GSC 或 GA4。

[marketingskills](https://github.com/coreyhaines31/marketingskills)、Hypit、9 个电商视觉库的 skill 正文是 C。marketingskills 仓库里另有调用 GSC 和 GA4 API 的 CLI，那一部分是 B。

本仓库 v3 任务技能的目录名来自 marketingskills 在 2026-05-14 改名之前的目录（37 个里 32 个同名）。本地 git 历史没有引用该仓库，不能算 fork。现行 `marketing-*` 阶段名是 v3 自己的编排，抽取时才加前缀。

对德国 B2B 储能询盘站，方法层不必换掉。缺口是把 GSC/GA4 的展示和点击，以及邮箱回复，写进 Google 表格并据此决定下一步。现成可看的代码是上面三个 B 档接口，不是再找一套 skill。

## 特别回答：v3 营销 skill 的命名从哪来

**查证。** 来源是 [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)。仓库创建于 2026-01-15，MIT，检索日 54,608 star，最后推送 2026-10-14。作者页写明这是给 coding agent 用的营销 skill 集：<https://github.com/coreyhaines31/marketingskills/blob/main/README.md>。

2026-04-24 的目录快照有 40 个 skill，提交 `1bcff9fc79c64fd7886c3c7aa583f4bd63916ff2`：<https://github.com/coreyhaines31/marketingskills/tree/1bcff9fc79c64fd7886c3c7aa583f4bd63916ff2/skills>。其中这 32 个名字与本地 `~/Documents/marketing-playbook-v3/skills/` 的目录名相同：

`ab-test-setup`、`ad-creative`、`ai-seo`、`analytics-tracking`、`churn-prevention`、`cold-email`、`competitor-alternatives`、`content-strategy`、`copy-editing`、`copywriting`、`email-sequence`、`form-cro`、`free-tool-strategy`、`launch-strategy`、`marketing-ideas`、`marketing-psychology`、`onboarding-cro`、`page-cro`、`paid-ads`、`paywall-upgrade-cro`、`popup-cro`、`pricing-strategy`、`product-marketing-context`、`programmatic-seo`、`referral-program`、`revops`、`sales-enablement`、`schema-markup`、`seo-audit`、`signup-flow-cro`、`site-architecture`、`social-content`。

v3 多出来、上游当时没有的 5 个：`image-prompts`（上游叫 `image`）、`video-script`（上游叫 `video`）、`marketing-playbook`、`marketing-teach`、`skill-eval`。上游当时有、v3 没有的 8 个：`aso-audit`、`community-marketing`、`competitor-profiling`、`customer-research`、`directory-submissions`、`lead-magnets`、`image`、`video`。

正文不是逐字拷贝，框架句还在。上游 2026-04-24 的 `page-cro` 以 “Check for product marketing context first” 开头，分析顺序是价值主张（5 秒）、标题、CTA，弱 CTA 举的是 “Submit”“Learn More”：<https://github.com/coreyhaines31/marketingskills/blob/1bcff9fc79c64fd7886c3c7aa583f4bd63916ff2/skills/page-cro/SKILL.md>。同一句和同一套顺序出现在 v3 的 `skills/page-cro/SKILL.md`，只是把注册改成了询盘和样品。上游 `copy-editing` 的 Seven Sweeps 七个名字是 Clarity、Voice and Tone、So What、Prove It、Specificity、Heightened Emotion、Zero Risk：<https://github.com/coreyhaines31/marketingskills/blob/main/skills/copy-editing/SKILL.md>。v3 现行 `/.claude/skills/copywriting/SKILL.md` 第 2.7 节用了同一组名字。上游 `seo-audit` 写明客户端注入的 JSON-LD 不能靠静态抓取判断：<https://github.com/coreyhaines31/marketingskills/blob/1bcff9fc79c64fd7886c3c7aa583f4bd63916ff2/skills/seo-audit/SKILL.md>。v3 `skills/seo-audit/SKILL.md` 保留了这条限制，工具名改成了 WebFetch 和 Tavily。

2026-05-14 上游自己改了名。提交 `30f9b9a729bbbe3da562fc1108c31f3a35afcca1`（2026-05-13 22:05 PDT）说明是 “v2.0 skill renames and CRO consolidation (#291)”：<https://github.com/coreyhaines31/marketingskills/commit/30f9b9a729bbbe3da562fc1108c31f3a35afcca1>。现行 README 里 `page-cro` 已变成 `cro`，`paid-ads` 变成 `ads`，`product-marketing-context` 变成 `product-marketing`：<https://github.com/coreyhaines31/marketingskills/blob/main/README.md>。本仓库抽的不是这份现行目录。

**查证，本地。** `~/Documents/marketing-playbook-v3` 没有 git remote。在该仓库历史里检索 `coreyhaines` 和 `marketingskills`，没有提交命中（2026-10-14）。所以这不是 git fork，也没有 submodule 记录。`skill-eval` 另有一处引用，指向 Anthropic 的 skill-creator，不是这个营销集：`docs/superpowers/plans/2026-03-15-skill-eval-reconstruction.md` 写了 <https://github.com/anthropics/skills/tree/main/skills/skill-creator>。

**推断。** 目录名集合、产品上下文文件名、CRO 骨架和 Seven Sweeps 对得上，上游创建日又早于 v3 规格里的 2026-03，所以 v3 的任务技能名和结构取自该集 2026 年 5 月改名之前的版本，然后改写成不锈钢外贸管线。不能把「同名」说成「整份正文来自上游」。

和本仓库现行 `marketing-*` 的差别：

- 阶段入口是 v3 自己的。`docs/legacy-command-migration.md` 把 `/marketing-page-cro` 收成 `landing-page`，把 `/marketing-cold-email` 和 `/marketing-email-sequence` 收成 `email-outreach`，并写明 `/marketing-paywall-cro`、`/marketing-popup-cro`、`/marketing-signup-cro` 已删除，原因是不适用于 B2B 外贸。
- 抽进本仓库时，无前缀的名字才加上 `marketing-`。映射在 [`wayfinder/extraction-spec.md`](../../extraction-spec.md)。
- 上游现行集多了 `marketing-loops`、`prospecting`、`cold-email` 等，本仓库没有照单再导入。
- 上游 `tools/clis/` 里有 `ga4.js`、`google-search-console.js`、`instantly.js` 等可执行客户端。本仓库没有这些脚本。

获客线 43 个 `lead-*` 不在这个问题里。抽取规格写的是来自用户自购的付费 prompt，不是公开 skill 集。本轮没有把那份付费原文拿去对公开仓库。

## 分档一览

| 对象 | 档 | 闭环读到哪 | 会不会驱动下一步 |
| --- | --- | --- | --- |
| CoreSpeed | B | 文中描述到再测排名；案例虚构。未点名 GSC/GA4 | 示例要求改页面前给人看。调度靠外部 cron |
| AminForou/mcp-gsc | B | L1 展示与索引，L2 点击 | 不会。人再问一次才有建议 |
| Google 官方 GA4 MCP | B | 已配置的事件可当转化；无 GSC | 不会 |
| google-marketing-stack-mcp | B | L1/L2，并能写入 Sheets | 不会自己排下一步 |
| OpenSEO | B | 第三方 SEO 数据，不是本站 GSC | README 未写自动改页 |
| marketingskills 的 skill 正文 | C | 无 | `marketing-loops` 只规定人去挂 cron |
| marketingskills 的 `tools/clis` | B | GSC、GA4、Instantly 等 API | CLI 是单次调用，不是台账回路 |
| AgentSDR | B | L2 回复；序列发送接近 L0 | 回复稿等人批准；跟进序列按排程发 |
| smart-trade-ai | 未升档 | README 声称阿里询盘与周复盘 | 调度代码未逐行核对 |
| Hypit | C | 无营销分级 | 无 |
| 9 个电商视觉库 | C | 无 | 无 |

## 起点

### CoreSpeed

现成产品，不是开源仓库。本轮没有找到它的连接器源码。产品自己说：一个 MCP 端点 `https://api.corespeed.io/mcp`，代理已授权应用的 OAuth，凭证不交给 agent。介绍文 2026-09-14：<https://corespeed.io/blog/introducing-corespeed>。给 agent 的入口是 <https://corespeed.io/SKILL.md>，索引在 <https://corespeed.io/llms.txt>。

`llms.txt` 点名的应用包括 Gmail、Slack、GitHub、Notion、Linear、HubSpot。SEO 文（2026-10-12，Milton Yan）点名的工作区连接是 PostHog、Google Ads、Google Sheets、Notion、Slack，站点连接是 Webflow 和 Contentful，另有 `web__google_search` 和一组第三方 SEO 页面抓取：<https://corespeed.io/blog/corespeed-for-seo>。这篇没有出现 Google Search Console，也没有出现 GA4。连接器文档写明，完整清单只能向已登录的 `https://api.corespeed.io/connectors` 要，不要把名单写死：<https://corespeed.io/docs/connectors>。因此「有没有 GSC / GA4 连接器」未查证。

同一篇 SEO 文把演示站 `fernway.example`、关键词和排名数字标成虚构，并写 “Not a measured result”。同日另有一笔非虚构数字：五个公开数据抓取合计约 $0.039825，其中一次 Semrush 抓取没有返回记录。这是工具计费，不是一次 SEO 或询盘结果，所以不升到 A。

回路停在哪：示例提示要求先给人看改动再写入 CMS；下一步靠 `memory__remember` 和外部 cron、CI 或 agent 自己的定时任务。9 月 14 日的介绍文把 “Scheduling and coordination” 标成 Planned。活动日志是工具调用审计，不是本仓库的执行登记：<https://corespeed.io/docs/activity>。批准门在 <https://corespeed.io/docs/approvals>。

维护：文档更新到 2026-10。定价页有免费档和 Pro $20/月：<https://corespeed.io/pricing>。

和本仓库可比的是「凭证集中、写操作可拦住、有调用记录」。不可比的是它不产出 L0–L3 台账，也不知道 Woo 询盘。

**推断，适用度。** 若登录后的连接器索引里有 Gmail 和 Sheets，它可以当读信和写表的托管层。GSC/GA4 未在公开 SEO 文出现，不能当成 Google 优先的现成通路。德国站、德语、储能行业均未查证。

### AminForou/mcp-gsc

开源 GSC MCP。MIT，Python，1,918 star，创建 2025-03-14，最后推送 2026-09-15：<https://github.com/AminForou/mcp-gsc>。README 版本 0.4.1（2026 年 9 月）列出搜索分析（点击、展示、CTR、排名）、URL 检查、站点地图；OAuth 或服务账号；默认关掉添加和删除站点：<https://github.com/AminForou/mcp-gsc/blob/main/README.md>。实现文件是仓库根的 `gsc_server.py`。

仓库里还有四个 skill 目录：`seo-weekly-report`、`cannibalization-check`、`indexing-audit`、`content-opportunities`。README 把它们写成 Cursor 里的提示用法，例如「跑周报」「找 11–20 名的查询」。没有调度器，也没有写入 Sheets 的工具。

能读 L1（展示、索引结论）和 L2（点击、CTR）。读不到邮件送达，读不到询盘。下一步是人再提一个问题。README 的例子用 `mywebsite.com`，没有一家站点的前后数据。YouTube 链接是安装教程，不是案例。公开结果未查证，故 B 而不是 A。

README 另指向付费托管版 <https://www.advancedgsc.com/mcp>。该产品未查证。

**推断，适用度。** 这是德国站打通 GSC 最直接的开源代码：官方 Search Console API、只读即可覆盖 L1/L2。它不写执行登记，也不把某次上线归因到之后的展示。要闭环，还得另写「执行登记 → 拉这些工具 → 追加到表格 → 人决定下一页」。

### Hypit

[hypit-ai/hypit](https://github.com/hypit-ai/hypit)。检索日 22,041 star，最后推送 2026-10-13，主页 <https://hypit.ai>。仓库说明是用 agent 复刻一条视频的整套流程（画面、字幕、B-roll），再出变体。Skill 在 `skills/hypit/`，安装命令是 `npx skills add hypit-ai/hypit -g`：<https://github.com/hypit-ai/hypit/blob/main/docs/guide/skill.md>。技能文档讲的是参考片、脚本、提示词和可再跑的工程文件，没有 GSC、邮件或询盘。许可证字段是 NOASSERTION，不能写成 MIT。

分档 C。仓库描述里的 “100M views” 是宣传句，不是一条带回流的案例。

**推断，适用度。** 与德国储能询盘站的获客回路无关。只有在单独做视频素材时才沾边，那不是这张票要补的缺口。

### 九个电商视觉 skill

九个 README 都没有出现 Search Console、GA4、展示、定时回流。分档都是 C。星数和最后推送来自 GitHub API，2026-10-14。

| 仓库 | 是什么 | 维护 | 闭环 |
| --- | --- | --- | --- |
| [AJbeckliy/detail-flow](https://github.com/AJbeckliy/detail-flow) | 详情页规划、生成、审核、返修。217 star，无许可证字段 | 最后推送 2026-06-11 | 无 |
| [feichanggege/ecommerce-visual-copywriting-skill](https://github.com/feichanggege/ecommerce-visual-copywriting-skill) | 主图、详情、A+、文案和合规。888 star，MIT | 2026-09-17 | 无 |
| [oldred-byte/ec-visual-skill](https://github.com/oldred-byte/ec-visual-skill) | 产品图加参考图，出主图和详情流程。88 star，MIT | 2026-07-06 | 无 |
| [forest-USTC/ecommerce-visual-planning-skill](https://github.com/forest-USTC/ecommerce-visual-planning-skill) | 主图与详情策划，两道确认门。8 star，MIT | 2026-08-01 | 无 |
| [yejy53/Editable-Design](https://github.com/yejy53/Editable-Design) | 可编辑视觉稿。1,174 star，Apache-2.0。README 链到论文 <https://arxiv.org/abs/2609.04034> | 2026-09-29 | 论文不是营销回流 |
| [dlazy-ai/ecommerce-skills](https://github.com/dlazy-ai/ecommerce-skills) | 26 个视觉 skill，仓库自述可换图像后端。37 star，MIT。目录里有 `mcp/`、`evals/` | 2026-10-12 | 出图，不是反馈 |
| [ninemouth/sellerpilot-product-image-industrial](https://github.com/ninemouth/sellerpilot-product-image-industrial) | 工业品套图的策划、生成和质检。32 star，MIT。英文 README 写明不是一次性提示词包 | 2026-09-03 | 质检的是图，不是流量 |
| [gpt-img-2/gpt-image-2-ecommerce-skill](https://github.com/gpt-img-2/gpt-image-2-ecommerce-skill) | 保产品原样的主图提示词。10 star，MIT | 仅 2026-07-16 一次推送 | 无 |
| [meitu/designkit-ecommerce-skills](https://github.com/meitu/designkit-ecommerce-skills) | 美图 Designkit：抠图、修复、主图。8 star，无许可证字段。目录有 `scripts/`、`api/` | 最后推送 2026-03-31 | 出图 API，未查证有没有回流 |

**推断，适用度。** 这些库服务的是平台电商主图和详情页。德国储能站的买家是安装商、EPC 和电网开发商，询盘来自站内表单和邮件。视觉生产能力可以另作素材工序，补不上 GSC、GA4 或询盘回流。`detail-flow`、`gpt-image-2`、`designkit` 已经几个月没有推送。

## 主动扩展

### Google 官方 GA4 MCP

[googleanalytics/google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)。Apache-2.0，Python，3,452 star，最后推送 2026-10-02。README 标题写 Experimental，工具是 `get_account_summaries`、`run_report`、`run_funnel_report`、`run_realtime_report` 等，走 Analytics Admin API 和 Data API：<https://github.com/googleanalytics/google-analytics-mcp/blob/main/README.md>。发布记录 v0.7.0 在 2026-07-29：<https://github.com/googleanalytics/google-analytics-mcp/releases>。Google Analytics 频道 2025-07-22 的视频是产品介绍，不是某站的效果案例：<https://www.youtube.com/watch?v=PT4wGPxWiRQ>。

分档 B。能读报表；转化只在该 GA4 资源已经把事件标成 key event 时才有意义。没有 GSC，没有 Sheets，没有下一步调度。地图已写明当前站点和仓库都没有 GA4。在那之前，这个服务器无数据可读。

### google-marketing-stack-mcp

[generalist-club/google-marketing-stack-mcp](https://github.com/generalist-club/google-marketing-stack-mcp)。MIT，JavaScript，7 star，最后推送 2026-10-10。README 称 44 个工具、浏览器 OAuth、数据不经过第三方服务器：<https://github.com/generalist-club/google-marketing-stack-mcp/blob/main/README.md>。本轮核对到的表有 GA4 15 个（含 `ga4_conversions`）、GSC 9 个（含 `gsc_search_analytics`、`gsc_top_queries`、`gsc_sitemaps`）、Sheets 5 个（`sheets_read`、`sheets_write`、`sheets_append`、`sheets_info`、`sheets_clear`）、GTM 若干。44 这个总数没有逐个重数。PageSpeed 工具名未在本次摘录里单列，未查证是否齐。

分档 B。这是本轮唯一在同一份 README 里同时具备 GSC 读、GA4 读、Sheets 追加的开源服务器。示例全是「问一句」，没有 cron，没有 L0 执行登记，没有「追加一行之后做什么」的规则。没有公开案例。

**推断，适用度。** 和「Google 优先、表格当台账、人不自动发信」最贴的是这一份，而不是 CoreSpeed 或 mcp-gsc 单件。星数很少，当依赖来用之前要自己审 OAuth 范围和写入行为。它仍然不会自动驱动下一步；驱动规则得写在 playbook 里。

### OpenSEO

[every-app/open-seo](https://github.com/every-app/open-seo)。MIT，TypeScript，23,509 star，最后推送 2026-10-08，站点 <https://openseo.so>。README 写：自带 DataForSEO 密钥、按次付费；工作流包括关键词、排名、竞品、外链、站点审计、AI 可见度；对 Claude Code、OpenClaw、Hermes 暴露 MCP 和 skills：<https://github.com/every-app/open-seo/blob/main/README.md>。这份 86 行 README 没有 Search Console、GA4 或 Google Sheets。调用 DataForSEO 的源文件本轮没有打开。

分档按 README 记 B：它是接了外部 SEO 数据的应用，不是纯 markdown。公开的「排名变化之后改了哪一页、询盘是否上升」未查证。

**推断，适用度。** 它补的是关键词和可见度估算，不是本站 GSC 里的展示和点击。德国站的 L1/L2 仍要走 Search Console API。

### marketingskills：skill 是 C，CLI 是 B

skill 正文是写法。`marketing-loops` 把回路定义成九段（节奏、触发、自检、状态、停止条件、输出），并写明调度靠 Claude Code 的 cron、系统 cron，或者「每周一人手跑一次」：<https://github.com/coreyhaines31/marketingskills/blob/main/skills/marketing-loops/SKILL.md>。SEO 状态建议放在 `.agents/seo/`，外展状态放在 `.agents/outbound/`。这是台账形状的说明书，文件里没有 API 调用。`loop-catalog.md` 有没有点名下面这些 CLI，本轮未打开。

`tools/clis/` 是另一回事。检索日目录里有 `ga4.js`、`google-search-console.js`、`instantly.js`、`apollo.js`、`google-ads.js` 等。`google-search-console.js` 请求 `https://searchconsole.googleapis.com`，令牌来自 `GSC_ACCESS_TOKEN`：<https://github.com/coreyhaines31/marketingskills/blob/main/tools/clis/google-search-console.js>。`ga4.js` 请求 Data API 和 Admin API，文件顶部还有 Measurement Protocol 的 `https://www.google-analytics.com/mp/collect`：<https://github.com/coreyhaines31/marketingskills/blob/main/tools/clis/ga4.js>。哪些子命令会真正发送事件，未逐个核对。`instantly.js` 走 Instantly API v2，兴趣状态包括 interested、meeting-booked、won：<https://github.com/coreyhaines31/marketingskills/blob/main/tools/clis/instantly.js>。引导安装文档 `tools/SETUP.md` 把第一次成功定义成「读到昨天的 active users」，不是一次营销结果：<https://github.com/coreyhaines31/marketingskills/blob/main/tools/SETUP.md>。该表的前几行是 Google Ads、Meta、LinkedIn、GA4、Stripe，没有把 GSC 放进这段引导。

因此：skill 档 C；CLI 档 B。没有公开的、用这些 CLI 跑完并改变下一步的案例。

**推断，适用度。** 不要把现行 marketingskills 再导进来替换 v3。命名已经从这里来过，正文也改成了询盘而不是 SaaS 注册。值得单独看的是 `google-search-console.js` 和 `ga4.js` 这种薄客户端，以及 `marketing-loops` 对「状态、停止条件、人批准之后才发布」的写法。Instantly/Apollo CLI 会把发信交回那些平台，和「不自动发信」冲突。

### AgentSDR

[Kandid-ai/AgentSDR](https://github.com/Kandid-ai/AgentSDR)。MIT，TypeScript，38 star，最后推送 2026-10-09，文档 <https://docs.agentsdr.ai>。README 写：一个 Postgres 上的 Next.js 应用；邮件走自己的 Google Workspace 邮箱；LinkedIn 和 WhatsApp 走 Unipile；每个回复进同一队列，分类后起草，发出前要人点；跟进序列由应用内的定时任务排程。演示影片注明姓名是虚构的：<https://github.com/Kandid-ai/AgentSDR/blob/main/README.md>。产品页同样写草稿先拦住、序列从自己的邮箱发出：<https://docs.agentsdr.ai/>。没有公开的回复率或成交数。

分档 B。读到 L2（回复）。L0 的「发出」有一部分是排程自动发，不是每次人手点。L1 送达未在 README 单列。他们的 Interested 不是本仓库的询盘（Woo 订单或 `/kontakt/`）。台账在自己的数据库，不在 Google 表格。

**推断，适用度。** 结构上最像获客线要的「回复回来 → 分类 → 下一封等人发」。不能直接拿来用：自动序列违反「不自动发信」；LinkedIn 自动化依赖 Unipile，和德国 B2B 储能的邮件询盘不是一条路。可借鉴的是队列和批准，不是它的发送器。

### smart-trade-ai

[chefroger/smart-trade-ai](https://github.com/chefroger/smart-trade-ai)。AGPL-3.0，87 star，最后推送 2026-10-14。仓库说明是本地外贸助手，约 39 个 B2B skill。README 写了定时查看阿里国际站或中国制造网的新询盘，以及周度询盘复盘并输出跟进行动表：<https://github.com/chefroger/smart-trade-ai>。仓库根有 `server.py`、`skills/`、`trade/`。本轮没有打开定时任务的实现，所以不能确认它真的调用了平台 API。不升到 B。

**推断，适用度。** 它是「外贸 skill 加本地日程」的近亲，对象是平台询盘，不是德国独立站的 GSC 和 `chester@de-linker.com`。方法层可对照，数据层对不上。

## 对本仓库意味着什么

**推断。** 方法层（80 个 skill 的命名和阶段结构）不是缺口。任务技能名已经能对上一个公开集，而且 v3 已经把 SaaS 注册、付费墙和弹窗从现行入口删掉了。再换一套 skill 集，补不上看板。

数据层才是空的，而且是分开的：

- L1/L2 搜索：mcp-gsc，或 google-marketing-stack-mcp 的 `gsc_*`。官方没有对应的 GSC MCP；官方有的是 GA4 MCP。
- 转化事件：官方 GA4 MCP 或同一份 gstack 的 `ga4_conversions`。站上还没有 GA4，这一级现在读不到。
- 台账：gstack 的 `sheets_append` 是本轮唯一看见的「把行追加进 Google 表格」的开源工具。marketingskills 的 CLI 把结果打到 stdout，不写表。
- L2 邮件回复、L0 发信登记：上面没有一家在「只读 `chester@de-linker.com`、人点发送、一行执行登记」这个约束下做完。AgentSDR 读的是它自己发出的序列。CoreSpeed 的文档点了 Gmail，但是托管产品，而且没有询盘分级。

没有项目把这四段接成「人发一次 → 表格多一行 → 下次 skill 读这行决定写哪一页或写哪封信」。

## 仍未解决

- CoreSpeed 登录后的连接器索引里有没有 GSC 和 GA4。公开 SEO 文没有写。未查证。
- mcp-gsc、官方 GA4 MCP、gstack、AgentSDR、OpenSEO 在 README 之外有没有用户贴出的前后数据。未查证。
- `google-marketing-stack-mcp` 只有 7 star。OAuth 范围、`sheets_write` 会不会覆盖旧行、有没有测试，本轮没有审代码。
- marketingskills 的 `ga4.js` 是否真的会调用 Measurement Protocol 发送事件。只确认文件里有这个 URL。
- `marketing-loops` 的 `references/loop-catalog.md` 有没有绑定 `tools/clis`。未打开。
- smart-trade-ai 的定时询盘检查是真 API 还是说明文字。未打开 `server.py`。
- OpenSEO 的排名追踪会不会写出「下一篇改什么」。README 没有写。
- Advanced GSC 托管版、Instantly、Unipile 的条款和德国送达率。未查证。
- 没有找到针对德国储能、安装商或 EPC 询盘站跑通过的公开闭环。
- 获客 skill 的付费 prompt 源头没有对公开仓库。那是另一条来源，不是这张票的开源名单。
