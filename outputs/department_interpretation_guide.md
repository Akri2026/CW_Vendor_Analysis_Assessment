# Department Interpretation Guide

**Operational reference document.** Use this during classification to look up
per-department definitions, inclusion/exclusion rules, and worked examples.
All decisions must conform to `mapping_philosophy.md`.

---

## Quick Reference Card — All 12 Departments

| Department | One-Line Definition | Typical Spend Types |
|---|---|---|
| Engineering | Tools and infrastructure used to build, test, deploy, and monitor the product | Cloud infra, developer tools, CI/CD, logging, monitoring |
| Facilities | Direct cost of physical workspace and office operations | Rent, coworking, utilities, telecom, FM services, parking |
| G&A | General administrative overhead with no single functional owner | Travel, benefits/insurance, HR admin, government fees, office supplies |
| Legal | Legal advice, representation, compliance, IP, and immigration services | Law firms, legal tech, visa/immigration, IP management, regulator fees |
| M&A | Spend directly tied to a specific acquisition or merger transaction | Investment banks, VDRs, deal due diligence, transaction legal |
| Marketing | Demand generation, brand, content, and customer acquisition | Marketing software, agencies, PR, advertising, content tools |
| SaaS | IT-governed horizontal software with no single functional budget owner | Cross-functional productivity, collaboration, and business tools |
| Product | Tools and research used by Product/UX/Design to define and shape the product | Roadmapping, design, user research, prototyping tools |
| Professional Services | Ongoing external labor or advisory engaged for BAU operations | IT consulting, management consulting, staffing, training |
| Sales | Revenue generation tools and services owned by the Sales function | CRM, sales engagement, prospecting, lead intelligence |
| Support | Customer-facing support tools and services | Helpdesk software, customer success tools, support staffing |
| Finance | Financial reporting, accounting, audit, tax, payroll, and treasury | Accounting software, audit firms, tax advisors, FP&A tools |

---

## Per-Department Definitions

### Engineering

**Definition:** Spend on tools and infrastructure that engineers use directly to build, test, deploy, or monitor the product or its underlying systems.

**In scope:**
- Cloud infrastructure (AWS, GCP, Azure) — always Engineering, never SaaS
- Developer IDEs and editors (JetBrains, VS Code extensions)
- Source control and Git tools (GitKraken, GitHub)
- CI/CD pipelines, build tools, package managers (npm)
- Logging, monitoring, and observability (Papertrail, Datadog)
- Data grid and frontend libraries (Ag Grid)
- Integration platforms where Engineering is the operator (Workato)
- IT recruitment specifically for technical roles

**Out of scope (common errors to avoid):**
- General-purpose productivity software (→ SaaS)
- Design and prototyping tools (→ Product)
- Cloud spend for marketing analytics or BI (→ Marketing or Finance)
- General telecom / office internet (→ Facilities)

| Vendor Example | Spend | Confidence | Note |
|---|---|---|---|
| Amazon Web Services Llc / Inc. | $112K combined | H | Core cloud infra |
| JetBrains S.R.O. | $4.1K | H | Developer IDE |
| Npm Inc | $3.5K | H | Package manager |
| Papertrail Inc | $3.9K | H | Log management |
| Workato, Inc. | $16.1K | M | Integration platform — Engineering if Eng-governed |

### Facilities

**Definition:** Direct cost of providing and maintaining physical workspace, including rent, coworking, utilities, telecom, and facilities management services.

**In scope:**
- Office rent and commercial property leases
- Coworking and serviced office memberships (WeWork, Innovent, GPT Space)
- Office telecom and internet connectivity (Telefonica, Telemach, British Telecom)
- Facilities management and catering (Sodexo)
- Property management firms (Jones Lang Lasalle)
- Parking, cleaning, security, and physical access control
- Utilities (electricity, water, gas — e.g., HEP Elektra)

**Out of scope (common errors to avoid):**
- Travel management (→ G&A)
- Insurance and employee benefits (→ G&A)
- Corporate IT infrastructure (→ Engineering or SaaS)
- Events and entertainment at third-party venues (→ G&A unless venue-hire for office)

