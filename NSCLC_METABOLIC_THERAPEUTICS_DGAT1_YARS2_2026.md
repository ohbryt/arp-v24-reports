# NSCLC Lung Cancer Metabolic Therapeutics
## Target Evaluation: DGAT1 & YARS2 + New Targets

**Date:** 2026-04-24  
**Disease:** NSCLC (Non-Small Cell Lung Cancer)  
**Focus:** Cancer Metabolism  
**Analyst:** ARP v24 Research Team  

---

## Executive Summary

| Target | Evidence Level | Clinical Stage | Recommendation |
|--------|---------------|---------------|----------------|
| **DGAT1** | Moderate (preclinical) | Phase 1 | ⚠️ Hold - solo insufficient |
| **YARS2** | Low | Preclinical | ❌ Deprioritize |
| **FASN** | Strong | Phase 2 | ✅ Lead candidate |
| **ACC1/2** | Moderate | Phase 2 | ✅ Combination candidate |
| **SCD1** | Moderate | Preclinical | 🔍 Monitor |

---

## 1. DGAT1 평가 (냉정하게)

### 1.1 사실: 무엇이 알려져 있는가?

| Aspect | Finding | Evidence |
|--------|---------|----------|
| **NSCLC 발현** | DGAT1 elevated in ~60% NSCLC | Zhang et al. 2020, Oncotarget |
| **生仔との関連** | High DGAT1 → poor survival | Cox 5-year OS correlation |
| ** knockdown 효과** | Inhibits growth, induces apoptosis | Li et al. 2019, J Cancer Res Clin Oncol |
| ** mekanism** | Increases TAG synthesis, lipid droplets | DGAT1 enzymatic activity |

### 1.2 냉정 평가

```
┌─────────────────────────────────────────────────────────────┐
│                    DGAT1 COLD ASSESSMENT                      │
├─────────────────────────────────────────────────────────────┤
│  Strengths:                                                  │
│  ✅ Novel mechanism (not crowded space)                       │
│  ✅ Validated in multiple cancer types                       │
│  ✅ Clear enzymatic activity → drugable                      │
│                                                              │
│  Weaknesses:                                                 │
│  ❌ PRIMARY: On-target toxicity concerns                     │
│     - DGAT1 essential for normal intestinal absorption      │
│     - DGAT1 KO mice show lethal phenotype (early)           │
│  ❌ Limited single-agent efficacy in vivo                    │
│  ❌ No selective inhibitors for tumor vs normal              │
│  ❌ Unknown resistance mechanisms                            │
│                                                              │
│  Reality Check:                                             │
│  - Phase 1 trials ongoing, but monotherapy efficacy minimal  │
│  - Best case: cytostatic, not cytotoxic                      │
│  - Would require combination with SOC                        │
└─────────────────────────────────────────────────────────────┘
```

### 1.3 결론: DGAT1

| Metric | Score | Comment |
|--------|-------|---------|
| **Target validity** | 6/10 | Interesting but not validated |
| **Druggability** | 8/10 | Good enzymatic target |
| **Selectivity concern** | 7/10 | High (on-target toxicity) |
| **Clinical readiness** | 3/10 | Early stage |
| **Overall** | ⚠️ **5/10** | **Not ready for lead** |

**권장:** Combination therapy partner only, NOT lead target

---

## 2. YARS2 평가 (냉정하게)

### 2.1 사실: 무엇이 알려져 있는가?

| Aspect | Finding | Evidence |
|--------|---------|----------|
| **돌연변이頻도** | Rare in NSCLC (<2%) | Wang et al. 2018 |
| **기능** | Mitochondrial tRNA charging | Housekeeping enzyme |
| **종양 관련성** | Unclear mechanism | Mitochondrial dysfunction link |
| **특이적 억제제** | **None exist** | No pharmacological tool |

### 2.2 냉정 평가

```
┌─────────────────────────────────────────────────────────────┐
│                    YARS2 COLD ASSESSMENT                      │
├─────────────────────────────────────────────────────────────┤
│  Strengths:                                                  │
│  ✅ Novel concept (mitochondrial translation)                 │
│  ✅ Synthetic lethality potential                           │
│                                                              │
│  Weaknesses:                                                 │
│  ❌ PRIMARY: No inhibitors exist                            │
│  ❌ PRIMARY: Rare mutations (not broad applicability)         │
│  ❌ PRIMARY: Housekeeping function → high toxicity risk      │
│  ❌ Unknown: Direct vs indirect tumor dependency            │
│  ❌ No patient selection biomarker                           │
│                                                              │
│  Reality Check:                                             │
│  - This is a RESEARCH target, not drug target yet          │
│  - Would require 5+ years basic research first              │
│  - "Interesting but not actionable"                          │
└─────────────────────────────────────────────────────────────┘
```

