---
name: marketing-orchestrator
description: >
  Use when starting marketing, SEO, or content work in this repo, when the
  user asks for the next step, 下一步, 营销, 文案, 内容, 定位, CRO, 反馈,
  底表, or any multi-step marketing workflow with dependencies or gates, or
  when the operator reports a real action is done (点完了, 发了, 上线了),
  or when the operator comments on a draft (改一下, 这句不对, 可以了).
  Read state/marketing-status.md first, read feedback with
  scripts/next_step.py, pick one action by docs/feedback-rules.md, pass the
  evidence gate, revise outgoing copy with the operator until they say
  it is fine, tell the operator, update the ledger. Use this navigator
  rather than a parallel workflow. Greetings get a phase recap only.
---

# 营销编排（导航）

读台账，读反馈，挑一个动作，过证据闸，对外文字和操作者一起改到满意，说给操作者，回写台账。方法在方法 skill 里，规则在 `docs/feedback-rules.md`，依赖与产出路径在 `references/dependency-graph.md`。

两种模式，记在台账 `mode`：

- **冷启动**：按下表 phase 0–7 打底。每次「下一步」也读反馈；反馈命中 P1、P2 时先做反馈动作。
- **运营**：phase 7 做完后转入，不 stop。每次「下一步」完全由反馈规则决定。

## 步骤

1. **读台账** `state/marketing-status.md`（获客台账 `state/lead-status.md` 不读不写）。完成：能报出 `mode`、`phase`、`next`、`method_skill`、`output_dir`、`product_context`、`feedback_read_at`、`current_action`。
2. **分流**。
   - 推进意图（下一步 / 营销 / 文案 / 内容 / 价值主张 / SEO / CRO / “Do the next step…”）→ 步骤 3。
   - 操作者报告做完了一件真实的事（「点完了」「发了」「上线了」）→ 步骤 6。
   - 操作者对一份稿子提意见、或说「可以了」→ 步骤 5「审稿」那一条，接着上次那份稿子改。
   - 寒暄或无关问题 → 复述 `mode`、`phase`、`next`，停，不改文件。
3. **读反馈**。跑 `uv run scripts/next_step.py --line 营销 --format json --since "<台账 feedback_read_at>"`（`feedback_read_at` 为空就不带 `--since`）。它读底表、按 `docs/feedback-rules.md` 对规则、排好优先级，只留营销线的对象（营销线的登记、没登记过的全站页面、没归因的询盘）。不要自己读表格、不要手抄数据。完成：拿到 `actions`（已排序）、`ledger`、`waiting`、`data`。
   - 脚本报错（没网、凭据缺、表格读不到）：如实说读不到反馈和原因。冷启动照常做阶段工作；运营模式停，写缺口。
4. **挑一个动作**（规则第 7 节）。
   - 冷启动，`actions[0]` 是 P1 或 P2 → 本轮做这个反馈动作。
   - 冷启动，其余情况 → 本轮做阶段工作（按下表，从台账 `phase` 接着做），再顺带说一句最高的那件反馈和还有几件在排队。
   - 运营，`actions` 不空 → 本轮做 `actions[0]`。
   - 运营，`actions` 为空（只剩 P5）→ 按「运营里只剩记账时」挑一项新工作；挑不出就说「今天没有要动的」和在等什么，停。
5. **做这个动作**。
   - 反馈动作：照该条的「AI 会做的」做，有方法 skill 就先读它的 `SKILL.md`。要改新站的，按新站仓库 `AGENTS.md` 的规矩走分支、PR、CI；上不上由操作者决定。要发的信、要上线的文字，AI 起草后走下面的「审稿」，改到操作者满意，发不发由操作者决定，并由操作者亲手发。
   - 阶段工作：台账 `method_skill` 的 `SKILL.md` 存在 → 先读再按其步骤做；不存在 → 停，宣布缺口，不自造流程。需要隔离时 dispatch a subagent, else do it inline。产出进台账 `output_dir`（空则用下表目录）。同一 phase 无硬依赖的方法 skill 可并行，有硬依赖的串行；硬依赖没满足且没有 `user_waiver` → 不跳。
   - 交给操作者去做、去发、去上线之前，过**证据闸**（规则第 9 节，逐条打勾）。过了的交付物在 frontmatter 写 `status: approved` 和 `evidence_gate: <日期>`；`approved` 的意思就是「已过证据闸」，由 AI 自查后写，不需要操作者批准。过不了：修一轮再查；还不过就换下一个动作，并告诉操作者跳过了什么、为什么。
   - **审稿**（对外文字：页面正文、标题和描述、帖子、邮件、定位句与信息支柱等，范围见规则第 10 节）：过了证据闸，把全文给操作者看，说清这稿想达到什么、AI 拿不准的地方。操作者说哪里要改就改，每轮记进交付物「## 审稿记录」，改完重过证据闸再给看，来回几轮都行，不催。写初稿前先读写作偏好 `deliverables/marketing/00-system/writing-preferences.md`（有就读），同一类意见第二次出现时记进去。操作者说「可以了」→ frontmatter 写 `operator_ok: <日期>`；之后再改任何字就清空、重新给看。`approved` 加 `operator_ok` 才算可以发、可以上线。
   - 说给操作者：用规则第 11 节的格式（脚本的 text 输出就是这个格式，可以直接用 `uv run scripts/next_step.py --line 营销` 再跑一次拿全文）。阶段工作也按同样五栏说：为什么、你要做的、你要决定、AI 会做的、做完以后。英文只在要操作者去某个后台找按钮时出现，加括号注明。
   - 冷启动阶段里，要上线的页面、要发布的内容，在「做完以后」写明：操作者做完要告诉 AI，AI 走步骤 6 登记；发前自己又改过的，把实际版本贴给 AI。
   - 教学 / 评测 / 进化走 `skills/marketing-teach/SKILL.md`、`skills/marketing-eval/SKILL.md`、`skills/marketing-evolve/SKILL.md` 或 `skills/marketing-skill-eval/SKILL.md`；产出进 `deliverables/marketing/00-system/`，不改战役 `phase`。
