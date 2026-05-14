# Vendor Mapping Philosophy

**Document type:** Strategic governance — defines the classification framework before any vendor is assigned a department.
**Dataset:** 386 vendors, $7,887,360 total L12M spend, 0% pre-classified.
**Authority:** All downstream classifications must conform to the rules in this document. Deviations require documented rationale.

---

## Governing Philosophy

**Departments represent budget accountability** — the functional cost center that would own this vendor relationship in an integrated org chart.

This framing was chosen over three alternatives:

| Alternative | Why Rejected |
|---|---|
| Software category (CRM, ERP, HRIS…) | Fails for non-software vendors: law firms, insurance, coworking spaces, recruitment agencies |
| Vendor type (SaaS, Professional Services…) | 'SaaS' is already one of the 12 categories — using vendor type as the primary principle would create circular reasoning |
| Operational ownership (who manages the contract) | Unknowable from vendor name alone; IT often administers contracts it doesn't budget-own (e.g., Salesforce) |
| Business capability ownership | Too abstract for integration planning; doesn't map to real cost centers the CFO will recognise |

**Why budget accountability works in a post-acquisition context:**
- It answers the CFO's primary integration question: *which acquiring department absorbs this cost?*
- It enables synergy identification: does the parent company have a competing contract in the same function?
- It mirrors how integration workstreams are structured (Engineering track, Finance track, etc.)

**The taxonomy is intentionally hybrid.** Of the 12 Config categories, 8 are functional departments
(Engineering, G&A, Legal, Marketing, Product, Sales, Support, Finance), 1 is physical (Facilities),
1 is transaction-type (M&A), and 2 are cross-cutting overrides (SaaS, Professional Services).
This hybrid design is the correct one — the three overrides exist precisely to handle vendors that
don't have a single functional owner.

**Override hierarchy for the three non-functional categories:**

1. **SaaS** — IT-governed horizontal software used by 3+ departments with no single budget owner. If a tool clearly serves one function's core workflow, use that function instead.
2. **Professional Services** — Ongoing external labor or advisory engaged to operate the business (not tied to a transaction).
3. **M&A** — Spend directly traceable to a specific acquisition, merger, or divestiture event.

---

## Boundary Dispute Rules

Each of the 7 pairs below has a governing rule followed by examples drawn from this dataset.
When a vendor triggers one of these disputes, the rule supersedes intuition.

### 1. SaaS vs Engineering

> **Governing Rule:** If the tool is part of the Software Development Lifecycle (SDLC) — used primarily by engineers to build, test, deploy, or monitor software — assign **Engineering**. If it is a general-purpose business application licensed company-wide by IT, assign **SaaS**.

| Vendor | Spend | Decision | Reasoning |
|---|---|---|---|
| Amazon Web Services Llc / Inc. | $112K combined | **Engineering** | Core cloud infrastructure; SDLC-critical |
| JetBrains S.R.O. | $4.1K | **Engineering** | IDE; developer-exclusive tool |
| Npm Inc | $3.5K | **Engineering** | Package manager; part of build pipeline |
| Papertrail Inc | $3.9K | **Engineering** | Log management; SDLC monitoring |
| Ag Grid Ltd | $2.7K | **Engineering** | JavaScript data grid library |
| Axosoft GitKraken | $54 | **Engineering** | Developer Git client |
| Google Ireland Limited | $24.8K | **SaaS** | Likely Google Workspace; company-wide productivity |
| Microsoft Ireland Operations | $9.8K | **SaaS** | Likely Microsoft 365; company-wide |
| Goto Technologies UK | $7.3K | **SaaS** | Remote access / meeting tool; cross-functional |
| Trello | $6.7K | **SaaS** | Project management; cross-functional |
| Workato, Inc. | $16.1K | **Engineering** | Integration platform; typically IT/Engineering-governed |

### 2. SaaS vs Product

> **Governing Rule:** If the tool directly informs *what to build* or *how users experience the product*, or is used exclusively by Product/UX/Design teams, assign **Product**. If it is a general business tool the Product team uses alongside other functions, assign **SaaS**.

