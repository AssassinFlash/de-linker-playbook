---
wayfinder: task
status: closed
assignee: claude-opus-5-5 会话 2026-10-15
step: 3
blocked_by: [marketing-loop-orchestrator, execution-log-flow]
---

# 获客编排改循环

## Question

（AFK）按「营销编排改循环」同一形态重写 `skills/lead-generation`：冷启动阶段（phase 0–10）走完转运营循环，「下一步」读底表（执行登记里的发信、邮件反馈、询盘）按规则挑动作；`references/orchestration-protocol.md` 的「用户审批」闸改为证据闸 + 反馈闸（审计 #8），保留 `approved` → `stale` 的下游过期传播（可留用）。

- 复用营销侧的公共读表部分，不另写一套。
- 发信是操作者手动：外展阶段产出文案后，提示操作者发出并走「执行登记流程」。
- 邮件反馈数据由「邮箱 IMAP 回流」提供；本票不等它——底表列已定，规则照写，验收时有无数据都要能给出合理下一步（无数据 → 说明在等什么）。

- 台账（「台账拆两线」关票时写入，2026-10-14）：营销 `state/marketing-status.md`、获客 `state/lead-status.md`；旧的 `state/status.md` 已删除。两张共用键：YAML `phase`、`phase_name`、`next`、`method_skill`、`output_dir`、`product_context`（值 `docs/fact-sources.md`，`evals/validate_project.py` 会检查），同样的键再列一遍在「当前」表里，另有「阶段」「已完成」「回写」各节。获客台账另有「审批与过期」表（交付物、方法 skill、status、review_date、review_score、stale_reason、stale_date；frontmatter 为准，本表是索引）和「豁免（user_waiver）」表（日期、方法 skill、跳过的硬依赖、用户原话）。营销台账没有这两张表（只拆不改）。获客的回写规则写在台账「回写」节与 `references/orchestration-protocol.md` 步骤 7：每写一份交付物，就改「审批与过期」表里它那一行和被标 `stale` 的下游各行。用户审批闸改成证据闸 + 反馈闸后，「审批与过期」表的 status 语义要一并改掉（或换列），别留两套。

## 完成标准

- 获客台账上跑一次「下一步」：输出引用底表数据或明确说明缺哪类数据；不读写营销台账。

## 规则交接（「反馈分级规则定稿」关票时写入，2026-10-15）

- 规则正典：`docs/feedback-rules.md`。编排里不要另抄一份规则，只引用它的节号和规则编号（W-xx、M-xx、Q-xx、E-xx）。
- 「下一步」的输出格式见第 11 节；冷启动阶段和反馈怎么排（P1、P2 先做，P3–P5 让位给阶段工作）见第 7 节；证据闸清单见第 9 节，写进编排步骤。
- 每天早上会自动算一次「下一步」并发出去（第 12 节，「每日提醒」票）。所以规则匹配那一部分要做成脚本：不进对话，直接在命令行输出第 11 节格式的文字，「每日提醒」票直接调用。会话里说「下一步」时，跑同一个脚本，再由 AI 过证据闸、展开讲。
- AGENTS.md 和编排 skill 里要加一处指向 `docs/feedback-rules.md` 的指针。

## 编排交接（「营销编排改循环」关票时写入，2026-10-15）

- **公共读表部分已做好**：`scripts/next_step.py`，规则文件第 1 节有用法。邮件规则 M-01–M-15、询盘 Q-01–Q-05、执行登记 E-01–E-03 已在脚本里，获客线直接用 `--format json` 的 `actions`，不另写。
- **只要获客的动作**：
  - 按 `rule` 前缀 M、Q 筛，或按 `objects` 里的登记编号去执行登记看「线」= 获客。
  - 现在脚本不分线。要按线过滤，就在脚本里加 `--line 营销|获客`，不要在 skill 里再算一遍。
