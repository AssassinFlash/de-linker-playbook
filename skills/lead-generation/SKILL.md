---
name: lead-generation
description: >
  Use when starting B2B lead generation, 获客, 客户开发, ICP, 找客户,
  分销商调研, 联系人采集, 冷邮件, 开发信, 外展, LinkedIn 获客, 定向开发,
  when the user asks 下一步获客 or about 回信, 退信, 询盘, when the operator
  reports an outreach email is sent (发了), or comments on a draft (改一下,
  可以了). Read state/lead-status.md first, read lead-line feedback with
  scripts/next_step.py --line 获客, pick one action by
  docs/feedback-rules.md, pass the evidence gate, revise outgoing copy with
  the operator until they say it is fine, tell the operator, update the
  ledger. Use this navigator rather than a parallel pipeline. Greetings get
  a phase recap only. Marketing-tree work stays with marketing-orchestrator.
---

# 获客编排（导航）

读台账，读反馈，挑一个动作，过证据闸，对外文字和操作者一起改到满意，说给操作者，回写台账。方法在各 `lead-*` skill 里，规则在 `docs/feedback-rules.md`，依赖与审查清单在 `references/dependency-graph.md`，一份交付物从依赖检查到写入、过期在 `references/orchestration-protocol.md`。

两种模式，记在台账 `mode`：

- **冷启动**：按下表 phase 0–10 打底。每次「下一步」也读反馈；反馈命中 P1、P2 时先做反馈动作。
- **运营**：phase 10 做完后转入，不 stop。每次「下一步」完全由反馈规则决定。

## 步骤

1. **读台账** `state/lead-status.md`（营销台账 `state/marketing-status.md` 不读不写）。完成：能报出 `mode`、`phase`、`next`、`method_skill`、`output_dir`、`product_context`、`feedback_read_at`、`current_action`。
2. **分流**。
   - 推进意图（下一步获客 / 获客 / 客户开发 / ICP / 找客户 / 分销商 / 联系人 / 冷邮件 / LinkedIn 获客 / 定向开发 / 回信 / 退信）→ 步骤 3。
   - 操作者报告做完了一件真实的事（「发了」「发出去了」「回了」）→ 步骤 6。
   - 操作者对一份稿子提意见、或说「可以了」→ 步骤 5「审稿」那一条，接着上次那份稿子改。
   - 营销树工作 → 打开 `skills/marketing-orchestrator/SKILL.md`，本 skill 不推进。
   - 寒暄或无关问题 → 复述 `mode`、`phase`、`next`，停，不改文件。
3. **读反馈**。跑 `uv run scripts/next_step.py --line 获客 --format json --since "<台账 feedback_read_at>"`（`feedback_read_at` 为空就不带 `--since`）。它读底表、按 `docs/feedback-rules.md` 对规则、排好优先级，只留获客线的对象：执行登记「线」= 获客 的登记（外展邮件）、挂在这些登记上的询盘、没归因的询盘。不要自己读表格、不要手抄数据。完成：拿到 `actions`（已排序）、`ledger`、`waiting`、`data`。
   - `actions` 为空、`waiting` 里写着「还没有获客线的登记」或「邮件反馈还是空的」：这不是出错，是还没发过外展邮件、或「邮箱 IMAP 回流」还没接上。照 `waiting` 原话告诉操作者在等什么，按步骤 4 往下走。
   - 脚本报错（没网、凭据缺、表格读不到）：如实说读不到反馈和原因。冷启动照常做阶段工作；运营模式停，写缺口。
4. **挑一个动作**（规则第 7 节）。
   - 冷启动，`actions[0]` 是 P1 或 P2 → 本轮做这个反馈动作。
   - 冷启动，其余情况 → 本轮做阶段工作（按下表，从台账 `phase` 接着做），再顺带说一句最高的那件反馈和还有几件在排队。phase 6 之后再说一句：外展文案里还有几封在等你看、几家已经说「可以了」还没发出（见「运营里只剩记账时」第 1 条怎么数）。
   - 运营，`actions` 不空 → 本轮做 `actions[0]`。
   - 运营，`actions` 为空（只剩 P5）→ 按「运营里只剩记账时」挑一项新工作；挑不出就说「今天没有要动的」和在等什么，停。
