---
name: lead-generation
description: >
  Use when starting B2B lead generation, 获客, 外贸获客, 客户开发, ICP,
  客户画像, 找客户, 分销商调研, 零售商名单, 联系人采集, 冷邮件, 开发信,
  外展, LinkedIn 获客, 定向开发, or when the user asks for the next lead
  step, 下一步获客, or a multi-step outreach workflow that needs
  dependencies, parallel company research, or review gates. Read
  state/status.md first; announce the current lead phase, the next
  method skill, and the output path under deliverables/lead/; then run
  that work (dispatch a subagent, else do it inline) and update the
  ledger. Use this navigator rather than inventing a parallel pipeline.
  Greetings get a phase recap only. Marketing-tree work stays with
  marketing-orchestrator. Not for website copy or marketing-tree SEO
  audits.
---

# 获客编排（导航）

读台账、宣布获客阶段、执行当前方法 skill、回写台账。方法本身在各 `lead-*` skill 里。依赖、闸门与审查清单见 `references/dependency-graph.md`；验证—审查—审批—写入见 `references/orchestration-protocol.md`。

## 步骤

1. **读台账** `state/status.md`。完成：能报出 `phase`、`next`、`method_skill`、`output_dir`、`product_context`。
2. **分流**。推进意图（下一步获客 / 获客 / 客户开发 / ICP / 找客户 / 分销商 / 联系人 / 冷邮件 / LinkedIn 获客 / 定向开发）→ 步骤 3。寒暄或无关问题 → 复述 `phase` 与 `next`，停。营销树工作 → 打开 `skills/marketing-orchestrator/SKILL.md`，本 skill 不推进。
3. **从当前获客 phase 做到交付物落地**。进度以台账为准；阶段含义与默认方法 skill 见下表，闸门见 `references/dependency-graph.md`。
   - 台账或 `deliverables/lead/` 缺失 → 先打开 `skills/marketing-init/SKILL.md`；该文件不存在则只报缺口。
   - 台账已写 `method_skill` 且 `skills/<method_skill>/SKILL.md` 存在 → 先读该文件再按其步骤做。需要隔离时 dispatch a subagent, else do it inline。产出进台账 `output_dir`（空则用下表目录）。
   - 该文件不存在 → 停，宣布缺口，不自造流程。
   - 同一 phase 有多个方法 skill：无硬依赖的可并行 dispatch a subagent, else do it inline；有硬依赖的串行。`ANY(...)` 表示括号内至少一个已批准即可。
   - 产品上下文与已批准上游仍不够清楚时，先打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则把缺口写入台账，不自造访谈。
   - 方法 skill 做完后，按 `references/orchestration-protocol.md` 做数据验证、六维审查、用户审批、写入。验证优先打开 `skills/lead-data-validation/SKILL.md`（存在则按其做，否则按协议在本会话内联做完）。
   - 每完成一阶段先回写台账再继续。硬依赖未满足且无 `user_waiver` → 不停跳。
   - 教学走 `skills/lead-teach/SKILL.md`；产出进 `deliverables/lead/00-system/`，不改战役 `phase`。
4. **回写台账**（步骤 3 的每个 phase 边界都做）。完成：YAML、「当前」表、「已完成」与磁盘一致；`output_dir` 落在 `deliverables/lead/` 下；`next` 指向下一动作或 `stop`。下一方法 skill 取：台账已指定且文件仍存在的；否则取全量表中依赖已满足、`SKILL.md` 存在的下一个。都没有 → `next: stop`。

## 阶段

