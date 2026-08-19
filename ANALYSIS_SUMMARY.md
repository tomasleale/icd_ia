# Analysis Summary: PyMEs & Competentes Survey Data

**Status:** Final synthesis document  
**Last Updated:** 2026-08-19  
**Notebooks:** `ia_icd_pymes_analysis.ipynb`, `ia_icd_competentes_analysis.ipynb`  
**Evidence Base:** Steps 2–10 of PIPELINE_PLAN.md  

---

## Executive Summary

This analysis examined survey responses from two distinct populations in Chile:

- **PyMEs** (368 respondents): Small business owners navigating operational bottlenecks and digital tool adoption
- **Competentes** (503 respondents): Job seekers and employed professionals improving digital skills and employability

### Three Key Findings Across Both Datasets

1. **Weak but real demographic patterns**: Demographic characteristics (age, education, NSE) associate with response patterns, but all effect sizes are small (Cramér's V ≤ 0.17). Age and education are the most consistent predictors; socioeconomic group and gender show minimal signal.

2. **Segmentation, not prediction**: Classification targets are severely imbalanced (PyMEs willingness 94.3% positive; Competentes interest 90.3% positive). This creates a fundamental statistical barrier: trivial baselines (predicting majority class) match trained models. **The real value lies in transparent segmentation indices and rule-based routing, not machine-learning classifiers.**

3. **Institutional gap**: Both datasets reveal heavy reliance on informal support (51.4% of PyMEs use family/friends; 89.3% of Competentes want support but most reach informal networks). Formal institutions (SERCOTEC, courses, counselling) capture <10% of demand, indicating both an opportunity and a constraint for intervention design.

### Why "Value is in Segmentation, Not Per-Person Prediction"

The phrase encapsulates critical findings from Step 10 (USE_CASES.md):

- Weak associations (V ≤ 0.17) mean demographic features explain ≤3% of variance
- Severe class imbalance means trivial baseline models match trained classifiers to 3 decimal places
- No outcome labels (single-wave, cross-sectional) means targets are stated intentions, not validated behaviors
- **Result:** Individual-level classifiers are unstable and potentially discriminatory

**Better alternative:** Group-level indices (UC4), rule-first recommenders (UC2), and re-specified balanced targets (UC1) deliver actionable insights without requiring individual prediction accuracy.

---

## Comparative Insights: PyMEs vs. Competentes

### Demographic Profiles

| Dimension | PyMEs | Competentes | Interpretation |
|-----------|-------|-------------|-----------------|
| Sample size | 368 | 503 | Competentes ~37% larger; both adequate for descriptive stats |
| Age | 64.7% over 41 | 87.2% age 31–60; 0% over 61 | PyMEs older (career stage); Competentes skip senior job-seekers |
| Education | 70.7% post-secondary | 76.7% post-secondary | Competentes ~6pp more educated |
| Employment | ~78% owners; dual roles | 10.1% unemployed; 89.9% employed/student | PyMEs operating; Competentes mobile |
| Gender | 52.2% F / 47.8% M | 50.7% F / 49.3% M | Both balanced |
| NSE | 68.8% C2+C3 | 72.1% C2+C3 | Both middle-class focused |

**Key structural difference:** PyMEs are operationally focused (running existing businesses); Competentes are career-mobile (changing/upgrading roles).

### Response Patterns: Univariate Summary

**PyMEs:**
- p01: No dominant task (max 27.2% for customer service)
- p02: Strong reliance on informal: 51.4% family/friends; institutional <5%
- p03: One dominant barrier: 60.3% cite "falta de capital"
- p04: High willingness: 94.3% willing (any amount); evenly split across time bands

**Competentes:**
- p01: Bimodal distribution: 35.6% time barrier, 32.4% "nada me frena"
- p_02: High support need: 89.3% request ≥1 form; 56.7% CV, 53.1% interview, 42.9% job search
- p03: Weak disinterest: 90.3% say "no" to mobile (V ≤ 0.01 across demographics)

**Interpretation:** PyMEs face capital constraints (digital tools cannot solve); Competentes face soft barriers (time/attitude split).

### Statistical Associations: Which Demographics Matter

**PyMEs (Chi-Square, Step 5):**
1. edad × p01 (V = 0.17, strongest): Age extremes cluster on operational; middle ages on customer-facing
2. edad × p04 (V = 0.11): Older owners show lower >4h/wk willingness
3. niveduc × p04 (V = 0.14): University-educated show higher time commitment
- sexo: No signal across all pairs (V < 0.06)

**Competentes (Chi-Square, Step 6):**
1. niveduc × p_02 (V = 0.14): University-educated seek broader support (CV 59% vs. 48%)
2. ocupacion × p_02: Wide CA dispersion suggests occupation affects support needs
3. edad × p01 (V = 0.09, weak): Older cite time barrier more
- p03 × any demographic (V ≤ 0.01): No variation; avoid modeling

**Summary:** Education is most consistent (both datasets); age works but weakly; gender adds no signal; p03 has no demographic differentiation.

### Latent Structure Findings

**PyMEs (CA on edad × p01):**
- Dimension 1 (71.6% inertia): Task axis (accounting/inventory ↔ customer service)
- Pattern: Age extremes cluster operationally; middle ages toward growth

**Competentes (CA on niveduc × p_02):**
- Dimension 1 (90.4% inertia): Support breadth axis (single ↔ multiple)
- Pattern: University-educated seek integrated support; media-completa narrower

**Cross-dataset insight:** One dominant dimension each suggests response structure is surprisingly simple—bundled interventions may be more effective than targeted single solutions.

---

## Cross-Dataset Validation: Replication & Divergence

### Associations That Replicate

1. **Education predicts engagement breadth** (robust across both)
   - PyMEs: niveduc × p04 (V = 0.14), age structure
   - Competentes: niveduc × p_02 (V = 0.14), breadth of support
   - **Finding:** Post-secondary education is consistent signal of openness

2. **Age matters weakly and non-linearly**
   - PyMEs: edad × p01 (V = 0.17, non-monotonic)
   - Competentes: edad × p01 (V = 0.09, weak monotonic)
   - **Finding:** Age proxies for career stage; requires domain judgment (binning)

3. **Gender is not a lever** (both datasets)
   - sexo × responses: V < 0.06 across all pairs
   - **Finding:** Can exclude from models; retain for fairness audits

### Dataset-Specific Divergences

1. **PyMEs: One barrier (capital 60.3%) vs. Competentes: Bimodal (time 35.6%, none 32.4%)**
   - Implication: Capital constraints are structural; digital alone won't help PyMEs

2. **PyMEs: Informal closed loops (51% family) vs. Competentes: Multi-form support (89% want multiple)**
   - Implication: PyMEs weak institutional integration; Competentes actively mobile

3. **PyMEs: Balanced willingness to invest time vs. Competentes: Polarized mobile disinterest (90.3% no)**
   - Implication: Channel matters; PyMEs time-flexible; Competentes prefer traditional formats

---

## Use-Case Recommendations: Ranked Priority

**Full design:** See USE_CASES.md. Quick reference below.

### Rank 1: Weekly Time-Commitment Tier (PyMEs) — UC1

**Target:** p04_high (binary: ≥2h/wk), balanced 49.4% / 50.6%  
**Features:** edad, niveduc, p03, p01  
**Success:** Macro-F1 ≥ 0.62 (5-fold CV); ROC-AUC ≥ 0.65  
**Why:** High willingness (94.3%) means capacity is constraint. Balanced target learnable.  
**Timeline:** Immediate (1–2 weeks)

### Rank 2: Job-Search Support Triage (Competentes) — UC2

**Target:** p02_integral (≥2 of {CV, interview, search, contact}), 24.3% / 75.7%  
**Strategy:** Rule-first (use declarations), model-second (suggest missing)  
**Features:** niveduc, ocupacion, p01, edad  
**Success:** F1 ≥ 0.45; recall ≥ 0.55 at precision ≥ 0.40  
**Timeline:** 2–4 weeks

### Rank 2: Digital-Exclusion Risk Index (Both Datasets) — UC4

**Design:** Transparent 0–10 segmentation index (not ML)  
**PyMEs risk:** Capital barrier (3pt), NSE D+E (2pt), education ≤ media (2pt), age extremes (1pt), low time (1pt), informal network (1pt)  
**Competentes risk:** Soft barriers (3pt), NSE D+E (2pt), education ≤ media (2pt), age 51–60 (1pt), informal (1pt), no support (1pt), disengagement (0.5pt)  
**Timeline:** 4–6 weeks (requires expert weight workshop)

### Rank 2: Operational Bottleneck Routing (PyMEs) — UC5

**Target:** p01 (5-class or binary: customer-facing vs. back-office)  
**Features:** edad, ocupacion, p03, nse  
**Success:** Macro-F1 ≥ 0.32; top-2 accuracy ≥ 0.60  
**Timeline:** 2–3 weeks (parallel with UC2)

### Rank 3: DO NOT BUILD — Low-Interest Detection (Competentes) — UC3

**Why:** p03 is 90.3% "no" with zero demographic signal (V ≤ 0.01). Models match trivial baseline.  
**Alternative:** Rule-based (use p_02 selections directly); fund data collection first (target 150+ "yes" cases).

---

## Limitations & Next Steps

### Data Limitations

1. **No outcome labels** — Single-wave, cross-sectional. Targets are intentions, not behaviors.
2. **Missing longitudinal follow-up** — Cannot measure causal effects or distinguish barriers from preferences.
3. **Sample bias** — PyMEs older (64.7% over 41), more educated (70.7%) than national average. Competentes ~10% unemployed (vs. 8% national), skewed toward professionals.
4. **Fragile categories** — niveduc has n < 10 for basica; ocupacion 29% out-of-order; chi-square assumptions violated 13+ pairs.
5. **Multi-select ambiguity** — Competentes p_02a–e: NaN = not selected vs. missing, resolved by documentation.

### Recommended Next Data Collection

1. **Outcome tracking** (6–12 months): Re-contact 50% sample; measure training enrollment, completion, skill gain. Enables UC1 validation.
2. **Stratified oversampling:** Target UC3 minority ("yes" on mobile), UC2 integral-need, high-risk segments (NSE D+E, age extremes). Enables balanced classification.
3. **Instrument redesign:** Add behavioral indicators (have you tried X? What stopped you?). Bridge intention-behavior gap.
4. **Channel research:** Measure barriers to institutional adoption (SERCOTEC reach <5%); test alternatives (peer referral, embedded training).

---

## How to Use This Analysis

### Navigation Guide

**"Demographic profile of business owners?"**  
→ Comparative Insights: Demographic Profiles table; PyMEs Step 2

**"Which demographics drive business barriers?"**  
→ Comparative Insights: Statistical Associations; PyMEs Step 5

**"Segment by support needs?"**  
→ Use-Case Recommendations: UC2; Competentes Step 4, Step 9

**"Build predictive model for [outcome]?"**  
→ Use-Case Recommendations (full section); cross-reference USE_CASES.md. Decision: V > 0.15? Target ≥25% minority? Outcome labels? If "no" to any, use UC4 or UC2.

**"Which segments at-risk?"**  
→ Cross-Dataset Validation: Implications; UC4 index components

**"What replicates across datasets?"**  
→ Cross-Dataset Validation: Associations That Replicate

**"Biggest surprises?"**  
→ Methodological Summary: What Revealed Surprises

### Common Questions

**Q: Why not build model for [target]?**  
A: Check USE_CASES.md. Common blockers: severe imbalance (model matches baseline), weak signal (V < 0.15), no outcome labels. Alternative: segmentation index (UC4) or rule-first (UC2).

**Q: Reliable given sample size?**  
A: Descriptive stats robust. Predictive models have high test variance; use 5-fold stratified CV. Minority classes need class weighting, SMOTE, stratified CV. Causal inference requires experiment.

**Q: Real behavior or survey bias?**  
A: High positive rates (94.3% willing, 90.3% seeking support) may reflect social desirability. Mitigate with external behavior data (enrollment, tool usage) or qualitative interviews.

**Q: Use for restrictive targeting (deny access)?**  
A: No. All use cases are additive only. UC4 index for extra support (high-risk), not denial. Individual models unstable (V ≤ 0.17); group indices more defensible.

**Q: Collect more data before deploying?**  
A: Outcome tracking before high-stakes deployment. UC1, UC2, UC5: current data enough for pilot shadowing. UC3: don't build; collect first. UC4: ready (transparent rules, expert weights).

### Data Refresh Schedule

1. **Immediate:** Generate UC4 index scores; publish segment counts by demographics
2. **6-month interim (Mar 2027):** Outcome tracking on Phase 1; feed results to UC4 re-weighting
3. **Annual retrain (Sep 2027):** New survey wave; retrain UC1, UC2, UC5; update UC4; reassess UC3

**Off-cycle triggers:**
- Policy change: re-weight UC4 immediately
- Model drift: retrain on latest data
- Outcome data available: shift from intention- to outcome-based

---

## File Index

**Notebooks:**
- `/Users/tomas/github/icd_ia/ia_icd_pymes_analysis.ipynb`
- `/Users/tomas/github/icd_ia/ia_icd_competentes_analysis.ipynb`

**Supporting:**
- `/Users/tomas/github/icd_ia/analysis_helpers.py`
- `/Users/tomas/github/icd_ia/USE_CASES.md`
- `/Users/tomas/github/icd_ia/PIPELINE_PLAN.md`
- `/Users/tomas/github/icd_ia/CLAUDE.md`

**Data:**
- `data/ia_pymes.xlsx`
- `data/ia_comp.xlsx`

**Figures:**
- `figures/pymes/` — PyMEs charts, crosstabs, stats
- `figures/comp/` — Competentes charts, crosstabs, stats

---

## Closing: Honest Assessment

This analysis provides **robust descriptive findings** and **clear warnings about what not to do** (don't build UC3; don't assume gender matters). It offers **reasonable foundations for segmentation and rule-based routing** (UC1, UC2, UC4, UC5) that deliver business value without requiring high per-person prediction accuracy.

It does **not** support confident individual-level outcome prediction. Associations are weak (V ≤ 0.17), targets imbalanced, outcome labels missing. Expect pilot phases, staged deployment, ongoing validation before high-stakes automation.

**Path forward:** Collect outcome data (6–12 months), fund stratified oversampling, bridge intention-behavior gaps, pilot in controlled settings. This analysis is a strong starting point, not a finished product.

---

**Document prepared:** 2026-08-19  
**Analysis period:** Steps 2–10 of PIPELINE_PLAN.md  
**Next review:** Sep 2027 (annual retrain cycle)
