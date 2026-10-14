---
name: lead-linkedin-topic-research
description: >
  Use when LinkedIn topic research, LinkedIn content ideas, topic
  list, 话题研究, 内容选题, LinkedIn 选题, 领英话题,
  what to post on LinkedIn, trending B2B topics, angle research, or
  planning what to write before drafting, including phase 8 LinkedIn
  of this repo's lead run. Rank ICP-first high-engagement topic
  angles from a 1-2 year window; output is a ranked topic list with
  rationale, not a finished post. Read the fact-source entry docs/fact-sources.md and approved ICP; verify
  trends with web search; invent no engagement rates. Distinct from
  all lead-linkedin-* post-writing skills. Not for writing post
  copy, multi-platform calendars, publishing, email outreach, or
  phase navigation.
---

# LinkedIn 选题调研（ICP 优先）

为指定 ICP 找出近 1–2 年可核验的高互动选题与角度，写成排序清单，落到 `deliverables/lead/08-linkedin/`。本 skill 只产话题卡，不写成品帖、不发布。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。

2. **输入与闸门**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。硬依赖：`deliverables/lead/01-icp/icp-analysis.md` 的 `status` 为 `approved` 或 `approved_with_concerns`，或台账已记 `user_waiver`。未批准 → 停，打开 `skills/lead-icp-analysis/SKILL.md`（存在则按其做）；不编 ICP。本 skill 无软依赖。圈定三项：品类/利基、目标市场、ICP 角色。仍缺则打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则停并只要这三项。完成：能指出三项各依据哪几条；原文不拷进本仓库。

3. **采集**。按 `references/methodology.md` 的四路意图用网页搜索查证：行业趋势、买家痛点与抱怨、公开内容讨论、法规与市场变化。查询年份取环境当前公历年；窗口为当前年与上一年。字段取步骤 2，不把查询模板抄进交付物。产地/供应路径只取产品上下文，不预设某一出口国。需要原文则抓取指定 URL。LinkedIn 结果页登录墙或搜不到公开互动数据 → 改用行业媒体、买家论坛、法规原文，不编「高互动帖」。搜索不可用则停止并写缺口，不编造趋势。概念型最低查证见 `skills/lead-generation/references/search-protocol.md`：至少 5 次网页搜索，且四路各至少 1 次有用结果；不够则再搜，仍不够按实有证据写缺口，不空搜凑次数。多页需要隔离时 dispatch a subagent, else do it inline。完成：四路各有 URL、访问日期与摘录，或该路已标缺口。

4. **筛选**。每条候选必须通过 `references/methodology.md` 的 ICP 三问（至少一问）与换品类测试（把利基换成无关品类后选题仍成立 → 丢弃）。时效必须落在 1–2 年窗口，并有来源年份。卖家新品发布、纯功能清单、无证据争议、点名攻击对手，一律丢弃。完成：保留表每条能指回至少一条来源；丢弃表有原因。

5. **编制话题卡**。对保留候选写六字段：选题标题（英文）、角度（五类之一）、回答的 ICP 问、此刻为何成立、建议帖类型、Hook 草稿（一句英文开场）。角度、帖类型与排序规则见 `references/methodology.md`。目标 8–10 条互不相同的已验证话题。角度须多于一类，禁止全是揭误区；目标覆盖 3 类，来源撑不起则按实有类数写缺口，不硬编角度。搜不够 → 按实有已验证条数交付并写缺口，不用未验证条凑满。搜索对某候选零相关结果 → 标 `unverified`，不进主名单。Hook 只是测停滑的一句开场，不是成品帖；成品帖规范见 `skills/lead-generation/references/linkedin-post-guidelines.md`，本文件不写帖、不发布。完成：主名单每条六字段齐全；未验证条（若有）进附录且带旗标。

6. **落盘**。按「产出」写入 `deliverables/lead/08-linkedin/topic-research.md`。策略与筛选说明用中文；标题与 Hook 用英文（用户本轮点名其他语种除外）。必须含搜索日志。完成：主文件非空；教学支架原文零出现。

## 默认

- 共用规则若存在则读 `skills/marketing-playbook-standards/SKILL.md`。
- 产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理；不在本仓库另存档案。
- 产出只进 `deliverables/lead/08-linkedin/`。Markdown only，不写 Excel。
- 查证用网页搜索；需要原文时抓取指定 URL。缺搜索则停止并写缺口，不编造。
- 本 skill 是十条 `lead-linkedin-*` 帖类型 skill 的上游选题；建议帖类型只点名对应 `skills/lead-linkedin-*/SKILL.md`，不代写帖骨架。下游闸门以各帖类型 skill 为准。
- 多平台日历或战役走 `skills/marketing-social-content/SKILL.md`（文件存在时）；本 skill 只产 LinkedIn 选题卡。
- 不发布。发帖由用户自行发布或经用户已配置的工具发布。
- 不承诺点赞、评论或曝光率。排序只按 ICP 贴合、来源条数、角度多样性。
- 数字、法规、趋势必须带来源名、URL、年份、访问日期。钩子里的数字同此；来源没有数字就不用数字钩。
- 进度只认台账。落盘后的验证、六维审查、用户审批由编排器按 `skills/lead-generation/references/orchestration-protocol.md` 做。
- 单文件、无并行机会的工作 inline 做完，不 dispatch。

