# Yao et al. 2026 - Dietary Intake and BCAA Metabolism Regulate Pulmonary Fibrosis through KDM4A-Mediated Epigenetic Remodeling
## Full Paper Analysis - With Quantitative Data

**Date:** 2026-04-30  
**Source:** Nature Communications | DOI: 10.1038/s41467-026-72273-3  
**Authors:** Jie Yao, Su Fang, Miao Lei, Zexian Ou, Chuanfei Zeng, et al.  
**Correspondence:** Qian Han (hanqian1020@yahoo.com), Wenxiang Hu (hu_wenxiang@gzlab.ac.cn)  
**Institution:** Guangzhou National Laboratory, Guangzhou Medical University

---

## Publication Details

```
Received: 29 May 2025
Accepted: 13 April 2026
License: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0
Data availability: GEO datasets (GSE295426, GSE295424, GSE295425, GSE295423, GSE295427)
```

---

## Abstract (Complete)

```
Idiopathic pulmonary fibrosis (IPF) is a progressive, fatal disorder characterized by 
abnormal activation of alveolar fibroblasts. This study shows:

1. BCAA uptake INCREASED, catabolism IMPAIRED in fibrotic lung fibroblasts
2. BCAAs promote lung fibroblast activation AND bleomycin-induced lung fibrosis
3. Genetic inactivation of BCAT2 EXACERBATES fibrosis
4. Inhibition of SLC7A5 or enhancement of catabolism ATTENUATES pulmonary fibrosis

Mechanistically:
├── ATF4 regulates SLC7A5 expression
├── PPARγ regulates BCAA catabolic genes
├── KDM4A = key epigenetic mediator of fibrotic genes
└── H3K36me3 modification on collagen genes

Clinical relevance:
└── Dysregulated BCAA metabolism correlates with disease severity in IPF patients
```

---

## Key Quantitative Data

### 1. BCAA Levels in Fibrotic Conditions

**In TGFβ-treated MLFs (Mouse Lung Fibroblasts):**
```
Leucine fold change: ~1.2 vs PBS (p < 0.0001)
Isoleucine fold change: ~1.4 vs PBS (p < 0.0001)  
Valine fold change: ~1.75 vs PBS (p < 0.0001)
```

**In Bleomycin-treated mouse lungs:**
```
Leucine: elevated vs PBS
Isoleucine: elevated vs PBS
Valine: elevated vs PBS
```

### 2. BCAA Metabolic Gene Expression (TGFβ-treated MLFs)

**Upregulated:**
```
SLC7A5: upregulated (transporter)
BCAT1: upregulated (contrary to BCAT2)
```

**Downregulated:**
```
BCAT2: dramatically downregulated
BCKDHA: downregulated
BCKDHB: downregulated
DBT: downregulated
DLD: downregulated
```

### 3. BCAT2 Heterozygous Mice (BCAT2+/-)

**Serum BCAA (Day 14 post-BLM):**
```
WT PBS: baseline
WT BLM: elevated
BCAT2 Het BLM: further elevated vs WT BLM
  - p < 0.05 for leucine
  - p < 0.05 for isoleucine
  - p < 0.05 for valine
```

**Hydroxyproline content (lung collagen):**
```
BCAT2 Het mice: significantly elevated vs WT after BLM
(p < 0.01)
```

### 4. KDM4A Expression

**KDM4A in BCAA-free conditions with TGFβ:**
```
KDM4A: significantly upregulated
  - Reversed upon BCAA reintroduction
  - Controls H3K36me3 demethylation
```

**KDM4A overexpression:**
```
COL1A1: INHIBITED (protective)
H3K36me3: reduced globally
```

**KDM4A knockdown:**
```
COL1A1: ENHANCED (exacerbates fibrosis)
H3K36me3: increased at BCAA-dependent genes (Col5a3, Col7a1)
```

### 5. Drug Treatment Effects

**BCH (SLC7A5 inhibitor, 100 mg/kg):**
```
Treatment: BLM + BCH
Results:
- Lower BCAA in serum and lung
- Reduced fibrotic changes on microCT
- Decreased collagen deposition (Masson staining)
- Lower Col1a1 expression
```