| Vendor | Spend | Decision | Reasoning |
|---|---|---|---|
| Figma, Inc. | $460 | **Product** | Design/prototyping; Product and UX-owned |
| Aha! Labs Inc | $3.7K | **Product** | Product roadmapping; Product-team exclusive |
| Peakon Aps | $17.1K | **G&A** | Employee engagement analytics; HR tool, not a product tool |
| Planful, Inc. | $27.7K | **Finance** | FP&A software; Finance budget-owned |
| Tmforum | $57.6K | **Professional Services** | Telecoms industry body membership; not product tooling |

### 3. SaaS vs Sales  ← CRITICAL (Salesforce = 39.5% of total spend)

> **Governing Rule:** If the tool's primary value driver is enabling revenue generation — pipeline management, sales prospecting, engagement, or deal closing — assign **Sales**, regardless of who administers the contract. IT governance does not change budget ownership.

> **The Salesforce decision:** Salesforce is the single largest vendor at $3,117,226 (39.5% of total spend).
> It is a CRM. Its primary users are Sales. Its budget owner is Sales. It is **not SaaS**.
> This single classification governs more spend than the next 9 vendors combined.

| Vendor | Spend | Decision | Reasoning |
|---|---|---|---|
| Salesforce Uk Ltd-Uk | $3,117,226 | **Sales** | CRM; Sales-owned budget; primary users are Sales reps |
| Cognism Limited | $27K | **Sales** | Lead intelligence and prospecting; Sales-owned |
| Outreach Corporation | $9.2K | **Sales** | Sales engagement platform |
| Lusha | $2.6K | **Sales** | Contact intelligence for prospecting |
| 6Sense Insights Inc | $76 | **Sales** | ABM/intent data; revenue team-owned |
| HubSpot Ireland Limited | $32.2K | **Marketing** | Inbound marketing CRM; primary use is demand generation |
| LinkedIn Ireland Limited | $55.6K | **Marketing** | Default Marketing (LinkedIn Ads / Recruiter); Sales Navigator would flip to Sales — name alone insufficient to override |
| Uberflip | $26.1K | **Marketing** | Content experience platform; Marketing-owned |
| Kimble Applications Ltd | $52.8K | **Professional Services** | PSA tool for professional services delivery teams |

### 4. G&A vs Finance

> **Governing Rule:** Assign **Finance** when spend is directly tied to financial reporting, accounting, audit, tax, treasury, payroll, or financial compliance. Assign **G&A** for general administrative overhead without a specific financial function: travel, employee benefits, HR admin, office supplies.

| Vendor | Spend | Decision | Reasoning |
|---|---|---|---|
| BDO LLP | $343K | **Finance** | External audit and accounting firm |
| RSM UK Corporate Finance LLP | $117K | **M&A** (provisional) | 'Corporate Finance' signals deal advisory; verify before finalising |
| Sage UK Limited | $46.9K | **Finance** | Accounting software |
| Planful, Inc. | $27.7K | **Finance** | FP&A / financial planning software |
| Grant Thornton | $46.5K | **Finance** | Accounting and business advisory firm |
| Taxstudio, Ltd. | $14.6K | **Finance** | Tax advisory services |
| PricewaterhouseCoopers LLP | $4.9K | **Finance** | Big 4 accounting (unless engagement is deal-specific → M&A) |
| Australian Payroll Professionals | $4.4K | **Finance** | Payroll processing is a Finance function |
| Eurofast International | $18.2K | **Finance** | International payroll and accounting services |
| Navan / TripActions | $415.9K combined | **G&A** | Travel and expense management is company-wide admin, not Finance |
| Mercer Limited | $5.4K | **G&A** | Benefits consulting; employee benefits = G&A, not Finance |

### 5. G&A vs Legal

> **Governing Rule:** Assign **Legal** when the vendor's primary service is legal advice, representation, contract management, immigration/visa services, IP management, or regulatory compliance fees. All other administrative overhead → **G&A**.

