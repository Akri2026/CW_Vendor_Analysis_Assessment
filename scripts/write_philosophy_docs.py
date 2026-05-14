"""
Step 2: Vendor Categorization Philosophy & Mapping Guide
Writes mapping_philosophy.md and department_interpretation_guide.md to /outputs/
No Excel reading; all reasoning derived from Step 1 findings.
"""

import csv
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).parent.parent
OUTPUTS = BASE / "outputs"

# ── Load CSV to compute brand group spend at runtime ──────────────────────────
csv_path = OUTPUTS / "raw_valid_records_preview.csv"
vendors = []
with open(csv_path, encoding="utf-8") as f:
    for row in csv.DictReader(f):
        vendors.append({"name": row["vendor_name"], "cost": float(row["cost_usd"])})

# Canonical brand group registry (determined in Step 1 analysis)
BRAND_GROUPS = {
    "Amazon Web Services / Amazon": [
        "Amazon Web Services Llc",
        "Amazon Web Services Inc.",
        "Amazon.Co.Uk",
        "Amazon (Aus)",
    ],
    "Navan / TripActions": [
        "Navan (Tripactions Inc)",
        "Navan, Inc",
    ],
    "Bupa Group": [
        "Bupa- Supplier",
        "Bupa Australia",
    ],
    "Allianz": [
        "Allianz Australia Workers' Compensation (Victoria) Limited",
        "Allianz Wa",
    ],
    "HRsolution International": [
        "Hr Solution International Gmbh",
        "Hrsolution International Ag",
    ],
    "Apple": [
        "Apple Retail Uk Ltd",
        "Apple Pty Ltd",
        "Apple Distribution International Ltd",
        "Apple - Amer",
    ],
    "Acclime": [
        "Acclime Corporate Services",
        "Acclime Usa, Inc",
    ],
    "4I Group": [
        "4I Advisory Services",
        "4I Management Consulting Private Limited",
    ],
}

# Compute combined spend per group
name_to_cost = {v["name"]: v["cost"] for v in vendors}
group_spend = {}
for brand, members in BRAND_GROUPS.items():
    group_spend[brand] = sum(name_to_cost.get(m, 0) for m in members)

# Spend tier counts from Step 1
TIERS = [
    ("T1", "Strategic",   "≥ $100K",       13,   5_042_189, 63.9),
    ("T2", "Significant", "$25K – $99.9K",  27,    857_090, 10.9),
    ("T3", "Operational", "$10K – $24.9K",  39,    522_048,  6.6),
    ("T4", "Tail",        "$1K – $9.9K",   129,    340_006,  4.3),
    ("T5", "Noise",       "< $1K",         178,    126_028,  1.6),
]

TOTAL_SPEND = 7_887_360.40


# ══════════════════════════════════════════════════════════════════════════════
# OUTPUT 1: mapping_philosophy.md
# ══════════════════════════════════════════════════════════════════════════════

