---
wayfinder: task
status: open
assignee:
step: 0
blocked_by: [fact-source-entry]
---

# 101 个 skill 改指新事实源

## Question

（AFK）把 `skills/` 下写死 `~/Documents/New` 的文件（「现仓库闭环缺口审计」#1：101 个；减去「事实源入口」已改的两个编排 skill 目录）全部改为指向事实源入口，缺省值与回退路径一并去掉。

- 只改指针与「从哪读事实」的指令句；方法正文不动（方法层留用）。
- 例子：已标「仅供理解，禁止引用到输出」的例子是教学支架，正文不因来自 New 而重写；但凡是让 agent **去读** New 的句子一律改指入口。若某例子写着会被当成现行事实的产品参数，改成不含具体参数的通用说法，不从新源补数字。
- 文件所有权：本票不碰 `skills/marketing-orchestrator/**`、`skills/lead-generation/**`（归「台账拆两线」与编排循环票）。
- 量大：可按目录分批；可派 subagent 执行，主会话逐批抽查 diff。

入口路径与指针写法：〔待「事实源入口」关票时写入〕

## 完成标准

- `grep -rl "Documents/New" skills | wc -l` = 0。
- `evals/` 现有校验脚本全绿；随机抽 5 个 skill 读一遍，指针读得通、无残留回退。
- 不打开 `~/Documents/New` 的任何文件。
