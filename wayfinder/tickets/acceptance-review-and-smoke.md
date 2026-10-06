---
wayfinder: task
status: open
assignee:
blocked_by: [overlap-dedup-adjudication, assets-migration]
---

# 验收：对照 review + 抽查 + 冒烟

## Question

三道闸，检查项以「抽取规格定稿」的验收清单为准（清单吸收研究票的 best-practice 结论）：

1. **子代理逐 skill 对照 review**：方法保真（对照源文件）、无不锈钢残留、无 harness 专属字段、例子标注在位、前缀命名正确
2. **主模型抽查 20%**
3. **真实冒烟**：挑一个导入的 skill 对一个真实 de-linker 任务跑一遍（如用 site-architecture 或 content-strategy 跑一个真实页面），产出可用即过
4. **五家兼容验证**（用户定的目标：Kimi / Z Code / DeepSeek / OpenCode / Hermes）：逐家冷启动实测，矩阵与通过标准参照试点薄片（`wayfinder/pilot/`）。先探测各 CLI 的安装与登录状态，缺环境的列出来由用户决定装不装（环境准备不算票内工作）

随本票定稿 `AGENTS.md` / `README.md` 终稿（含跨 harness 交接说明）。全部通过后地图闭环。
