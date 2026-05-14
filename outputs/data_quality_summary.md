# Data Quality Summary

**Source:** `Vendor Analysis Assessment` tab  
**Analysis date:** 2026-05-14  

---

## 1. Record Counts

| Metric | Count |
|--------|-------|
| Total rows in sheet (excl. header) | 813 |
| Populated vendor records | 386 |
| Blank / formatting-only rows | 427 |
| Header row | 1 |

---

## 2. Column Completeness

| Column | Populated | Null | Null % | Status |
|--------|-----------|------|--------|--------|
| Vendor Name | 386 | 0 | 0% | ✓ Complete |
| Department | 0 | 386 | 100% | ✗ Empty |
| Cost (USD) | 386 | 0 | 0% | ✓ Complete |
| 1-line Description | 0 | 386 | 100% | ✗ Empty |
| Suggestions | 0 | 386 | 100% | ✗ Empty |

> **Critical:** Department, Description, and Suggestions are 100% empty.
> The dataset as delivered contains only vendor names and spend figures.
> All downstream department-level analysis requires manual or AI-assisted categorization.

---

## 3. Duplicate Analysis

**Exact duplicate vendor names:** 0

> No exact duplicates found.

**Near-duplicate groups (normalized, legal suffix stripped):** 1

| Normalized Root | Variants |
|----------------|----------|
| `amazon web services` | Amazon Web Services Llc / Amazon Web Services Inc. |

---

## 4. Encoding Issues

**Vendors with corrupted non-ASCII characters:** 11

> All affected entries appear to be Croatian entities. The corruption pattern
> (e.g., `ä_x008d_`, `å¡`, `ã³`, `â€™`) is consistent with a UTF-8 → Latin-1
> mojibake introduced during export or import.

| Row # | Corrupted Name |
|-------|---------------|
| 30 | Sveuä_x008d_Iliå¡Te U Zagrebu, Studentski Centar |
| 73 | Grad Zagreb, Gradski Ured Za Prostorno Ureä‘Enje,.. |
| 93 | Telefã³Nica Compras Electrã³Nicas S.L. |
| 129 | Oâ€™Donnell Salzano Lawyers |
| 147 | Garaå¾A Firule D.O.O. |
| 176 | Porezno Savjetniå¡Tvo Tuk D.O.O. |
| 207 | Mãœller Trgovina Zagreb D.O.O. |
| 233 | Catering Iviä‡ D.O.O. |
| 267 | Super Odrediå¡Te D.O.O. |
| 300 | Nastavni Zavod Za Javno Zdravstvo Dr. Andrija Å Tampar |
| 321 | Zagrebaä_x008d_Ki Holding D.O.O. |

---

## 5. Multi-Entity Brand Fragmentation

**Brands appearing as multiple distinct vendor entries:** 4

| Brand | Entity Count | Entities | Combined Spend |
|-------|-------------|----------|----------------|
| Amazon | 4 | `Amazon Web Services Llc` / `Amazon Web Services Inc.` / `Amazon.Co.Uk` / `Amazon (Aus)` | $112,892.56 |
| AWS | 2 | `Amazon Web Services Llc` / `Amazon Web Services Inc.` | $111,552.30 |
| Bupa | 2 | `Bupa- Supplier` / `Bupa Australia` | $35,262.71 |
| Allianz | 2 | `Allianz Australia Workers' Compensation (Victoria) Limited` / `Allianz Wa` | $7,069.34 |

> **Risk:** Fragmented entries understate true spend per vendor. AWS LLC + AWS Inc.
> are the same supplier; Amazon.co.uk and Amazon (Aus) may also consolidate.
> True Amazon/AWS exposure must be summed before negotiation or benchmarking.

---

## 6. Individual Names Appearing as Vendors

**Entries matching individual-name pattern (2-word title-case, no corporate keywords):** 18

