# 底表

底表是一本 Google 表格，存放执行登记和反馈分级的数据（术语见 `CONTEXT.md`）。脚本和 AI 往里写，操作者阅读，看板（Looker Studio）也从这里取数。本页只写角色名；表格链接和 ID 记在私有 vault 的 `deliverables/marketing/00-system/base-table.md` 里。

## 两本表

| 表 | 用途 | 数据 |
| --- | --- | --- |
| 底表 | 正式数据。看板和 AI 的「下一步」只读这一本 | 由脚本和 AI 写入；`build` 从不清数据行 |
| 底表（样例） | 给人看懂表的样子，也给后续脚本票当对照 | 全是假数据；每次 `build --target sample` 都整页重写 |

两本表都由 `所有者账号` 持有，并以编辑者身份共享给 `日常账号` 和 `服务账号`。服务账号自己不建文件，因为它没有 Drive 存储配额，所以表格由人建好后再共享给它。

## 表结构

正典是 [`schemas/base-table.schema.json`](../schemas/base-table.schema.json)。每个工作表对应一个定义，属性的顺序就是列的顺序，属性名就是中文表头。每列还标注了这列是什么、从哪来、谁写、示例和空值含义。要改列，先改这个文件，再重新 `build`。

工作表依次为：首页；执行登记、网页收录、网页表现、搜索词、邮件反馈、询盘、动作进度；每张数据表后面紧跟一张同名的「说明」页。时刻列一律北京时间（`年-月-日 时:分`）；网页表现、搜索词的日期按 Google 的太平洋时间切日。列一律摆开、往细里分（操作者要清晰详细，不要合并）。

| 工作表 | 一行代表什么 | 不重复键 | 级别 |
| --- | --- | --- | --- |
| 执行登记 | 一次手动动作（动作大类 + 动作，清单在 schema 里，不够用先记「其他」） | 登记编号 `E-YYYYMMDD-NN` | L0 |
| 网页收录 | 一个网址的一次收录检查（URL Inspection）：收录结论 → 收录状态（中文细分）→ 英文原文三层，加和上次比、四个原因分项与一句原因说明 | 检查日期 + 网址 | L0 / L1 |
| 网页表现 | 一个网址一天的搜索数据（Search Analytics），按搜索类型 × 国家 × 设备分开 | 日期 + 网址 + 搜索类型 + 国家 + 设备 | L1 / L2 |
| 搜索词 | 同上再细分到搜索词；因隐私丢行，合计小于网页表现 | 日期 + 网址 + 搜索词 + 搜索类型 + 国家 + 设备 | L1 / L2 |
| 邮件反馈 | 一封已登记邮件上发生的一件事 | 登记编号 + 事件类型 + 回信 Message-ID | L0 / 未到 L1 / L1 / L2 |
| 询盘 | 一笔形式发票申请；状态变化时原地更新这一行 | 询盘内部编号 | L3 |
| 动作进度 | 执行登记的一行，汇总它目前走到哪一级 | 登记编号 | 汇总 |

## 归因锚

所有反馈都按登记编号接回某次动作：

- 网页类（网页收录、网页表现、搜索词）：按网址到执行登记的「网址」或「旧网址」里找，取执行日期不晚于数据日期的最近一条。站点地图里从未登记过的页面，编号留空，只用于看全站情况。
- 邮件类：执行登记的「邮件 Message-ID」与来信的 `In-Reply-To` / `References` 对上。对不上任何登记的来信不进表。
- 询盘：AI 有证据时才填「归因登记编号」，并在「归因依据」里写明凭什么。没有证据就留空（未归因）。未归因的询盘照样计入北极星，但不计入任何一次动作的成效。
- 动作进度由脚本在每次回流后整表重算，算法就是 `scripts/base_table.py` 里的 `action_progress`。

## 隐私

公司名可以进表。人名、邮箱地址、电话、地址、邮件正文、询盘备注和 IP 都不进表，读取时在内存里丢弃。询盘只保留「询盘数据从哪读」那张票定下的最小集合。回信只记 Message-ID、公司、日期和分类，不放正文。

## 脚本

脚本是 [`scripts/base_table.py`](../scripts/base_table.py)：一个文件，用 `uv` 运行，依赖写在文件头里（PEP 723）。任何能执行 shell 的 harness 都用同一条命令跑。

```sh
uv run scripts/base_table.py check --target main     # 核对表结构与 schema 一致，不一致退出码 1
uv run scripts/base_table.py build --target main     # 建/补正式底表结构，可重跑，不动数据行
uv run scripts/base_table.py build --target sample   # 重建样例表（假数据整页覆盖）
uv run scripts/base_table.py xlsx                    # 生成 templates/base-table-sample.xlsx
```

