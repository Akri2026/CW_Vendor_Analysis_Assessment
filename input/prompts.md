# CW_Vendor_Analysis_Assessment
#PROMPT 1
You are acting as a VP-level post acquisition operating strategist reviewing vendor spend
from an acquired company.

I have uploaded the file: Vendor_Spend_Strategy.xlsx

Your first task is ONLY to understand and validate the dataset.
Do not classify vendors. Do not make recommendations.

STEP 1 — Workbook Discovery
1. Read all workbook tabs using Python/openpyxl
2. Summarize the purpose of each tab
3. Identify: primary analysis tab, config/reference tabs, derived tabs

STEP 2 — Data Validation
Analyze the main vendor sheet and identify:
1. Total populated vendor records vs blank/formatting-only rows
2. Duplicate vendors (exact and near-duplicate/multi-entity)
3. Missing values per column
4. Inconsistent formatting (encoding issues, capitalization, number precision)
5. Whether spend data is already sorted
6. Spend concentration (top 10/20/50 vendor share of total)
7. Long tail profile (vendors under $1K, $5K, $10K)

STEP 3 — Strategic Risks
Identify risks that could lead to poor downstream analysis:
- Ambiguous department categories
- Multi-entity brand fragmentation
- Encoding-corrupted vendor names
- Individual names appearing as vendors

OUTPUTS REQUIRED (write to /outputs/):
1. workbook_discovery.md
2. data_quality_summary.md
3. raw_valid_records_preview.csv (populated vendors only, all columns)

At the end, give a concise executive summary covering dataset quality,
major risks, and recommended next step.


#PROMPT2:
Using the data_quality_summary.md findings from the previous step, define the strategic categorization philosophy BEFORE any vendor mapping begins.

Note, The Config tab defines 12 department categories, NOT 13:
Engineering, Facilities, G&A, Legal, M&A, Marketing, SaaS, Product,
Professional Services, Sales, Support, Finance

Answer the following with full reasoning:

1. What should departments represent? Evaluate and choose from: software category,
   vendor type, operational ownership, budget ownership, business capability ownership etc.
   Justify your choice.

2. Resolve ALL boundary disputes between ambiguous category pairs.
   For each dispute, write a governing rule and examples.
   At minimum address:
   - SaaS vs Engineering
   - SaaS vs Product
   - SaaS vs Sales (critical — Salesforce is the largest vendor)
   - G&A vs Finance
   - G&A vs Legal
   - M&A vs Professional Services
   - Facilities vs G&A

3. How should spend magnitude influence classification diligence and later
   recommendations? Define spend tiers with thresholds.

4. How should multi-entity/near-duplicate vendors be handled?
   Define a brand grouping approach that preserves row-level data.

5. Define:
   - Classification principles (at least 6)
   - Edge case rules (individual names, government entities, insurance,
     recruitment agencies, events/entertainment, coworking)
   - Fallback rules in priority order
   - Confidence scoring framework: H / M / L / R with definitions

IMPORTANT: Do NOT modify the workbook. Do NOT classify vendors yet.

OUTPUTS REQUIRED (write to /outputs/):
1. mapping_philosophy.md
2. department_interpretation_guide.md

At the end: state the final agreed mapping philosophy, key assumptions,
and unresolved ambiguities.

#PROMPT3:

Before proceeding to classification, I need to do two things. First, challenge you on classifying Salesforce as Sales and not SaaS. I want to be sure of this claissifcaiton because there are more teams other than sales that can use Salesforce eg. Marketing. 
So, i really want to be sure of this claissificaiton as this contiributes to almost 40% of the total spend. 
Second, handle the unresolved vendor ambiguities identified in the mapping philosophy.
 
Constraint: I do not have access to HR/Finance or the acquired company's departments.
I must proceed to final VP-level recommendations anyway.
 
For each unresolved vendor:
1. Search the web to attempt resolution
2. If resolvable via research: classify with appropriate confidence and document the finding
3. If not resolvable via research: apply one of two strategies:
   - Strategy A — Classify with a declared assumption: vendor has a dominant plausible
     interpretation; state the assumption explicitly; set confidence = L
   - Strategy B — Accept ambiguity as strategically irrelevant: both classifications
     lead to the same recommendation; pick the more likely one; note it
 
