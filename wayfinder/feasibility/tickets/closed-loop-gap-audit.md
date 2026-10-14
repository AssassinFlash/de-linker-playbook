---
wayfinder: task
status: closed
assignee: claude-main (charting session, user-directed 2026-10-14)
blocked_by: []
---

# 现仓库闭环缺口审计

## Question

拿 Destination 的闭环定义逐条对照本仓库（AFK，只读）：从「事实源 → 方法 skill → 交付物 → 执行登记 → 反馈分级回流 → 台账决定下一步」这条链上，每一环在仓库里是否存在、是否可验证、证据是什么？

已知线索（须核实并扩展）：`state/status.md` 只有营销 0–7、无获客线；完成标准仅「交付物非空且不是例子原文」；`product_context` 指向已过期的 `~/Documents/New`；无数据层、无执行登记；上一张地图把「实际执行营销」列为 Out of scope；验收只测了 harness 冷启动能读台账。

产出：缺口清单（环节、现状、证据路径、严重度），写进本票 Resolution。

## Resolution

2026-10-14，只读对照（主模型，用户指定在建图会话内做）。链：事实源 → 方法 skill → 交付物 → 执行登记 → 反馈回流 → 台账决定下一步，外加验证层。严重度：**致命** = 闭环在这一环必断；**高** = 能跑但结论不可信或一条线跑不通；**中** = 可用但需改。

| # | 环节 | 现状 | 证据 | 严重度 |
|---|---|---|---|---|
| 1 | 事实源 | 101 个 skill 文件把 `~/Documents/New`（已过期）**写死**为缺省或参数路径；指向新站仓库 `~/Documents/de-linker` 的引用为 0。改台账 `product_context` 一处换不了源，「指路不复制」被写死的回退路径架空。 | `grep -rl "Documents/New" skills \| wc -l` = 101；`state/status.md` `product_context` | 致命 |
| 2 | 反馈回流（L1–L3） | skill 里 GSC / Search Console / Google Sheets / IMAP / Woo 的引用全为 0；唯一的度量 skill（phase 7 `marketing-analytics-and-optimization`）只**设计**事件与实验，数字只收「用户本轮提供的值」；仓内无任何取数脚本；Google 侧为零（见「Google 账号现状清点」）。 | `skills/marketing-analytics-and-optimization/SKILL.md:23,32`；`evals/` 无取数代码 | 致命 |
| 3 | 台账决定下一步 | 编排是**瀑布**：`next` = 依赖已满足的下一个 phase，走完 7 即 `stop`，没有任何一条规则读反馈来选下一步；度量排在最后一相，反馈结构上无处回流。 | `skills/marketing-orchestrator/SKILL.md:29`；`state/status.md` 阶段表 | 致命 |
| 4 | 两条线共用台账 | 营销与获客两个编排器读写同一 `state/status.md` 的同名键（`phase`/`next`/`output_dir`）；台账只有营销 0–7，获客字段为 0；获客硬依赖的审批状态只存在交付物 frontmatter。跑一次获客就会覆盖营销进度。 | `skills/lead-generation/SKILL.md` 步骤 4；`references/write-protocol.md:3`；`grep -c approved state/status.md` = 0 | 致命 |
| 5 | 执行登记（L0） | 全仓无执行登记的概念与位置（「执行登记」「上线记录」0 处）。 | grep | 高 |
| 6 | 交付物 → 线上（站点侧） | 「上线只是手动点一下」对新站不成立：页面模板在新站 git 仓库（`plugins/linker-commerce/content/livecanvas/`），营销十页文案冻结，客户可见文案须走对抗式文案评审，用户不亲自部署。playbook 交付物到新站没有定义好的交接面（谁接、以什么格式、经哪道评审）。GSC 验证、GA4 标签、同意横幅同样要落到新站。 | `~/Documents/de-linker/AGENTS.md:26`；「Google 账号现状清点」站点部署行 | 高 |
| 7 | 获客线的对象 | 获客流水线按**陌生开发**设计（ICP → 找公司 → 找联系人 → 冷邮件）；首要资产「激活名单」没有入口：无 skill 以导入的已同意客户表为输入，激活/win-back 词汇只在营销线 `marketing-retention` 与交付后的 `lead-service-retention`。 | `grep -rli "激活\|win-back\|dormant" skills` | 高 |
| 8 | 验证层 | 完成标准 =「交付物非空且不是例子原文」；`validate_deliverables` 只验 schema 可解析与来源栏存在（实跑通过）——验形式不验效果。仓库**确有一个闭环，但闭在错的对象上**：`marketing-eval` / `marketing-skill-eval` → `marketing-evolve` 循环改的是 skill 文本质量，不是市场结果。获客线的闸门是「用户审批」，而操作者无行业判断依据（见 Notes）——审批是**不可验证的中间状态**。 | `state/status.md` 完成标准列；`evals/validate_deliverables.py`；三个 eval/evolve skill 的 description；`lead-generation/references/orchestration-protocol.md:29` | 高 |
| 9 | 前一轮验收为何全绿 | 上一张地图把「实际执行营销」列为 Out of scope，验收测的是保真搬运与 harness 冷启动能读台账，不测产出有没有效果。 | `wayfinder/map.md` Out of scope；`wayfinder/tickets/acceptance-review-and-smoke.md` | 背景 |

**可直接留用的**：方法正文（上游 marketingskills，见「开源参照全景」）；文件台账跨 harness 可接力的机制（上一图五家实测）；获客编排协议的下游过期传播（`approved` → `stale`）；schemas/templates；新站侧现成的 L3 数据（Woo 询盘状态、每日摘要）。

**缺口的分布**：方法层没有致命缺口。致命缺口集中在三处——事实源写死（机械但量大，101 文件）、反馈回流整层缺失、编排是瀑布而非循环且两线共用一张台账。后两者是结构性的：要让「数据决定下一步」，台账需要新字段、编排器需要一条读反馈选动作的规则，这在现结构上是重写级改动（局限在 2 个编排 skill + 台账 + 新增取数脚本），不是逐 skill 修补。另有两处接口缺口：playbook → 新站的交接面、激活名单的入口。

### 用户更正（2026-10-14，审计后）

- **#1 事实源**：新源 = 竞品调研 + 线上站点 + 新站仓库三方映射（见地图 Notes）。缺口性质不变（101 处写死仍须改），但新源已找到且比 New 更丰富。
- **#6 降为「中」**：「营销十页文案冻结」是开发期的阶段性规定，由 AI 定义、可改；现进入内容建设期，全部不冻结。剩下的缺口只是交接面：playbook 产出由谁、以什么格式进新站（用户不亲自部署，新站有文案评审流程）。
- **#7 降为「中」**：获客线按陌生开发来做是对的；名单只是一串名字，背后情况未知。现有陌生开发流水线（调研公司 → 联系人 → 外展）适用，缺的只是「以一份给定名单作为种子输入」的入口，不是缺一整套激活方法。
