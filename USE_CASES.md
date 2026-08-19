# Classification Use Cases — PyMEs & Competentes

**Pipeline reference:** `PIPELINE_PLAN.md`, Step 10  
**Evidence base:** `ia_icd_pymes_analysis.ipynb` (Steps 2, 4, 5, 7, 8) and `ia_icd_competentes_analysis.ipynb` (Steps 3, 6, 7, 9)  
**Status:** Design document. No production models proposed; every use case specified to decision point.

---

## Overview: 5 Use Cases

| Priority | Use Case | Dataset | Target | Status |
|---|---|---|---|---|
| **P1** | Weekly time-commitment tier | PyMEs | `p04_high` (49/51 balanced) | Proceed with re-specification |
| **P1** | Job-search support triage | Competentes | `p02_integral` (24.3% / 75.7%) | Proceed (rule-first) |
| **P2** | Digital-exclusion risk index | Both | Transparent 0–10 index | Proceed (no ML) |
| **P2** | Bottleneck routing | PyMEs | `p01` (5-class, 27.2% max) | Proceed |
| **P3** | Low-interest detection | Competentes | `p03` (9.7% / 90.3%) | Do NOT build; collect data instead |

---

## Shared Constraints (All Use Cases)

**C1 — Severe class imbalance.** PyMEs `p04_bin` is 94.3/5.7 (~21 minority after split). Competentes `p03` is 90.3/9.7 (~12 minority after split).

**C2 — Weak associations.** 3 of 25 PyMEs and 4 of 25 Competentes pairs significant. All Cramér's V ≤ 0.17 (small effect sizes).

**C3 — Fragile categories.** 13+ pairs violate Cochran's rule (>20% cells with expected < 5).

**C4 — No outcome labels.** Cross-sectional, single-wave; targets are stated intention, not behaviour.

**C5 — RF importance bias.** Ordinal demographics rank above sparse dummies due to impurity bias.

---

## UC1: Weekly Time-Commitment Tier (PyMEs) — P1

**Problem:** 94.3% willing but capacity varies: 1h or less (16%), 1–2h (28.8%), 2–4h (25.5%), >4h (23.9%).

**Target:** `p04_high` = binary, 1 if >=2h/week (49.4% / 50.6%). Balanced, learnable, maps to two course formats.

**Why re-specify?** Original `p04_bin` (94.3/5.7) degenerates: LR predicts majority for every test row (recall 0%), matches trivial baseline to three decimals.

**Features:** `edad` (V=0.17, best PyMEs association), `niveduc` (education gradient on >4h: 21.6%→33.7%), `p03` ("nada me frena" = largest LR coeff), `p01` task type, drop `sexo` (no signal).

**Success metrics:** Macro-F1 ≥0.62 (5-fold CV); ROC-AUC ≥0.65; minority recall ≥0.55 at precision ≥0.55.

**Ethical guardrails:**
- Format routing only, never deny access
- Within ±10pp selection-rate parity by education/NSE band
- Explicit consent for scoring individuals

**Roadmap:** (1) Re-baseline with `p04_high`; (2) Shadow pilot one programme cycle; (3) Deploy as ranked outreach list.

---

## UC2: Job-Search Support Triage (Competentes) — P1

**Problem:** 89.3% requested support; 75.1% wanted one thing, 24.9% needed multiple. Integral-need segment consumes disproportionate counsellor time.

**Target:** `p02_integral` = binary, 1 if ≥2 of {CV, interviews, job search, company contact} selected (24.3%).

**Features:** `niveduc` (V=0.14, CA Dim1 90.4% of inertia — one clean axis), `ocupacion` (wide CA dispersion, use one-hot), `p01` barrier type, `nse`, `edad` (monotonic).

**Success metrics:** F1 ≥0.45 on integral class (5-fold CV); recall ≥0.55 at precision ≥0.40; precision@capacity ≥1.6x base rate.

**Key design:** Rule-first (use declared needs directly), model-second (suggest what they may not ask).

**Ethical guardrails:**
- Self-declaration always wins
- No employer disclosure (hard architectural boundary)
- Opt-out with no penalty
- Note: only 10.1% unemployed; don't transfer to unemployment programme without revalidation

**Roadmap:** (1) Resolve `p_02e` contradiction (57 vs 54); (2) Build rule-first recommender; (3) Counsellor triage pilot.

---

## UC3: Low-Interest Detection (Competentes) — P3 [DO NOT BUILD]