6. **登记做完的事**（执行登记是 L0 的唯一来源，数据靠它挂回动作）。
   - 在 GSC 请求编入索引：`uv run scripts/next_step.py log-request --url <网址>`（一个网址一个 `--url`）。
   - AI 做完一次性核查：W-13 用 `uv run scripts/next_step.py mark --rule W-13 --url <网址> --note "<结论>"`；W-24 用 `mark --rule W-24 --id <登记编号> --note "<结论>"`。
   - 其他真实动作（上线页面、改页、发信、发帖），以及新站上线的改动：打开 `skills/marketing-execution-log/SKILL.md`，按它查证并登记。
   - 完成：说清登记了什么、编号是多少；回写台账 `current_action_log`。
7. **回写台账**（每轮都做；冷启动每个 phase 边界也做）。
   - `feedback_read_at` 写成本轮读反馈的时刻（北京时间「年-月-日 时:分」）；`current_action` 写成「规则编号 + 一句话」或「phase N：方法 skill」；`current_action_log` 写登记编号（没有就留空）。
   - 冷启动：YAML、「当前」表、「已完成」与磁盘一致；`next` 指向下一动作。下一方法 skill 取：台账已指定且文件仍存在的；否则取下表中依赖已满足、`SKILL.md` 存在的下一个。phase 7 做完 → `mode: 运营`，`next` 写「按反馈规则给下一步」，不写 `stop`。
   - 完成：YAML 和「当前」表一致。

## 阶段（冷启动）

| phase | 名称 | 方法 skill | 产出目录 | 完成标准 |
| --- | --- | --- | --- | --- |
| 0 | 读产品上下文 | 只读 `product_context`；需要档案时打开 `skills/marketing-profile/SKILL.md` | 不把原文写入本仓库 | 三条陈述：买家、所卖、缺口 |
| 1 | 基础 | `marketing-positioning`、`marketing-competitor-intelligence`、`marketing-pricing-strategy` | `deliverables/marketing/01-foundation/` | 各方法 skill 交付物非空，不是例子原文，且过了证据闸 |
| 2 | SEO | `marketing-seo-audit`、`marketing-ai-seo`、`marketing-programmatic-seo`、`marketing-site-and-schema` | `deliverables/marketing/02-seo/` | 同上 |
| 3 | 内容 | `marketing-content-strategy`、`marketing-copywriting`、`marketing-visual-content` | `deliverables/marketing/03-content/` | 同上 |
| 4 | 获客 | `marketing-social-content`、`marketing-paid-advertising`、`marketing-email-outreach` | `deliverables/marketing/04-acquisition/` | 同上 |
| 5 | CRO | `marketing-landing-page`、`marketing-inquiry-flow`、`marketing-funnel-optimization` | `deliverables/marketing/05-cro/` | 同上 |
| 6 | 增长 | `marketing-launch-strategy`、`marketing-referral-program`、`marketing-retention` | `deliverables/marketing/06-growth/` | 同上 |
| 7 | 度量 | `marketing-analytics-and-optimization` | `deliverables/marketing/07-measurement/` | 同上 |

调研摘录可进 `deliverables/marketing/00-research/`。台账 `output_dir` 若仍是试点根 `deliverables/`，本轮照台账写。

## 运营里只剩记账时

`actions` 为空时，按顺序找一项新工作，找到第一项就做：

1. 下表方法 skill 里，交付物缺失、或没过证据闸（没有 `status: approved`）的，按依赖顺序取第一个；对外文字过了证据闸、还没有 `operator_ok` 的，拿给操作者审稿。
2. 都齐了：取 `evidence_gate` 日期最早的那份交付物，对照事实源入口重新过一遍证据闸。事实源（线上站点、新站仓库、竞品调研）有变化才改，没变化只把 `evidence_gate` 改成今天。
3. 都没有：说「今天没有要动的」，列出脚本 `waiting` 里在等的事，停。