5. **做这个动作**。
   - 反馈动作：照该条的「AI 会做的」做，有承接 skill（如 M-01 的 `lead-service-quotation`、M-11 的 `lead-followup-sequence`）就先读它的 `SKILL.md`。回信、跟进信由 AI 起草，走下面的「审稿」改到操作者满意，发不发由操作者决定，并由操作者从自己的邮箱亲手发；停序列、停用地址这类只记在外展交付物和台账里。
   - 阶段工作：台账 `method_skill` 的 `SKILL.md` 存在 → 先读再按其步骤做；不存在 → 停，宣布缺口，不自造流程。按 `references/orchestration-protocol.md` 走完依赖检查、意图确认、执行、数据验证（优先 `skills/lead-data-validation/SKILL.md`）、六维审查、证据闸、写入与下游过期。需要隔离时 dispatch a subagent, else do it inline。产出进台账 `output_dir`（空则用下表目录）。同一 phase 无硬依赖的方法 skill 可并行，有硬依赖的串行；`ANY(...)` 表示括号内至少一个 `approved` 即可；硬依赖没满足且没有 `user_waiver` → 不跳。
   - 产品上下文与已过闸的上游仍不够清楚时，先打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则把缺口写入台账，不自造访谈。
   - 交给操作者去发、去上线之前，过**证据闸**（规则第 9 节，逐条打勾；协议步骤 6）。过了的交付物在 frontmatter 写 `status: approved` 和 `evidence_gate: <日期>`；`approved` 的意思就是「已过证据闸」，和营销线同一个意思，由 AI 自查后写，不需要操作者批准。过不了：修一轮再查；还不过就换下一个动作，并告诉操作者跳过了什么、为什么。
   - **审稿**（对外文字：外展信、跟进信、回信、LinkedIn 帖、SEO 正文、引流资料等，范围见规则第 10 节；协议步骤 6）：过了证据闸，把全文给操作者看，说清这稿想达到什么、AI 拿不准的地方。操作者说哪里要改就改，每轮记进交付物「## 审稿记录」，改完重过证据闸再给看，来回几轮都行，不催。写初稿前先读写作偏好 `deliverables/marketing/00-system/writing-preferences.md`（两线共用，有就读），同一类意见第二次出现时记进去。操作者说「可以了」→ frontmatter 写 `operator_ok: <日期>`；之后再改任何字就清空、重新给看。`approved` 加 `operator_ok` 才算可以发。
   - **外展要发出**（phase 6、7 的邮件文案过闸、审稿改到操作者说「可以了」以后）：只产文案，不代发。告诉操作者发哪几封、发给哪家公司、按什么顺序；每封标明它在序列里是第几封、计划共几封、下一封计划日期（从 `lead-email-sequence-strategy`、`lead-followup-sequence` 的交付物取；交付物里没写就不代定，规则 M-13）。「做完以后」写明：发一封跟 AI 说一声，AI 走步骤 6 登记。
   - 说给操作者：用规则第 11 节的格式（脚本的 text 输出就是这个格式，可以 `uv run scripts/next_step.py --line 获客` 再跑一次拿全文）。阶段工作也按同样五栏说：为什么、你要做的、你要决定、AI 会做的、做完以后。
   - 阻塞（登录、验证码、付费审批、能力缺失）按 `references/manual-intervention-protocol.md` 请操作者接手，从当前进度续，不重头开始。
   - 教学走 `skills/lead-teach/SKILL.md`；产出进 `deliverables/lead/00-system/`，不改战役 `phase`。
6. **登记做完的事**（执行登记是 L0 的唯一来源，回信、退信、询盘都靠它挂回动作）。
   - 打开 `skills/marketing-execution-log/SKILL.md`（两条线共用），按它查证并登记。操作者发前在邮箱里自己又改过的，请操作者把实际发出的版本贴过来，交付物改成实际版本（规则第 10 节第 7 条）。外展邮件用 `--line 获客`，要备齐：收件公司、外展序列（`S-公司名`）、第几封、计划共几封、下一封计划日期、对应交付物路径；收件人姓名、邮箱地址不进表。
   - 邮件登记时查证结果是「待邮箱接入后查证」，由「邮箱 IMAP 回流」在「已发送」里找到后回填；在那之前，「下一步」会把它记在 M-15（等邮箱接上），不算出错。
   - 获客线产出的 LinkedIn 帖（phase 8）、SEO 正文（phase 9）发布后同样登记，「线」按执行登记 skill 的归线规则（网站与社媒内容归营销）；它们的收录与表现由营销编排看。
   - 底表写不进（没网、凭据缺）：先记台账「待补登」表，下次登记时补进底表，补完删行。
   - 完成：说清登记了什么、编号是多少；回写台账 `current_action_log`。