| Row # | Name | Spend (USD) |
|-------|------|-------------|
| 29 | Grant Thornton | $46,538.55 |
| 47 | Bupa- Supplier | $22,799.78 |
| 55 | Peakon Aps | $17,108.07 |
| 69 | Cigna Sg | $13,248.95 |
| 87 | The Guardian | $8,070.27 |
| 149 | It London | $2,838.04 |
| 160 | Stipe Piric | $2,301.60 |
| 165 | John Smith | $2,162.81 |
| 166 | Fabiola Thistlewhaite | $2,154.29 |
| 169 | George Anchor | $2,107.46 |
| 201 | Icare Nsw | $1,150.37 |
| 212 | Allianz Wa | $970.71 |
| 249 | Tm Forum | $510.05 |
| 308 | Vitality Works | $181.53 |
| 322 | Event Ors | $142.83 |
| 359 | Snappy Snaps | $58.97 |
| 366 | Axosoft Gitkraken | $54.37 |
| 367 | Istra Wine | $53.45 |

> These may be contractor/freelancer payments, expense reimbursements, or data entry
> errors. They should be reviewed and either recategorized (e.g., under a staffing
> agency) or excluded from vendor consolidation analysis.

---

## 7. Spend Distribution

| Metric | Value |
|--------|-------|
| Total L12M spend | $7,887,360.40 |
| Highest single vendor | $3,117,225.89 (Salesforce Uk Ltd-Uk) |
| Lowest single vendor | $17.51 (Coles) |
| Salesforce share of total | 39.5% |
| Data already sorted descending | No |

---

## 8. Spend Concentration

| Vendor Tier | Vendor Count | Cumulative Spend | % of Total |
|-------------|-------------|------------------|------------|
| Top 10 vendors | 10 | $5,042,189.13 | 63.9% |
| Top 20 vendors | 20 | $5,898,424.10 | 74.8% |
| Top 50 vendors | 50 | $6,981,333.71 | 88.5% |
| Remaining 336 vendors | 336 | $906,026.69 | 11.5% |

---

## 9. Long Tail Profile

| Spend Threshold | Vendor Count | % of All Vendors |
|----------------|-------------|------------------|
| Under $1,000 | 178 | 46% |
| Under $5,000 | 283 | 73% |
| Under $10,000 | 307 | 80% |
| $10K and above (strategic tier) | 79 | 20% |

> 46% of vendors (178) generate under $1K in annual spend.
> The bottom ~336 vendors (87%) account for only 11.5% of total spend.
> A strategic review can focus on ~79 vendors ($10K+) covering 80% of spend.

---

## 10. Strategic Risks Summary

| # | Risk | Severity | Detail |
|---|------|----------|--------|
| 1 | **Zero department mapping** | 🔴 Critical | 100% of vendors lack a department tag. No cost-center or functional analysis is possible without a categorization pass. |
| 2 | **Salesforce single-vendor concentration** | 🔴 Critical | One vendor = 39.5% of total L12M spend ($3.1M). Any contract risk or pricing change has outsized P&L impact. |
| 3 | **Encoding-corrupted vendor names** | 🟠 High | 11 Croatian entities have garbled names. These cannot be matched to external databases or contracts without manual correction. |
| 4 | **Amazon multi-entity fragmentation** | 🟠 High | 4 separate AWS/Amazon entries mask true exposure (~$113K combined). Likely undercounted if procurement is split across entities. |
| 5 | **Individual names as vendor records** | 🟠 High | 18 entries appear to be people, not companies. These distort vendor count, average spend, and category analysis. |
| 6 | **Extreme long tail** | 🟡 Medium | 178 vendors under $1K represent administrative drag with negligible savings potential. Should be filtered before strategic analysis. |
| 7 | **No descriptions or suggestions populated** | 🟡 Medium | Columns D and E are 100% blank. Vendor context and prior recommendations must be sourced externally or generated fresh. |
| 8 | **Columns F–O unused** | 🟢 Low | The workbook has 15 columns but only 5 are in use. No hidden data risk, but the schema is wider than needed. |