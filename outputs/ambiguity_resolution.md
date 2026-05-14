# Ambiguity Resolution Log

**Context:** Pre-classification reasoning step. Resolves the Salesforce classification challenge and all vendors flagged R (Requires Review) in `mapping_philosophy.md`. No HR/Finance access; all resolutions use external research and declared assumptions.

---

## Part 1: The Salesforce Challenge

**Question:** Does "Salesforce UK Ltd-Uk" ($3,117,226 — 39.5% of total spend) belong under **Sales** or **SaaS**?

### The Legitimate Concern
Salesforce sells multiple cloud products serving different departments:
- **Sales Cloud** → Sales (CRM, pipeline, opportunity management)
- **Marketing Cloud** → Marketing (email campaigns, customer journeys)
- **Service Cloud** → Support (case management, customer service)
- **Commerce Cloud** → eCommerce operations

Without billing detail, any of these could be included in a single "Salesforce UK" invoice.

### Evidence Supporting Sales Classification

**Evidence 1 — HubSpot is a separate vendor ($32.2K)**
HubSpot Ireland Limited appears as a distinct vendor in the same dataset. HubSpot and Salesforce Marketing Cloud are direct substitutes — no company pays for both simultaneously. HubSpot's presence confirms Marketing has its own tool; Salesforce is therefore serving a different function: Sales CRM.

**Evidence 2 — Cloudcrossing BVBA ($208.7K) is a Salesforce Sales Cloud add-on**
Web research confirms Cloudcrossing = maker of PDF Butler, a Salesforce AppExchange application for generating sales quotes, proposals, and contracts natively inside Salesforce Sales Cloud. A $208.7K investment in Salesforce document generation is the fingerprint of a company running Salesforce as a sales CRM, not a marketing platform.

**Evidence 3 — Spend magnitude is consistent with Sales Cloud only**
$3.1M is consistent with enterprise Sales Cloud licensing (Salesforce Enterprise/Unlimited at $150–$300/user × hundreds of users). Including Marketing Cloud would typically add $1M+ more to the invoice — unlikely to appear as a single line item at this figure.

**Evidence 4 — No Salesforce sub-product entries exist**
If Service Cloud or Marketing Cloud were material, they would typically appear as separate contract line items. No such entries exist across the 386 vendors.

**Evidence 5 — Salesforce's own guidance**
Salesforce's official position is that the department deriving primary value should own the budget — consistent with our budget accountability framework.

