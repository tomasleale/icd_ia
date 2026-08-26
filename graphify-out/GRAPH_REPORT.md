# Graph Report - icd_ia  (2026-08-19)

## Corpus Check
- 72 files · ~162,514 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 254 nodes · 361 edges · 34 communities (19 shown, 15 thin omitted)
- Extraction: 47% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Correspondence Analysis (CA)
- Education & Demographics
- Analysis Helpers (Functions)
- Class Imbalance & Constraints
- Data Visualization & Plotting
- Categorical & Label Utilities
- Documentation & Reports
- Data Loading & Cleaning
- Statistical Testing (Chi²/V)
- Crosstab Analysis
- Response Distributions (Comp)
- Dataset Characteristics
- Configuration & Environment
- Effect Size Metrics
- Crosstab Functions
- Model Classification
- Occupational Hierarchy
- Predictors & Features
- Demographic Patterns
- Small Cluster 19
- Small Cluster 20
- Small Cluster 21
- Small Cluster 22
- Small Cluster 23
- Small Cluster 24
- Small Cluster 25
- Small Cluster 26
- Small Cluster 27
- Small Cluster 28
- Small Cluster 29
- Small Cluster 30
- Small Cluster 31
- Small Cluster 32
- Small Cluster 33

## God Nodes (most connected - your core abstractions)
1. `get_label()` - 17 edges
2. `Cramér's V Association Matrix` - 10 edges
3. `apply_categoricals()` - 8 edges
4. `_require_mpl()` - 8 edges
5. `normalize_text()` - 7 edges
6. `load_survey()` - 7 edges
7. `set_labels()` - 7 edges
8. `get_labels()` - 7 edges
9. `_wrap()` - 7 edges
10. `stacked_bar()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `Chi-Square Test of Independence` ----> `Weak Demographic Patterns (Cramér's V ≤ 0.17)`  [HIGH]
  PIPELINE_PLAN.md → ANALYSIS_SUMMARY.md
- `Fragile Categories Constraint (Cochran violation)` ----> `Weak Demographic Patterns (Cramér's V ≤ 0.17)`  [HIGH]
  USE_CASES.md → ANALYSIS_SUMMARY.md
- `No Outcome Labels (Cross-sectional, Single-Wave)` ----> `Value is in Segmentation, Not Per-Person Prediction`  [HIGH]
  USE_CASES.md → ANALYSIS_SUMMARY.md
- `Education Predicts Support-Seeking Breadth` ----> `UC2: Job-Search Support Triage with Rule-First (P1 Priority)`  [HIGH]
  ANALYSIS_SUMMARY.md → USE_CASES.md
- `PyMEs & Competentes Survey Analysis` ----> `Competentes Dataset (503 respondents)`  [HIGH]
  PIPELINE_PLAN.md → ANALYSIS_SUMMARY.md

## Import Cycles
- None detected.

## Communities (34 total, 15 thin omitted)

### Community 0 - "Correspondence Analysis (CA)"
Cohesion: 0.05
Nodes (54): Correspondence Analysis: Age x Barriers to Learning, Correspondence Analysis: Age x Barriers, Correspondence Analysis: Education Level x Barriers to Learning, Correspondence Analysis: NSE Group x Barriers to Learning, Correspondence Analysis: NSE x Help Source, Correspondence Analysis: Occupation Type x Barriers to Learning, Age Range Distribution (Rango Etario), Socioeconomic Group Distribution (NSE) (+46 more)

### Community 1 - "Education & Demographics"
Cohesion: 0.10
Nodes (25): Correspondence Analysis: Education Level x Job Search Support Needed, Correspondence Analysis: Education x Learning Time, Education Level Distribution (Nivel Educacional), Job Search Support Needed (p_02a-p_02e, Multi-select), Distribution of Selections per Respondent (p02), Hierarchical Clustering by Age Group, Hierarchical Clustering by Education Level, Crosstab: Education x Barriers (+17 more)

### Community 2 - "Analysis Helpers (Functions)"
Cohesion: 0.13
Nodes (22): correspondence_analysis(), freq_table(), get_label(), labeled_crosstab(), labeled_describe(), labeled_head(), labeled_value_counts(), labeled_value_counts_detailed() (+14 more)

### Community 3 - "Class Imbalance & Constraints"
Cohesion: 0.10
Nodes (22): Balanced Target Re-specification, Severe Class Imbalance Constraint, Class Weight Balancing Strategy, Data Refresh Schedule (Immediate, 6-Month, Annual), Education Predicts Support-Seeking Breadth, Fairness & Ethical Guardrails (Additive Only, No Denial), Macro-F1 Score Success Metric, Minority Recall Success Metric (+14 more)

### Community 4 - "Data Visualization & Plotting"
Cohesion: 0.17
Nodes (18): bar_freq(), ca_biplot(), heatmap(), missingness_heatmap(), plot_dendrogram(), analysis_helpers.py =================== Shared helper library for the ICD-IA…, Symmetric CA biplot: demographic categories (o) + response categories (^)., Hierarchical clustering dendrogram over a (groups x features) profile matrix,… (+10 more)

### Community 5 - "Categorical & Label Utilities"
Cohesion: 0.23
Nodes (12): apply_categoricals(), copy_labels(), get_labels(), load_survey(), lowercase_df(), Load a survey workbook, rename columns, attach labels, set categoricals., Lowercase and strip all string cells, preserving dtypes and labels., Attach/merge a {code: label} dict onto df.attrs['variable_labels']. (+4 more)

### Community 6 - "Documentation & Reports"
Cohesion: 0.17
Nodes (12): ANALYSIS_SUMMARY.md - Cross-Dataset Validation & Use-Case Roadmap, Step 10: Use-Case Design & Actionable Classification, Step 11: Notebook Integration & Final Synthesis, Step 1: Design Analysis Architecture and Data Validation, Step 2: Descriptive Statistics - PyMEs Dataset, Step 3: Descriptive Statistics - Competentes Dataset, Step 4: Cross-Tabulation Analysis - PyMEs, Step 5: Inferential Statistics & Hypothesis Testing - PyMEs (+4 more)

### Community 7 - "Data Loading & Cleaning"
Cohesion: 0.22
Nodes (10): build_rename_map(), _canonical_lookup(), category_report(), normalize_text(), Remove diacritics from text (é -> e), leaving 'ñ' intact., Lowercase, strip accents, collapse whitespace. Used as a lookup key., Map raw Spanish headers to short English codes., Build {normalized_value: canonical_category} for one variable. (+2 more)

### Community 8 - "Statistical Testing (Chi²/V)"
Cohesion: 0.20
Nodes (10): Chi-Square Test of Independence, Cramér's V Effect Size Measurement, Age (Edad) Matters Weakly and Non-Linearly, Education (Niveduc) as Most Consistent Predictor, Edad: Age Range (ordered categorical), Fragile Categories Constraint (Cochran violation), Niveduc: Education Level (ordered categorical), Ocupacion: Occupation (ordered categorical, 29% out-of-order) (+2 more)

### Community 9 - "Crosstab Analysis"
Cohesion: 0.33
Nodes (6): chi2_scale_profile(), combined_profile(), Row-normalized crosstab: for each level of group_col, the frequency…, Rescale profile columns by 1/sqrt(average column profile). This is the same…, Concatenate chi-square-scaled response profiles across several response…, response_profile()

### Community 10 - "Response Distributions (Comp)"
Cohesion: 0.40
Nodes (6): Interest in Mobile Skills Training (p03), Crosstab: Age x Barriers, Business growth barriers (P03) - Horizontal bar chart, Strong Interest in Mobile-Based Skills Training, Pattern: Capital is dominant business constraint, Interest in Mobile Skills Training (p03)

### Community 11 - "Dataset Characteristics"
Cohesion: 0.40
Nodes (6): Competentes: Bimodal Distribution (Time 35.6%, None 32.4%), Competentes Dataset (503 respondents), Lowercase Value Normalization (lowercase_df function), PyMEs: Capital Constraints Dominate (60.3%), PyMEs Dataset (368 respondents), PyMEs & Competentes Survey Analysis

### Community 12 - "Configuration & Environment"
Cohesion: 0.40
Nodes (4): COLAB_AUTH_MODE, colab, npx, @google/colab-mcp

### Community 13 - "Effect Size Metrics"
Cohesion: 0.50
Nodes (4): chi2_association(), cramers_v(), Cramer's V effect size for a contingency table of raw counts., Chi-square test of independence plus Cramer's V for two columns.

### Community 14 - "Crosstab Functions"
Cohesion: 0.50
Nodes (4): crosstab_pct(), Contingency table as counts or percentages., 100%-stacked bar chart of cols distribution within each rows level., stacked_bar()

### Community 15 - "Model Classification"
Cohesion: 0.50
Nodes (4): labeled_info(), Structured .info() replacement: code, label, dtype, non-null, %missing., Check shape, schema, dtypes and categorical ordering for one dataset., validate_dataset()

### Community 16 - "Occupational Hierarchy"
Cohesion: 0.50
Nodes (4): Channel Research: Test Institutional Alternatives, Competentes: 89% Want Multiple Support Forms, Heavy Reliance on Informal Support, Institutional Adoption <10%, PyMEs: Informal Support Dominates (51% family/friends)

### Community 17 - "Predictors & Features"
Cohesion: 0.50
Nodes (4): p03: Mobile Training Interest (90.3% 'no', no signal), Stratified Oversampling for Minority Classes, UC3: DO NOT BUILD Low-Interest Detection (P3 - Insufficient Data), Weak Associations Constraint (V ≤ 0.17)

### Community 18 - "Demographic Patterns"
Cohesion: 0.67
Nodes (3): Bundled Interventions More Effective Than Targeted, Correspondence Analysis Single Dominant Dimension, Correspondence Analysis (CA)

## Knowledge Gaps
- **77 isolated node(s):** `npx`, `@google/colab-mcp`, `COLAB_AUTH_MODE`, `Chi-Square Test of Independence`, `Cramér's V Effect Size Measurement` (+72 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Cramér's V Association Matrix` connect `Correspondence Analysis (CA)` to `Education & Demographics`, `Response Distributions (Comp)`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **Why does `Value is in Segmentation, Not Per-Person Prediction` connect `Class Imbalance & Constraints` to `Statistical Testing (Chi²/V)`?**
  _High betweenness centrality (0.010) - this node is a cross-community bridge._
- **Why does `Random Forest Feature Importance` connect `Education & Demographics` to `Correspondence Analysis (CA)`?**
  _High betweenness centrality (0.009) - this node is a cross-community bridge._
- **What connects `npx`, `@google/colab-mcp`, `COLAB_AUTH_MODE` to the rest of the system?**
  _77 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Correspondence Analysis (CA)` be split into smaller, more focused modules?**
  _Cohesion score 0.05380852550663871 - nodes in this community are weakly interconnected._
- **Should `Education & Demographics` be split into smaller, more focused modules?**
  _Cohesion score 0.10333333333333333 - nodes in this community are weakly interconnected._
- **Should `Analysis Helpers (Functions)` be split into smaller, more focused modules?**
  _Cohesion score 0.12987012987012986 - nodes in this community are weakly interconnected._