# Analysis Pipeline Development Plan

## Overview
Develop a comprehensive analysis pipeline for two survey datasets (PyMEs and Competentes) with descriptive statistics, cross-tabulations, inferential analysis, pattern detection, and classification modeling.

## Data Architecture

- **Dataset 1**: `data/ia_pymes.xlsx` - Small business owner survey responses
- **Dataset 2**: `data/ia_comp.xlsx` - Job seeker survey responses

Demographic characterization variables (both datasets):
- `sexo` (Gender)
- `edad` (Age range)
- `niveduc` (Education level)
- `ocupacion` (Occupation)
- `nse` (Socioeconomic group)

---

## Step 1 — Design Analysis Architecture and Data Validation

**Intent**: Review the data structure, validate data integrity, establish analysis framework, and set up helper functions for consistent visualization and reporting across both notebooks.

**Details**:
- Load both datasets and inspect shape, dtypes, missing patterns
- Validate demographic variables and response variables
- Document column mapping (Spanish → English codes)
- Establish reusable plotting style and labeling conventions
- Create helper functions for labeled outputs, categorical ordering, and summary statistics

**Acceptance**:
- Both datasets load without errors; row/column counts documented
- All demographic variables are correctly typed as ordered categoricals
- Helper function library ready for import into both analysis notebooks
- Visualization defaults (colors, fonts, themes) are defined

**Out of scope**: Data imputation or synthetic data generation

---

## Step 2 — Descriptive Statistics: PyMEs Dataset (Univariate)

**Intent**: Perform comprehensive univariate descriptive statistics on the PyMEs dataset, covering all demographic and response variables, including frequency distributions, summary statistics, and missingness patterns.

**Details**:
- Compute frequency tables (counts, percentages) for all categorical variables
- Summary statistics (mean, median, std, quartiles) for any continuous variables
- Missingness analysis per column and by response variable type
- Generate visual representations: bar charts, histograms, heatmaps of missingness
- Write interpretive text blocks explaining key findings (e.g., "60% of respondents are female; age skews toward 31–40")

**Acceptance**:
- Frequency tables and summary statistics computed for all variables
- Missingness documented; visual representation generated
- At least 5 interpretation blocks written, one per major finding
- All outputs render correctly in Jupyter notebook

**Out of scope**: Cross-variable associations (covered in Step 4)

---

## Step 3 — Descriptive Statistics: Competentes Dataset (Univariate)

**Intent**: Mirror Step 2 for the Competentes dataset, ensuring parallel structure and consistent interpretation style for later comparison.

**Details**:
- Repeat univariate analysis (frequencies, summaries, missingness) for all variables
- Generate the same chart types as PyMEs for comparability
- Write interpretive blocks following the same structure and tone
- Note any dataset-specific patterns (e.g., different response rate for p01 vs. p02a–p02e)

**Acceptance**:
- Univariate analysis complete and output matches Step 2 structure
- Visual outputs generated; interpretation blocks written
- Dataset-specific insights documented (e.g., multi-select response patterns)

**Out of scope**: Comparative analysis between datasets (defer to later synthesis step)

---

## Step 4 — Cross-Tabulation: Characterization × Response Variables (PyMEs)

**Intent**: Analyze how demographic characteristics (sexo, edad, niveduc, ocupacion, nse) associate with each response variable (p01, p02, p03, p04, p01_otro) using contingency tables, row/column percentages, and visualizations.

**Details**:
- For each response variable, create crosstabs with each demographic variable
- Compute row percentages and column percentages to identify patterns
- Generate stacked bar charts or heatmaps for each crosstab
- Write 2–3 interpretation blocks per crosstab (e.g., "Younger respondents (18–30) prioritize customer service; older ones (51+) focus on accounting")
- Identify and document notable associations (e.g., education level predicts willingness to learn)

**Acceptance**:
- All crosstabs (5 response vars × 5 demographic vars = 25 tables) completed
- Visual representations generated for each crosstab
- Interpretation blocks identify 2–3 key insights per crosstab
- Patterns noted for later modeling (Step 8)

**Out of scope**: Statistical significance testing (covered in Step 5)

---

## Step 5 — Inferential Statistics: Hypothesis Testing (PyMEs)

**Intent**: Test statistical significance of associations between demographic characteristics and response variables using chi-square tests, Fisher exact, or other appropriate tests.