7. **回写台账**（每轮都做；冷启动每个 phase 边界也做）。
   - `feedback_read_at` 写成本轮读反馈的时刻（北京时间「年-月-日 时:分」）；`current_action` 写成「规则编号 + 一句话」或「phase N：方法 skill」；`current_action_log` 写登记编号（没有就留空）。
   - 每写入一份交付物：改「审批与过期」表里它那一行和被标 `stale` 的下游各行（协议步骤 7）。
   - 冷启动：YAML、「当前」表、「已完成」与磁盘一致；`output_dir` 落在 `deliverables/lead/` 下；`next` 指向下一动作。下一方法 skill 取：台账已指定且文件仍存在的；否则取下表中依赖已满足、`SKILL.md` 存在的下一个。phase 10 做完 → `mode: 运营`，`next` 写「按反馈规则给下一步」，不写 `stop`。
   - 完成：YAML 和「当前」表一致。

## 阶段（冷启动）

| phase | 名称 | 方法 skill | 产出目录 | 完成标准 |
| --- | --- | --- | --- | --- |
| 0 | 读产品上下文 | 只读 `product_context`；需要档案时打开 `skills/marketing-profile/SKILL.md` | 不把原文写入本仓库 | 三条陈述：买家、所卖、缺口 |
| 1 | 画像 | `lead-icp-analysis`、`lead-search-term-expansion` | `deliverables/lead/01-icp/` | 每 ICP 含画像 + 销售策略 + 数据洞察；每 ICP ≥10 个已验证术语；交付物不是例子原文；已过证据闸 |
| 2 | 公司 | `lead-company-research`、`lead-distributor-research`、`lead-retailer-research` | `deliverables/lead/02-companies/` | 目标公司每家 3 信息块；分销商 11 维或简版字段齐；零售商规模与定位字段齐；域名已抓取验证；已过证据闸。有激活名单时从名单开始（见表下） |
| 3 | 联系人 | `lead-contact-discovery` | `deliverables/lead/03-contacts/` | 按 ICP / 公司类型 / 职位分列；未配置发现服务则标「联系人待补」，不编造邮箱；名单公司的联系人以名单为准；已过证据闸 |
| 4 | 市场 | `lead-competitor-analysis`、`lead-market-analysis` | `deliverables/lead/04-market/` | 定位×代表公司 + 空白；市场 10 板块；数字有来源与年份；已过证据闸 |
| 5 | USP | `lead-usp-extraction`、`lead-product-knowledge` | `deliverables/lead/05-usp/` | 差异化方案可执行；产品知识可回溯事实源，不编造合规；已过证据闸 |
| 6 | 外展 | `lead-cold-email-gen`、`lead-warm-email-transform`、`lead-followup-sequence`、`lead-email-sequence-strategy`、`lead-magnet-gen` | `deliverables/lead/06-outreach/` | 文案非空且不是例子原文；每条序列写明计划共几封与间隔；已过证据闸；只产文案，由操作者手动发 |
| 7 | 定向 | `lead-targeted-research`、`lead-targeted-outreach` | `deliverables/lead/07-targeted/` | 调研先于外展；已过证据闸 |
| 8 | LinkedIn | `lead-linkedin-topic-research` 及各 `lead-linkedin-*` 帖类型 | `deliverables/lead/08-linkedin/` | 帖子遵守 `references/linkedin-post-guidelines.md`；已过证据闸 |
| 9 | SEO | `lead-seo-editorial-guidelines`、`lead-seo-outline-gen`、`lead-seo-content-gen`、`lead-seo-content-edit` | `deliverables/lead/09-seo/` | 规范 → 大纲 → 成稿 → 编辑，串行；已过证据闸 |
| 10 | 销售 | `lead-service-first-contact`、`lead-service-quotation`、`lead-service-objection`、`lead-service-first-order`、`lead-service-delivery`、`lead-service-retention`、`lead-buyer-psychology` | `deliverables/lead/10-sales/` | 服务链串行；心理分析可与服务链并行；已过证据闸 |

`lead-company-research` 的 emerging 产出、`lead-distributor-research` 的 brief 产出是同一 skill 的第二种交付物，不是另一个入口。归档进 `deliverables/lead/99-archive/`。

