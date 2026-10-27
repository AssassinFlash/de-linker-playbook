export type Field = { label: string; value: string }
export type Spec = { label: string; value: string }
export type LineItem = {
  name: string
  sku?: string
  quantity?: number | string
  total?: string
  manufacturer?: string
  model?: string
  partNumber?: string
  specs?: Spec[]
}
export type DocumentRow = { kind: string; reference: string; fields: Field[] }
export type Inquiry = {
  id: string
  number: string
  company: string
  created: string
  status: string
  issued: string
  attribution: string
  attributionBasis: string
  source: string
  device: string
  pages: number | string
  sheetNote: string
  contact: string
  email: string
  phone: string
  address: string
  shipAddress: string
  note: string
  topic: string
  via: string
  payment: string
  currency: string
  total: string
  project: string
  projectRef: string
  items: LineItem[]
  shipping: string
  documents: DocumentRow[]
  fields: Field[]
}
export type ActionRow = {
  date: string
  id: string
  registeredAt?: string
  line?: string
  channel?: string
  category?: string
  action: string
  summary?: string
  evidence?: string
  verifiedAt?: string
  note?: string
  source?: string
  oldUrl?: string
  url?: string
  company?: string
  verified?: string
  level?: string
  indexStatus?: string
  compared?: string
  impressions7?: number | null
  clicks7?: number | null
  impressions7De?: number | null
  clicks7De?: number | null
  queries7?: string
  mailEvent?: string
  attributed?: number
  feedbackDate?: string
  reason?: string
}
export type PageCheck = {
  checked: string
  status: string
  verdict?: string
  compared?: string
  reason?: string
  robots?: string
  indexable?: string
  fetch?: string
  fetchedAt?: string
  googleCanonical?: string
  declaredCanonical?: string
  language?: string
  level?: string
  actionId?: string
}
export type PageRow = PageCheck & { url: string; history: PageCheck[] }
export type PerfRow = {
  date: string
  url?: string
  country?: string
  device?: string
  type?: string
  impressions: number
  clicks: number
  ctr?: string
  position?: string
}
export type QueryRow = PerfRow & { query: string }
export type Dashboard = {
  exportedAt: string
  ladder: { L0: number; L1: number; L2: number; L3: number }
  ladderRule: string
  inquiries: {
    total: number
    byStatus: Record<string, number>
    issued: number
    attributed: number
    byDate: { date: string; count: number }[]
    items: Inquiry[]
    liveError?: string
    rule?: string
  }
  gsc: { performanceRows: number; queryRows: number; indexRows: number; indexUrls: number }
  actions: ActionRow[]
  pages: PageRow[]
  performance: PerfRow[]
  queries: QueryRow[]
  mail: {
    connected: boolean
    total: number
    events: MailEvent[]
    rule: string
  }
  ga4: {
    connected: boolean
    error: string
    window: string
    timezone: string
    sessions: number
    users: number
    pageViews: number
    sources: { label: string; channel: string; source: string; sessions: number }[]
    landings: { path: string; sessions: number }[]
    events: { name: string; count: number }[]
    inquiryEvents: { name: string; count: number }[]
    byDate: { date: string; sessions: number }[]
    rule: string
  }
}
export type MailEvent = {
  date: string
  id: string
  company: string
  event: string
  level: string
  bounce: string
  replyClass: string
  replyId: string
  note: string
  writtenAt: string
}
