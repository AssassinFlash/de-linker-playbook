---
wayfinder: map
created: 2026-10-14
---

# 地图：playbook 闭环可行性——补齐还是从零开始

## Destination

一份可行性结论：本仓库（作为一个整体）距「闭环」还缺哪些环节；每个缺口有无已被验证的开源/现成路径可补；结论是在现仓库上补齐还是从零开始，以及补齐顺序（Google 渠道先通）。闭环 = 执行由人手动 + 执行登记；反馈按反馈分级自动回流到 Google 表格并驱动下一步（术语见 [`CONTEXT.md`](../../CONTEXT.md)）。

## Notes

- **只规划不执行（用户定 2026-10-14）**：本图产出结论，不改仓库；重写/补齐是下一张地图。
- **不拆（用户定）**：仓库作为一个整体评判，不分块下「保留/重写」结论。
- **两条线都闭环（用户定）**：营销线与获客线都要，不砍。
- **执行手动、反馈自动（用户定）**：发布与发信由人手动点，每次动作写执行登记（含发信）；自动化只投在反馈回流。自动发信、自动发布不做。
- **反馈分级要成体系（用户定）**：L0–L3 每级要有定义、记录与据此行动的规则。北极星 = 询盘（任一入口，不去重）。记录与呈现见「可行性裁定」Q8–Q10（底表 + 看板；用户 2026-10-14 推翻了早先的「不自建仪表盘」，自建作为后备）。
- **Google 优先（用户定）**：先打通 GSC、GA4、Google Sheets（记录工具选 Google 而非本地 Excel）。
- **邮箱**：只读 `chester@de-linker.com`（不是 sales@），读发件与收件，得 L0（发了）与 L2（回了）。已查明托管在腾讯企业邮（非 Google），走 IMAP。
- **事实源 = 三方映射（用户定 2026-10-14）**：竞品调研 + 线上站点 + `~/Documents/de-linker`（重构后新站仓库），三者互相对照；`~/Documents/New` 已过期，不再读。竞品调研已整理进私有 vault（经 `deliverables/` 软链）：`deliverables/marketing/00-research/competitor-study-2026-10-01/`（12 家同类储能供货商画像 + 两轮核查后的综合分析 + 老板转发的定位邮件 + 三方比对；副本已去掉问老板的清单，〔未证实〕项以线上站点与新站仓库为准、查不到即按没有）与 `deliverables/marketing/00-research/industry-research-2026-09-20/`（32 份：制造商、批发商、6 类买家画像、链上摩擦、论坛等；29–31 号写的是旧站，可能过期）。连同原始抓取与核查证据整体复制（本地 + GitHub 私有双份），原件不动。读路径时把 `~` 展开为用户主目录。
- **五家兼容降级（用户定）**：方法文本保持跨 harness 可移植；数据接入走仓内脚本（任何 harness 能跑），不再要求逐家冷启动实测。
- **参照的「已验证」标准（用户定）**：有人用它跑出过数据/结果，或自带数据接入代码；纯 prompt 集只作写法参考。用户给的清单（corespeed.io、AminForou/mcp-gsc、hypit skills、9 个电商视觉 skill 等）是起点不是全集，调研须主动扩展。
- **调研派 Grok Build（用户定 2026-10-14）**：research 票不用 Claude 子代理，经 grok-build-bridge（`~/Documents/grok-build-bridge`）派给 Grok Build；主模型只派工、跟进、抽查来源、验收。产出落 `wayfinder/feasibility/research/<票名>.md`，每条事实带来源 URL。
- **外展对象均已取得同意（用户定 2026-10-14）**：「外展的合法边界」的法律约束不作为本图阻碍，lead 外展 skill 不因此改道；同意的留证由用户负责。
- **操作者是新入行者（用户 2026-10-14）**：拿不到老板的隐性知识，也不能回头问；系统不得依赖操作者的行业判断来把关质量——能依赖的只有外部反馈（L1–L3）与可查证的事实。获客线一律按陌生开发来做；老板给的名单只是一串已同意的名字，背后情况未知（见 `CONTEXT.md`「激活名单」），名单不进仓库。
- **冻结是阶段性的（用户定 2026-10-14）**：新站「营销文案冻结」只为开发期防乱改，由 AI 定义、可改；代码基本完工，进入文案与内容建设阶段，所有页面与文案都不冻结。
- **质量优先，无时间预算；一票一新会话**（research 票可并行）。
- 新站已知事实（2026-10-14 只读核查）：询盘 = Woo 订单状态 `inquiry-received` → `proforma-issued`，另有 `/kontakt/` 联系表单；每日 09:00 摘要邮件已列未处理询盘（规格 `docs/specs/74-daily-digest.md`）；`just pull` 出只读伪名化快照；站点与仓库中无 GSC/GA4/同意横幅。

