import type { ActionRow, Inquiry, PageRow } from "../types"
import { askOf, fieldLabel, levelName, money, shortUrl, show } from "../format"
import { LEVEL } from "../format"

function Rows({ rows }: { rows: [string, string][] }) {
  const filled = rows.filter(([, value]) => value && value !== "—")
  if (!filled.length) return null
  return (
    <dl className="grid grid-cols-[96px_minmax(0,1fr)] gap-x-3 gap-y-2 text-sm">
      {filled.map(([label, value]) => (
        <div key={label} className="contents">
          <dt className="text-muted-foreground-1">{label}</dt>
          <dd className="text-foreground break-words">{value}</dd>
        </div>
      ))}
    </dl>
  )
}

function link(url?: string, label?: string) {
  if (!url) return "—"
  return <a className="text-primary hover:underline break-all" href={url} target="_blank" rel="noreferrer">{label || url}</a>
}

export function InquiryDetail({ row }: { row: Inquiry }) {
  const skip = new Set(["主题", "入口", "项目", "项目编号"])
  return (
    <div className="space-y-5">
      <div>
        <h2 className="text-xl font-semibold text-foreground">{row.company || row.contact || "没有公司名"}</h2>
        <p className="text-sm text-muted-foreground-1">{row.number || row.id} · {row.created}</p>
        <span className="mt-2 inline-flex rounded-full bg-primary/10 px-2 py-0.5 text-xs font-medium text-primary">{row.status || "未标状态"}</span>
      </div>
      <section>
        <h3 className="mb-2 text-sm font-semibold">谁提交的</h3>
        <Rows rows={[["公司", row.company], ["联系人", row.contact], ["邮箱", row.email], ["电话", row.phone], ["地址", row.address], ["收货地址", row.shipAddress]]} />
      </section>
      <section>
        <h3 className="mb-2 text-sm font-semibold">申请了什么</h3>
        {row.items?.length ? row.items.map((item) => (
          <div key={item.name + item.sku} className="border-t border-card-divider py-3">
            <strong className="block text-sm">{item.name}</strong>
            <p className="text-xs text-muted-foreground-1">{[item.sku && `SKU ${item.sku}`, item.quantity != null && item.quantity !== "" && `数量 ${item.quantity}`, item.total && `小计 ${item.total}`, item.manufacturer, item.model].filter(Boolean).join(" · ")}</p>
            {item.specs?.length ? <ul className="mt-2 list-disc ps-5 text-sm text-foreground">{item.specs.map((spec) => <li key={spec.label}>{fieldLabel(spec.label)}：{spec.value}</li>)}</ul> : null}
          </div>
        )) : <p className="text-sm text-muted-foreground-1">这单没有行项目。{askOf(row) !== row.note ? askOf(row) : ""}</p>}
      </section>
      {row.note ? <section><h3 className="mb-2 text-sm font-semibold">客户原话</h3><pre className="whitespace-pre-wrap rounded-xl bg-surface p-3 text-sm">{row.note}</pre></section> : null}
      {row.sheetNote ? <section><h3 className="mb-2 text-sm font-semibold">底表备注</h3><pre className="whitespace-pre-wrap rounded-xl bg-surface p-3 text-sm">{row.sheetNote}</pre></section> : null}
      <section>
        <h3 className="mb-2 text-sm font-semibold">金额和来源</h3>
        <Rows rows={[["金额", money(row)], ["付款", row.payment], ["运费", row.shipping], ["入口", row.via], ["主题", row.topic], ["项目", row.project], ["项目编号", row.projectRef], ["签发", row.issued], ["来源", row.source || ""], ["设备", row.device || ""], ["会话页数", row.pages ? String(row.pages) : ""], ["归因", row.attribution], ["归因依据", row.attributionBasis]]} />
      </section>
      {row.documents?.length ? <section><h3 className="mb-2 text-sm font-semibold">单据</h3>{row.documents.map((doc) => <div key={doc.kind + doc.reference} className="border-t border-card-divider py-3"><strong className="text-sm">{doc.kind} {doc.reference}</strong><Rows rows={doc.fields.map((field) => [field.label, field.value])} /></div>)}</section> : null}
      {row.fields?.filter((field) => !skip.has(field.label)).length ? <section><h3 className="mb-2 text-sm font-semibold">其他有内容的字段</h3><Rows rows={row.fields.filter((field) => !skip.has(field.label)).map((field) => [field.label, field.value])} /></section> : null}
    </div>
  )
}

