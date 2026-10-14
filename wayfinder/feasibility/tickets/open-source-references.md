---
wayfinder: research
status: closed
assignee: grok-build (dispatched 2026-10-14)
blocked_by: []
---

# 开源参照全景

## Question

营销、获客（B2B 外展/SDR）、SEO/AI 搜索三类 agent 化的开源实现与现成产品里，哪些已经形成**稳定闭环**（执行 → 反馈数据回流 → 驱动下一步），哪些只是 prompt/skill 集？

- 起点（用户给，必须覆盖但不限于）：https://corespeed.io/ 、https://github.com/AminForou/mcp-gsc 、「hypit skills」、9 个电商视觉 skill（AJbeckliy/detail-flow、feichanggege/ecommerce-visual-copywriting-skill、oldred-byte/ec-visual-skill、forest-USTC/ecommerce-visual-planning-skill、yejy53/Editable-Design、dlazy-ai/ecommerce-skills、ninemouth/sellerpilot-product-image-industrial、gpt-img-2/gpt-image-2-ecommerce-skill、meitu/designkit-ecommerce-skills）。须主动扩展（如 marketing skill 集、台账驱动的 agent 工作流、带 GSC 回路的 SEO agent、开源 SDR）。
- 按 Notes 的「已验证」标准分档：A 有数据接入代码且有公开结果/案例；B 有数据接入代码无结果；C 纯 prompt/skill 集。
- 每条记：是什么、闭环到哪一级（L0–L3）、数据源、维护活跃度、与本仓库可比的点、对 B2B 储能询盘站（德国）的适用度。
- 特别回答：本仓库 v3 营销 skill 的命名/结构是否来自某个开源 skill 集（如有，给出处与差异）。

产出：`wayfinder/feasibility/research/open-source-references.md`，每条事实带来源 URL。

## 派工记录

Grok Build 桥接会话 `27524965-d394-4753-b65f-8c3cff050451`（2026-10-14 派出；`grok_status`/`grok_events` 可查）。产出：`wayfinder/feasibility/research/open-source-references.md`。

## Resolution

**没有找到 A 档（有数据接入代码 + 公开闭环结果）的开源实现。** 最接近的是开源 SDR AgentSDR（B：回复入队、分类、起草下一封待人批准）；SEO 侧能读 L1/L2 的是 mcp-gsc、Google 官方 GA4 MCP、google-marketing-stack-mcp（均 B：人问一次答一次，不写执行登记、不排下一步）。CoreSpeed 是托管连接器、案例虚构；marketingskills、Hypit、9 个电商视觉库的 skill 正文都是 C。**本仓库 v3 营销 skill 源自 coreyhaines31/marketingskills 2026-05 改名前的目录**（38 个里 32 个同名、框架句保留，非 fork）。推断：方法层不必换，缺的是把展示/点击/回复写进表格并据此决定下一步——这一段业内也没有现成闭环，要自己接。

全文：[`research/open-source-references.md`](../research/open-source-references.md)。主模型抽查（2026-10-14）：上游目录 40 个、与 v3 同名 32 个（gh api 复核）；四个参照仓库存在且在维护。