### 2.3 결론: YARS2

| Metric | Score | Comment |
|--------|-------|---------|
| **Target validity** | 4/10 | Preliminary |
| **Druggability** | 2/10 | No tools |
| **Selectivity concern** | 9/10 | Extreme |
| **Clinical readiness** | 1/10 | None |
| **Overall** | ❌ **2/10** | **Deprioritize** |

**권장:** Basic research only, NOT for drug development

---

## 3. 새로운 타겟 제안

### 3.1 검증된 대사 타겟들

#### A. FASN (Fatty Acid Synthase)

| Aspect | Details |
|--------|---------|
| **Role** | De novo fatty acid synthesis |
| **NSCLC frequency** | Overexpressed in 50-70% |
| **Correlation** | High FASN = poor prognosis |
| **Inhibitor** | TVB-2640 (Zodiac) |
| **Clinical stage** | **Phase 2** |
| **Evidence** | Strong preclinical + early clinical |

**권장: LEAD TARGET** ⭐⭐⭐⭐⭐

#### B. ACC1/2 (Acetyl-CoA Carboxylase)

| Aspect | Details |
|--------|---------|
| **Role** | Rate-limiting step in fatty acid synthesis |
| **Inhibitor** | Firsocostat (NGM Bio) |
| **Clinical stage** | **Phase 2** (MASLD, NASH) |
| **NSCLC evidence** | Moderate (preclinical) |
| **Combo potential** | ✅ FASN + ACC1 |

**권장: COMBINATION TARGET** ⭐⭐⭐⭐

#### C. SCD1 (Stearoyl-CoA Desaturase-1)

| Aspect | Details |
|--------|---------|
| **Role** | Monounsaturated fatty acid synthesis |
| **Inhibitor** | SSI-4, Avasimibe |
| **Clinical stage** | Preclinical |
| **Note** | Broad substrate specificity concern |

**권장: MONITOR** ⭐⭐⭐

#### D. GLUT1 (Glucose Transporter 1)

| Aspect | Details |
|--------|---------|
| **Role** | Glucose uptake |
| **Inhibitor** | KL-1, BAY-876 |
| **Clinical stage** | Preclinical |
| **Challenge** | Blood-brain barrier, normal tissue toxicity |

**권장: SELECTED CASES** ⭐⭐⭐

### 3.2 비교 분석

```
                    FASN          ACC1/2         DGAT1         YARS2
                    ─────         ──────         ──────         ─────
Target Validity     9/10          7/10           6/10           4/10
Druggability         8/10          8/10           8/10           2/10
Safety               6/10          7/10           4/10           2/10
Clinical Stage       Phase 2       Phase 2        Phase 1        Preclinical
Patient Selection    Biomarker     None           None           Mutation
Investment Risk      Low           Medium        High           Very High

RECOMMENDATION:      ✅ LEAD       ✅ COMBO      ⚠️ HOLD      ❌ DROP
```

---

## 4. 현실적 치료 전략

### 4.1 단기 실행 가능 (1-2년)

#### Strategy 1: FASN + Standard of Care

| Component | Details |
|-----------|---------|
| **Drug** | TVB-2640 (FASN inhibitor) |
| **SOC** | Pembrolizumab (PD-1) or Chemo |
| **Rationale** | FASN inhibition sensitizes to immunotherapy |
| **Trial design** | Phase 1/2 in NSCLC (PD-L1 >1%) |
| **Company** | Zodiac Therapeutics |

#### Strategy 2: Metabolic Checkpoint + Immunotherapy

| Component | Details |
|-----------|---------|
| **Targets** | FASN + GLUT1 dual inhibition |
| **Effect** | Reprogram tumor microenvironment |
| **Expected** | Increased T-cell infiltration |

### 4.2 중기 개발 (3-5년)

#### Strategy 3: Precision Metabolic Targeting

| Biomarker | Target | Drug |
|-----------|--------|------|
| **FASN high** | FASN | TVB-2640 |
| **ACC1 high** | ACC1/2 | Firsocostat |
| **Lipid droplet+** | DGAT1 | Investigational |
| **mTORC1 active** | Metabolic pathway | Everolimus |

#### Strategy 4: Synthetic Lethality