**BT2 (BCKDK inhibitor, 20 mg/kg):**
```
Compared to Nintedanib (60 mg/kg/day):
- Similar reduction in fibrosis severity
- Both reduced hydroxyproline
- BT2 + Nintedanib: NO synergistic effect
```

### 6. Clinical Data (IPF Patients, n=33)

**Serum BCAA by GAP stage:**
```
GAP Stage I: highest BCAA
GAP Stage II: intermediate
GAP Stage III: lowest BCAA
(p < 0.05 for leucine, isoleucine, valine)
```

**Correlation with lung function:**
```
Serum Leucine vs FVC: r = 0.5003 (p = 0.0079)
Serum Leucine vs FVC% predicted: r = 0.4659 (p = 0.0251)
Serum Leucine vs DLCO: r = 0.4242 (p = 0.0274)
Serum Leucine vs DLCO% predicted: r = 0.4302 (p = 0.0404)

(Negative correlations with GAP and mMRC scores)
```

---

## Mechanistic Pathway

```
                    BCAAs (Leucine, Isoleucine, Valine)
                           ↓
                    SLC7A5 (LAT1 transporter) - ATF4 ↑
                           ↓
                    ↑ Intracellular BCAA
                           ↓
              ┌───────────┴───────────┐
              ↓                       ↓
         BCAT1 (↑)            BCAT2 (↓↓) - PPARγ ↓
         (TGFβ target)       (catabolism impaired)
              ↓                       ↓
         BCKA production        Impaired BCAA breakdown
              ↓                       ↓
              └───────────┬───────────┘
                         ↓
                  BCAA Accumulation
                         ↓
              ┌───────────┴───────────┐
              ↓                       ↓
        mTORC1 pathway          KDM4A (↑↑) 
        (not main effect)       H3K36me3 demethylation
              ↓                       ↓
        fibroblast             ECM gene activation
        activation             (Col1a1, Col5a1, etc.)
              ↓                       ↓
         LUNG FIBROSIS
```

---

## Therapeutic Targets

### Target 1: SLC7A5 (LAT1)

**Inhibitor:** BCH (2-amino-2-norbornanecarboxylic acid)  
**Dose:** 100 mg/kg in mice  
**Effect:** Reduced fibrosis, lower BCAA in lung tissue

**Clinical Relevance:**
- SLC7A5 = LAT1 (Large neutral amino acid transporter)
- JPH203/Nanvuranlat = clinical SLC7A5 inhibitors in cancer trials
- Repositioning potential for IPF

### Target 2: BCAT2

**Approach:** Enhance expression/activity  
**Note:** BCAT2 Het = worse fibrosis, BCAT2 overexpression = protective

### Target 3: KDM4A

**Inhibitor:** ML324 (pharmacological)  
**Effect:** Inhibits H3K36me3 demethylation, reduces collagen expression

**Connection to our research:**
- KDM4A also regulates SLC7A11 (ferroptosis)
- KDM4A-SLC7A11 axis in cancer (Chen et al. 2021)

### Target 4: BCKDK (BCKDH complex)

**Inhibitor:** BT2  
**Effect:** Enhances BCAA catabolism, reduces circulating BCAA

**Alternative:** Sodium phenylbutyrate (FDA-approved, targets BCKDK)

---

## Drug Doses Summary

| Drug | Target | Dose (mouse) | Route | Effect |
|------|--------|--------------|-------|--------|
| BCH | SLC7A5 | 100 mg/kg | IP | ↓ fibrosis |
| BT2 | BCKDK | 20 mg/kg | IP | ↓ fibrosis, comparable to Nintedanib |
| ML324 | KDM4A | (in vitro) | - | ↓ collagen |
| Rosiglitazone | PPARγ | (in vitro) | - | ↑ BCAA catabolism |
| Nintedanib | TKI | 60 mg/kg/day | Oral | Positive control |

---

## Animal Model Details

