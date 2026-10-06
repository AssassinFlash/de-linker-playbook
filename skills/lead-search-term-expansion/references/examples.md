# 搜索词扩展例子

> 仅供理解，禁止引用到输出。

本文全部例子都是教学支架，禁止把原文写入任何交付物。

表里的公司类型、定位语和粗热度都是示意形状，不是可引用的检索结果。

### 形状：已验证行长什么样

> 仅供理解，禁止引用到输出。

输入画像（示意）：「工业设备维修公司，给大型机械做维修，常要换滚动轴承。」目标市场英语。下面每一行都假设已经用网页搜索看到匹配公司，并记下了例证 URL。`estimated_search_volume` 写成粗热度，因为本轮没有关键词工具导出。

| icp_category | company_type | positioning_term | tone | search_keyword | estimated_search_volume | use_case |
| --- | --- | --- | --- | --- | --- | --- |
| Equipment Repair | General Repair | Industrial Equipment Maintenance Solutions Provider | Professional | "industrial equipment maintenance company" | autocomplete:yes; page1_companies:8 | Google, LinkedIn |
| Equipment Repair | General Repair | Your Go-To Machine Repair Shop | Casual | "machine repair shop near me" | autocomplete:yes; page1_companies:10 | Google |
| Equipment Repair | Predictive | Predictive Maintenance Technology Firm | Cutting-edge | "predictive maintenance company" | autocomplete:yes; page1_companies:6 | Google, LinkedIn |
| Equipment Repair | Traditional | Established Machinery Service and Repair Company | Traditional | "machinery repair service company" | autocomplete:yes; page1_companies:7 | Google |
| Equipment Repair | Specialist | Heavy Equipment Breakdown Recovery Specialists | Professional | "heavy equipment repair specialist" | autocomplete:yes; page1_companies:5 | Google |
| Equipment Repair | MRO | Industrial MRO Parts and Service Provider | Professional | "industrial MRO service provider" | autocomplete:partial; page1_companies:4 | LinkedIn |
| Equipment Repair | On-site | On-Site Industrial Equipment Servicing Team | Casual | "on-site equipment repair service" | autocomplete:yes; page1_companies:5 | Google |
| Equipment Repair | Digital | Digital Equipment Health Monitoring Service | Cutting-edge | "equipment monitoring company" | autocomplete:yes; page1_companies:4 | LinkedIn |
| Equipment Repair | Family | Family-Owned Industrial Repair Since 1985 | Traditional | "family owned industrial repair" | autocomplete:yes; page1_companies:3 | Google |
| Equipment Repair | Emergency | 24/7 Emergency Machinery Repair Contractor | Casual | "emergency machinery repair" | autocomplete:yes; page1_companies:9 | Google |
| Equipment Repair | Turnkey | Turnkey Plant Maintenance and Repair Solutions | Professional | "plant maintenance solutions" | autocomplete:yes; page1_companies:6 | LinkedIn |
| Equipment Repair | Rotating | Rotating Equipment Repair and Overhaul Specialist | Professional | "rotating equipment repair" | autocomplete:yes; page1_companies:7 | Google, LinkedIn |

观察（示意，不是交付结论）：

- Professional 适合职业网络直搜
- Casual 适合本地网页检索
- Cutting-edge 适合在找新技术方案的公司
- Traditional 适合采购习惯稳定的老公司

年份「1985」在真跑时必须来自已抓取页；示意表里的数字禁止抄进交付物。

### 形状：哪些候选必须丢掉

> 仅供理解，禁止引用到输出。

| 候选 | 丢掉原因 |
| --- | --- |
| Commercial and Industrial Machinery and Equipment Repair and Maintenance | 分类学名，公司不这么自称 |
| Synergistic Kinetic Asset Stewardship Platform | 无搜索结果里的真实公司在用 |
| repair shop | 过宽，结果页大量非目标 |
| Industrial Equipment Maintenance Solutions Providers | 与已留行只差复数，不算新词 |
| Smart AI-Powered IoT Predictive Twin Firm | 该 ICP 摘录里没有这种自称，属于硬凑 Cutting-edge |