| Vendor | Spend | Decision | Reasoning |
|---|---|---|---|
| Bisley Law Ltd | $67.4K | **Legal** | Law firm |
| Zuric I Partneri D.O.O. | $24.1K | **Legal** | Croatian law firm |
| Pinsent Masons Mpillay LLP | $4.1K | **Legal** | International law firm |
| Virtual Legal Counsel Ltd | $4.8K | **Legal** | Legal services |
| Visalogic Limited | $11.2K | **Legal** | Immigration and visa management services |
| ICO | $67 | **Legal** | UK Information Commissioner registration fee; data protection compliance |
| Lane IP Limited | $851 | **Legal** | IP management and filing |
| Kilgannon & Partners LLP | $681 | **Legal** | Law firm |
| Induslaw | $596 | **Legal** | Indian law firm |
| Jensten Insurance Brokers | $142.7K | **G&A** | Insurance broker; employee and company policies = G&A, not Legal |

### 6. M&A vs Professional Services

> **Governing Rule:** Assign **M&A** when the vendor was specifically engaged for a transaction (investment banking, deal due diligence, virtual data rooms). Assign **Professional Services** for ongoing external labor or advisory engaged to run business-as-usual operations. Default: investment banks and VDR providers → M&A; consulting and staffing firms → Professional Services.

| Vendor | Spend | Decision | Reasoning |
|---|---|---|---|
| Houlihan Lokey Advisors, LLC | $37.5K | **M&A** | Investment bank; exclusively M&A advisory |
| Vector Capital Management LP | $32.4K | **M&A** | PE investment management; deal-related |
| SS&C Intralinks Inc | $40K | **M&A** | Virtual data room; deal-specific platform |
| RSM UK Corporate Finance LLP | $117K | **M&A** (provisional) | 'Corporate Finance' in name signals deal advisory; confirm |
| Infosys | $66.6K | **Professional Services** | IT services and consulting; ongoing BAU engagement |
| Big Frontier Pty Ltd (Cult Of Monday) | $66.1K | **Professional Services** | Creative/marketing consultancy; BAU engagement |
| Harmonic Group Limited | $65.4K | **Professional Services** | Consulting and advisory; no deal signal |
| Cloud Technology Solutions Ltd | $60.7K | **Professional Services** | IT consulting (Google Cloud partner); BAU |
| Mason Frank International Ltd | $38.1K | **Professional Services** | Salesforce specialist recruitment/staffing |
| Accutrainee Limited | $38.8K | **Professional Services** | Training and recruitment firm |
| 4I Advisory Services | $71.9K | **Professional Services** | Generic advisory; no transaction signal in name |
| Westbrook Advisers | $15.4K | **R — Requires Review** | 'Advisers' could be M&A or PS; engagement purpose unknown |

### 7. Facilities vs G&A

> **Governing Rule:** Assign **Facilities** for the direct cost of physical workspace: rent, coworking fees, office maintenance, utilities, cleaning, parking, physical access control, and FM services. Assign **G&A** for administrative overhead that is not itself a physical space cost.

| Vendor | Spend | Decision | Reasoning |
|---|---|---|---|
| Tog UK Properties Limited | $263.8K | **Facilities** | Commercial property / office rent (UK) |
| Zagrebtower D.O.O. | $183.8K | **Facilities** | Croatian office tower / rent |
| Innovent Spaces Private Limited | $147.3K | **Facilities** | Coworking and office spaces (India) |
| Weking D.O.O. | $144.1K | **Facilities** | Croatian office property |
| GPT Space & Co | $133.5K | **Facilities** | Australian office / event space |
| Wework Singapore Pte. Ltd. | $64.4K | **Facilities** | Coworking space |
| Sodexo Svc India Private Limited | $17.8K | **Facilities** | FM and catering services for office |
| Jones Lang Lasalle (Nsw) Pty Ltd | $16.3K | **Facilities** | Property management services |
| Work Easy Space Solutions | $14.9K | **Facilities** | Coworking / serviced offices |
| Telefonica Global Services GmbH | $89.9K | **Facilities** | Office telecom / connectivity = physical operations cost |
| Jensten Insurance Brokers | $142.7K | **G&A** | Insurance broker; not a physical space cost |
| Navan / TripActions | $415.9K combined | **G&A** | Travel management; not a physical space cost |

