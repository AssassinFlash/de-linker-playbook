---
wayfinder: task
status: open
assignee: claude-code-fact-source-entry (同会话续) 2026-10-14
step: 0
blocked_by: [fact-source-entry]
---

# 台账拆两线

## Question

（AFK）把共用的 `state/status.md` 拆成营销、获客两张台账，各管自己的冷启动阶段与下一步（裁定 Q3），消除「跑一次获客就覆盖营销进度」（审计 #4）。

- 两张台账的文件名与键自定；获客台账补全 phase 0–10 与审批 / 过期状态（现只存在于交付物 frontmatter，见 `skills/lead-generation/references/write-protocol.md`、`orchestration-protocol.md`）。
- 改读写方：`AGENTS.md`「台账」节、`skills/marketing-orchestrator/**`、`skills/lead-generation/**`、`skills/marketing-init/SKILL.md`、`docs/`、`evals/` 中引用台账路径处。
- **只拆不改流程**：瀑布 → 运营循环、证据闸 / 反馈闸是「营销编排改循环」「获客编排改循环」的事；本票不加循环字段，免得两次改形。执行登记与反馈数据也不进台账——它们在底表（Google 表格），台账只记阶段与下一步。
- 迁移现有进度（营销 phase 0 未开始；获客无进度）。

- 依赖已清（2026-10-14）：「事实源入口」已关，本票可以动两个编排 skill 与 `state/status.md` 了。那张票只改了 `product_context` 的值（现为 `docs/fact-sources.md`）和 `next` 的措辞，键名与台账结构没动；拆台账时两张新台账都保留 `product_context: docs/fact-sources.md`（`evals/validate_project.py` 会检查这个键）。

## 完成标准

- `grep -rn "state/status.md"` 在 `skills/ AGENTS.md docs evals` 里只剩指向新文件的引用（或旧文件已删除、引用为 0）。
- 冷启动演练：分别对两条线说「下一步」（本会话内联模拟即可），各自只读写自己的台账，另一张不变。

## 交接

- 新台账文件名与键名，关票时写进「营销编排改循环」「获客编排改循环」「执行登记流程」三张票正文。