**Why deferred:** Target is 9.7% minority (49 cases). Step 9 found LR matches trivial baseline (0.905); RF below baseline (0.889). One correct minority prediction out of 12 test cases.

**Recommendation:** Convert to rule (`p_02a`–`p_02d` directly, no model) and fund targeted data collection (aim for ~150+ "no" cases).

**If revisiting after data collection:** Recall ≥0.50 at precision ≥0.25 on class-weighted 5-fold CV. Stop rule: if not met, no usable signal.

---

## UC4: Digital-Exclusion Risk Index (Both Datasets) — P2

**Design:** Transparent, published 0–10 index (not ML). Segmentation tool, not individual classifier.

**Rationale:** Effect sizes weak (V ≤ 0.17); transparent index beats black-box model on auditability, stability, and policy controllability.

**Components (illustrative; experts set weights):**

*PyMEs:* `p03`="falta de capital", informal-network dependency, `nse`=D+E, education≤media completa, age 61+, `p04`=capacity constraint.

*Competentes:* `p01`∈{connectivity, confidence, low skills}, `nse`=D+E, age 51–60, informal work, `p_02e`+low education, `p03`=no.

**Validation:** Deciles reproduce Step 7 clusters ≥70%, correlation with NSE alone <0.70, top 3 deciles capture ≥60% with structural barriers.

**Ethical guardrails:**
- Published weights (full rule public)
- Additive only, never restrictive
- Right to explanation and appeal
- Segment-level reporting by default

**Roadmap:** (1) Weight workshop; (2) Retrospective validation; (3) Instrumented pilot (one outreach campaign with control).

---

## UC5: Operational Bottleneck Routing (PyMEs) — P2

**Problem:** No majority task (max 27.2%): `atender clientes` 27.2%, `hacer publicidad` 25.5%, `controlar inventario` 16.3%, `llevar contabilidad` 16.0%, `ninguna` 14.9%.

**Target:** `p01` multiclass (5-class), or binary collapse (customer-facing 52.7% vs. back-office 32.3%).

**Why strong:** `edad × p01` is p=0.004, V=0.11 (most statistically reliable PyMEs association), 0% Cochran violation. Step 7 shows Dim1 at 71.6%, age orders tasks non-monotonically (extremes cluster together).

**Features:** `edad` (binning or tree split), `ocupacion` (wide CA dispersion, one-hot), `p03` barrier type, `nse`.

**Success metrics:** Macro-F1 ≥0.32 (5-fold CV, V≈0.11 so modest targets appropriate); top-2 accuracy ≥0.60 (real interface shows 2–3 demos); per-class recall ≥0.20 all five.

**Ethical guardrails:**
- Recommendation only, catalogue always one click away
- Age monitoring: advanced-content access ≥80% of overall by age band
- Never feed to credit decisions
- Cold-start: show unsorted catalogue for new owners

**Roadmap:** (1) Multinomial LR+RF, 5-fold CV; (2) Reframe as ranked list; (3) A/B test engagement + parity.

---

## Deferred: Occupation Upgrade

**Not feasible now.** Single-wave, cross-sectional (no outcome labels). `ocupacion` ordinal broken (29.2% outside hierarchy). Demographics-based "who will advance" with V≤0.17 mechanises existing inequality.

**Prerequisite:** Second survey wave (12+ months) + business-agreed `ocupacion` ordering. Use UC4 risk index instead for now.

---

## Measurement Standards

1. Never report accuracy alone; include trivial-baseline + minority-class metric
2. Stratified 5-fold CV (not single 75/25)
3. `class_weight="balanced"` on all imbalanced targets
4. Collapse fragile categories before modelling
5. Drop `sexo` from PyMEs (no signal; retain for fairness audits)
6. Report fairness slice per model: by `niveduc`, `nse`, `sexo`
7. Every stakeholder number carries effect size (all V ∈ [0.09, 0.17])
8. State acquiescence caveat where relevant (high positive rates may reflect response style)

---

## Summary for Stakeholders

Structure in both datasets is real but weak (V ≤ 0.17), and headline targets are so imbalanced that trivial baselines match trained models. **Value is in segmentation and prioritisation, not per-person prediction.**

**Recommended first moves** (generate outcome labels for future systems):
1. Re-specify PyMEs target (UC1)
2. Build Competentes rule-first (UC2)
3. Publish transparent index (UC4)

All three deliver operational value without requiring per-person model accuracy.