```
BLEOMYCIN-INDUCED PF MODEL:
- Single dose: 1.25 mg/kg (intratracheal)
- Analysis: Day 21 post-BLM

BCAA SUPPLEMENTATION:
- 30 mM each in drinking water (Leu, Ile, Val)
- 7 days before BLM
- Daily consumption: ~15.9 mg Leu, 15.9 mg Ile, 14.2 mg Val

BCAA-FREE DIET:
- 0%, 25%, 50%, 100% BCAA levels tested
- Started Day -7 or Day +7 relative to BLM

REPETITIVE BLM MODEL:
- 1.0 mg/kg weekly for 4 weeks
- Then 1 week rest
- Then BCAA-free diet for 14 days
```

---

## scRNA-seq Findings

**Cell populations in BCAT2 Het lungs:**
```
12 distinct clusters:
- Epithelial cells: REDUCED in BCAT2 Het
- Fibroblasts: INCREASED
- Macrophages: INCREASED

Fibroblast subtypes:
- Cthrc1+ pathological fibroblasts: INCREASED
- Alv. Fib-1 (alveolar fibroblast): DECREASED
```

---

## Key Statistics

**Patient correlation data (GSE47460, n=211):**
```
SLC7A5 vs DLCO: negative correlation (p = 5.915e-10)
BCAT2 vs DLCO: positive correlation (p = 1.56e-01, ns)
```

**In vitro data:**
```
TGFβ + BCAA vs TGFβ alone:
- COL1A1: ~2-3 fold increase
- ACTA2: increased
- FN1: increased

BCAA-free + TGFβ vs Complete + TGFβ:
- COL1A1: significantly reduced
```

---

## Clinical Relevance Summary

```
KEY FINDING: BCAA metabolism is druggable in IPF

1. Diagnostic marker potential:
   - Serum BCAAs correlate with lung function
   - Higher BCAA = better preserved lung function

2. Therapeutic strategies:
   a. SLC7A5 inhibition (BCH, JPH203)
   b. Enhance BCAA catabolism (BT2, NaPB)
   c. BCAA dietary restriction
   d. KDM4A inhibition (future)

3. Combination potential:
   - BT2 + Nintedanib: additive (though not synergistic in mice)
   - BT2 alone comparable to Nintedanib

4. Cross-organ implications:
   - BCAA metabolism also dysregulated in heart failure
   - KDM4A implicated in cardiac fibrosis
   - Potential for cardio-pulmonary cross-talk
```

---

## Connection to Our Research

### 1. KDM4A-SLC7A11 Axis (Our Discovery)
```
Yao 2026: KDM4A regulates collagen genes via H3K36me3
Chen 2021: KDM4A regulates SLC7A11 via H3K9me3

IMPLICATION:
KDM4A has DUAL targets:
├── Fibrotic genes (H3K36me3) → IPF
└── SLC7A11 (H3K9me3) → Ferroptosis

KDM4A inhibitor = potential for BOTH IPF and cancer
```

### 2. SLC7A5 (LAT1) - Repositioning
```
Cancer clinical trials: JPH203, Nanvuranlat (SLC7A5 inhibitors)
IPF potential: Yao 2026 shows BCH works in mice
→ Repositioning candidate
```

### 3. BCAT2 - Cardiac Connection
```
Heart failure studies show BCAA catabolism impaired
Yao 2026 shows BCAT2 is protective in lung
→ BCAT2 activation may help both lung AND heart
```

### 4. Triple Combination Potential
```
FOR IPF/Fibrosis:
BCH (SLC7A5) + BT2 (BCKDK) + KDM4A inhibitor

FOR CANCER (our focus):
JPH203 (SLC7A5) + KDM4A inhibitor + SLC7A11 inhibitor
→ Enhanced ferroptosis + anti-fibrotic
```

---

## Data Availability

```
RNA-seq: GSE295426
ATF4/PPARγ CUT&Tag: GSE295424
Histone modification CUT&Tag: GSE295425, GSE325209
ATAC-seq: GSE295423
scRNA-seq: GSE295427
Metabolomics: OMIX009983
```

---

*Document: arp-v24/sources/yao-2026-dietary-intake-and-bcaa-metabolism.md*  
*Created: 2026-04-30 (Updated with full paper data)*  
*Original abstract analysis date: 2026-04-30*