配置都放在两个仓库之外，后续的回流脚本也照这个约定读：

- 凭据：先看 `GOOGLE_APPLICATION_CREDENTIALS`，没有则用 `~/.config/de-linker-playbook/service-account.json`（权限 600）。
- 表格 ID：先看 `PLAYBOOK_CONFIG`，没有则用 `~/.config/de-linker-playbook/config.toml`（权限 600），格式如下：

```toml
[base_table]
spreadsheet_id = "..."         # 底表
sample_spreadsheet_id = "..."  # 底表（样例）
```

回流脚本复用 `base_table.py` 的读写层：`google_service`、`read_table`、`upsert_rows`（按不重复键新增或覆盖；内容没变的行不碰）、`replace_rows`、`refresh_progress`（按网址重挂登记编号，再重算动作进度）。写行一律写到固定行号，不用 `values.append`。所有接口调用都设了超时，遇到 429、5xx 或网络超时会自动重试。

## GSC 回流

[`scripts/gsc_pull.py`](../scripts/gsc_pull.py) 负责把 Search Console 的数据写进三张表：网页收录、网页表现、搜索词。写完这三张表后，它会重算一次动作进度。

```sh
uv run scripts/gsc_pull.py run                # 跑一次
uv run scripts/gsc_pull.py run --dry-run      # 只取数、打印条数，不写表
uv run scripts/gsc_pull.py schedule install   # 装每日定时（这台 Mac 的 launchd，每天 08:30）
uv run scripts/gsc_pull.py schedule status    # 看装没装、上次退出码、日志最后几行
uv run scripts/gsc_pull.py schedule remove    # 卸掉定时
```

- **网页收录**：先查执行登记里的网址（含旧网址），再查站点地图里的网址。每个网址每天查一次；当天已经有那一行，就不再查。每天最多查 1900 个，官方上限是每站每天 2000 个。
- **网页表现、搜索词**：每次取最近 10 天的数据（按太平洋时间），取的时候带上还没定稿的数据。最近几天的数先写成「初步」，之后的运行会用「定稿」数覆盖同一行。Google 有几处不给拆分：
  - Discover 的数据不按设备拆，「设备」列写「不区分（Discover 不给设备）」。
  - Discover 和 Google 新闻不给搜索词，所以搜索词表里没有这两类。
- **耗时**：收录检查一个一个查，Google 每次要几秒才回。2026-10-14 首跑查 297 个网址，用了约 38 分钟。偶尔 Google 会回「内部错误」（500），脚本自动重试 5 次仍失败，就把这个网址记进日志，第二天再查。
- **日志**：定时运行时写到 `~/Library/Logs/de-linker-playbook/gsc-pull.log`。哪一步出了错，日志里会写明，退出码不为 0，`schedule status` 能看到。
- **断档**：Mac 睡眠时，launchd 会在唤醒后补跑；关机那天就跳过。搜索数据每次重取 10 天，所以断几天会自己补上。收录检查补不回来，那几天就没有行。
- **容量**：一本 Google 表格最多 1000 万个格子。网页收录每天大约 300 行 × 18 列，一年约 200 万格，是最大的一张。总量接近上限时，要把旧数据移到存档表里（见地图「Not yet specified」）。

`build` 每次都整页重写首页和各「说明」页。数据表只重写表头、格式、下拉、冻结行和列宽。若某张数据表已经有数据，而表头又与 schema 不同，`build --target main` 会停下来报错，不会覆盖；这种情况需要手动迁移。所有数据单元格都设为纯文本（数字列除外），日期和编号不会被表格自作主张改格式。

## 翻译对照

Google 接口给的英文原值（coverageState、robotsTxtState、indexingState、pageFetchState、搜索类型、设备、国家代码）怎么翻成表里的中文，写在 schema 对应列的 `x-map` 里，收录状态的含义与所属结论写在 `x-states` 里。回流脚本用 `scripts/base_table.py` 的 `translate_inspection`、`compare_with_previous`、`translate_search_row` 照这些对照翻译。国家对照覆盖 ISO 3166 的全部 249 个三字母代码：中文名取自 ISO 3166 的简体中文译名，其中韩国、朝鲜和港澳台改用常用叫法；Google 判断不出国家时给的 `zzz`，表里写「未知」。对照表里英文的确切写法以首次真实调用为准，对不上的落到「不在对照表里（看英文原文）」。