For each vendor, state:
- Which strategy you applied
- The classification chosen
- The exact assumption or reasoning
- The strategic risk of being wrong (High / Medium / Low)

 The unresolved vendors from the previous step are listed in mapping_philosophy.md.
 
No new output files required — this is a reasoning and decision step
that informs the classification prompt.

#PROMPT4:

Now classify all vendors in the dataset based on the mapping philosophy and department
interpretation guide produced in previous steps.

Read the raw_valid_records_perview file and the following outputs from previous steps:
- mapping_philosophy.md
- department_interpretation_guide.md
- ambiguity_resolution.md

For every populated vendor record (386 total):
1. Assign a Department from the 12-category Config taxonomy
2. Write a 1-line business capability description of what the vendor does
3. Assign Classification Confidence: H / M / L / R
4. Assign Brand Group if part of a multi-entity group (else blank)
5. Add Classification Notes for Low/Review confidence entries or encoding issues

Classification rules: Refer to the outputs from the previous steps
- mapping_philosophy.md
- department_interpretation_guide.md
- ambiguity_resolution.md


OUTPUTS REQUIRED (write to /outputs/mappings/):
1. full_vendor_mapping.xlsx — raw_valid_records_perview with columns B (Department),
   D (Description), F (Classification Confidence), G (Brand Group),
   H (Classification Notes) populated.
   Color-code confidence column: green=H, yellow=M, orange=L, red=R.
   Enable autofilter on all columns. Freeze row 1.
2. full_vendor_mapping.csv — flat export of all populated records
3. full_mapping_summary.md — spend by department table, confidence distribution,
   key findings per department, brand group consolidation summary,
   under-review footnote

#PROMPT 5:
Using the vendor classification in /outputs/mappings/full_vendor_mapping.xlsx what should be the governing logic to update column F (suggestions) with one of the three values - Consolidate, Optimize, Terminate?
CONSOLIDATE — use when:
- Vendor has a direct equivalent in a typical acquirer's stack
OPTIMIZE — use when:
- Vendor is strategically necessary and will continue post-integration
TERMINATE — use when:
- Vendor is M&A-related and non-recurring

#PROMPT 6:
Using the completed vendor data in /outputs/mappings/full_vendor_mapping.xlsx,
fill the three remaining empty tabs. Refer to the /input/Vendor_Spend_Strategy.xlsx only to map the tabs between the two xlsx files. 

DO NOT do any updates to the Vendor Mapping tab. 
Do updates only to ‘Top 3 Opportunities’, ‘Methodology’ , ‘CEOCFO Recommendations’ tabs. 

TAB: 'Top 3 Opportunities'
Identify the three highest-impact vendor spend opportunities based on:
- Spend magnitude
- Feasibility of action (Consolidate/Terminate/Optimize)
- Speed to value (can this be acted on within 90 days of acquisition close?)
- Strategic clarity (is the recommendation unambiguous?)
 
For each of the 3 opportunity the recommendation should include:
- A summary title (e.g “CRM Tool consolidation”)
- A brief explanation
- An estimated annual savings in USD
- Strategic clarity (is the recommendation unambiguous?)

TAB: 'Methodology'
In the Methodology tab, summarize shortly
- How this task was approached
- Which tools used (Claude code)
- Prompts used
- How the work was validated and quality checked
 
TAB: 'CEOCFO Recommendations'
Write a one-page executive memo addressed to the CEO and CFO. Rules:
- Maximum one page — do not exceed this under any circumstance
- Lead with the number that matters: total spend, total vendors, and the one
  insight that reframes everything
- Three to four action points maximum — busy executives need decisions,
  not inventories
- Flag the one non-obvious risk they would not expect
- Do not list every department — focus only on what requires a decision from them
- Do not use consultant language ('leverage synergies', 'unlock value')
  — be direct
- End with a clear recommended next step and owner
 
Save the updated workbook to /outputs/mappings/full_vendor_mapping_final.xlsx
Also write the one page CEOCFO recommendation to a new file /outputs/mappings/CEOCFOreco.md

#PROMPT 7:
verify the final Excel file is complete:
- Column C (Department):            386/386 populated
- Column E (Description):           386/386 populated
- Column F (Suggestions):           386/386 populated with color coding
- Tab 'Top 3 Opportunities':        filled
- Tab 'CEOCFO Recommendations':     filled

Report any gaps and fix them.

Final output: /outputs/mappings/full_vendor_mapping_final.xlsx