---

## Spend Tiers and Classification Diligence

Spend magnitude governs how much research effort to invest before assigning a department.
Higher tiers require confirmed classification; lower tiers accept heuristic assignment.

| Tier | Label | Threshold | Vendors | Spend | % Total | Classification Diligence |
|---|---|---|---|---|---|---|
| T1 | Strategic | ≥ $100K | 13 | $5,042,189 | 63.9% | Full research required. Confirm vendor's primary service line before assigning. Confidence must be H or M. Escalate ambiguities immediately. |
| T2 | Significant | $25K – $99.9K | 27 | $857,090 | 10.9% | Apply all boundary rules. Use vendor name + common knowledge. Target H or M confidence. Flag any L for review. |
| T3 | Operational | $10K – $24.9K | 39 | $522,048 | 6.6% | Batch processing acceptable. Apply boundary rules. M confidence acceptable; flag R only if name is truly unresolvable. |
| T4 | Tail | $1K – $9.9K | 129 | $340,006 | 4.3% | Expedited assignment via name pattern. L confidence acceptable. Correctness at category level; not sub-level nuance. |
| T5 | Noise | < $1K | 178 | $126,028 | 1.6% | Bulk heuristic assignment. Exclude from strategic reports. Most are meal/catering/courier/retail receipts. |

**T1 classification decisions with the highest strategic impact:**
- Salesforce UK ($3,117,226) → **Sales** — governs 39.5% of total spend; the most consequential single assignment
- Navan / TripActions ($415,913 combined) → **G&A** — two rows for one vendor; normalise before reporting
- BDO LLP ($343,081) → **Finance** — largest single Finance vendor
- RSM UK Corporate Finance ($117,078) → **M&A provisional** — name strongly implies deal advisory; verify
- Cloudcrossing BVBA ($208,675) → **R — Requires Review** — name gives no functional signal

---

## Multi-Entity Brand Grouping

**Approach: preserve row-level data; add a canonical brand column.**

Rules:
1. **Do NOT merge rows** — `row_number`, `vendor_name`, and `cost_usd` remain untouched
2. **Add `canonical_brand` column** — the normalised parent brand name
3. **Add `brand_group_spend` column** — summed spend across all group members (computed field)
4. **Add `is_multi_entity` flag** — True when two or more rows share the same canonical brand

| Canonical Brand | Entity Count | Member Vendor Names | Combined Spend |
|---|---|---|---|
| Amazon Web Services / Amazon | 4 | `Amazon Web Services Llc` / `Amazon Web Services Inc.` / `Amazon.Co.Uk` / `Amazon (Aus)` | $112,893 |
| Navan / TripActions | 2 | `Navan (Tripactions Inc)` / `Navan, Inc` | $415,913 |
| Bupa Group | 2 | `Bupa- Supplier` / `Bupa Australia` | $35,263 |
| Allianz | 2 | `Allianz Australia Workers' Compensation (Victoria) Limited` / `Allianz Wa` | $7,069 |
| HRsolution International | 2 | `Hr Solution International Gmbh` / `Hrsolution International Ag` | $87,810 |
| Apple | 4 | `Apple Retail Uk Ltd` / `Apple Pty Ltd` / `Apple Distribution International Ltd` / `Apple - Amer` | $8,256 |
| Acclime | 2 | `Acclime Corporate Services` / `Acclime Usa, Inc` | $10,408 |
| 4I Group | 2 | `4I Advisory Services` / `4I Management Consulting Private Limited` | $83,978 |

> **Highest-risk near-duplicate:** Navan (Tripactions Inc) + Navan, Inc.
> Combined spend: $415,913. Two entries for one vendor — confirm before any recommendation.
>
> **Note on Apple:** Four entries totalling ~$9.6K across retail, distribution, and regional entities.
> Likely a mix of hardware purchases (Facilities/Engineering) and software (SaaS). Classify each row individually.

---

## Classification Framework

### 6 Core Classification Principles

