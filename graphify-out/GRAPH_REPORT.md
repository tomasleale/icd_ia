# Graph Report - icd_ia  (2026-08-26)

## Corpus Check
- 10 files · ~67,046 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 167 nodes · 294 edges · 15 communities (14 shown, 1 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 7 edges (avg confidence: 0.81)
- Token cost: 184,764 input · 0 output

## Community Hubs (Navigation)
- Analysis Pipeline & Use Cases
- Labeled Display Helpers
- Visualization Helpers
- Cluster Profiles & Typology
- FirmaGob Adoption Study (TOE-UTAUT)
- Correspondence Analysis Helpers
- Category Normalization Helpers
- Variable Label Management
- Survey Findings (Informe)
- Notebook Pipeline & estado_laboral
- CLAUDE.md Documentation
- Data Loading Helpers
- Statistical Association Tests
- Data Validation Helpers
- Figure Saving Utility

## God Nodes (most connected - your core abstractions)
1. `Análisis Comparativo de Clustering: PyMEs vs. Competentes` - 18 edges
2. `get_label()` - 17 edges
3. `Factores incidentes en la adquisición y uso de la firma digital: FirmaGob` - 17 edges
4. `Analysis Summary: PyMEs & Competentes Survey Data` - 14 edges
5. `Analysis Pipeline Development Plan` - 12 edges
6. `apply_categoricals()` - 9 edges
7. `Classification Use Cases — PyMEs & Competentes` - 9 edges
8. `set_labels()` - 8 edges
9. `get_labels()` - 8 edges
10. `add_estado_laboral()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `H5: Características del Entorno (Apoyo DGD/Otras Instituciones)` --semantically_similar_to--> `Institutional Gap: Informal Support vs. Formal Institutions`  [INFERRED] [semantically similar]
  bid.md → ANALYSIS_SUMMARY.md
- `H1: Priorización y Costos` --semantically_similar_to--> `PyMEs: Falta de Capital como Barrera Dominante (60%)`  [INFERRED] [semantically similar]
  bid.md → informe_pymes_competentes.html
- `Step 7: Pattern Detection — Latent Structure Analysis` --conceptually_related_to--> `Análisis Comparativo de Clustering: PyMEs vs. Competentes`  [INFERRED]
  PIPELINE_PLAN.md → ANALISIS_CLUSTERING_COMPARATIVO.md
- `Step 1: Design Analysis Architecture and Data Validation` --shares_data_with--> `CLAUDE.md Project Guidance`  [INFERRED]
  PIPELINE_PLAN.md → CLAUDE.md
- `Competentes: 90% Interés en Formato Móvil (Transversal, No Discriminante)` --shares_data_with--> `Competentes Cluster 1: Desinteresados (rechazan móvil)`  [INFERRED]
  informe_pymes_competentes.html → ANALISIS_CLUSTERING_COMPARATIVO.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Segmento D: Vulnerable/Alto Riesgo (PyMEs C3 + Competentes C3 + Índice de Vulnerabilidad)** — analisis_clustering_comparativo_pymes_c3, analisis_clustering_comparativo_comp_c3, analisis_clustering_comparativo_vulnerability_index, analisis_clustering_comparativo_segmento_d [EXTRACTED 1.00]
- **TOE-UTAUT Hipótesis H1-H6 de Adopción de FirmaGob** — bid_h1_costs, bid_h2_conocimiento, bid_h3_caracteristicas_tecnicas, bid_h4_caracteristicas_organizacion, bid_h5_caracteristicas_entorno, bid_h6_influencia_social, bid_toe_utaut_hybrid [EXTRACTED 1.00]
- **Prioritized Use-Case Roadmap (UC1–UC5)** — use_cases_uc1_weekly_time_commitment, use_cases_uc2_job_search_triage, use_cases_uc3_low_interest_detection, use_cases_uc4_digital_exclusion_risk_index, use_cases_uc5_operational_bottleneck_routing [EXTRACTED 1.00]

## Communities (15 total, 1 thin omitted)

### Community 0 - "Analysis Pipeline & Use Cases"
Cohesion: 0.10
Nodes (28): Analysis Summary: PyMEs & Competentes Survey Data, Institutional Gap: Informal Support vs. Formal Institutions, Value is in Segmentation, Not Per-Person Prediction, UC1: Weekly Time-Commitment Tier (PyMEs), UC2: Job-Search Support Triage (Competentes), UC3: Low-Interest Detection (Do Not Build), UC4: Digital-Exclusion Risk Index, UC5: Operational Bottleneck Routing (PyMEs) (+20 more)

### Community 1 - "Labeled Display Helpers"
Cohesion: 0.10
Nodes (21): crosstab_pct(), freq_table(), get_label(), labeled_crosstab(), labeled_describe(), labeled_head(), labeled_value_counts(), labeled_value_counts_detailed() (+13 more)

### Community 2 - "Visualization Helpers"
Cohesion: 0.13
Nodes (19): bar_freq(), ca_biplot(), heatmap(), missingness_heatmap(), plot_dendrogram(), Symmetric CA biplot: demographic categories (o) + response categories (^)., Hierarchical clustering dendrogram over a (groups x features) profile matrix,…, Return the first font in FONT_STACK that is actually installed. (+11 more)

### Community 3 - "Cluster Profiles & Typology"
Cohesion: 0.20
Nodes (18): Competentes Cluster 0: Mujeres Jóvenes Profesionales, Competentes Cluster 1: Desinteresados (rechazan móvil), Competentes Cluster 2: Hombres Profesionales Maduros, Competentes Cluster 3: Vulnerable/Baja Confianza, Análisis Comparativo de Clustering: PyMEs vs. Competentes, estado_laboral: Categoría de Empleo Agrupada, K-Means Clustering (k=4) Methodology, Corrección de Métricas de Clustering (Silhouette/Davies-Bouldin) (+10 more)

### Community 4 - "FirmaGob Adoption Study (TOE-UTAUT)"
Cohesion: 0.16
Nodes (18): Dirección de Gobierno Digital (DGD), DocDigital Platform, Factores incidentes en la adquisición y uso de la firma digital: FirmaGob, FirmaGob (Chilean Advanced Digital Signature System), GTD Ransomware Incident (Nov 2023), H1: Priorización y Costos, H2: Conciencia / Vacíos de Conocimiento, H3: Características de Software/Técnicas (+10 more)

### Community 5 - "Correspondence Analysis Helpers"
Cohesion: 0.22
Nodes (11): chi2_scale_profile(), combined_profile(), correspondence_analysis(), preview_columns(), Simple correspondence analysis (CA) via SVD of standardized residuals. Classic…, Row-normalized crosstab: for each level of group_col, the frequency…, Rescale profile columns by 1/sqrt(average column profile). This is the same…, Concatenate chi-square-scaled response profiles across several response… (+3 more)

### Community 6 - "Category Normalization Helpers"
Cohesion: 0.24
Nodes (10): apply_categoricals(), _canonical_lookup(), category_report(), normalize_text(), Remove diacritics from text (é -> e), leaving 'ñ' intact., Lowercase, strip accents, collapse whitespace. Used as a lookup key., Build {normalized_value: canonical_category} for one variable., Return (matched, unknown) raw values for a categorical column. (+2 more)

### Community 7 - "Variable Label Management"
Cohesion: 0.29
Nodes (8): copy_labels(), get_labels(), lowercase_df(), Lowercase and strip all string cells, preserving dtypes and labels., Attach/merge a {code: label} dict onto df.attrs['variable_labels']., Return a copy of the full label dictionary (empty dict if unset)., Propagate labels from src to dst., set_labels()

### Community 8 - "Survey Findings (Informe)"
Cohesion: 0.25
Nodes (8): Competentes: Patrón de Edad Continuo (escala gradual), PyMEs: Patrón de Edad en Forma de U (extremos similares), Competentes: Barrera Bimodal (Tiempo 36% / Nada me Frena 32%), Competentes: 90% Interés en Formato Móvil (Transversal, No Discriminante), Discrepancia de Cifras CV/Entrevista vs. ANALYSIS_SUMMARY.md, PyMEs y Competentes — Lectura Narrativa, PyMEs: Falta de Capital como Barrera Dominante (60%), PyMEs: Canal Informal de Ayuda (Familia/Amigos 51%, Institucional 4%)

### Community 9 - "Notebook Pipeline & estado_laboral"
Cohesion: 0.38
Nodes (3): add_estado_laboral(), analysis_helpers.py =================== Shared helper library for the ICD-IA…, Add `estado_laboral`, grouping `ocupacion` into 4 categories. Uses…

### Community 10 - "CLAUDE.md Documentation"
Cohesion: 0.60
Nodes (5): CLAUDE.md Project Guidance, Labeled Display Helper Functions (labeled_head, labeled_info, labeled_value_counts, labeled_crosstab, labeled_describe), lowercase_df() Function, Ordered Categorical Variables (sexo, edad, niveduc, ocupacion), SPSS-style Variable Labels System

### Community 11 - "Data Loading Helpers"
Cohesion: 0.50
Nodes (4): build_rename_map(), load_survey(), Map raw Spanish headers to short English codes., Load a survey workbook, rename columns, attach labels, set categoricals.

### Community 12 - "Statistical Association Tests"
Cohesion: 0.50
Nodes (4): chi2_association(), cramers_v(), Cramer's V effect size for a contingency table of raw counts., Chi-square test of independence plus Cramer's V for two columns.

### Community 13 - "Data Validation Helpers"
Cohesion: 0.50
Nodes (4): labeled_info(), Structured .info() replacement: code, label, dtype, non-null, %missing., Check shape, schema, dtypes and categorical ordering for one dataset., validate_dataset()

## Knowledge Gaps
- **15 isolated node(s):** `Ordered Categorical Variables (sexo, edad, niveduc, ocupacion)`, `Step 2: Descriptive Statistics — PyMEs (Univariate)`, `Step 3: Descriptive Statistics — Competentes (Univariate)`, `Step 4: Cross-Tabulation — PyMEs`, `Step 5: Inferential Statistics — PyMEs` (+10 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Analysis Summary: PyMEs & Competentes Survey Data` connect `Analysis Pipeline & Use Cases` to `Survey Findings (Informe)`, `CLAUDE.md Documentation`, `Cluster Profiles & Typology`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **Why does `Análisis Comparativo de Clustering: PyMEs vs. Competentes` connect `Cluster Profiles & Typology` to `Analysis Pipeline & Use Cases`?**
  _High betweenness centrality (0.073) - this node is a cross-community bridge._
- **What connects `Ordered Categorical Variables (sexo, edad, niveduc, ocupacion)`, `Step 2: Descriptive Statistics — PyMEs (Univariate)`, `Step 3: Descriptive Statistics — Competentes (Univariate)` to the rest of the system?**
  _15 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Analysis Pipeline & Use Cases` be split into smaller, more focused modules?**
  _Cohesion score 0.10317460317460317 - nodes in this community are weakly interconnected._
- **Should `Labeled Display Helpers` be split into smaller, more focused modules?**
  _Cohesion score 0.1 - nodes in this community are weakly interconnected._
- **Should `Visualization Helpers` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._