| Vendor Example | Spend | Confidence | Note |
|---|---|---|---|
| Tog UK Properties Limited | $263.8K | H | UK office rent |
| Zagrebtower D.O.O. | $183.8K | H | Croatian office building |
| Innovent Spaces Private Limited | $147.3K | H | Coworking (India) |
| Telefonica Global Services GmbH | $89.9K | H | Office telecom |
| Wework Singapore Pte. Ltd. | $64.4K | H | Coworking (Singapore) |
| HEP Elektra D.O.O. | $3.7K | H | Office electricity (Croatia) |

### G&A

**Definition:** General and administrative overhead that supports the whole company without belonging to a specific functional department. The default catch-all for company-wide costs.

**In scope:**
- Travel and expense management (Navan / TripActions)
- Employee benefits, insurance, and occupational health (Aetna, Jensten, Bupa, Cigna, ICICI Lombard)
- HR administration and people operations (Peakon, Benefit Systems)
- Government fees, regulatory filings (Cayman Islands Government, ICO — unless pure legal compliance → Legal)
- General recruitment agencies (not function-specific)
- Medical and occupational health vendors
- Office supplies, food delivery, canteen (Sodexo India if staff meals vs. FM)
- Company-wide social and morale spend (team events, gifts)
- Real persons appearing as vendors (if reclassified from individual-name flag)

**Out of scope (common errors to avoid):**
- Payroll processing (→ Finance)
- Benefits consulting that overlaps with Finance (→ Finance if financial advisory; G&A if HR operational)
- Physical office space (→ Facilities)
- Law firms and legal compliance tools (→ Legal)

| Vendor Example | Spend | Confidence | Note |
|---|---|---|---|
| Navan (Tripactions Inc) + Navan, Inc | $415.9K combined | H | Travel & expense management |
| Jensten Insurance Brokers | $142.7K | H | Employee insurance broker |
| Aetna Life And Casualty Ltd | $124.7K | H | Health insurance |
| Hr Solution International GmbH | $80.8K | H | HR staffing/admin (company-wide) |
| Peakon Aps | $17.1K | H | Employee engagement analytics |

### Legal

**Definition:** All spend on legal advice, representation, contract management, IP, immigration, and mandatory regulatory compliance fees.

**In scope:**
- Law firms and solicitors (Bisley Law, Zuric I Partneri, Pinsent Masons, etc.)
- In-house or virtual legal counsel services
- Immigration and visa management (Visalogic)
- IP management and patent filing (Lane IP)
- Notary services
- Regulatory compliance fees where primary purpose is legal (ICO registration)
- Legal technology (contract management platforms, eDiscovery)

**Out of scope (common errors to avoid):**
- M&A deal-specific legal work where legal is part of a transaction engagement (→ M&A, or split if significant)
- Insurance (→ G&A, even if legal liability insurance)
- Compliance consulting that is primarily accounting/tax (→ Finance)

| Vendor Example | Spend | Confidence | Note |
|---|---|---|---|
| Bisley Law Ltd | $67.4K | H | UK law firm |
| Zuric I Partneri D.O.O. | $24.1K | H | Croatian law firm |
| Visalogic Limited | $11.2K | H | Visa/immigration services |
| Pinsent Masons Mpillay LLP | $4.1K | H | International law firm |
| ICO | $67 | H | UK data protection regulator fee |

### M&A

**Definition:** Spend directly and exclusively tied to a specific acquisition, merger, or divestiture transaction. Not for ongoing advisory or BAU professional services.

**In scope:**
- Investment banks and deal advisors (Houlihan Lokey, Vector Capital)
- Virtual data rooms (SS&C Intralinks)
- Transaction-specific due diligence firms
- Deal-specific legal fees (if separable from ongoing Legal spend)
- Corporate finance advisory where the engagement is transaction-specific (RSM Corporate Finance — provisional)

**Out of scope (common errors to avoid):**
- Ongoing consulting or advisory engagements (→ Professional Services)
- General accounting or tax work (→ Finance)
- Integration implementation after deal close (→ Engineering or Professional Services)