- **照营销的形态写**（`skills/marketing-orchestrator/SKILL.md`）：7 步、两种模式、「运营里只剩记账时」怎么挑新工作。
- 获客台账要加同样四个键：`mode`、`feedback_read_at`、`current_action`、`current_action_log`。`evals/validate_project.py` 的 `validate_loop` 目前只查营销台账，本票把获客台账也加进去。
- **`approved` 的含义**：营销侧已改成「已过证据闸」（AI 自查后写 `status: approved` + `evidence_gate: <日期>`）。获客「审批与过期」表的 status 要用同一个意思，或者换列，别留两套。`approved` → `stale` 的下游过期传播可以保留。
- **登记**：
  - 操作者说「发了」，AI 查证后登记。
  - 「执行登记流程」定稿前，先记进台账「待补登」表（营销台账已有这张表，获客台账照加）。

## 执行登记交接（「执行登记流程」关票时写入，2026-10-15）

- **怎么登**：读 `skills/marketing-execution-log/SKILL.md`（两条线共用，名字带 `marketing-` 只因仓内命名规则）。发信登记：`uv run scripts/execution_log.py add --line 获客 --channel 邮件 --action 发出首封|发出跟进|回复对方来信 --desc "一句话" --company "公司名" --sequence S-公司名 --nth N [--planned 计划共几封] [--next-date 下一封计划日期] [--deliverable lead/06-outreach/…]`。收件人姓名、邮箱地址不进表。
- **编号**：`E-执行日期-两位序号`（例 `E-20261015-12`），按执行日期顺延、全表唯一；脚本输出里就有，写进获客台账 `current_action_log`。需要在代码里登记时调 `execution_log.prepare()` + `execution_log.register()`（`next_step.py log-request` 就是这么用的），不要另写编号。
- **邮件的查证留给「邮箱 IMAP 回流」**：登记时查证结果是「待邮箱接入后查证」，Message-ID、查证证据、查证时刻都空着，由那张票的脚本在「已发送」里找到后回填。
- **认重复**：同一天、同一公司、同一序列、同一封已有一行就不写（退出码 3）。
- **「待补登」表**：流程已定稿，这张表的意思改成「底表写不进（没网、凭据缺）时的暂存，下次登记时补进底表、补完删行」。获客台账照这个意思加，不再是「流程定稿前」。

## Resolution（2026-10-15）

- **读表**：复用 `scripts/next_step.py`，不另写。脚本加了 `--line 营销|获客`：
  - 每个对象按执行登记「线」归线；没登记过的全站页面算营销；
  - 询盘：归因了的跟它那次登记的线，没归因的两条线都看到（北极星两线共用）；
  - `--line 获客` 没有获客登记时，`waiting` 会写「执行登记里还没有获客线的登记」。
  - 不带 `--line` 时输出和改之前逐字相同（样例数据 text / plain / json 三种都比过，JSON 只多一个 `line` 键）。所以每日提醒不用改，仍两线合看。
  - 营销编排改为带 `--line 营销`。在真实底表上，`--line 营销` 和不带 `--line` 的 actions、ledger 完全相同（67 条登记都是营销线）。
- **编排**：`skills/lead-generation/SKILL.md` 按营销编排的形态重写成 7 步、两种模式。冷启动是 phase 0–10，P1、P2 插队，phase 10 做完转运营，不 stop。获客线自己加的几处：
  - 外展只产文案，由操作者亲手发。每封标明第几封、计划共几封、下一封计划日期，从序列交付物取；没写就不代定（M-13）。
  - 发出后按 `skills/marketing-execution-log/SKILL.md` 登记，带 `--line 获客`。`execution_log.py add` 默认是营销线，不带就会登错线，获客编排就看不到这一行。
  - 获客线产出的 LinkedIn 帖、SEO 正文，按执行登记的归线规则归营销，反馈由营销编排看。
  - 「运营里只剩记账时」：①提示发出已过闸、还没发的外展；②补缺失、`draft` 或 `stale` 的交付物；③重查 `evidence_gate` 最早的那份，名单类先重跑数据验证；④说在等什么。
  - 规则第 7 节改为指向这里；第 1 节加了 `--line` 用法。