def build_mapping_philosophy():
    lines = []
    def h(level, text): lines.append(f"{'#' * level} {text}\n")
    def p(*args): lines.extend(args); lines.append("")
    def rule(text): lines.append(f"> **Governing Rule:** {text}\n")
    def table(headers, rows):
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("|" + "|".join(["---"] * len(headers)) + "|")
        for row in rows:
            lines.append("| " + " | ".join(str(c) for c in row) + " |")
        lines.append("")
    def hr(): lines.append("---\n")

    h(1, "Vendor Mapping Philosophy")
    p(
        "**Document type:** Strategic governance — defines the classification framework before any vendor is assigned a department.",
        "**Dataset:** 386 vendors, $7,887,360 total L12M spend, 0% pre-classified.",
        "**Authority:** All downstream classifications must conform to the rules in this document. Deviations require documented rationale.",
    )
    hr()

    # ── Governing Philosophy Statement ────────────────────────────────────────
    h(2, "Governing Philosophy")
    p(
        "**Departments represent budget accountability** — the functional cost center that would own this vendor relationship in an integrated org chart.",
        "",
        "This framing was chosen over three alternatives:",
    )
    table(
        ["Alternative", "Why Rejected"],
        [
            ["Software category (CRM, ERP, HRIS…)", "Fails for non-software vendors: law firms, insurance, coworking spaces, recruitment agencies"],
            ["Vendor type (SaaS, Professional Services…)", "'SaaS' is already one of the 12 categories — using vendor type as the primary principle would create circular reasoning"],
            ["Operational ownership (who manages the contract)", "Unknowable from vendor name alone; IT often administers contracts it doesn't budget-own (e.g., Salesforce)"],
            ["Business capability ownership", "Too abstract for integration planning; doesn't map to real cost centers the CFO will recognise"],
        ]
    )
    p(
        "**Why budget accountability works in a post-acquisition context:**",
        "- It answers the CFO's primary integration question: *which acquiring department absorbs this cost?*",
        "- It enables synergy identification: does the parent company have a competing contract in the same function?",
        "- It mirrors how integration workstreams are structured (Engineering track, Finance track, etc.)",
    )
    p(
        "**The taxonomy is intentionally hybrid.** Of the 12 Config categories, 8 are functional departments",
        "(Engineering, G&A, Legal, Marketing, Product, Sales, Support, Finance), 1 is physical (Facilities),",
        "1 is transaction-type (M&A), and 2 are cross-cutting overrides (SaaS, Professional Services).",
        "This hybrid design is the correct one — the three overrides exist precisely to handle vendors that",
        "don't have a single functional owner.",
    )
    p(
        "**Override hierarchy for the three non-functional categories:**",
        "",
        "1. **SaaS** — IT-governed horizontal software used by 3+ departments with no single budget owner. If a tool clearly serves one function's core workflow, use that function instead.",
        "2. **Professional Services** — Ongoing external labor or advisory engaged to operate the business (not tied to a transaction).",
        "3. **M&A** — Spend directly traceable to a specific acquisition, merger, or divestiture event.",
    )
    hr()

    # ── Q2: Boundary Disputes ─────────────────────────────────────────────────
    h(2, "Boundary Dispute Rules")
    p(
        "Each of the 7 pairs below has a governing rule followed by examples drawn from this dataset.",
        "When a vendor triggers one of these disputes, the rule supersedes intuition.",
    )

    # SaaS vs Engineering
    h(3, "1. SaaS vs Engineering")
    rule(
        "If the tool is part of the Software Development Lifecycle (SDLC) — used primarily by engineers "
        "to build, test, deploy, or monitor software — assign **Engineering**. "
        "If it is a general-purpose business application licensed company-wide by IT, assign **SaaS**."
    )
    table(
        ["Vendor", "Spend", "Decision", "Reasoning"],
        [
            ["Amazon Web Services Llc / Inc.", "$112K combined", "**Engineering**", "Core cloud infrastructure; SDLC-critical"],
            ["JetBrains S.R.O.", "$4.1K", "**Engineering**", "IDE; developer-exclusive tool"],
            ["Npm Inc", "$3.5K", "**Engineering**", "Package manager; part of build pipeline"],
            ["Papertrail Inc", "$3.9K", "**Engineering**", "Log management; SDLC monitoring"],
            ["Ag Grid Ltd", "$2.7K", "**Engineering**", "JavaScript data grid library"],
            ["Axosoft GitKraken", "$54", "**Engineering**", "Developer Git client"],
            ["Google Ireland Limited", "$24.8K", "**SaaS**", "Likely Google Workspace; company-wide productivity"],
            ["Microsoft Ireland Operations", "$9.8K", "**SaaS**", "Likely Microsoft 365; company-wide"],
            ["Goto Technologies UK", "$7.3K", "**SaaS**", "Remote access / meeting tool; cross-functional"],
            ["Trello", "$6.7K", "**SaaS**", "Project management; cross-functional"],
            ["Workato, Inc.", "$16.1K", "**Engineering**", "Integration platform; typically IT/Engineering-governed"],
        ]
    )

    # SaaS vs Product
    h(3, "2. SaaS vs Product")
    rule(
        "If the tool directly informs *what to build* or *how users experience the product*, "
        "or is used exclusively by Product/UX/Design teams, assign **Product**. "
        "If it is a general business tool the Product team uses alongside other functions, assign **SaaS**."
    )
    table(
        ["Vendor", "Spend", "Decision", "Reasoning"],
        [
            ["Figma, Inc.", "$460", "**Product**", "Design/prototyping; Product and UX-owned"],
            ["Aha! Labs Inc", "$3.7K", "**Product**", "Product roadmapping; Product-team exclusive"],
            ["Peakon Aps", "$17.1K", "**G&A**", "Employee engagement analytics; HR tool, not a product tool"],
            ["Planful, Inc.", "$27.7K", "**Finance**", "FP&A software; Finance budget-owned"],
            ["Tmforum", "$57.6K", "**Professional Services**", "Telecoms industry body membership; not product tooling"],
        ]
    )

    # SaaS vs Sales — CRITICAL
    h(3, "3. SaaS vs Sales  ← CRITICAL (Salesforce = 39.5% of total spend)")
    rule(
        "If the tool's primary value driver is enabling revenue generation — pipeline management, "
        "sales prospecting, engagement, or deal closing — assign **Sales**, regardless of who "
        "administers the contract. IT governance does not change budget ownership."
    )
    p(
        "> **The Salesforce decision:** Salesforce is the single largest vendor at $3,117,226 (39.5% of total spend).",
        "> It is a CRM. Its primary users are Sales. Its budget owner is Sales. It is **not SaaS**.",
        "> This single classification governs more spend than the next 9 vendors combined.",
    )
    table(
        ["Vendor", "Spend", "Decision", "Reasoning"],
        [
            ["Salesforce Uk Ltd-Uk", "$3,117,226", "**Sales**", "CRM; Sales-owned budget; primary users are Sales reps"],
            ["Cognism Limited", "$27K", "**Sales**", "Lead intelligence and prospecting; Sales-owned"],
            ["Outreach Corporation", "$9.2K", "**Sales**", "Sales engagement platform"],
            ["Lusha", "$2.6K", "**Sales**", "Contact intelligence for prospecting"],
            ["6Sense Insights Inc", "$76", "**Sales**", "ABM/intent data; revenue team-owned"],
            ["HubSpot Ireland Limited", "$32.2K", "**Marketing**", "Inbound marketing CRM; primary use is demand generation"],
            ["LinkedIn Ireland Limited", "$55.6K", "**Marketing**", "Default Marketing (LinkedIn Ads / Recruiter); Sales Navigator would flip to Sales — name alone insufficient to override"],
            ["Uberflip", "$26.1K", "**Marketing**", "Content experience platform; Marketing-owned"],
            ["Kimble Applications Ltd", "$52.8K", "**Professional Services**", "PSA tool for professional services delivery teams"],
        ]
    )

    # G&A vs Finance
    h(3, "4. G&A vs Finance")
    rule(
        "Assign **Finance** when spend is directly tied to financial reporting, accounting, audit, tax, "
        "treasury, payroll, or financial compliance. Assign **G&A** for general administrative overhead "
        "without a specific financial function: travel, employee benefits, HR admin, office supplies."
    )
    table(
        ["Vendor", "Spend", "Decision", "Reasoning"],
        [
            ["BDO LLP", "$343K", "**Finance**", "External audit and accounting firm"],
            ["RSM UK Corporate Finance LLP", "$117K", "**M&A** (provisional)", "'Corporate Finance' signals deal advisory; verify before finalising"],
            ["Sage UK Limited", "$46.9K", "**Finance**", "Accounting software"],
            ["Planful, Inc.", "$27.7K", "**Finance**", "FP&A / financial planning software"],
            ["Grant Thornton", "$46.5K", "**Finance**", "Accounting and business advisory firm"],
            ["Taxstudio, Ltd.", "$14.6K", "**Finance**", "Tax advisory services"],
            ["PricewaterhouseCoopers LLP", "$4.9K", "**Finance**", "Big 4 accounting (unless engagement is deal-specific → M&A)"],
            ["Australian Payroll Professionals", "$4.4K", "**Finance**", "Payroll processing is a Finance function"],
            ["Eurofast International", "$18.2K", "**Finance**", "International payroll and accounting services"],
            ["Navan / TripActions", "$415.9K combined", "**G&A**", "Travel and expense management is company-wide admin, not Finance"],
            ["Mercer Limited", "$5.4K", "**G&A**", "Benefits consulting; employee benefits = G&A, not Finance"],
        ]
    )

    # G&A vs Legal
    h(3, "5. G&A vs Legal")
    rule(
        "Assign **Legal** when the vendor's primary service is legal advice, representation, "
        "contract management, immigration/visa services, IP management, or regulatory compliance fees. "
        "All other administrative overhead → **G&A**."
    )
    table(
        ["Vendor", "Spend", "Decision", "Reasoning"],
        [
            ["Bisley Law Ltd", "$67.4K", "**Legal**", "Law firm"],
            ["Zuric I Partneri D.O.O.", "$24.1K", "**Legal**", "Croatian law firm"],
            ["Pinsent Masons Mpillay LLP", "$4.1K", "**Legal**", "International law firm"],
            ["Virtual Legal Counsel Ltd", "$4.8K", "**Legal**", "Legal services"],
            ["Visalogic Limited", "$11.2K", "**Legal**", "Immigration and visa management services"],
            ["ICO", "$67", "**Legal**", "UK Information Commissioner registration fee; data protection compliance"],
            ["Lane IP Limited", "$851", "**Legal**", "IP management and filing"],
            ["Kilgannon & Partners LLP", "$681", "**Legal**", "Law firm"],
            ["Induslaw", "$596", "**Legal**", "Indian law firm"],
            ["Jensten Insurance Brokers", "$142.7K", "**G&A**", "Insurance broker; employee and company policies = G&A, not Legal"],
        ]
    )

    # M&A vs Professional Services
    h(3, "6. M&A vs Professional Services")
    rule(
        "Assign **M&A** when the vendor was specifically engaged for a transaction (investment banking, "
        "deal due diligence, virtual data rooms). Assign **Professional Services** for ongoing external "
        "labor or advisory engaged to run business-as-usual operations. "
        "Default: investment banks and VDR providers → M&A; consulting and staffing firms → Professional Services."
    )
    table(
        ["Vendor", "Spend", "Decision", "Reasoning"],
        [
            ["Houlihan Lokey Advisors, LLC", "$37.5K", "**M&A**", "Investment bank; exclusively M&A advisory"],
            ["Vector Capital Management LP", "$32.4K", "**M&A**", "PE investment management; deal-related"],
            ["SS&C Intralinks Inc", "$40K", "**M&A**", "Virtual data room; deal-specific platform"],
            ["RSM UK Corporate Finance LLP", "$117K", "**M&A** (provisional)", "'Corporate Finance' in name signals deal advisory; confirm"],
            ["Infosys", "$66.6K", "**Professional Services**", "IT services and consulting; ongoing BAU engagement"],
            ["Big Frontier Pty Ltd (Cult Of Monday)", "$66.1K", "**Professional Services**", "Creative/marketing consultancy; BAU engagement"],
            ["Harmonic Group Limited", "$65.4K", "**Professional Services**", "Consulting and advisory; no deal signal"],
            ["Cloud Technology Solutions Ltd", "$60.7K", "**Professional Services**", "IT consulting (Google Cloud partner); BAU"],
            ["Mason Frank International Ltd", "$38.1K", "**Professional Services**", "Salesforce specialist recruitment/staffing"],
            ["Accutrainee Limited", "$38.8K", "**Professional Services**", "Training and recruitment firm"],
            ["4I Advisory Services", "$71.9K", "**Professional Services**", "Generic advisory; no transaction signal in name"],
            ["Westbrook Advisers", "$15.4K", "**R — Requires Review**", "'Advisers' could be M&A or PS; engagement purpose unknown"],
        ]
    )

    # Facilities vs G&A
    h(3, "7. Facilities vs G&A")
    rule(
        "Assign **Facilities** for the direct cost of physical workspace: rent, coworking fees, "
        "office maintenance, utilities, cleaning, parking, physical access control, and FM services. "
        "Assign **G&A** for administrative overhead that is not itself a physical space cost."
    )
    table(
        ["Vendor", "Spend", "Decision", "Reasoning"],
        [
            ["Tog UK Properties Limited", "$263.8K", "**Facilities**", "Commercial property / office rent (UK)"],
            ["Zagrebtower D.O.O.", "$183.8K", "**Facilities**", "Croatian office tower / rent"],
            ["Innovent Spaces Private Limited", "$147.3K", "**Facilities**", "Coworking and office spaces (India)"],
            ["Weking D.O.O.", "$144.1K", "**Facilities**", "Croatian office property"],
            ["GPT Space & Co", "$133.5K", "**Facilities**", "Australian office / event space"],
            ["Wework Singapore Pte. Ltd.", "$64.4K", "**Facilities**", "Coworking space"],
            ["Sodexo Svc India Private Limited", "$17.8K", "**Facilities**", "FM and catering services for office"],
            ["Jones Lang Lasalle (Nsw) Pty Ltd", "$16.3K", "**Facilities**", "Property management services"],
            ["Work Easy Space Solutions", "$14.9K", "**Facilities**", "Coworking / serviced offices"],
            ["Telefonica Global Services GmbH", "$89.9K", "**Facilities**", "Office telecom / connectivity = physical operations cost"],
            ["Jensten Insurance Brokers", "$142.7K", "**G&A**", "Insurance broker; not a physical space cost"],
            ["Navan / TripActions", "$415.9K combined", "**G&A**", "Travel management; not a physical space cost"],
        ]
    )
    hr()

    # ── Q3: Spend Tiers ───────────────────────────────────────────────────────
    h(2, "Spend Tiers and Classification Diligence")
    p(
        "Spend magnitude governs how much research effort to invest before assigning a department.",
        "Higher tiers require confirmed classification; lower tiers accept heuristic assignment.",
    )
    tier_rows = []
    for tier, label, threshold, count, spend, pct in TIERS:
        diligence = {
            "T1": "Full research required. Confirm vendor's primary service line before assigning. Confidence must be H or M. Escalate ambiguities immediately.",
            "T2": "Apply all boundary rules. Use vendor name + common knowledge. Target H or M confidence. Flag any L for review.",
            "T3": "Batch processing acceptable. Apply boundary rules. M confidence acceptable; flag R only if name is truly unresolvable.",
            "T4": "Expedited assignment via name pattern. L confidence acceptable. Correctness at category level; not sub-level nuance.",
            "T5": "Bulk heuristic assignment. Exclude from strategic reports. Most are meal/catering/courier/retail receipts.",
        }[tier]
        tier_rows.append([tier, label, threshold, count, f"${spend:,.0f}", f"{pct:.1f}%", diligence])
    table(
        ["Tier", "Label", "Threshold", "Vendors", "Spend", "% Total", "Classification Diligence"],
        tier_rows
    )
    p(
        "**T1 classification decisions with the highest strategic impact:**",
        f"- Salesforce UK ($3,117,226) → **Sales** — governs 39.5% of total spend; the most consequential single assignment",
        f"- Navan / TripActions ($415,913 combined) → **G&A** — two rows for one vendor; normalise before reporting",
        f"- BDO LLP ($343,081) → **Finance** — largest single Finance vendor",
        f"- RSM UK Corporate Finance ($117,078) → **M&A provisional** — name strongly implies deal advisory; verify",
        f"- Cloudcrossing BVBA ($208,675) → **R — Requires Review** — name gives no functional signal",
    )
    hr()

    # ── Q4: Multi-Entity Brand Grouping ───────────────────────────────────────
    h(2, "Multi-Entity Brand Grouping")
    p(
        "**Approach: preserve row-level data; add a canonical brand column.**",
        "",
        "Rules:",
        "1. **Do NOT merge rows** — `row_number`, `vendor_name`, and `cost_usd` remain untouched",
        "2. **Add `canonical_brand` column** — the normalised parent brand name",
        "3. **Add `brand_group_spend` column** — summed spend across all group members (computed field)",
        "4. **Add `is_multi_entity` flag** — True when two or more rows share the same canonical brand",
    )
    group_rows = []
    for brand, members in BRAND_GROUPS.items():
        spend = group_spend[brand]
        group_rows.append([
            brand,
            str(len(members)),
            " / ".join(f"`{m}`" for m in members),
            f"${spend:,.0f}",
        ])
    table(["Canonical Brand", "Entity Count", "Member Vendor Names", "Combined Spend"], group_rows)
    p(
        "> **Highest-risk near-duplicate:** Navan (Tripactions Inc) + Navan, Inc.",
        f"> Combined spend: ${group_spend['Navan / TripActions']:,.0f}. Two entries for one vendor — confirm before any recommendation.",
        ">",
        "> **Note on Apple:** Four entries totalling ~$9.6K across retail, distribution, and regional entities.",
        "> Likely a mix of hardware purchases (Facilities/Engineering) and software (SaaS). Classify each row individually.",
    )
    hr()

    # ── Q5: Classification Framework ──────────────────────────────────────────
    h(2, "Classification Framework")

    h(3, "6 Core Classification Principles")
    principles = [
        ("Budget accountability over administrative custody",
         "Classify by who OWNS the budget, not who manages the contract. "
         "Salesforce is Sales even if IT runs the licences."),
        ("Primary use over incidental use",
         "If 80%+ of a vendor's value flows to one function, assign to that function. "
         "Don't over-engineer cross-functional tools that happen to have secondary users."),
        ("Spend-weighted diligence",
         "Invest classification effort proportional to spend magnitude. "
         "T1/T2 vendors warrant research; T5 vendors warrant a heuristic. See Tier table."),
        ("Single assignment only",
         "Each vendor receives exactly ONE department. No split codes. "
         "Forced clarity surfaces real decisions instead of avoiding them."),
        ("Preserve source data",
         "Never modify vendor_name, cost_usd, or row_number. "
         "Classification is additive — new columns only: department_assigned, confidence, canonical_brand."),
        ("Boundary rules over intuition",
         "When a dispute applies, the governing rule in this document supersedes gut feel. "
         "Ad hoc overrides require documented rationale."),
    ]
    for i, (name, desc) in enumerate(principles, 1):
        lines.append(f"**{i}. {name}**")
        lines.append(f"{desc}")
        lines.append("")

    h(3, "Edge Case Rules")
    table(
        ["Vendor Type", "Governing Rule", "Assigned Category", "Examples from Dataset"],
        [
            ["Individual names (real persons)",
             "Flag `possible_individual_name=True`. Classify as Professional Services if likely contractor payment; G&A if HR/admin reimbursement. Mark confidence **R**.",
             "Professional Services or G&A",
             "Stipe Piric, John Smith, Fabiola Thistlewhaite, George Anchor, Susan Lee, Ansar Madovic"],
            ["False-positive individual names (companies)",
             "Apply corporate context to override the heuristic flag. Classify normally.",
             "Classify normally per rules",
             "Grant Thornton (Finance), Peakon Aps (G&A), Axosoft GitKraken (Engineering)"],
            ["Government entities",
             "→ G&A (regulatory or compliance payments; no functional owner).",
             "G&A",
             "Cayman Islands Government, Australian Taxation Office, ICO"],
            ["Insurance / health benefits",
             "→ G&A. Employee benefits are a company-wide cost with no single functional owner. No HR category exists in Config.",
             "G&A",
             "Aetna ($124.7K), Jensten ($142.7K), Bupa ($35.3K combined), Agram Life ($25K), Care Health ($24K), Cigna ($13.2K), Allianz ($7.1K combined), ICICI Lombard ($6K), Mercer ($5.4K)"],
            ["Recruitment agencies",
             "→ G&A if company-wide. → Engineering if name explicitly signals tech/IT recruitment. Check for functional signal in name.",
             "G&A or Engineering",
             "Technet IT Recruitment (Engineering), Cedar Recruitment (G&A), HR Solution (G&A), Mason Frank — Salesforce staffing (Professional Services)"],
            ["Events / entertainment",
             "→ Facilities if office-event catering. → G&A if company social/morale spend. → Marketing if client-facing. → Noise label if T5.",
             "Facilities / G&A / Marketing / Noise",
             "Tattu Manchester (G&A), Gaucho Restaurants (G&A), Uber Eats (Noise), Istra Wine (Noise)"],
            ["Coworking / serviced offices",
             "→ Facilities always, regardless of which team uses the space.",
             "Facilities",
             "WeWork ($64.4K), Innovent ($147.3K), GPT Space ($133.5K), Work Easy ($14.9K), Platinum Office D.O.O. ($62)"],
            ["Telecom / office utilities",
             "→ Facilities. Office connectivity and utilities are a physical operations cost, not IT.",
             "Facilities",
             "Telefonica Global ($89.9K), Hrvatski Telekom ($18.1K), British Telecommunications ($1.5K), Starhub ($2.2K), Telemach ($5.1K)"],
            ["Medical / occupational health",
             "→ G&A. Employee wellness is company-wide; no HR category in Config.",
             "G&A",
             "Specijalisticka Ordinacija x3 (~$20 each), Ustanova Za Medicinu Rada ($20)"],
            ["Encoding-corrupted names (11 vendors)",
             "Attempt transliteration. If decodable, classify normally. If not, assign best guess from geographic/linguistic context. Mark confidence **R**.",
             "Varies (mostly Facilities or G&A — Croatian D.O.O. entities)",
             "Garaža Firule (Facilities — parking garage), Sveuč. Zagreb (Facilities — university venue)"],
            ["Training / certification",
             "→ Engineering if technical/developer training. → G&A if general HR/people development. → Support if customer-facing certification.",
             "Engineering / G&A / Support",
             "Pluralsight (Engineering), Accutrainee (Professional Services), Interaction Design Foundation (Product)"],
        ]
    )

    h(3, "Fallback Rules — Priority Order")
    fallbacks = [
        "Name unambiguously identifies function → assign directly, confidence **H**",
        "Name is ambiguous, Tier 1 or 2 → consult boundary dispute table; if still unclear, mark **R** (Requires Review) for human input before proceeding",
        "Name is ambiguous, Tier 3 → apply boundary dispute table; assign confidence **M**",
        "Name is ambiguous, Tier 4 → assign most probable category from name pattern; confidence **L**",
        "Name gives no signal, Tier 5 → assign G&A as catch-all; confidence **N** (Noise)",
        "Encoding-corrupted name → attempt transliteration; apply above rules if successful; mark **R** if not",
        "Confirmed individual name (real person) → mark **R**, note 'requires HR/Finance clarification'",
    ]
    for i, rule_text in enumerate(fallbacks, 1):
        lines.append(f"{i}. {rule_text}")
    lines.append("")

    h(3, "Confidence Scoring Framework")
    table(
        ["Score", "Label", "Definition", "Required Action"],
        [
            ["H", "High",
             "Vendor name clearly and unambiguously maps to one department. No applicable boundary dispute. Primary use is self-evident.",
             "Proceed. No review needed."],
            ["M", "Medium",
             "Vendor fits 2+ categories. A governing boundary rule was applied to choose. Classification is defensible but not self-evident.",
             "Proceed. Document which rule was applied."],
            ["L", "Low",
             "Vendor name gives minimal signal. Classification is best-guess from name pattern or geography alone.",
             "Flag for batch review. Lower-priority."],
            ["R", "Requires Review",
             "Encoding-corrupted name, confirmed individual name, genuine multi-function ambiguity, or T1/T2 vendor where the governing rule produces two equally valid outputs.",
             "Do NOT finalise without human input. Escalate."],
            ["N", "Noise",
             "Tier 5 vendor (< $1K). Classification assigned but has no strategic relevance.",
             "Exclude from strategic analysis outputs. Bulk-assign; no diligence required."],
        ]
    )
    hr()

    # ── Key Assumptions & Unresolved Ambiguities ──────────────────────────────
    h(2, "Key Assumptions")
    assumptions = [
        "**Salesforce = Sales** (not SaaS). The most consequential single decision: 39.5% of spend moves on this choice.",
        "**Navan / TripActions = one vendor** (two row entries). Combined spend $415,913 → G&A. Normalise before any department-level reporting.",
        "**Insurance and employee benefits = G&A** (no HR category exists in Config; benefits are company-wide admin cost).",
        "**Telecom and office utilities = Facilities** (office connectivity is a physical operations cost, not an IT cost).",
        "**AWS / cloud infrastructure = Engineering** (not SaaS; SDLC-critical infrastructure owned by Engineering).",
        "**RSM UK Corporate Finance = M&A provisional** — 'Corporate Finance' in the name strongly implies deal advisory; must be confirmed against contract before finalising.",
        "**Google Ireland = SaaS** (assumed to be Google Workspace, not Google Cloud Platform; GCP would flip to Engineering).",
        "**Microsoft Ireland = SaaS** (assumed to be Microsoft 365, not Azure; Azure would flip to Engineering).",
    ]
    for a in assumptions:
        lines.append(f"- {a}")
    lines.append("")

    h(2, "Unresolved Ambiguities — Flagged R")
    ambiguities = [
        ("Cloudcrossing BVBA", "$208,675", "T1",
         "Belgian entity; name gives zero functional signal. Could be telecoms, IT reseller, or professional services. Requires vendor website lookup before classification."),
        ("RSM UK Corporate Finance LLP", "$117,078", "T1",
         "'Corporate Finance' implies M&A deal advisory, but RSM also provides Finance/accounting services. Confirm engagement scope."),
        ("Sveu[corrupted] Zagreb / Studentski Centar", "$44,299", "T2",
         "University of Zagreb student center — likely a Facilities venue booking. Croatian-speaker or contract review needed to confirm."),
        ("Big Frontier Pty Ltd (Cult Of Monday)", "$66,131", "T2",
         "Creative/marketing agency vs. general management consultancy. Classification (Marketing vs. Professional Services) depends on what they actually delivered."),
        ("4I Advisory Services", "$71,860", "T2",
         "Generic advisory firm. Could be M&A, Professional Services, or G&A depending on engagement scope. Classified Professional Services provisionally."),
        ("Westbrook Advisers", "$15,360", "T3",
         "'Advisers' alone is insufficient to distinguish M&A from Professional Services. Engagement purpose unknown."),
        ("Harmonic Group Limited", "$65,418", "T2",
         "Consulting/advisory firm with generic name. Professional Services provisionally; confirm scope."),
    ]
    for vendor, spend, tier, note in ambiguities:
        lines.append(f"- **{vendor}** ({spend}, {tier}): {note}")
    lines.append("")
    hr()

    lines.append("*This document governs all downstream vendor classification. Last updated: 2026-05-14.*")
    return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════════════