| Vendor Example | Spend | Confidence | Note |
|---|---|---|---|
| Houlihan Lokey Advisors, LLC | $37.5K | H | Investment bank |
| Vector Capital Management LP | $32.4K | H | PE deal management |
| SS&C Intralinks Inc | $40K | H | Virtual data room |
| RSM UK Corporate Finance LLP | $117K | M | Corporate finance advisory — confirm scope |

### Marketing

**Definition:** Spend on demand generation, brand building, content creation, advertising, and customer acquisition — owned by the Marketing function.

**In scope:**
- Inbound marketing platforms (HubSpot)
- Content experience and distribution (Uberflip)
- SEO and content tools (SEMrush, Plus Your Business)
- PR and press release distribution (Cision PR Newswire)
- Social media and advertising tools
- Marketing agencies and creative consultancies (Big Frontier / Cult of Monday — if scope confirmed as marketing)
- LinkedIn (default, absent Sales Navigator evidence)
- Design software where Marketing-owned (not Product-owned)

**Out of scope (common errors to avoid):**
- Sales prospecting and CRM (→ Sales)
- Product design tools (→ Product)
- General content purchased as office reading (The Guardian → G&A)

| Vendor Example | Spend | Confidence | Note |
|---|---|---|---|
| HubSpot Ireland Limited | $32.2K | H | Inbound marketing platform |
| LinkedIn Ireland Limited | $55.6K | M | Marketing default; flip to Sales if Sales Navigator confirmed |
| Uberflip | $26.1K | H | Content experience platform |
| Mightyhive Ltd | $19K | H | Digital marketing agency |
| Cision PR Newswire | $2.1K | H | PR distribution |

### SaaS

**Definition:** IT-governed horizontal software with no single functional budget owner — tools used by 3 or more departments equally, administered by IT.

**In scope:**
- Company-wide productivity suites (Google Workspace, Microsoft 365)
- Cross-functional collaboration and project management (Trello, Smartsheet, Goto)
- Identity and access management tools
- IT security and monitoring tools not embedded in SDLC
- General e-signature tools (DocuSign) if company-wide
- HR information systems used across all functions

**Out of scope (common errors to avoid):**
- CRM and sales tools (→ Sales)
- Developer/SDLC infrastructure (→ Engineering)
- Product design tools (→ Product)
- FP&A and accounting software (→ Finance)
- Any tool clearly owned by one department's budget

| Vendor Example | Spend | Confidence | Note |
|---|---|---|---|
| Google Ireland Limited | $24.8K | M | Google Workspace assumed — flip to Engineering if GCP |
| Microsoft Ireland Operations | $9.8K | M | M365 assumed — flip to Engineering if Azure |
| Goto Technologies UK | $7.3K | H | GoTo Meeting / remote access; cross-functional |
| Trello | $6.7K | H | Cross-functional project management |
| Smartsheet Inc. | $3K | H | Cross-functional project management |

### Product

**Definition:** Tools and services used exclusively or primarily by Product Management, UX, and Design to define what to build and how users experience it.

**In scope:**
- Product roadmapping tools (Aha!)
- Design and prototyping software (Figma)
- User research and feedback platforms
- Product analytics (if Product-owned, not shared with Engineering)
- UX/design community memberships (Interaction Design Foundation)

**Out of scope (common errors to avoid):**
- Developer tools (→ Engineering)
- General project management used by multiple teams (→ SaaS)
- Customer support tools (→ Support)

| Vendor Example | Spend | Confidence | Note |
|---|---|---|---|
| Figma, Inc. | $460 | H | Design and prototyping |
| Aha! Labs Inc | $3.7K | H | Product roadmapping |
| Interaction Design Foundation | $138 | M | UX/design learning — Product or G&A |

### Professional Services

**Definition:** Ongoing external labor or advisory engaged to run BAU operations — consulting, staffing, and implementation firms that are not tied to a transaction.

**In scope:**
- IT consulting and implementation (Infosys, Cloud Technology Solutions)
- Management consulting (4I Advisory, Harmonic Group)
- Staffing and recruitment agencies for specific functions (Mason Frank for Salesforce roles)
- Training firms (Accutrainee)
- Professional services automation/delivery tools (Kimble)
- Industry body memberships where the primary value is standards/consulting (TMForum)