不按点击率、回复率、询盘数挑工作，也不按日历上移（规则第 8 节）。

## 默认

- 进度只认台账；反馈只认底表（经 `scripts/next_step.py --line 营销` 读）。
- 产品事实只读 `product_context`（事实源入口 `docs/fact-sources.md`），按其指路取证；查不到标〔未证实〕，按没有处理；不在本仓库另存一份。
- 共用规则若存在则读 `skills/marketing-playbook-standards/SKILL.md`。
- 台账或 `deliverables/marketing/` 缺失时，先打开 `skills/marketing-init/SKILL.md`；该文件不存在则只报缺口。
- 缺来源、缺搜索：停止并写缺口，不编造。需要查证时用网页搜索；需要原文时抓取指定 URL 的正文。
- 交付物带来源栏；数字必须能回溯产品上下文、已抓取 URL 或底表里的某一行。
- 质量闸：执行前是证据闸（AI 自查事实）加审稿（对外文字由操作者看、提意见、改到满意，规则第 10 节），执行后是反馈闸（看 L1–L3）。事实对不对、行业里该怎么做不靠操作者判断；文字发出去行不行、哪里想改，由操作者说了算。
- 单文件、无并行机会的工作 inline 做完，不 dispatch。
- 证据闸没过：修一轮，或记录 `user_waiver`（台账「豁免」表）。自动修补不超过 3 轮，其后把决策交还操作者。
- 获客树 `deliverables/lead/` 不由本 skill 推进；获客线的反馈（外展邮件的回信、退信、挂在获客登记上的询盘）由 `skills/lead-generation/SKILL.md` 用 `--line 获客` 读，`--line 营销` 不会给出这类动作。
- 每天早上另有一份自动的「下一步」送到操作者的「提醒事项」和邮箱（规则第 12 节），和本 skill 用同一个脚本、同一套规则。操作者说「下一步」时以本轮现读的为准。

## 产出

推进时当众宣布：

```markdown
- mode:
- phase:
- phase_name:
- method_skill:
- output_dir:
- product_context:
- feedback: <脚本 data 那一行；最高的一件反馈及其优先级>
```

然后按规则第 11 节说「下一步」。回写格式见台账「回写」节。不要写仓外路径，不要建外部产出根。

## 例子

> 仅供理解，禁止引用到输出。

本 skill 是编排导航，例子教流程形状不教营销内容，无对应事实源材料可借，保留通用支架。

用户说「下一步」。台账 `mode: 冷启动`、`phase: 1`。跑脚本，`actions[0]` 是 P3（全站页面的正式地址不一致），不是 P1、P2，所以本轮做 phase 1 的方法 skill；说完阶段工作后补一句「反馈里最高的是 P3：某页正式地址不一致，另有 2 件排队」。下一次跑脚本，`actions[0]` 变成 P1（有人回信要报价），本轮先起草回信，阶段工作排在后面。操作者说「发了」，AI 查证后登记。用户说「你好」只复述 `mode`、`phase`、`next`，不改文件、不跑脚本。

## 易错

- 未读台账就开跑，或另写一套阶段。
- 不跑脚本，凭记忆或手抄表格说反馈。
- 冷启动时 P1、P2 反馈排在阶段工作后面；或 P3–P5 反馈挤掉阶段工作。
- phase 7 做完写 `next: stop`，没有转入运营。
- 把操作者点头当成事实核查（事实归证据闸）；或反过来，对外文字没给操作者看、没改到满意就当成可以发。
- 只给一稿就让操作者选「发 / 不发」，不接受修改意见；操作者提了意见却没记进审稿记录，同类意见不进写作偏好。
- `operator_ok` 之后又改了字却没清空、没重新给看。
- 没过证据闸就写 `status: approved`。
- 操作者说做完了，却没有登记。
- `product_context` 读不到仍往下做。
- 硬依赖缺失且无 `user_waiver` 时跳步。
- 方法 skill 文件不存在时自造步骤。
- 把产品上下文原文拷进本仓库。
- 把 skill 例子原文写入交付物。
- 教学/评测改了战役 `phase`。
- 寒暄时改文件。

## 清单

- [ ] 已读台账并当众宣布 mode / phase / 下一 skill / 产出路径 / 反馈
- [ ] 反馈经 `scripts/next_step.py` 读出，动作按规则第 7 节挑
- [ ] 推进时按方法 skill 做完，而不是自造流程
- [ ] 交给操作者的东西过了证据闸；`approved` 只在过闸后写
- [ ] 对外文字经操作者审稿、改到满意，有审稿记录和 `operator_ok`；发前自改的已同步成实际版本
- [ ] 「下一步」按规则第 11 节说，引用了底表的具体数据（哪页、哪天、什么状态）
- [ ] 操作者做完的事已登记（底表写不进时进了台账「待补登」）
- [ ] 硬依赖已满足或已记录 user_waiver
- [ ] 交付物不是 skill 例子原文
- [ ] 台账已回写（含 `feedback_read_at`、`current_action`）