# OUTPUT 2: department_interpretation_guide.md
# ══════════════════════════════════════════════════════════════════════════════

def build_department_guide():
    lines = []
    def h(level, text): lines.append(f"{'#' * level} {text}\n")
    def p(*args): lines.extend(args); lines.append("")
    def table(headers, rows):
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("|" + "|".join(["---"] * len(headers)) + "|")
        for row in rows:
            lines.append("| " + " | ".join(str(c) for c in row) + " |")
        lines.append("")
    def hr(): lines.append("---\n")

    h(1, "Department Interpretation Guide")
    p(
        "**Operational reference document.** Use this during classification to look up",
        "per-department definitions, inclusion/exclusion rules, and worked examples.",
        "All decisions must conform to `mapping_philosophy.md`.",
    )
    hr()

    # ── Quick Reference Card ─────────────────────────────────────────────────
    h(2, "Quick Reference Card — All 12 Departments")
    table(
        ["Department", "One-Line Definition", "Typical Spend Types"],
        [
            ["Engineering", "Tools and infrastructure used to build, test, deploy, and monitor the product", "Cloud infra, developer tools, CI/CD, logging, monitoring"],
            ["Facilities", "Direct cost of physical workspace and office operations", "Rent, coworking, utilities, telecom, FM services, parking"],
            ["G&A", "General administrative overhead with no single functional owner", "Travel, benefits/insurance, HR admin, government fees, office supplies"],
            ["Legal", "Legal advice, representation, compliance, IP, and immigration services", "Law firms, legal tech, visa/immigration, IP management, regulator fees"],
            ["M&A", "Spend directly tied to a specific acquisition or merger transaction", "Investment banks, VDRs, deal due diligence, transaction legal"],
            ["Marketing", "Demand generation, brand, content, and customer acquisition", "Marketing software, agencies, PR, advertising, content tools"],
            ["SaaS", "IT-governed horizontal software with no single functional budget owner", "Cross-functional productivity, collaboration, and business tools"],
            ["Product", "Tools and research used by Product/UX/Design to define and shape the product", "Roadmapping, design, user research, prototyping tools"],
            ["Professional Services", "Ongoing external labor or advisory engaged for BAU operations", "IT consulting, management consulting, staffing, training"],
            ["Sales", "Revenue generation tools and services owned by the Sales function", "CRM, sales engagement, prospecting, lead intelligence"],
            ["Support", "Customer-facing support tools and services", "Helpdesk software, customer success tools, support staffing"],
            ["Finance", "Financial reporting, accounting, audit, tax, payroll, and treasury", "Accounting software, audit firms, tax advisors, FP&A tools"],
        ]
    )
    hr()

    # ── Per-Department Deep Dives ─────────────────────────────────────────────
    h(2, "Per-Department Definitions")

    depts = [
        {
            "name": "Engineering",
            "definition": "Spend on tools and infrastructure that engineers use directly to build, test, deploy, or monitor the product or its underlying systems.",
            "in_scope": [
                "Cloud infrastructure (AWS, GCP, Azure) — always Engineering, never SaaS",
                "Developer IDEs and editors (JetBrains, VS Code extensions)",
                "Source control and Git tools (GitKraken, GitHub)",
                "CI/CD pipelines, build tools, package managers (npm)",
                "Logging, monitoring, and observability (Papertrail, Datadog)",
                "Data grid and frontend libraries (Ag Grid)",
                "Integration platforms where Engineering is the operator (Workato)",
                "IT recruitment specifically for technical roles",
            ],
            "out_scope": [
                "General-purpose productivity software (→ SaaS)",
                "Design and prototyping tools (→ Product)",
                "Cloud spend for marketing analytics or BI (→ Marketing or Finance)",
                "General telecom / office internet (→ Facilities)",
            ],
            "examples": [
                ("Amazon Web Services Llc / Inc.", "$112K combined", "H", "Core cloud infra"),
                ("JetBrains S.R.O.", "$4.1K", "H", "Developer IDE"),
                ("Npm Inc", "$3.5K", "H", "Package manager"),
                ("Papertrail Inc", "$3.9K", "H", "Log management"),
                ("Workato, Inc.", "$16.1K", "M", "Integration platform — Engineering if Eng-governed"),
            ],
        },
        {
            "name": "Facilities",
            "definition": "Direct cost of providing and maintaining physical workspace, including rent, coworking, utilities, telecom, and facilities management services.",
            "in_scope": [
                "Office rent and commercial property leases",
                "Coworking and serviced office memberships (WeWork, Innovent, GPT Space)",
                "Office telecom and internet connectivity (Telefonica, Telemach, British Telecom)",
                "Facilities management and catering (Sodexo)",
                "Property management firms (Jones Lang Lasalle)",
                "Parking, cleaning, security, and physical access control",
                "Utilities (electricity, water, gas — e.g., HEP Elektra)",
            ],
            "out_scope": [
                "Travel management (→ G&A)",
                "Insurance and employee benefits (→ G&A)",
                "Corporate IT infrastructure (→ Engineering or SaaS)",
                "Events and entertainment at third-party venues (→ G&A unless venue-hire for office)",
            ],
            "examples": [
                ("Tog UK Properties Limited", "$263.8K", "H", "UK office rent"),
                ("Zagrebtower D.O.O.", "$183.8K", "H", "Croatian office building"),
                ("Innovent Spaces Private Limited", "$147.3K", "H", "Coworking (India)"),
                ("Telefonica Global Services GmbH", "$89.9K", "H", "Office telecom"),
                ("Wework Singapore Pte. Ltd.", "$64.4K", "H", "Coworking (Singapore)"),
                ("HEP Elektra D.O.O.", "$3.7K", "H", "Office electricity (Croatia)"),
            ],
        },
        {
            "name": "G&A",
            "definition": "General and administrative overhead that supports the whole company without belonging to a specific functional department. The default catch-all for company-wide costs.",
            "in_scope": [
                "Travel and expense management (Navan / TripActions)",
                "Employee benefits, insurance, and occupational health (Aetna, Jensten, Bupa, Cigna, ICICI Lombard)",
                "HR administration and people operations (Peakon, Benefit Systems)",
                "Government fees, regulatory filings (Cayman Islands Government, ICO — unless pure legal compliance → Legal)",
                "General recruitment agencies (not function-specific)",
                "Medical and occupational health vendors",
                "Office supplies, food delivery, canteen (Sodexo India if staff meals vs. FM)",
                "Company-wide social and morale spend (team events, gifts)",
                "Real persons appearing as vendors (if reclassified from individual-name flag)",
            ],
            "out_scope": [
                "Payroll processing (→ Finance)",
                "Benefits consulting that overlaps with Finance (→ Finance if financial advisory; G&A if HR operational)",
                "Physical office space (→ Facilities)",
                "Law firms and legal compliance tools (→ Legal)",
            ],
            "examples": [
                ("Navan (Tripactions Inc) + Navan, Inc", "$415.9K combined", "H", "Travel & expense management"),
                ("Jensten Insurance Brokers", "$142.7K", "H", "Employee insurance broker"),
                ("Aetna Life And Casualty Ltd", "$124.7K", "H", "Health insurance"),
                ("Hr Solution International GmbH", "$80.8K", "H", "HR staffing/admin (company-wide)"),
                ("Peakon Aps", "$17.1K", "H", "Employee engagement analytics"),
            ],
        },
        {
            "name": "Legal",
            "definition": "All spend on legal advice, representation, contract management, IP, immigration, and mandatory regulatory compliance fees.",
            "in_scope": [
                "Law firms and solicitors (Bisley Law, Zuric I Partneri, Pinsent Masons, etc.)",
                "In-house or virtual legal counsel services",
                "Immigration and visa management (Visalogic)",
                "IP management and patent filing (Lane IP)",
                "Notary services",
                "Regulatory compliance fees where primary purpose is legal (ICO registration)",
                "Legal technology (contract management platforms, eDiscovery)",
            ],
            "out_scope": [
                "M&A deal-specific legal work where legal is part of a transaction engagement (→ M&A, or split if significant)",
                "Insurance (→ G&A, even if legal liability insurance)",
                "Compliance consulting that is primarily accounting/tax (→ Finance)",
            ],
            "examples": [
                ("Bisley Law Ltd", "$67.4K", "H", "UK law firm"),
                ("Zuric I Partneri D.O.O.", "$24.1K", "H", "Croatian law firm"),
                ("Visalogic Limited", "$11.2K", "H", "Visa/immigration services"),
                ("Pinsent Masons Mpillay LLP", "$4.1K", "H", "International law firm"),
                ("ICO", "$67", "H", "UK data protection regulator fee"),
            ],
        },
        {
            "name": "M&A",
            "definition": "Spend directly and exclusively tied to a specific acquisition, merger, or divestiture transaction. Not for ongoing advisory or BAU professional services.",
            "in_scope": [
                "Investment banks and deal advisors (Houlihan Lokey, Vector Capital)",
                "Virtual data rooms (SS&C Intralinks)",
                "Transaction-specific due diligence firms",
                "Deal-specific legal fees (if separable from ongoing Legal spend)",
                "Corporate finance advisory where the engagement is transaction-specific (RSM Corporate Finance — provisional)",
            ],
            "out_scope": [
                "Ongoing consulting or advisory engagements (→ Professional Services)",
                "General accounting or tax work (→ Finance)",
                "Integration implementation after deal close (→ Engineering or Professional Services)",
            ],
            "examples": [
                ("Houlihan Lokey Advisors, LLC", "$37.5K", "H", "Investment bank"),
                ("Vector Capital Management LP", "$32.4K", "H", "PE deal management"),
                ("SS&C Intralinks Inc", "$40K", "H", "Virtual data room"),
                ("RSM UK Corporate Finance LLP", "$117K", "M", "Corporate finance advisory — confirm scope"),
            ],
        },
        {
            "name": "Marketing",
            "definition": "Spend on demand generation, brand building, content creation, advertising, and customer acquisition — owned by the Marketing function.",
            "in_scope": [
                "Inbound marketing platforms (HubSpot)",
                "Content experience and distribution (Uberflip)",
                "SEO and content tools (SEMrush, Plus Your Business)",
                "PR and press release distribution (Cision PR Newswire)",
                "Social media and advertising tools",
                "Marketing agencies and creative consultancies (Big Frontier / Cult of Monday — if scope confirmed as marketing)",
                "LinkedIn (default, absent Sales Navigator evidence)",
                "Design software where Marketing-owned (not Product-owned)",
            ],
            "out_scope": [
                "Sales prospecting and CRM (→ Sales)",
                "Product design tools (→ Product)",
                "General content purchased as office reading (The Guardian → G&A)",
            ],
            "examples": [
                ("HubSpot Ireland Limited", "$32.2K", "H", "Inbound marketing platform"),
                ("LinkedIn Ireland Limited", "$55.6K", "M", "Marketing default; flip to Sales if Sales Navigator confirmed"),
                ("Uberflip", "$26.1K", "H", "Content experience platform"),
                ("Mightyhive Ltd", "$19K", "H", "Digital marketing agency"),
                ("Cision PR Newswire", "$2.1K", "H", "PR distribution"),
            ],
        },
        {
            "name": "SaaS",
            "definition": "IT-governed horizontal software with no single functional budget owner — tools used by 3 or more departments equally, administered by IT.",
            "in_scope": [
                "Company-wide productivity suites (Google Workspace, Microsoft 365)",
                "Cross-functional collaboration and project management (Trello, Smartsheet, Goto)",
                "Identity and access management tools",
                "IT security and monitoring tools not embedded in SDLC",
                "General e-signature tools (DocuSign) if company-wide",
                "HR information systems used across all functions",
            ],
            "out_scope": [
                "CRM and sales tools (→ Sales)",
                "Developer/SDLC infrastructure (→ Engineering)",
                "Product design tools (→ Product)",
                "FP&A and accounting software (→ Finance)",
                "Any tool clearly owned by one department's budget",
            ],
            "examples": [
                ("Google Ireland Limited", "$24.8K", "M", "Google Workspace assumed — flip to Engineering if GCP"),
                ("Microsoft Ireland Operations", "$9.8K", "M", "M365 assumed — flip to Engineering if Azure"),
                ("Goto Technologies UK", "$7.3K", "H", "GoTo Meeting / remote access; cross-functional"),
                ("Trello", "$6.7K", "H", "Cross-functional project management"),
                ("Smartsheet Inc.", "$3K", "H", "Cross-functional project management"),
            ],
        },
        {
            "name": "Product",
            "definition": "Tools and services used exclusively or primarily by Product Management, UX, and Design to define what to build and how users experience it.",
            "in_scope": [
                "Product roadmapping tools (Aha!)",
                "Design and prototyping software (Figma)",
                "User research and feedback platforms",
                "Product analytics (if Product-owned, not shared with Engineering)",
                "UX/design community memberships (Interaction Design Foundation)",
            ],
            "out_scope": [
                "Developer tools (→ Engineering)",
                "General project management used by multiple teams (→ SaaS)",
                "Customer support tools (→ Support)",
            ],
            "examples": [
                ("Figma, Inc.", "$460", "H", "Design and prototyping"),
                ("Aha! Labs Inc", "$3.7K", "H", "Product roadmapping"),
                ("Interaction Design Foundation", "$138", "M", "UX/design learning — Product or G&A"),
            ],
        },
        {
            "name": "Professional Services",
            "definition": "Ongoing external labor or advisory engaged to run BAU operations — consulting, staffing, and implementation firms that are not tied to a transaction.",
            "in_scope": [
                "IT consulting and implementation (Infosys, Cloud Technology Solutions)",
                "Management consulting (4I Advisory, Harmonic Group)",
                "Staffing and recruitment agencies for specific functions (Mason Frank for Salesforce roles)",
                "Training firms (Accutrainee)",
                "Professional services automation/delivery tools (Kimble)",
                "Industry body memberships where the primary value is standards/consulting (TMForum)",
            ],
            "out_scope": [
                "Transaction-specific advisors (→ M&A)",
                "Law firms (→ Legal)",
                "Accounting firms (→ Finance)",
                "General company-wide recruitment (→ G&A)",
            ],
            "examples": [
                ("Infosys", "$66.6K", "H", "IT services and consulting"),
                ("Big Frontier Pty Ltd (Cult Of Monday)", "$66.1K", "M", "Creative/consulting agency — confirm scope"),
                ("Cloud Technology Solutions Ltd", "$60.7K", "H", "Google Cloud IT consulting"),
                ("Mason Frank International Ltd", "$38.1K", "H", "Salesforce specialist staffing"),
                ("Kimble Applications Ltd", "$52.8K", "H", "PSA tool for PS delivery"),
            ],
        },
        {
            "name": "Sales",
            "definition": "Tools and services whose primary value driver is enabling the Sales function to generate revenue — pipeline, prospecting, engagement, and deal management.",
            "in_scope": [
                "CRM platforms (Salesforce — the most important assignment in this dataset)",
                "Sales engagement and sequencing tools (Outreach)",
                "Lead and contact intelligence (Cognism, Lusha)",
                "ABM and intent data platforms (6Sense)",
                "Sales-specific LinkedIn licences (Sales Navigator — if confirmed)",
                "Revenue operations tools",
            ],
            "out_scope": [
                "Inbound marketing / marketing automation (→ Marketing)",
                "General business intelligence used by multiple teams (→ SaaS or Engineering)",
                "Professional services automation (→ Professional Services)",
            ],
            "examples": [
                ("Salesforce Uk Ltd-Uk", "$3,117,226", "H", "CRM — single largest vendor; unambiguously Sales"),
                ("Cognism Limited", "$27K", "H", "Lead intelligence / prospecting"),
                ("Outreach Corporation", "$9.2K", "H", "Sales engagement platform"),
                ("Lusha", "$2.6K", "H", "Contact intelligence"),
            ],
        },
        {
            "name": "Support",
            "definition": "Customer-facing support tools, services, and staffing that enable the post-sale customer success and support function.",
            "in_scope": [
                "Helpdesk and ticketing software",
                "Customer success platforms",
                "Support staffing and outsourced support",
                "Customer knowledge base tools",
                "Customer-facing certification and training (if owned by Support)",
            ],
            "out_scope": [
                "Internal IT helpdesk tools (→ SaaS or Engineering)",
                "Employee engagement and HR tools (→ G&A)",
            ],
            "examples": [
                ("Performancepro", "$10K", "L", "HR performance tool — G&A or Support; depends on user base"),
            ],
        },
        {
            "name": "Finance",
            "definition": "Spend directly tied to financial reporting, accounting, audit, tax, payroll, treasury, and financial compliance.",
            "in_scope": [
                "External audit and accounting firms (BDO, Grant Thornton, Crowe Horwath, PwC, Collards)",
                "Accounting and ERP software (Sage)",
                "FP&A and budgeting platforms (Planful)",
                "Tax advisory and compliance (Taxstudio, Porezno Savjetništvo Tuk)",
                "Payroll processing and international payroll (Australian Payroll Professionals, Eurofast)",
                "Financial data and benchmarking services",
            ],
            "out_scope": [
                "Travel and expense management (→ G&A)",
                "M&A-specific corporate finance advisory (→ M&A)",
                "Employee benefits consulting (→ G&A)",
                "General insurance (→ G&A)",
            ],
            "examples": [
                ("BDO LLP", "$343.1K", "H", "External audit and accounting"),
                ("Sage UK Limited", "$46.9K", "H", "Accounting software"),
                ("Grant Thornton", "$46.5K", "H", "Accounting and advisory"),
                ("Planful, Inc.", "$27.7K", "H", "FP&A software"),
                ("Taxstudio, Ltd.", "$14.6K", "H", "Tax advisory"),
            ],
        },
    ]

    for dept in depts:
        h(3, dept["name"])
        p(f"**Definition:** {dept['definition']}")
        lines.append("**In scope:**")
        for item in dept["in_scope"]:
            lines.append(f"- {item}")
        lines.append("")
        lines.append("**Out of scope (common errors to avoid):**")
        for item in dept["out_scope"]:
            lines.append(f"- {item}")
        lines.append("")
        if dept.get("examples"):
            table(
                ["Vendor Example", "Spend", "Confidence", "Note"],
                dept["examples"]
            )

    hr()

    # ── Decision Tree ─────────────────────────────────────────────────────────
    h(2, "Classification Decision Tree")
    p("Use this flowchart when unsure which department to assign.")
    decision_tree = """
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
"""
    lines.append("```")
    lines.append(decision_tree.strip())
    lines.append("```")
    lines.append("")
    hr()

    # ── Confidence Scoring with Worked Examples ───────────────────────────────
    h(2, "Confidence Scoring — Worked Examples")
    table(
        ["Vendor", "Assigned", "Confidence", "Worked Reasoning"],
        [
            ["Salesforce Uk Ltd-Uk", "Sales", "H",
             "Name contains 'Salesforce' — the world's dominant CRM. Primary users are Sales reps. No applicable boundary dispute. Unambiguous."],
            ["BDO LLP", "Finance", "H",
             "BDO is a Big 4-tier accounting and audit firm. No boundary dispute — 'LLP' confirms accounting partnership, not deal advisory."],
            ["Cloudcrossing BVBA", "R", "R",
             "Belgian entity (BVBA). 'Cloudcrossing' could suggest IT/networking, but name alone is insufficient. T1 spend ($208.7K) requires research."],
            ["RSM UK Corporate Finance LLP", "M&A (provisional)", "M",
             "'Corporate Finance' in RSM's entity name signals deal advisory rather than standard accounting. Applied M&A vs Finance rule: Finance = accounting/audit; M&A = deal advisory. Provisional pending contract review."],
            ["Navan (Tripactions Inc)", "G&A", "H",
             "Navan/TripActions is the leading T&E management platform. Company-wide admin cost. G&A vs Finance rule: travel management ≠ financial reporting."],
            ["Stipe Piric", "R", "R",
             "2-word title-case name matching individual-name pattern. No corporate keywords. Cannot classify without HR/Finance confirmation of whether this is a contractor invoice or expense reimbursement."],
            ["Garaža Firule D.O.O.", "Facilities", "R",
             "Croatian 'Garaža' = garage/parking. Facilities is the correct assignment. But encoding corruption makes the name unreadable in the system — flag R until name is corrected."],
            ["Amazon Web Services Llc", "Engineering", "H",
             "AWS = cloud infrastructure. SDLC-critical. SaaS vs Engineering rule: cloud infra → Engineering, not SaaS. Combined with AWS Inc. under canonical brand 'Amazon Web Services / Amazon'."],
        ]
    )
    hr()

    # ── Brand Group Registry ──────────────────────────────────────────────────
    h(2, "Brand Group Registry")
    p(
        "The following multi-entity groups were identified in Step 1.",
        "Use `canonical_brand` for grouping in analysis; do not merge rows.",
    )
    registry_rows = []
    for brand, members in BRAND_GROUPS.items():
        spend = group_spend[brand]
        dept_note = {
            "Amazon Web Services / Amazon": "Engineering (AWS entities) + G&A (Amazon retail) — classify each row individually",
            "Navan / TripActions": "G&A — travel and expense management",
            "Bupa Group": "G&A — employee health insurance",
            "Allianz": "G&A — workers compensation insurance",
            "HRsolution International": "G&A — HR staffing and admin",
            "Apple": "Mixed — classify each row: hardware → Facilities or Engineering; software → SaaS",
            "Acclime": "Finance — international payroll and corporate services",
            "4I Group": "Professional Services — management consulting",
        }.get(brand, "Classify each row individually")
        registry_rows.append([
            brand,
            str(len(members)),
            f"${spend:,.0f}",
            dept_note,
        ])
    table(
        ["Canonical Brand", "Entities", "Combined Spend", "Department Note"],
        registry_rows
    )
    hr()

    lines.append("*Operational reference guide for vendor department classification. Cross-reference with `mapping_philosophy.md`. Last updated: 2026-05-14.*")
    return "\n".join(lines)


# ── Write files ───────────────────────────────────────────────────────────────

philosophy_content = build_mapping_philosophy()
guide_content = build_department_guide()

(OUTPUTS / "mapping_philosophy.md").write_text(philosophy_content, encoding="utf-8")
print("✓ mapping_philosophy.md written")

(OUTPUTS / "department_interpretation_guide.md").write_text(guide_content, encoding="utf-8")
print("✓ department_interpretation_guide.md written")

print(f"\nOutputs written to: {OUTPUTS}/")
print(f"  mapping_philosophy.md         — {len(philosophy_content):,} chars")
print(f"  department_interpretation_guide.md — {len(guide_content):,} chars")