export function ActionDetail({ row }: { row: ActionRow }) {
  const hint = LEVEL[row.level || ""]?.[1] || ""
  return (
    <div className="space-y-5">
      <div>
        <h2 className="text-xl font-semibold">{row.action || "动作"}</h2>
        <p className="text-sm text-muted-foreground-1">{row.id} · {row.date}</p>
        <p className="mt-2 text-sm"><span className="rounded-full bg-primary/10 px-2 py-0.5 text-xs font-medium text-primary">{levelName(row.level)}</span> <span className="text-muted-foreground-1">{hint}</span></p>
      </div>
      <section><h3 className="mb-2 text-sm font-semibold">做了什么</h3><Rows rows={[["线", row.line || ""], ["渠道", row.channel || ""], ["大类", row.category || ""], ["动作", row.action], ["公司", row.company || ""], ["来源", row.source || ""], ["查证", row.verified || ""], ["查证时刻", row.verifiedAt || ""], ["登记时刻", row.registeredAt || ""]]} /></section>
      {row.summary ? <section><h3 className="mb-2 text-sm font-semibold">内容说明</h3><pre className="whitespace-pre-wrap rounded-xl bg-surface p-3 text-sm">{row.summary}</pre></section> : null}
      {row.evidence ? <section><h3 className="mb-2 text-sm font-semibold">查证证据</h3><pre className="whitespace-pre-wrap rounded-xl bg-surface p-3 text-sm">{row.evidence}</pre></section> : null}
      {row.note ? <section><h3 className="mb-2 text-sm font-semibold">备注</h3><pre className="whitespace-pre-wrap rounded-xl bg-surface p-3 text-sm">{row.note}</pre></section> : null}
      <section>
        <h3 className="mb-2 text-sm font-semibold">后来怎样</h3>
        <dl className="grid grid-cols-[96px_minmax(0,1fr)] gap-x-3 gap-y-2 text-sm">
          <dt className="text-muted-foreground-1">页面</dt><dd>{link(row.url, shortUrl(row.url))}</dd>
          {row.oldUrl ? <><dt className="text-muted-foreground-1">旧网址</dt><dd>{link(row.oldUrl)}</dd></> : null}
          <dt className="text-muted-foreground-1">收录</dt><dd>{show(row.indexStatus)}</dd>
          <dt className="text-muted-foreground-1">原因</dt><dd>{show(row.reason)}</dd>
          <dt className="text-muted-foreground-1">近 7 天展示</dt><dd>{show(row.impressions7)}</dd>
          <dt className="text-muted-foreground-1">近 7 天点击</dt><dd>{show(row.clicks7)}</dd>
          <dt className="text-muted-foreground-1">归因询盘</dt><dd>{show(row.attributed)}</dd>
        </dl>
      </section>
    </div>
  )
}

export function PageDetail({ row }: { row: PageRow }) {
  return (
    <div className="space-y-5">
      <div>
        <h2 className="text-xl font-semibold">收录检查</h2>
        <p className="text-sm">{link(row.url)}</p>
      </div>
      <section><h3 className="mb-2 text-sm font-semibold">最新一次</h3><Rows rows={[["状态", row.status], ["结论", row.verdict || ""], ["原因", row.reason || ""], ["和上次比", row.compared || ""], ["语言", row.language || ""], ["robots", row.robots || ""], ["是否允许收录", row.indexable || ""], ["抓取", row.fetch || ""], ["上次抓取", row.fetchedAt || ""], ["反馈级别", levelName(row.level)], ["对应动作", row.actionId || ""]]} /></section>
      <section>
        <h3 className="mb-2 text-sm font-semibold">历次检查</h3>
        <table className="w-full text-sm"><thead><tr className="text-left text-muted-foreground-1"><th className="py-2">日期</th><th>状态</th><th>变化</th><th>原因</th></tr></thead><tbody>{row.history.map((item) => <tr key={item.checked + item.status} className="border-t border-card-divider"><td className="py-2 whitespace-nowrap">{item.checked}</td><td>{item.status}</td><td>{item.compared}</td><td>{item.reason}</td></tr>)}</tbody></table>
      </section>
    </div>
  )
}