| phase | 名称 | 方法 skill | 产出目录 | 完成标准 |
| --- | --- | --- | --- | --- |
| 0 | 读产品上下文 | 只读 `product_context`；需要档案时打开 `skills/marketing-profile/SKILL.md`、`skills/marketing-product-profile/SKILL.md` | 不把原文写入本仓库 | 三条陈述：买家、所卖、缺口 |
| 1 | 画像 | `lead-icp-analysis`、`lead-search-term-expansion` | `deliverables/lead/01-icp/` | 每 ICP 含画像 + 销售策略 + 数据洞察；每 ICP ≥10 个已验证术语；交付物不是例子原文 |
| 2 | 公司 | `lead-company-research`、`lead-distributor-research`、`lead-retailer-research` | `deliverables/lead/02-companies/` | 目标公司每家 3 信息块；分销商 11 维或简版字段齐；零售商规模与定位字段齐；域名已抓取验证 |
| 3 | 联系人 | `lead-contact-discovery` | `deliverables/lead/03-contacts/` | 按 ICP / 公司类型 / 职位分列；未配置发现服务则标「联系人待补」，不编造邮箱 |
| 4 | 市场 | `lead-competitor-analysis`、`lead-market-analysis` | `deliverables/lead/04-market/` | 定位×代表公司 + 空白；市场 10 板块；数字有来源与年份 |
| 5 | USP | `lead-usp-extraction`、`lead-product-knowledge` | `deliverables/lead/05-usp/` | 差异化方案可执行；产品知识可回溯上下文，不编造合规 |
| 6 | 外展 | `lead-cold-email-gen`、`lead-warm-email-transform`、`lead-followup-sequence`、`lead-email-sequence-strategy`、`lead-magnet-gen` | `deliverables/lead/06-outreach/` | 文案非空且不是例子原文；未配置外发工具则只产文案不发送 |
| 7 | 定向 | `lead-targeted-research`、`lead-targeted-outreach` | `deliverables/lead/07-targeted/` | 调研先于外展 |
| 8 | LinkedIn | `lead-linkedin-topic-research` 及各 `lead-linkedin-*` 帖类型 | `deliverables/lead/08-linkedin/` | 帖子遵守 `references/linkedin-post-guidelines.md` |
| 9 | SEO | `lead-seo-editorial-guidelines`、`lead-seo-outline-gen`、`lead-seo-content-gen`、`lead-seo-content-edit` | `deliverables/lead/09-seo/` | 规范 → 大纲 → 成稿 → 编辑，串行 |
| 10 | 销售 | `lead-service-first-contact`、`lead-service-quotation`、`lead-service-objection`、`lead-service-first-order`、`lead-service-delivery`、`lead-service-retention`、`lead-buyer-psychology` | `deliverables/lead/10-sales/` | 服务链串行；心理分析可与服务链并行 |

`lead-company-research` 的 emerging 产出、`lead-distributor-research` 的 brief 产出是同一 skill 的第二种交付物，不是另一个入口。归档进 `deliverables/lead/99-archive/`。

## 默认

- 进度只认台账。产出只进 `deliverables/lead/`。营销树 `deliverables/marketing/` 不由本 skill 推进。
- 产品事实只读 `product_context`（默认 `~/Documents/New/CONTEXT.md`），不在本仓库另存一份。
- 共用规则若存在则读 `skills/marketing-playbook-standards/SKILL.md`。
- 缺来源、缺搜索：停止并写缺口，不编造。需要查证时用网页搜索；需要原文时抓取指定 URL 的正文。
- 交付物带来源栏；数字必须能回溯产品上下文或已抓取 URL。策略/分析用中文；表列名 English snake_case；公司名不翻译。
- 联系人/邮箱发现服务、网页采集服务、外发工具：仅当用户已配置（付费项须先告知并获准）；否则标「联系人待补」或只产文案。
- 单文件、无并行机会的工作 inline 做完，不 dispatch。
- 清单未过：修一轮，或记录 `user_waiver`。自动修补不超过 3 轮，其后把决策交还用户。
- 阻塞（登录、验证码、付费审批、能力缺失）按 `references/manual-intervention-protocol.md` 请用户接手，从当前进度续，不重头开始。

## 产出

推进时当众宣布：

```markdown
- phase:
- phase_name:
- method_skill:
- output_dir:
- product_context:
```

回写格式见台账「回写」节。不要写仓外路径，不要建外部产出根。写入约定见 `references/write-protocol.md`。

## 例子

> 仅供理解，禁止引用到输出。

用户说「按 Meisterbetrieb、C&I 安装商、EPC 规划席、EPC 采购席、IPP/资产业主分层做获客」。读出台账后当众说：当前 phase 1 画像，下一方法 skill 为 `lead-icp-analysis`，产出路径 `deliverables/lead/01-icp/`。然后打开该 SKILL.md 做，不在本层展开各人格。用户说「先找卡在中间带的公司名单」而台账仍是 phase 1 → 仍宣布画像与同一路径，不跳到 `02-companies/`。用户说「你好」只复述 `phase` 与 `next`，不改文件、不跑管线。

## 易错

- 未读台账就开跑，或另写一套阶段。
- 用斜杠命令名当入口，而不打开 `skills/<name>/SKILL.md`。
- `product_context` 读不到仍往下做。
- 硬依赖缺失且无 `user_waiver` 时跳步；把 `ANY(...)` 当成必须全部批准。
- 方法 skill 文件不存在时自造步骤。
- 把 emerging / brief 当成独立入口另写流程。
- 把产品上下文原文拷进本仓库。
- 把 skill 例子原文写入交付物。
- 教学改了战役 `phase`。
- 寒暄时改文件。
- 编造公司、域名、邮箱或市场规模。
- 营销树与获客树混写。

## 清单

- [ ] 已读台账并当众宣布 phase / 下一 skill / 产出路径
- [ ] 推进时按方法 skill 做完，而不是自造流程
- [ ] 硬依赖已满足（含 `ANY(...)`）或已记录 user_waiver
- [ ] 已按编排协议验证、审查、审批后写入 `deliverables/lead/`
- [ ] 交付物不是 skill 例子原文；无编造联系人
- [ ] 台账已回写；`output_dir` 在 `deliverables/lead/` 下
