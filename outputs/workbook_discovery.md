# Workbook Discovery Report

**Source file:** `input/Vendor_Spend_Strategy.xlsx`  
**Tabs found:** 5  

---

## Tab Inventory

| Tab Name | Type | Dimensions | Populated Rows | Purpose |
|----------|------|-----------|----------------|---------|
| Vendor Analysis Assessment | Primary Analysis | A1:O814 | 387 | Master vendor list with spend data — the dataset under review. |
| Top 3 Opportunities | Derived / Template | A1:D7 | 4 | Candidate fill-in: top consolidation/savings opportunities (currently blank). |
| Methodology | Template | A1:B7 | 1 | Candidate fill-in: explanation of analytical approach (currently blank). |
| CEOCFO Recommendations | Template | A1:B7 | 1 | Candidate fill-in: executive memo link for CEO/CFO (currently blank). |
| Config | Reference | A1:A13 | 13 | Controlled vocabulary of 13 department categories for classification. |

---

## Primary Analysis Tab: `Vendor Analysis Assessment`

- **Total row extent:** 814 rows × 15 columns
- **Populated vendor records:** 386
- **Blank/formatting-only rows:** 427
- **Last row with data:** row 387

### Column Map

| Column | Header |
|--------|--------|
| A | Vendor Name |
| B | Department |
| C | Last 12 months Cost (USD) |
| D | 1-line Description on what the Vendor does |
| E | Suggestions (Consolidate / Terminate / Optimize costs) |
| F | (no header) |
| G | (no header) |
| H | (no header) |
| I | (no header) |
| J | (no header) |
| K | (no header) |
| L | (no header) |
| M | (no header) |
| N | (no header) |
| O | (no header) |

> **Note:** Columns F–O have no headers and contain no data. The workbook width is
> inflated to 15 columns but only 5 are in use.

---

## Reference Tab: `Config`

Contains the controlled vocabulary of **department categories** available for vendor classification:

- Engineering
- Facilities
- G&A
- Legal
- M&A
- Marketing
- SaaS
- Product
- Professional Services
- Sales
- Support
- Finance

> **Critical gap:** None of the 386 vendor records has a department value assigned.
> The Config list exists as a reference but has not been applied to the data.

---

## Template / Derived Tabs (currently blank)

| Tab | Status | Notes |
|-----|--------|-------|
| Top 3 Opportunities | Blank | Candidate fill-in: top savings/consolidation opportunities |
| Methodology | Blank | Candidate fill-in: analytical approach description |
| CEOCFO Recommendations | Blank | Candidate fill-in: Google Doc link to executive memo |

> These three tabs are structured as assessment deliverables, not source data.
> They do not affect upstream data quality.