**Out of scope (common errors to avoid):**
- Transaction-specific advisors (→ M&A)
- Law firms (→ Legal)
- Accounting firms (→ Finance)
- General company-wide recruitment (→ G&A)

| Vendor Example | Spend | Confidence | Note |
|---|---|---|---|
| Infosys | $66.6K | H | IT services and consulting |
| Big Frontier Pty Ltd (Cult Of Monday) | $66.1K | M | Creative/consulting agency — confirm scope |
| Cloud Technology Solutions Ltd | $60.7K | H | Google Cloud IT consulting |
| Mason Frank International Ltd | $38.1K | H | Salesforce specialist staffing |
| Kimble Applications Ltd | $52.8K | H | PSA tool for PS delivery |

### Sales

**Definition:** Tools and services whose primary value driver is enabling the Sales function to generate revenue — pipeline, prospecting, engagement, and deal management.

**In scope:**
- CRM platforms (Salesforce — the most important assignment in this dataset)
- Sales engagement and sequencing tools (Outreach)
- Lead and contact intelligence (Cognism, Lusha)
- ABM and intent data platforms (6Sense)
- Sales-specific LinkedIn licences (Sales Navigator — if confirmed)
- Revenue operations tools

**Out of scope (common errors to avoid):**
- Inbound marketing / marketing automation (→ Marketing)
- General business intelligence used by multiple teams (→ SaaS or Engineering)
- Professional services automation (→ Professional Services)

| Vendor Example | Spend | Confidence | Note |
|---|---|---|---|
| Salesforce Uk Ltd-Uk | $3,117,226 | H | CRM — single largest vendor; unambiguously Sales |
| Cognism Limited | $27K | H | Lead intelligence / prospecting |
| Outreach Corporation | $9.2K | H | Sales engagement platform |
| Lusha | $2.6K | H | Contact intelligence |

### Support

**Definition:** Customer-facing support tools, services, and staffing that enable the post-sale customer success and support function.

**In scope:**
- Helpdesk and ticketing software
- Customer success platforms
- Support staffing and outsourced support
- Customer knowledge base tools
- Customer-facing certification and training (if owned by Support)

**Out of scope (common errors to avoid):**
- Internal IT helpdesk tools (→ SaaS or Engineering)
- Employee engagement and HR tools (→ G&A)

| Vendor Example | Spend | Confidence | Note |
|---|---|---|---|
| Performancepro | $10K | L | HR performance tool — G&A or Support; depends on user base |

### Finance

**Definition:** Spend directly tied to financial reporting, accounting, audit, tax, payroll, treasury, and financial compliance.

**In scope:**
- External audit and accounting firms (BDO, Grant Thornton, Crowe Horwath, PwC, Collards)
- Accounting and ERP software (Sage)
- FP&A and budgeting platforms (Planful)
- Tax advisory and compliance (Taxstudio, Porezno Savjetništvo Tuk)
- Payroll processing and international payroll (Australian Payroll Professionals, Eurofast)
- Financial data and benchmarking services

**Out of scope (common errors to avoid):**
- Travel and expense management (→ G&A)
- M&A-specific corporate finance advisory (→ M&A)
- Employee benefits consulting (→ G&A)
- General insurance (→ G&A)

| Vendor Example | Spend | Confidence | Note |
|---|---|---|---|
| BDO LLP | $343.1K | H | External audit and accounting |
| Sage UK Limited | $46.9K | H | Accounting software |
| Grant Thornton | $46.5K | H | Accounting and advisory |
| Planful, Inc. | $27.7K | H | FP&A software |
| Taxstudio, Ltd. | $14.6K | H | Tax advisory |

---

## Classification Decision Tree

Use this flowchart when unsure which department to assign.