**Details**:
- Perform chi-square test of independence for each demographic × response pair
- Report test statistic, p-value, effect size (Cramér's V)
- Filter results by significance threshold (p < 0.05)
- Visualize effect sizes (e.g., Cramér's V heatmap)
- Interpret significant associations in plain language (e.g., "Age and p03 barriers are significantly associated, V = 0.32")

**Acceptance**:
- Chi-square tests computed for all 25 pairs
- Effect sizes calculated and visualized
- Significant associations highlighted and interpreted
- At least 10 significant associations documented with context

**Out of scope**: Regression modeling (covered in Step 8)

---

## Step 6 — Inferential Statistics: Hypothesis Testing (Competentes)

**Intent**: Mirror Step 5 for Competentes dataset, ensuring parallel statistical rigor.

**Details**:
- Repeat chi-square testing and effect size analysis
- Note any dataset-specific patterns in statistical significance
- Compare effect sizes between PyMEs and Competentes for the same demographic variables

**Acceptance**:
- Chi-square tests completed for all response × demographic pairs
- Significant associations documented and interpreted
- Comparison notes prepared for synthesis step

---

## Step 7 — Pattern Detection: Latent Structure Analysis (Both Datasets)

**Intent**: Identify latent patterns, clusters, and hidden structures using exploratory techniques (PCA, hierarchical clustering, or correspondence analysis on contingency tables).

**Details**:
- Apply correspondence analysis (CA) to demographic × response contingency tables to visualize associations in low-dimensional space
- Perform hierarchical clustering on response profiles by demographic group
- Identify and visualize clusters of similar response patterns
- Generate biplot-style visualizations showing which demographics align with which responses
- Write interpretation blocks explaining discovered clusters (e.g., "Cluster 1: Young, high-education females seeking upskilling")

**Acceptance**:
- Correspondence analysis performed on 3–5 key contingency tables
- Cluster analysis completed; dendrograms/biplots generated
- Latent patterns identified and documented
- Interpretation blocks explain business relevance of clusters

**Out of scope**: Dimensionality reduction via PCA on raw features (use CA for categorical data)

---

## Step 8 — Classification Modeling: Feature Engineering & Baseline (PyMEs)

**Intent**: Engineer features from demographic and response data, establish baseline classification models, and identify best predictors for downstream tasks.

**Details**:
- Encode categorical variables (one-hot, ordinal encoding)
- Handle missingness (imputation strategy documented)
- Develop baseline classification models predicting high-priority response values (e.g., predicting p04 willingness from demographics)
- Evaluate baseline accuracy, precision, recall, F1-score
- Feature importance ranking to identify strongest predictors
- Visualize feature importance and model performance

**Acceptance**:
- Features engineered and documented
- At least 2 baseline models trained (e.g., Logistic Regression, Random Forest)
- Model performance metrics computed and visualized
- Feature importance ranking generated
- Interpretation blocks explain which features drive predictions

**Out of scope**: Hyperparameter tuning (focus on baseline performance)

---

## Step 9 — Classification Modeling: Feature Engineering & Baseline (Competentes)

**Intent**: Parallel feature engineering and baseline modeling for Competentes, with focus on job-search-specific response patterns.

**Details**:
- Engineer features from Competentes-specific response variables (p_02a–p_02e multi-select job search support needs)
- Build baseline classification models (e.g., predict job search support preferences from demographics)
- Evaluate and compare model performance
- Identify differences in feature importance between datasets

**Acceptance**:
- Feature engineering complete; multi-select variables handled appropriately
- Baseline models trained and evaluated
- Performance metrics and feature importance documented
- Comparison to PyMEs models noted

---

## Step 10 — Use-Case Design: Actionable Classification Applications

**Intent**: Propose 3–5 high-impact classification use cases that could drive business decisions or targeted interventions for survey respondents.

**Details**:
- **Use Case 1**: Predict high-priority business barriers (p03) from demographics → segment respondents for targeted support programs
- **Use Case 2**: Predict willingness to invest in digital learning (p04) → identify cost-effective training targets
- **Use Case 3**: Classify job seekers by primary support needs (p_02a–p_02e) → personalize training curriculum
- **Use Case 4** (optional): Identify "at-risk" respondents (e.g., high barriers + low education + limited time) → prioritize intervention
- **Use Case 5** (optional): Predict occupation upgrade likelihood from barriers + demographics → long-term career planning
- For each use case: articulate business value, required model architecture, success metrics, and ethical considerations

**Acceptance**:
- 3–5 use cases fully specified with business drivers and success metrics
- Model requirements (binary/multiclass) defined for each
- Ethical guardrails documented (e.g., no discriminatory targeting)
- Feasibility and data requirements assessed

**Out of scope**: Implementation of production models (scope-limited to design and prototyping)

---

## Step 11 — Notebook Integration & Final Synthesis

**Intent**: Assemble all analyses into two polished, self-contained Jupyter notebooks (one per dataset) with clear section navigation, inline interpretations, and export-ready visualizations. Create a summary document linking patterns across datasets and proposing the prioritized use case roadmap.

**Details**:
- Consolidate all analyses into `ia_icd_pymes_analysis.ipynb` and `ia_icd_competentes_analysis.ipynb`
- Add table of contents, markdown section headers, and clear cell labeling
- Embed all charts, tables, and interpretation blocks in correct narrative order
- Ensure all code is reusable and well-commented
- Create a `ANALYSIS_SUMMARY.md` document:
  - Comparative insights across datasets (e.g., demographic skews, question response patterns)
  - Cross-dataset validation of significant associations (e.g., education effect on barrier perception)
  - Prioritized use-case recommendations with implementation roadmap
  - Key limitations and next-steps (e.g., missing longitudinal data, need for larger sample)

**Acceptance**:
- Both notebooks render without errors in Jupyter Lab
- All sections properly titled and navigable via table of contents
- All visualizations are publication-ready (legible fonts, clear legends, color-blind safe)
- `ANALYSIS_SUMMARY.md` synthesizes findings and proposes ranked use cases
- Code is documented and reproducible

---

## Success Criteria (Overall)

- [ ] Two independent Jupyter notebooks (`ia_icd_pymes_analysis.ipynb`, `ia_icd_competentes_analysis.ipynb`) with full analysis pipeline
- [ ] 200+ visualization outputs (charts, tables, heatmaps) across both notebooks
- [ ] 50+ interpretation blocks documenting key findings and insights
- [ ] Statistical tests (chi-square, effect sizes) validate demographic associations
- [ ] Latent pattern analysis identifies 3–5 distinct respondent clusters
- [ ] Classification baseline models achieve ≥70% accuracy on key response variables
- [ ] 3–5 actionable use cases designed with business drivers and success metrics
- [ ] `ANALYSIS_SUMMARY.md` integrates findings and roadmap
- [ ] All notebooks and outputs ready for stakeholder review and decision-making