## Decisions so far

<!-- 每关一票加一行：[票名](tickets/x.md)：一句话 gist -->

- [现仓库闭环缺口审计](tickets/closed-loop-gap-audit.md)：方法层无致命缺口；致命缺口在事实源写死 New（101 文件）、反馈回流整层缺失、编排是瀑布且两线共用台账；另缺执行登记；playbook→新站交接面与名单种子入口为中等缺口（用户更正后降级）；现有闭环闭在 skill 文本质量上，不在市场结果上。
- [可行性裁定](tickets/feasibility-verdict.md)：**补齐，不从零开始；编排与台账局部重写**。冷启动阶段 + 运营循环、台账拆两线共用底表、证据闸 + 反馈闸、站点接入归 agent 而内容发布归操作者、GSC 先 GA4 后、底表（Google 表格）+ 看板（Looker Studio）；补齐顺序 0–6 见票。**地图闭环。**
- [Google 账号现状清点](tickets/google-account-inventory.md)：Google 侧全零从头开；全部资源归 `所有者账号`、`日常账号` 加同级管理；无 DNS 权限 → GSC 用网址前缀资源（Site Kit 或 meta 验证）；chester@ 在腾讯企业邮（非 Workspace）；用户不亲自部署。

- [开源参照全景](tickets/open-source-references.md)：无 A 档闭环开源实现；SEO 数据接口（mcp-gsc、GA4 MCP）与 SDR（AgentSDR）止于 B 档；v3 营销 skill 源自 coreyhaines31/marketingskills 改名前目录——方法层可留，闭环段要自接。
- [Google 渠道接入路径](tickets/google-channel-access.md)：1 个 Cloud 项目 + 服务账号 + 三处授权 + 1 个仓内 Python 脚本即可让 GSC 的 L1/L2 回流 Google 表格；GA4 在德国须先有同意横幅。
- [只读邮箱接入](tickets/mailbox-readonly-access.md)：chester@ 在腾讯企业邮，只能走 IMAP 只读；L2 回复可按 Message-ID 对齐；站点询盘通知发 sales@，L3 应取站点 Woo 数据。
- [成熟的反馈分级做法](tickets/feedback-ladder-practice.md)：冷启动只看收录与送达；排名、询盘个位数只记账不决策；德国 UWG §7 限制无同意的邮件广告。
- [外展的合法边界](tickets/outreach-legal-boundary.md)：德国 B2B 冷邮件无事先明示同意即违法；获客线主路径须改为「买家先开口 + 先取同意再手动发信」，5 个外展 skill 的默认动作要改道。

## Not yet specified

<!-- 2026-10-14 清空：剩余疑点均已并入「可行性裁定」的问题。 -->

## Out of scope

- 自动发信、自动发布（执行由人手动）。
- 裁定之后的实际补齐或重写（下一张地图），含：Google 表格的表/列设计、读线上事实走 Woo REST API 还是 `just pull` 快照——两者都已有可行路径，不影响可行性结论。