```
START: What does this vendor primarily provide?

├── Physical workspace or office operations?
│   └── YES → **Facilities**
│       (rent, coworking, utilities, telecom, FM, parking)

├── Legal services, IP, immigration, or compliance fees?
│   └── YES → **Legal**

├── Financial reporting, audit, tax, accounting, or payroll?
│   └── YES → **Finance**
│       (unless deal-specific → M&A)

├── Transaction-specific deal advisory or VDR?
│   └── YES → **M&A**

├── Sales prospecting, CRM, or revenue enablement?
│   └── YES → **Sales**
│       ← SALESFORCE IS HERE (not SaaS)

├── Demand generation, brand, or marketing content?
│   └── YES → **Marketing**

├── Product design, roadmapping, or UX research?
│   └── YES → **Product**

├── Customer-facing support tools or staffing?
│   └── YES → **Support**

├── SDLC tools — developers use it to build/test/deploy?
│   └── YES → **Engineering**
│       (cloud infra always here, not SaaS)

├── Ongoing external consulting, staffing, or implementation?
│   └── YES → **Professional Services**
│       (not transaction-specific)

├── Horizontal software, no single functional owner, IT-governed?
│   └── YES → **SaaS**
│       (Google Workspace, M365, Trello, cross-functional tools)

└── Company-wide admin cost with no specific function?
    └── YES → **G&A**
        (travel, benefits, insurance, HR admin, government fees,
         medical, general recruitment, individual name vendors)
    └── STILL UNSURE → mark **R** (Requires Review)
```

---

## Confidence Scoring — Worked Examples

| Vendor | Assigned | Confidence | Worked Reasoning |
|---|---|---|---|
| Salesforce Uk Ltd-Uk | Sales | H | Name contains 'Salesforce' — the world's dominant CRM. Primary users are Sales reps. No applicable boundary dispute. Unambiguous. |
| BDO LLP | Finance | H | BDO is a Big 4-tier accounting and audit firm. No boundary dispute — 'LLP' confirms accounting partnership, not deal advisory. |
| Cloudcrossing BVBA | R | R | Belgian entity (BVBA). 'Cloudcrossing' could suggest IT/networking, but name alone is insufficient. T1 spend ($208.7K) requires research. |
| RSM UK Corporate Finance LLP | M&A (provisional) | M | 'Corporate Finance' in RSM's entity name signals deal advisory rather than standard accounting. Applied M&A vs Finance rule: Finance = accounting/audit; M&A = deal advisory. Provisional pending contract review. |
| Navan (Tripactions Inc) | G&A | H | Navan/TripActions is the leading T&E management platform. Company-wide admin cost. G&A vs Finance rule: travel management ≠ financial reporting. |
| Stipe Piric | R | R | 2-word title-case name matching individual-name pattern. No corporate keywords. Cannot classify without HR/Finance confirmation of whether this is a contractor invoice or expense reimbursement. |
| Garaža Firule D.O.O. | Facilities | R | Croatian 'Garaža' = garage/parking. Facilities is the correct assignment. But encoding corruption makes the name unreadable in the system — flag R until name is corrected. |
| Amazon Web Services Llc | Engineering | H | AWS = cloud infrastructure. SDLC-critical. SaaS vs Engineering rule: cloud infra → Engineering, not SaaS. Combined with AWS Inc. under canonical brand 'Amazon Web Services / Amazon'. |

---

## Brand Group Registry

The following multi-entity groups were identified in Step 1.
Use `canonical_brand` for grouping in analysis; do not merge rows.

| Canonical Brand | Entities | Combined Spend | Department Note |
|---|---|---|---|
| Amazon Web Services / Amazon | 4 | $112,893 | Engineering (AWS entities) + G&A (Amazon retail) — classify each row individually |
| Navan / TripActions | 2 | $415,913 | G&A — travel and expense management |
| Bupa Group | 2 | $35,263 | G&A — employee health insurance |
| Allianz | 2 | $7,069 | G&A — workers compensation insurance |
| HRsolution International | 2 | $87,810 | G&A — HR staffing and admin |
| Apple | 4 | $8,256 | Mixed — classify each row: hardware → Facilities or Engineering; software → SaaS |
| Acclime | 2 | $10,408 | Finance — international payroll and corporate services |
| 4I Group | 2 | $83,978 | Professional Services — management consulting |

---

*Operational reference guide for vendor department classification. Cross-reference with `mapping_philosophy.md`. Last updated: 2026-05-14.*