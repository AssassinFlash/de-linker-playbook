# de-linker playbook

v3 的 37 个营销 skill 与 lead-gen 的 43 个获客 skill，去不锈钢化、跨 harness 通用化后的自包含 playbook。方法在正典；产品事实指路不复制，只指向事实源入口 `docs/fact-sources.md`（线上站点 + 新站仓库 + 竞品调研）。

## 目录

```
skills/              正典（SKILL.md）
.agents/skills/      适配器（软链到正典）
state/               台账（营销、获客各一张）
deliverables/        产出（marketing/ 与 lead/ 双树）——软链到私有仓库 ../de-linker-vault（公开克隆者看到的是悬链，属正常：公开方法/私有数据分层）
wayfinder/           过程管理（地图与票）
schemas/             交付物 JSON Schema
templates/           产出 xlsx 模板与导出脚本
evals/               校验/评测脚本
docs/                人读说明
CONTEXT.md           词汇表
AGENTS.md            agent 入口（只指路）
```

## 当前状态

37 个 marketing skill + 43 个 lead skill（共 80）已全部迁入并通用化；终闸验收通过：80 skill 逐一对照源文件 review（3 处保真问题当轮修复）、主模型抽查 16/16、真实冒烟（site-and-schema 对 de-linker.com）产出可用、五家 harness（Kimi / Z Code / DeepSeek / OpenCode / Hermes）冷启动实测全 PASS。过程管理见 wayfinder/map.md；各家 headless 调用矩阵见 wayfinder/pilot/。

## 怎么用

- Agent：读 `AGENTS.md`，按其指路取用正典。
- 人：看本文件和 `wayfinder/map.md`。

事实从 `docs/fact-sources.md` 进。兼容目标五家：Kimi / Z Code / DeepSeek / OpenCode / Hermes。