**激活名单**（`CONTEXT.md`「激活名单」）是第 2、3 阶段多一个输入来源，不是新阶段、不是新 skill。名单只在私有 vault `deliverables/lead/00-system/activation-list/`；进度跑 `uv run scripts/activation_list.py progress`，台账「激活名单」节只写数字和 vault 相对路径。phase 2 有名单时先从名单开始：按 `progress` 给的下一家，用 `lead-company-research` 的名单模式（`skills/lead-company-research/references/list-mode.md`）逐家调研，按陌生开发，先调研再接触。名单调研不设完成数、不挡 phase 推进：phase 2 其余方法 skill 达标就进 phase 3，名单剩下的公司之后逐家接着做（「运营里只剩记账时」第 2 条；操作者点名「名单下一家」随时做）。phase 3 里，`list_verdict: 可接触` 的名单公司，联系人从名单取（`lead-contact-discovery` 步骤 1）。

## 运营里只剩记账时

`actions` 为空时，按顺序找一项新工作，找到第一项就做：

1. **还没审完、还没发出的外展**：外展交付物（`06-outreach/`、`07-targeted/`）里过了证据闸、还没有 `operator_ok` 的 → 拿给操作者审稿。已有 `operator_ok` 的收件公司，在执行登记里还没有「线」= 获客、渠道 = 邮件的行（`uv run scripts/execution_log.py show` 对照「收件公司」列）。有 → 提示操作者发下一家，说清发哪封、第几封、计划共几封；没发出就不会有回信、退信，反馈规则也没有对象。
2. **缺的、没过闸的、过期的**：下表方法 skill 里，交付物缺失、`draft`、或 `stale` 的，按依赖顺序取第一个，按协议做到 `approved`。都齐了而激活名单还有没调研的公司（`uv run scripts/activation_list.py progress` 有「下一家」），就调研下一家。
3. **都齐了**：取「审批与过期」表里 `evidence_gate` 日期最早的那份交付物重过证据闸。名单类（公司、联系人）先按 `skills/lead-data-validation/SKILL.md` 重查五项；其余对照事实源入口。有变化才改，没变化只把 `evidence_gate` 改成今天。
4. **都没有**：说「今天没有要动的」，列出脚本 `waiting` 里在等的事，停。

不按回复率、零回复、询盘数挑工作，不因为没人回就追加封数或改写序列，也不按日历上移（规则第 8 节）。

## 默认

- 进度只认台账；反馈只认底表（经 `scripts/next_step.py --line 获客` 读）。产出只进 `deliverables/lead/`。营销树 `deliverables/marketing/` 不由本 skill 推进；例外是两线共用的写作偏好 `deliverables/marketing/00-system/writing-preferences.md`，本 skill 可读可追加。
- 产品事实只读 `product_context`（事实源入口 `docs/fact-sources.md`），按其指路取证；查不到标〔未证实〕，按没有处理；不在本仓库另存一份。
- 共用规则若存在则读 `skills/marketing-playbook-standards/SKILL.md`。
- 台账或 `deliverables/lead/` 缺失时，先打开 `skills/marketing-init/SKILL.md`；该文件不存在则只报缺口。
- 缺来源、缺搜索：停止并写缺口，不编造。需要查证时用网页搜索；需要原文时抓取指定 URL 的正文。
- 交付物带来源栏；数字必须能回溯事实源、已抓取 URL 或底表里的某一行。策略/分析用中文；表列名 English snake_case；公司名不翻译。
- 联系人/邮箱发现服务、网页采集服务：仅当操作者已配置（付费项须先告知并获准）；否则标「联系人待补」。外发、发布工具不接：不论是否配置、操作者是否要求，AI 都不代发信、不代发帖；一律由操作者亲手做（操作者 2026-10-15：「任何代发都不要做」）。
- 质量闸：执行前是证据闸（AI 自查事实）加审稿（对外文字由操作者看、提意见、改到满意，规则第 10 节），执行后是反馈闸（看 L1–L3）。事实对不对、行业里该怎么做不靠操作者判断；文字发出去行不行、哪里想改，由操作者说了算。
- 单文件、无并行机会的工作 inline 做完，不 dispatch。
- 审查或证据闸没过：修一轮，或记录 `user_waiver`（台账「豁免」表）。自动修补不超过 3 轮，其后把决策交还操作者。
- 网站类反馈（收录、表现、标题）不由本 skill 处理；`--line 获客` 不会给出这类动作。没归因的询盘两条线都会看到：报告一次即可，归因证据找到后填进底表，之后只出现在它那条线。
- 每天早上另有一份自动的「下一步」送到操作者的「提醒事项」和邮箱（规则第 12 节），两条线合看，和本 skill 用同一个脚本、同一套规则。操作者说「下一步获客」时以本轮现读的为准。