**1. Budget accountability over administrative custody**
Classify by who OWNS the budget, not who manages the contract. Salesforce is Sales even if IT runs the licences.

**2. Primary use over incidental use**
If 80%+ of a vendor's value flows to one function, assign to that function. Don't over-engineer cross-functional tools that happen to have secondary users.

**3. Spend-weighted diligence**
Invest classification effort proportional to spend magnitude. T1/T2 vendors warrant research; T5 vendors warrant a heuristic. See Tier table.

**4. Single assignment only**
Each vendor receives exactly ONE department. No split codes. Forced clarity surfaces real decisions instead of avoiding them.

**5. Preserve source data**
Never modify vendor_name, cost_usd, or row_number. Classification is additive — new columns only: department_assigned, confidence, canonical_brand.

**6. Boundary rules over intuition**
When a dispute applies, the governing rule in this document supersedes gut feel. Ad hoc overrides require documented rationale.

### Edge Case Rules

| Vendor Type | Governing Rule | Assigned Category | Examples from Dataset |
|---|---|---|---|
| Individual names (real persons) | Flag `possible_individual_name=True`. Classify as Professional Services if likely contractor payment; G&A if HR/admin reimbursement. Mark confidence **R**. | Professional Services or G&A | Stipe Piric, John Smith, Fabiola Thistlewhaite, George Anchor, Susan Lee, Ansar Madovic |
| False-positive individual names (companies) | Apply corporate context to override the heuristic flag. Classify normally. | Classify normally per rules | Grant Thornton (Finance), Peakon Aps (G&A), Axosoft GitKraken (Engineering) |
| Government entities | → G&A (regulatory or compliance payments; no functional owner). | G&A | Cayman Islands Government, Australian Taxation Office, ICO |
| Insurance / health benefits | → G&A. Employee benefits are a company-wide cost with no single functional owner. No HR category exists in Config. | G&A | Aetna ($124.7K), Jensten ($142.7K), Bupa ($35.3K combined), Agram Life ($25K), Care Health ($24K), Cigna ($13.2K), Allianz ($7.1K combined), ICICI Lombard ($6K), Mercer ($5.4K) |
| Recruitment agencies | → G&A if company-wide. → Engineering if name explicitly signals tech/IT recruitment. Check for functional signal in name. | G&A or Engineering | Technet IT Recruitment (Engineering), Cedar Recruitment (G&A), HR Solution (G&A), Mason Frank — Salesforce staffing (Professional Services) |
| Events / entertainment | → Facilities if office-event catering. → G&A if company social/morale spend. → Marketing if client-facing. → Noise label if T5. | Facilities / G&A / Marketing / Noise | Tattu Manchester (G&A), Gaucho Restaurants (G&A), Uber Eats (Noise), Istra Wine (Noise) |
| Coworking / serviced offices | → Facilities always, regardless of which team uses the space. | Facilities | WeWork ($64.4K), Innovent ($147.3K), GPT Space ($133.5K), Work Easy ($14.9K), Platinum Office D.O.O. ($62) |
| Telecom / office utilities | → Facilities. Office connectivity and utilities are a physical operations cost, not IT. | Facilities | Telefonica Global ($89.9K), Hrvatski Telekom ($18.1K), British Telecommunications ($1.5K), Starhub ($2.2K), Telemach ($5.1K) |
| Medical / occupational health | → G&A. Employee wellness is company-wide; no HR category in Config. | G&A | Specijalisticka Ordinacija x3 (~$20 each), Ustanova Za Medicinu Rada ($20) |
| Encoding-corrupted names (11 vendors) | Attempt transliteration. If decodable, classify normally. If not, assign best guess from geographic/linguistic context. Mark confidence **R**. | Varies (mostly Facilities or G&A — Croatian D.O.O. entities) | Garaža Firule (Facilities — parking garage), Sveuč. Zagreb (Facilities — university venue) |
| Training / certification | → Engineering if technical/developer training. → G&A if general HR/people development. → Support if customer-facing certification. | Engineering / G&A / Support | Pluralsight (Engineering), Accutrainee (Professional Services), Interaction Design Foundation (Product) |