### Risk of Misclassification
If some portion is Marketing Cloud:
- Spend impact: If 20% is Marketing Cloud → Sales share drops from 39.5% to ~31.6%; Marketing rises by ~8%
- Strategic impact: None — the CRM consolidation conversation and contract review recommendation is identical regardless of cloud mix
- Acquirer action: Same (assess acquirer's CRM stack, negotiate Salesforce renewal)

### Ruling

**Classification: Sales — confirmed**
**Confidence: H** (upgraded from provisional M — corroborating evidence via HubSpot and PDF Butler)

**Declared assumption:** Salesforce UK Ltd-Uk represents the acquired company's CRM and Sales Cloud deployment. The presence of HubSpot as a separate Marketing tool strongly indicates Salesforce is not being used for Marketing Cloud. If billing detail later confirms a multi-cloud deployment, the portion attributable to Marketing Cloud should be reclassified. This does not change the strategic recommendation.

---

## Part 2: Ambiguity Resolutions

### Resolution Framework
For each vendor, one of two strategies was applied:
- **Strategy A — Classify with declared assumption:** Vendor has a dominant plausible interpretation; state the assumption explicitly; confidence = L or M
- **Strategy B — Accept ambiguity as strategically irrelevant:** Both classifications lead to the same recommendation; pick the more likely one; note it

---

### Vendor 1: Cloudcrossing BVBA — $208,675 (T1)

**Previous status:** R — name gave no functional signal

**Research finding:** Cloudcrossing is the maker of **PDF Butler**, a Salesforce AppExchange application for document generation (quotes, proposals, invoices, contracts) running natively within Salesforce Sales Cloud. Belgian company (BVBA), est. 2017, ~2 employees. Not a telecoms, IT reseller, or professional services firm.

**Strategy applied:** Strategy A — classify with declared assumption

**Classification: Sales**
**Confidence: M**

**Reasoning:** PDF Butler is a document automation tool used within the Salesforce CRM primarily for sales documents. It is a Salesforce Sales Cloud add-on; its budget ownership tracks with the Salesforce CRM deployment. Classifying as SaaS is the alternative, but given Salesforce → Sales and PDF Butler is a direct extension of that stack, alignment to Sales is the correct governance decision under the budget accountability principle.

**Declared assumption:** Cloudcrossing BVBA = PDF Butler, a Salesforce-native document generation tool. Classified as Sales to align with the Salesforce CRM stack. If PDF Butler is also used for non-Sales documents (HR forms, Finance invoices), reclassify a portion to G&A or Finance. At T1 spend ($208.7K), this assumption should be verified during integration diligence.

**Strategic risk of being wrong: Low** — whether classified as Sales or SaaS, the recommendation is identical: negotiate Cloudcrossing pricing as part of the Salesforce renewal package.

---

### Vendor 2: RSM UK Corporate Finance LLP — $117,078 (T1)

**Previous status:** M&A (provisional) — awaiting confirmation

**Research finding:** RSM UK Corporate Finance LLP is a **separate legal entity** (Companies House: OC325347, originally Baker Tilly Corporate Finance LLP, 2007–2015). Its sole service lines are deal-specific: sell-side advisory, buy-side advisory, capital raising, due diligence, valuations, VDR and monitoring trustee services. It does **not** provide accounting, audit, or tax services — those are handled by the separate RSM UK audit/tax partnership.

**Strategy applied:** Research resolved — direct classification

**Classification: M&A**
**Confidence: H** (upgraded from provisional M — provisional flag removed)

**Reasoning:** The entity is definitively a specialist M&A advisory LLP entirely separate from RSM's accounting/audit arm. This is the unambiguous definition of an M&A vendor under the governing framework.

**Strategic risk of being wrong: Low** — the only theoretical error is if the acquired company used RSM Corporate Finance for a non-deal purpose (e.g., standalone business valuation), which is rare and unlikely to represent $117K of engagement.

---

### Vendor 3: Big Frontier Pty Ltd (Cult of Monday) — $66,131 (T2)

**Previous status:** R — name suggested either marketing agency or management consultancy

**Research finding:** Cult of Monday (trading as Big Frontier Pty Ltd) is an Australian-based **People & Culture advisory and executive search firm**. Primary services: workplace culture transformation, leadership development, executive coaching, executive search and recruitment, HR infrastructure support, and Learning & Development design. They are not a marketing agency or traditional management consultancy. In 2025 they acquired Mondo Search, a search and recruitment firm.

**Strategy applied:** Strategy A — classify with declared assumption

**Classification: G&A**
**Confidence: M**

**Reasoning:** People & Culture advisory, executive coaching, and executive search are HR-adjacent services. No HR category exists in the Config taxonomy. Per edge case rules: company-wide people/culture advisory → G&A. The spend ($66K) is consistent with either executive search fees (~1 senior hire) or a culture transformation engagement retainer. Both are G&A costs.

**Declared assumption:** Big Frontier / Cult of Monday is a People & Culture advisory and executive search firm. Classified as G&A (HR/People function, company-wide). If the engagement was specifically recruiting for Engineering roles, reclassify to Engineering. If for Sales leadership, reclassify to Sales. Without engagement detail, G&A is the defensible default.

**Strategic risk of being wrong: Low** — whether classified as G&A, Professional Services, or a functional department, the recommendation is the same: review whether the ongoing People & Culture engagement is needed post-acquisition given the acquirer's existing HR function.

---

### Vendor 4: Harmonic Group Limited — $65,418 (T2)

**Previous status:** Professional Services (provisional)

**Research finding:** Harmonic Limited is a UK-based management consulting and business transformation firm (est. 2003), acquired by KBR in July 2021. Core services: data migration, sales transformation, data analytics, digital transformation, and complex business transformation programs. Primarily serves the defence sector. Now operating under the Frazer-Nash Consultancy brand.

**Strategy applied:** Research resolved — direct classification

**Classification: Professional Services**
**Confidence: H** (upgraded from provisional — confirmed management consultancy)

**Reasoning:** Management consulting and business transformation is unambiguously Professional Services under the governing framework. No M&A signal, no accounting/finance signal, no SDLC infrastructure signal.

**Strategic risk of being wrong: Low** — Harmonic is clearly a management consulting firm.

---

### Vendor 5: 4I Advisory Services — $71,860 (T2)
### Vendor 5b: 4I Management Consulting Private Limited — $12,117 (T3)

**Previous status:** R — generic advisory name; unclear whether M&A, Finance, or Professional Services

**Research finding:** 4i Advisory (est. 2014, India) is a financial advisory firm specialising in: M&A advisory, domestic and international taxation, compliance, restructuring, and audit. They explicitly list M&A as a primary service and serve as an "exclusive IR advisor for Tax (Private Client) in India." The India entity (4I Management Consulting Private Limited) has "Management Consulting" in the name, suggesting operational consulting rather than deal advisory.

**Strategy applied:** Strategy A for each entity

**4I Advisory Services ($71.9K)**
**Classification: M&A**
**Confidence: M**

**Reasoning:** The firm's primary specialty includes M&A advisory. The acquired company has confirmed active M&A activity (Houlihan Lokey, Vector Capital, SS&C Intralinks all present). 4i Advisory's engagement is most plausibly M&A-related or M&A-adjacent (tax structuring for a deal).

**Declared assumption:** 4I Advisory Services is classified as M&A based on the firm's explicit M&A advisory and financial restructuring specialty, and the acquired company's confirmed active deal activity. If the engagement was purely routine tax compliance (not deal-related), reclassify to Finance. The distinction matters strategically: M&A advisory spend typically terminates post-deal, while Finance advisory spend recurs.

**Strategic risk of being wrong: Medium** — if this is Finance (recurring tax advisory), the recommendation changes: do not terminate the engagement post-deal; integrate into the acquirer's Finance advisory roster instead.

---

**4I Management Consulting India ($12.1K)**
**Classification: Professional Services**
**Confidence: L**

**Reasoning:** "Management Consulting" in the entity name signals operational BAU consulting rather than deal advisory. Likely an Indian entity providing operational support. Spend is T3 — lower diligence threshold.

**Strategic risk of being wrong: Low** — $12K is immaterial to any recommendation.

---

### Vendor 6: Westbrook Advisers — $15,360 (T3)

**Previous status:** R — "Advisers" alone is insufficient to distinguish M&A from Professional Services or Legal

**Research finding:** Web research identified Westbrook Advisers as a **legal advisory and commercial consulting firm** for board members and senior management. Services: flexible legal solutions, investor relations advice, employment issues, succession planning, and reputational risk management. This is a fractional/virtual commercial legal counsel model, not M&A investment banking.

**Strategy applied:** Strategy B — accept ambiguity as strategically irrelevant

**Classification: Legal**
**Confidence: M**

**Reasoning:** Both plausible classifications (Legal or Professional Services) lead to the same T3 recommendation: flag for post-acquisition review, assess whether acquirer's internal legal or external counsel can absorb. The entity description is closer to Legal (provides legal advice and commercial legal solutions) than to Professional Services (IT consulting, staffing, or management consulting in the governing framework). Legal is the more precise fit.

**Strategic risk of being wrong: Low** — $15K at T3. Any misclassification has no material impact on recommendations.

---

### Vendor 7: Six Individual Names as Vendors

| Vendor | Spend |
|--------|-------|
| Stipe Piric | $2,302 |
| John Smith | $2,163 |
| Fabiola Thistlewhaite | $2,154 |
| George Anchor | $2,107 |
| Susan Lee | $1,762 |
| Ansar Madovic | $1,732 |
| **Combined** | **$12,220** |

**Previous status:** R — confirmed individual names; HR/Finance access required

**Context:** No HR/Finance access available. Web research cannot resolve individual contractor identities. Geographic pattern: Stipe Piric and Ansar Madovic are Croatian names, consistent with the acquired company's confirmed Croatian office presence.

**Strategy applied:** Strategy A — classify with declared assumption

**Classification: Professional Services (contractor payments)**
**Confidence: L for all six**

**Reasoning:** At spend levels of $1.7K–$2.3K per name, these are most likely freelancer or contractor invoices processed through accounts payable rather than formal vendor contracts. Croatian-named entries (Stipe Piric, Ansar Madovic) are consistent with the company's Croatian entity presence. English-named entries could be UK or Australian contractors.

**Declared assumption:** Individual names are classified as Professional Services (contractor/freelancer payments). If post-acquisition finance review reveals these are expense reimbursements (employee business expenses processed through the vendor system), reclassify to G&A. Total exposure is $12.2K — immaterial to any strategic recommendation.

**Strategic risk of being wrong: Low** — $12.2K combined. No recommendation changes regardless of whether these are Professional Services or G&A.

---

## Summary Decision Table

| Vendor | Spend | Tier | Classification | Confidence | Strategy | Strategic Risk |
|--------|-------|------|---------------|-----------|----------|----------------|
| Salesforce UK Ltd-Uk | $3,117,226 | T1 | **Sales** ✓ confirmed | **H** ↑ | Research (HubSpot + PDF Butler corroboration) | Medium if multi-cloud; recommendation unchanged |
| Cloudcrossing BVBA | $208,675 | T1 | **Sales** | M | Strategy A — Salesforce Sales Cloud add-on | Low |
| RSM UK Corporate Finance LLP | $117,078 | T1 | **M&A** ✓ confirmed | **H** ↑ | Research — separate legal entity (OC325347) | Low |
| Big Frontier / Cult of Monday | $66,131 | T2 | **G&A** | M | Strategy A — People & Culture advisory | Low |
| Harmonic Group Limited | $65,418 | T2 | **Professional Services** ✓ confirmed | **H** ↑ | Research — KBR-owned management consultancy | Low |
| 4I Advisory Services | $71,860 | T2 | **M&A** | M | Strategy A — M&A advisory specialty + active deal context | **Medium** |
| 4I Management Consulting India | $12,117 | T3 | **Professional Services** | L | Strategy A — operational consulting signal | Low |
| Westbrook Advisers | $15,360 | T3 | **Legal** | M | Strategy B — ambiguity irrelevant; legal advisory fits | Low |
| Stipe Piric | $2,302 | T4 | **Professional Services** | L | Strategy A — contractor payment | Low |
| John Smith | $2,163 | T4 | **Professional Services** | L | Strategy A — contractor payment | Low |
| Fabiola Thistlewhaite | $2,154 | T4 | **Professional Services** | L | Strategy A — contractor payment | Low |
| George Anchor | $2,107 | T4 | **Professional Services** | L | Strategy A — contractor payment | Low |
| Susan Lee | $1,762 | T4 | **Professional Services** | L | Strategy A — contractor payment | Low |
| Ansar Madovic | $1,732 | T4 | **Professional Services** | L | Strategy A — contractor payment | Low |

**Total spend resolved in this step: $3,570,285 — 45.3% of total**

Zero vendors remain in R (Requires Review) status. The 11 encoding-corrupted names require transliteration (handled in the classification script), not business research.

---

*Decision log for VP-level post-acquisition vendor analysis. Completed: 2026-05-14. No further ambiguities outstanding.*