## 产出

推进时当众宣布：

```markdown
- mode:
- phase:
- phase_name:
- method_skill:
- output_dir:
- product_context:
- feedback: <脚本 data 那一行；最高的一件反馈及其优先级，或 waiting 里在等什么>
```

然后按规则第 11 节说「下一步」。回写格式见台账「回写」节。不要写仓外路径，不要建外部产出根。写入约定见 `references/write-protocol.md`。

## 例子

> 仅供理解，禁止引用到输出。

本 skill 是编排导航，例子教流程形状不教获客内容，保留通用支架。

用户说「下一步获客」。台账 `mode: 冷启动`、`phase: 1`。跑脚本，`actions` 为空，`waiting` 写着「还没有获客线的登记」，所以本轮做 phase 1 的方法 skill，说完补一句「获客线还没有反馈：还没发过外展邮件」。几周后 phase 6 的冷邮件过了证据闸，AI 拿给操作者看；操作者说「太客气、太长」，AI 改短改直，再给看，第三轮操作者说「可以了」，AI 告诉操作者先发哪家；操作者说「发了」，AI 按执行登记 skill 登记、报出编号。之后某天脚本 `actions[0]` 是 P1（某家回信要报价），本轮先用报价 skill 起草回信，阶段工作排在后面。用户说「你好」只复述 `mode`、`phase`、`next`，不改文件、不跑脚本。

## 易错

- 未读台账就开跑，或另写一套阶段。
- 不跑脚本，凭记忆或手抄表格说反馈；或跑脚本不带 `--line 获客`，把网站类动作当成获客的。
- 冷启动时 P1、P2 反馈排在阶段工作后面；或 P3–P5 反馈挤掉阶段工作。
- phase 10 做完写 `next: stop`，没有转入运营。
- 把操作者点头当成事实核查（事实归证据闸）；或反过来，对外文字没给操作者看、没改到满意就当成可以发。
- 只给一稿就让操作者选「发 / 不发」，不接受修改意见；操作者提了意见却没记进审稿记录，同类意见不进写作偏好。
- `operator_ok` 之后又改了字却没清空、没重新给看；操作者发前自改了，交付物还是旧版本。
- 没过证据闸就写 `status: approved`；或还在用 `approved_with_concerns`（已并入 `approved`，concerns 记在 `review_concerns`）。
- 代操作者发信；或操作者说发了，却没有登记。
- 邮件反馈还没有数时说「没人回」：那是还没接上，不是零回复。
- 按零回复追加封数、改写序列，或替序列新定封数与间隔。
- 用斜杠命令名当入口，而不打开 `skills/<name>/SKILL.md`。
- `product_context` 读不到仍往下做。
- 硬依赖缺失且无 `user_waiver` 时跳步；把 `ANY(...)` 当成必须全部通过。
- 方法 skill 文件不存在时自造步骤。
- 把 emerging / brief 当成独立入口另写流程。
- 把产品上下文原文拷进本仓库；把 skill 例子原文写入交付物。
- 编造公司、域名、邮箱或市场规模。
- 教学改了战役 `phase`。
- 寒暄时改文件。
- 营销树与获客树混写；读写了营销台账。

## 清单

- [ ] 已读台账并当众宣布 mode / phase / 下一 skill / 产出路径 / 反馈
- [ ] 反馈经 `scripts/next_step.py --line 获客` 读出，动作按规则第 7 节挑；没数据时说清在等什么
- [ ] 推进时按方法 skill 和编排协议做完，而不是自造流程
- [ ] 交给操作者的东西过了证据闸；`approved` 只在过闸后写，带 `evidence_gate` 日期
- [ ] 对外文字经操作者审稿、改到满意，有审稿记录和 `operator_ok`；发前自改的已同步成实际版本
- [ ] 「下一步」按规则第 11 节说，引用了底表的具体数据（哪家公司、哪个登记编号、哪天、什么事件）
- [ ] 外展只产文案；操作者发出的每封都已登记（底表写不进时进了台账「待补登」）
- [ ] 硬依赖已满足（含 `ANY(...)`）或已记录 user_waiver
- [ ] 交付物不是 skill 例子原文；无编造联系人
- [ ] 台账已回写（含 `feedback_read_at`、`current_action`、「审批与过期」）；`output_dir` 在 `deliverables/lead/` 下