- **质量闸**：编排协议的步骤 6 原来是「用户审批」，改成「证据闸」。六维审查保留，审查通过后再过规则第 9 节的清单，然后写 `status: approved` 和 `evidence_gate`。
  - `approved_with_concerns` 并入 `approved`，concern 记在 `review_concerns` 里。`status` 只剩 `approved`、`draft`、`stale`、`missing` 四种，和营销线同一套。
  - `approved` → `stale` 的下游过期传播保留，过期后要重过审查和证据闸。
  - 依赖图的状态判定、闸门、机器可读图都已同步（加了 `evidence_gate`，`version` 改成 2）。写入约定里，`approved` 和 `stale` 的文件都先归档。
  - 方法 skill 里有 4 处硬依赖口径、5 句「用户审批」，都改成了「已过证据闸」或「证据闸」。只改了措辞，方法本身没动。
- **台账**：`state/lead-status.md` 加了 `mode`、`feedback_read_at`、`current_action`、`current_action_log`，「当前」表同步加；另外加了键说明和「待补登」表（底表写不进时暂存）。
  - 「审批与过期」表：`review_date` 列换成 `evidence_gate`，`status` 的说明改成「已过证据闸」的意思。
  - 「豁免」表也包括没过证据闸、操作者明确接受的那一条。「回写」节去掉了 `stop`。
- **evals**：`validate_loop` 改成两张台账都查，查这几项：
  - 循环键齐全，`mode` 合法，`next` 不是 stop；
  - 获客编排、编排协议、依赖图、台账都指向规则、脚本（含 `--line`）、执行登记和证据闸；
  - lead skill 和获客台账里不再出现 `approved_with_concerns`；
  - 两棵交付物树里，`approved` 都带 `evidence_gate`，并且没有 `approved_with_concerns`。
  - 在仓外临时副本里造了三个反例（`mode` 非法、`approved` 不带日期、旧状态），三个都报错了。正式仓库跑 `python3 -B evals/validate_project.py` 全部通过。还有 5 条「missing support file: scripts/…」警告，是检查器按 skill 目录去找 `scripts/`，旧问题，这次不改。
- **验收：在获客台账上跑一次「下一步」**（真实底表，2026-10-15 16:31，`uv run scripts/next_step.py --line 获客`）：

  ```text
  **下一步：今天没有要动的**

  - **为什么**：底表里所有对象都只命中「只记账」的规则（P5）。
  - **你要做的**：不用你动手
  - **你要决定**：不用你决定
  - **AI 会做的**：冷启动阶段还没走完的话，接着做阶段工作；否则从方法 skill 里挑下一项新工作
  - **做完以后**：明天早上再看一次

  **只在记账的**：无
  **在等的**：执行登记里还没有获客线的登记：还没发过外展邮件，邮件规则（M-01 至 M-15）没有对象；外展文案出来、操作者发出后登记，第二天起才有可对的；询盘表还是空的：在等「询盘回流 L3」；邮件反馈还是空的：在等「邮箱 IMAP 回流」

  _只看获客线。底表数据：网页收录最新检查 2026-10-15；网页表现最新 还没有数；邮件反馈最新 还没有数；询盘最新 还没有数；执行登记 获客线 0 条（全表 67 条）。规则：docs/feedback-rules.md。生成于 2026-10-15 16:31（北京时间）。_
  ```

  编排的判断：`mode: 冷启动`，`actions` 为空，所以本轮做阶段工作，即 phase 0 `marketing-profile`；反馈那一行说明获客线在等三样数据。获客台账已回写 `feedback_read_at: 2026-10-15 16:31` 和 `current_action`。营销台账没读也没写。
  - 样例数据（`--offline-sample --line 获客`）：下一步是 M-01，回复样例公司甲的报价请求（P1）。排队的依次是：Q-01 报告 2 条询盘、M-05 停用乙公司的地址、Q-01 给 90002 找归因。网页类动作一条都没有。