### Fallback Rules — Priority Order

1. Name unambiguously identifies function → assign directly, confidence **H**
2. Name is ambiguous, Tier 1 or 2 → consult boundary dispute table; if still unclear, mark **R** (Requires Review) for human input before proceeding
3. Name is ambiguous, Tier 3 → apply boundary dispute table; assign confidence **M**
4. Name is ambiguous, Tier 4 → assign most probable category from name pattern; confidence **L**
5. Name gives no signal, Tier 5 → assign G&A as catch-all; confidence **N** (Noise)
6. Encoding-corrupted name → attempt transliteration; apply above rules if successful; mark **R** if not
7. Confirmed individual name (real person) → mark **R**, note 'requires HR/Finance clarification'

### Confidence Scoring Framework

| Score | Label | Definition | Required Action |
|---|---|---|---|
| H | High | Vendor name clearly and unambiguously maps to one department. No applicable boundary dispute. Primary use is self-evident. | Proceed. No review needed. |
| M | Medium | Vendor fits 2+ categories. A governing boundary rule was applied to choose. Classification is defensible but not self-evident. | Proceed. Document which rule was applied. |
| L | Low | Vendor name gives minimal signal. Classification is best-guess from name pattern or geography alone. | Flag for batch review. Lower-priority. |
| R | Requires Review | Encoding-corrupted name, confirmed individual name, genuine multi-function ambiguity, or T1/T2 vendor where the governing rule produces two equally valid outputs. | Do NOT finalise without human input. Escalate. |
| N | Noise | Tier 5 vendor (< $1K). Classification assigned but has no strategic relevance. | Exclude from strategic analysis outputs. Bulk-assign; no diligence required. |

---

## Key Assumptions

- **Salesforce = Sales** (not SaaS). The most consequential single decision: 39.5% of spend moves on this choice.
- **Navan / TripActions = one vendor** (two row entries). Combined spend $415,913 → G&A. Normalise before any department-level reporting.
- **Insurance and employee benefits = G&A** (no HR category exists in Config; benefits are company-wide admin cost).
- **Telecom and office utilities = Facilities** (office connectivity is a physical operations cost, not an IT cost).
- **AWS / cloud infrastructure = Engineering** (not SaaS; SDLC-critical infrastructure owned by Engineering).
- **RSM UK Corporate Finance = M&A provisional** — 'Corporate Finance' in the name strongly implies deal advisory; must be confirmed against contract before finalising.
- **Google Ireland = SaaS** (assumed to be Google Workspace, not Google Cloud Platform; GCP would flip to Engineering).
- **Microsoft Ireland = SaaS** (assumed to be Microsoft 365, not Azure; Azure would flip to Engineering).

## Unresolved Ambiguities — Flagged R

- **Cloudcrossing BVBA** ($208,675, T1): Belgian entity; name gives zero functional signal. Could be telecoms, IT reseller, or professional services. Requires vendor website lookup before classification.
- **RSM UK Corporate Finance LLP** ($117,078, T1): 'Corporate Finance' implies M&A deal advisory, but RSM also provides Finance/accounting services. Confirm engagement scope.
- **Sveu[corrupted] Zagreb / Studentski Centar** ($44,299, T2): University of Zagreb student center — likely a Facilities venue booking. Croatian-speaker or contract review needed to confirm.
- **Big Frontier Pty Ltd (Cult Of Monday)** ($66,131, T2): Creative/marketing agency vs. general management consultancy. Classification (Marketing vs. Professional Services) depends on what they actually delivered.
- **4I Advisory Services** ($71,860, T2): Generic advisory firm. Could be M&A, Professional Services, or G&A depending on engagement scope. Classified Professional Services provisionally.
- **Westbrook Advisers** ($15,360, T3): 'Advisers' alone is insufficient to distinguish M&A from Professional Services. Engagement purpose unknown.
- **Harmonic Group Limited** ($65,418, T2): Consulting/advisory firm with generic name. Professional Services provisionally; confirm scope.

---

*This document governs all downstream vendor classification. Last updated: 2026-05-14.*