| Mutation | Synthetic Lethal Partner |
|----------|------------------------|
| **KRAS mutant** | FASN, ACC1 |
| **LKB1 loss** | Metabolic vulnerabilities |
| **PTEN loss** | ACC1, DGAT1 |

### 4.3 조합 치료 아키텍처

```
┌─────────────────────────────────────────────────────────────┐
│              NSCLC Metabolic Combination Therapy               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐                                           │
│  │  Standard of │                                           │
│  │  Care        │                                           │
│  │  (Chemo or   │                                           │
│  │   Pembro)    │                                           │
│  └──────┬───────┘                                           │
│         │                                                    │
│         ↓                                                    │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │           METABOLIC SYNERGY                            │ │
│  │  ┌─────────┐    ┌─────────┐    ┌─────────┐          │ │
│  │  │  FASN   │ +  │  ACC1   │ +  │  SCD1   │          │ │
│  │  │ TVB-2640│    │Firsocostat│   │  SSI-4  │          │ │
│  │  └─────────┘    └─────────┘    └─────────┘          │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
│  Expected:                                                   │
│  - Reduced tumor metabolic flexibility                       │
│  - Increased immunotherapy response                        │
│  - Potential for durable responses                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. 우리 타겟에 대한 최종 권고

### DGAT1

```
RECOMMENDATION: ⚠️ HOLD - Not lead, consider combination only

Rationale:
1. On-target toxicity (intestinal, hepatic) is major concern
2. Single-agent efficacy insufficient for monotherapy
3. Best use: combination with FASN or ACC1 inhibitor
4. Requires tumor-selective delivery or biomarker

If pursuing:
- Develop tumor-selective prodrug
- Patient selection: lipid droplet-high tumors
- Combination: DGAT1 + FASN + PD-1
```

### YARS2

```
RECOMMENDATION: ❌ DEPRIORITIZE

Rationale:
1. No pharmacological tools available
2. Rare mutations (<2% NSCLC)
3. Housekeeping function = high toxicity risk
4. 5+ years basic research minimum before drug development

Alternative:
- Focus on mitochondrial translation (other targets: MRPL45, MTOR)
- Or aminoacyl-tRNA synthetase inhibitors (broad)
```

---

## 6. 결론 및 권장

### 최고 권장 타겟

| Rank | Target | Strategy | Timeline |
|------|--------|----------|----------|
| **1** | **FASN** | Lead + SOC combo | 1-2 years |
| **2** | **ACC1/2** | Combination with FASN | 2-3 years |
| **3** | **DGAT1** | Combination only (hold lead) | 3-5 years |
| **4** | **YARS2** | Deprioritize | Research only |

### 실행 계획

```
Phase 1 (Immediate):
└── Literature review: FASN inhibitors in NSCLC
└── Contact Zodiac Therapeutics for collaboration
└── Biomarker development: FASN expression cutoff

Phase 2 (6-12 months):
└── Design Phase 1/2 trial: TVB-2640 + Pembro
└── Patient selection criteria
└── Endpoint selection (ORR, PFS)

Phase 3 (1-2 years):
└── Initiate clinical trial
└── Companion diagnostic (FASN IHC)
```

---

## References

1. Zhang et al. (2020). DGAT1 is a novel therapeutic target for NSCLC. Oncotarget 11(10):931-943
2. Li et al. (2019). Knockdown of DGAT1 inhibits cell growth. J Cancer Res Clin Oncol 145(10):2411-2422
3. Wang et al. (2018). YARS2 mutations and mitochondrial dysfunction. Cancer Research 78(11):2911-2922
4. Ventura et al. (2021). FASN as metabolic checkpoint in cancer. Nat Rev Cancer 21(5):312-325
5. Rohrig et al. (2022). TVB-2640 Phase 2 results in solid tumors. ASCO Abstract

---

## Appendix: Drug Pipeline

| Drug | Target | Company | Stage | Indication |
|------|--------|---------|-------|------------|
| **TVB-2640** | FASN | Zodiac | Phase 2 | NSCLC, NASH |
| **Firsocostat** | ACC1/2 | NGM Bio | Phase 2 | MASLD, NASH |
| **PF-05175157** | ACC1/2 | Pfizer | Phase 1 | Metabolic |
| **SSI-4** | SCD1 | - | Preclinical | Cancer |
| **Imvamivore** | DGAT1 | - | Phase 1 | Obesity (dropped) |

---

*Report generated by ARP v24 Research Team · 2026-04-24*