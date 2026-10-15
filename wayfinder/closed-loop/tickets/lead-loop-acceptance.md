---
wayfinder: task
status: open
assignee:
step: 7
blocked_by: [lead-loop-orchestrator, mailbox-pullback, activation-list-intake, l3-pullback]
---

# 获客线闭环验收

## Question

（HITL）用真实动作走一遍获客线：从激活名单里一家已调研的公司出发 → 产出外展信 → 操作者手动从 chester@ 发出 → 口述 → AI 在已发送里查证并写执行登记 → 送达 / 回复回流底表与看板 → 操作者说「下一步获客」→ AI 引用这条数据给出一个动作（有回复 / 无回复 / 退信各自合理）。

- 失败的环节当轮修，修不了的切新票并在本图登记。
- 证据存 vault；公开仓库只记「通过 / 不通过 + 环节」。

## 完成标准

- 一封真实发信能沿链追到底表、看板与 AI 下一步，且下一步可回溯到规则。

## 获客编排交接（「获客编排改循环」关票时写入，2026-10-15）

- **「下一步获客」**：按 `skills/lead-generation/SKILL.md` 走。脚本是 `uv run scripts/next_step.py --line 获客`，会话里先用 `--format json`，再按第 11 节说给操作者。
  - 冷启动下，只有 P1、P2 插队（真人回复 M-01 到 M-03 是 P1；永久退信 M-05、到期的下一封 M-11 是 P2）。P3–P5 让位给阶段工作，只顺带报告。
  - 验收要看三种情况：有回复 → M-01/M-02/M-03（P1）；无回复 → M-11（到期，P2）或 M-12、M-13（P5，只记账）；退信 → M-05（P2）或 M-06（P5）。
- **基线**：2026-10-15 16:31 在真实底表上，获客线 0 条登记、0 条邮件反馈、0 条询盘。输出是「今天没有要动的」，并列出在等的三样（原文见「获客编排改循环」Resolution）。验收时这三条应该变成引用具体登记编号、事件日期的动作。
- **登记那一环**：发信后按 `skills/marketing-execution-log/SKILL.md` 登记，必须带 `--line 获客`、`--company`、`--sequence S-公司名`、`--nth`。最好再带 `--planned` 和 `--next-date`，不带的话无回复时只会落到 M-13，只记账。编号写进获客台账的 `current_action_log`。
- **台账**：每轮都要回写 `feedback_read_at`、`current_action`、`current_action_log`。验收时可以对一下，营销台账没有被改。
- **询盘**：没归因的询盘两条线都会报告。只有填了「归因登记编号」、并且指向获客登记的，才只出现在获客线。

## 审稿交接（「操作者审稿」关票时写入，2026-10-15）

- 「产出外展信」这一步要走审稿（`docs/feedback-rules.md` 第 10 节）：初稿过证据闸 → 给操作者看 → 按意见改到操作者说「可以了」（`operator_ok`）→ 操作者从 chester@ 手动发出。审稿至少一轮，记录留在交付物里。
- 操作者在邮箱里发前又改过的，登记时把实际发出的版本同步回交付物，否则邮箱回流在「已发送」里对上的和交付物不是同一份字。
- 有回复时，回信（M-01–M-03）同样先审稿再发。

## 不代发（用户 2026-10-15 写入）

- 验收时确认：这一轮对外文字全部由操作者亲手发出，AI 没有代发、代发布或在任何工具里建活动 / 排期；交付物的 `send_status` / `publish_status` 为 `copy_only`，发没发以执行登记为准。`python3 evals/validate_project.py` 会拦 skill 里的代发口子。

## 激活名单交接（「激活名单入口」关票时写入，2026-10-15）

- **从哪家出发**：名单里已调研的是 `L-0002`，调研文件在 vault `deliverables/lead/02-companies/activation/L-0002.md`，`approved`，结论 `可接触`。
  - 查名单原行：`uv run scripts/activation_list.py show --id L-0002`。
  - 再要别家：`uv run scripts/activation_list.py progress` 给下一家，下一家是 L-0021（priority 1）。
- **公司名写法**：执行登记的 `--company` 和 `--sequence S-公司名`，都照名单 CSV 的 `company_name` 原文，和调研文件的标题、表行一致。官网或 Creditreform 上的其他写法只记在调研文件里，不用。
- **外展前还缺什么**：依赖图里 `lead-cold-email-gen -> [lead-icp-analysis, lead-usp-extraction]` 没改，而获客台账还在 phase 0，这两份都没有。所以写外展信之前，二选一：
  - 先把 phase 1 的 ICP、phase 4 的竞品分析、phase 5 的 USP 做到 `approved`；
  - 或者操作者明确同意跳过，记进获客台账「豁免」表。
- **联系人**：`lead-contact-discovery/list -> [lead-company-research/list]`，从名单取，`data_source` 指回名单行。名单里约 1612 行是免费邮箱（gmx、gmail、web.de 等），照录，在采集报告里列出。L-0002 的调研结论里写了接触前要知道的两点（细节在 vault 调研文件「结论」节）：它现在经一家电气批发商拿材料和方案支持；它用哪家的逆变器或储能〔未证实〕。
- **隐私**：名单有约 8 千人的姓名、邮箱、电话，只在私有 vault。验收证据里写编号，不写人名或邮箱。
