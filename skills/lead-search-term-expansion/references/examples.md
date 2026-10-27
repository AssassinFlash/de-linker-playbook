# 搜索词扩展例子

> 仅供理解，禁止引用到输出。

本文全部例子都是教学支架，禁止把原文写入任何交付物。

表里的公司类型、定位语和粗热度都是示意形状，不是可引用的检索结果。货架名借同档多国店面导航的栏目结构，不是某店原句。

### 形状：已验证行长什么样

> 仅供理解，禁止引用到输出。

输入画像（示意）：德语区电气师傅行，车上写师傅行 / 电气专业店，做户用与小型工商业光伏和储能安装。目标市场德语。下面每一行都假设已经用 Apify 搜索看到匹配公司，并记下了例证 URL。`estimated_search_volume` 写成粗热度，因为本轮没有关键词工具导出；`n` 是占位，真跑时填本轮首页匹配公司数。

| icp_category | company_type | positioning_term | tone | search_keyword | estimated_search_volume | use_case |
| --- | --- | --- | --- | --- | --- | --- |
| Small installer | Meisterbetrieb | Elektro-Meisterbetrieb für Photovoltaik | Professional | "elektro meisterbetrieb photovoltaik" | autocomplete:yes; page1_companies:n | Google, LinkedIn |
| Small installer | Meisterbetrieb | Meisterfachbetrieb Elektrotechnik | Professional | "meisterfachbetrieb elektrotechnik" | autocomplete:yes; page1_companies:n | Google, 行业名录 |
| Small installer | Meisterbetrieb | Eingetragener Elektrofachbetrieb | Traditional | "elektrofachbetrieb photovoltaik" | autocomplete:yes; page1_companies:n | Google, 行业名录 |
| Small installer | Meisterbetrieb | Elektriker vor Ort für PV und Speicher | Casual | "elektriker photovoltaik speicher" | autocomplete:yes; page1_companies:n | Google |
| Small installer | PV specialist | Fachbetrieb für Photovoltaik und Speicher | Professional | "fachbetrieb photovoltaik speicher" | autocomplete:yes; page1_companies:n | Google, LinkedIn |
| Small installer | Local | Regionaler Elektroinstallateur | Casual | "elektroinstallateur photovoltaik" | autocomplete:partial; page1_companies:n | Google |

未覆盖的语气与原因（示意）：Cutting-edge → 无已验证用语。该 ICP 摘录是资格与本地，不是「智能平台」口号，不硬编一行凑齐四种语气。

观察（示意，不是交付结论）：

- Professional 适合职业网络与名录：师傅行、专业店是车上 / About 自称
- Casual 适合本地网页检索；地理尾巴留给 `search_keyword` 的 use_case，不写进定位语
- Traditional 适合行业协会名录里的「已登记专业店」
- 市场外号（安装工俗称及其活拼写）只作发现查询变体，不替代 `positioning_term`
- 年份、地区必须来自已抓取页；示意表禁止抄进交付物

### 形状：自动补全是验证，不是定位语来源

> 仅供理解，禁止引用到输出。

输入写：把「品类 + 批发」种子的补全前十（城市尾巴、「附近」、邻国地名）整表当成公司定位语。

成稿应改成：补全只作需求证据与粗热度（有没有补全、首页匹配公司数）。地理尾巴确认 Casual / 本地 `use_case`，不把「批发 + 城市」写入 `positioning_term`。该形状匹配师傅行 ICP；规划总包 / EPC 另采，不复用同一份补全。品牌 + 品类 + 经销、以及「逆变器 + 电池 + 兼容」，是找货或配对查询，也不是公司自称。

### 形状：同一货架四国四名

> 仅供理解，禁止引用到输出。

同档批发店多国店面把同一货架写成四国四名（示意结构，不是检索结果）：

| 货架 | DE | NL | IT | PL |
| --- | --- | --- | --- | --- |
| 户用储能 | Heimspeicher | Batterijopslag thuis | Accumulo domestico | Magazyny energii |
| 工商业储能 | Gewerbespeicher | Batterijopslag bedrijven | Accumulo per il commerciale | Komercyjne akumulatory |

输入写一个英语伞词（battery storage company）覆盖四国。成稿应改成：每个目标市场一张属性卡、一套本国货架名与自称；`search_keyword` 跟该市场用语。不要机器映射，也不要用英美电表前后场黑话替换本国货架名。

### 形状：哪些候选必须丢掉

> 仅供理解，禁止引用到输出。

| 候选 | 丢掉原因 |
| --- | --- |
| 手工艺名录分类号 / 政府采购分类代码 | 分类学名，公司不这么自称 |
| Energy Infrastructure Platform；把自造段名当搜索词 | 卖方自造品类，目标公司 About 不用 |
| behind-the-meter storage company | 英美电表前后场黑话，挤掉本国货架名 |
| elektriker | 过宽，结果页大量非目标 |
| Elektro-Meisterbetrieb für Photovoltaik（只改复数） | 与已留行只差单复数，不算新词 |
| Smart AI-Powered IoT Solar Twin Firm | 该 ICP 摘录里没有这种自称，属于硬凑 Cutting-edge |
| pv großhandel + 城市 / in der Nähe | 买家找货查询，不是公司自称 |
| battery storage company（拿去搜 NL / IT / PL） | 把四国四名压成一个英语伞词 |
| 目录聚合标题、纯文章页上的学名 | 首页看不到符合该 ICP 的公司 |