## 写法

- 用买家视角选题，不用卖家视角。「我们上新了」丢掉；接到该 ICP 的风险、KPI 或相对对手的可见落后才留。
- 具体优于宽泛：选题应同时绑利基、应用场景、目标市场，使换品类测试会失败。
- 优先五类互动角度（方法约定，不是平台承诺的互动率）：揭误区、前后对比、短案例、清单/决策框架、买家真实抱怨。
- 可负责任地挑战常规，但争议必须有来源；无证据的耸动标题不进主名单。
- 不写该 ICP 不具备的深技术；不点名攻击对手；不把产品功能清单伪装成话题。
- 常青套话、空「AI 将改变一切」、无行业锚点的励志内容，一律不写。

## 产出

主文件 `deliverables/lead/08-linkedin/topic-research.md`。字段说明见 `references/methodology.md`。

```markdown
# LinkedIn 选题 — {利基} × {市场}

- source: 台账 product_context（不粘贴原文）
- upstream: deliverables/lead/01-icp/icp-analysis.md
- accessed:
- window:
- icps:

## 摘要

## 主名单（已验证）

### T1. {英文标题}

- angle:
- icp_question:
- icp_ref:
- why_now:
- suggested_post_skill:
- hook:
- sources:

## 丢弃

| topic | 原因 |
| --- | --- |

## 未验证附录

## 缺口

## 搜索日志
| # | Capability | Query/URL | Results | Useful | Notes |
|---|------------|-----------|---------|--------|-------|
Total: N calls, M useful
```

断言（未满足则不算全量完成）：

- 主名单每条六字段齐全，且 `sources` 至少一条可打开 URL
- 主名单条数为 8–10，或少于 8 且「缺口」写明差几条、缺在哪一路查询
- 主名单角度多于一类；目标 3 类，不足则缺口写明
- 搜索日志四路意图均有记录
- 教学支架原文零出现

## 例子

> 仅供理解，禁止引用到输出。

「缩短交期、品质可靠」不能当选题，消费端那种「这台适不适合我家 / 在哪买 / 字母什么意思」也不能——那是 C 端 SEO FAQ 反模式，换品类仍通顺，也不是贸易买家在论坛里问的事。输入写批发店 FAQ 的登录/购物车问，或厂家 FAQ 标题墙（问很多、当页不答、点进去才进知识库/工单），不要编成高互动帖。要改成该 ICP 在目标市场近 1–2 年能核验的主题簇：卖家可不可信、交期是否被改口、票流转有没有人对上、到货损谁认、保修找批发还是厂家。同档批发店共用一套交易问、技术问转厂家——这是问句类型密度，不是按型号填空。业主/自装帖再热闹也不进安装商主名单。每条带来源。完整正反形状见 `references/examples.md`。不要把本节句子粘进交付物。

## 易错

- 未读已批准 ICP 就选题，或自己编画像。
- 用模型记忆填趋势、法规或「高互动」。
- 用未验证条凑满 8–10。
- 五类角度硬编齐，尤其是来源里没有的前后对比数字。
- 把卖家上新、功能清单写成话题。
- 点名攻击对手，或无来源的争议标题。
- 预设某一出口国或某一电商平台。
- 把 Hook 草稿写成成品帖，或接着去发布。
- 把 skill 例子原文写入交付物。
- 承诺点赞率、评论数或曝光。

## 清单

- [ ] 已读共用规则、`product_context` 与已批准 ICP；原文未拷进本仓库
- [ ] 四路查询已做；至少 5 次网页搜索；每条有用结果有 URL 与日期
- [ ] 主名单每条通过 ICP 三问与换品类测试；有 1–2 年窗口来源
- [ ] 主名单 8–10 条已验证，或已写实际条数与缺口；未用 `unverified` 凑数
- [ ] 角度多于一类；目标 3 类或缺口已写明；每条有建议帖类型与一句 Hook
- [ ] 无编造互动率；无点名攻击；无教学例子原文
- [ ] 文件在 `deliverables/lead/08-linkedin/topic-research.md`
- [ ] 未写成品帖、未发布
