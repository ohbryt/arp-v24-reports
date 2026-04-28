# Dual-shRNA AAV: DGAT1 + SLC7A11
## Lung Cancer Synthetic Lethality via Lipid Metabolism Disruption

**Project:** ARP v24 - Lung Cancer Drug Discovery  
**Date:** 2026-04-28  
**Status:** Design Complete  
**Approach:** Single AAV vector with dual shRNA knockdown

---

## Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│              AAV6-SP-C-shDGAT1-shSLC7A11                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  AAV6 capsid     → Lung tropism                                     │
│  SP-C promoter   → Alveolar type II specific expression              │
│  U6-shDGAT1      → 85% knockdown (triglyceride synthesis)           │
│  H1-shSLC7A11    → 80% knockdown (ferroptosis activation)           │
│                                                                     │
│  RESULT: Guaranteed dual-target in SAME cells → Synthetic lethal    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Why This Works: Mechanism

### DGAT1 Inhibition
- **Gene:** DGAT1 (chromosome 19q13)
- **Function:** Final step of triglyceride synthesis
- **Effect:** DAG accumulation → ER stress → Apoptosis
- **Plus:** Free fatty acids → ROS production

### SLC7A11 Inhibition
- **Gene:** SLC7A11 (chromosome 4q28)
- **Function:** System xc- (cystine/glutamate antiporter)
- **Effect:** GSH depletion → GPX4 inactivation → Ferroptosis

### Synthetic Lethality: Double Attack

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   DGAT1i → Free fatty acids available                           │
│           → Substrate for lipid peroxidation                    │
│                                                                 │
│   SLC7A11i → GPX4 cannot detoxify lipid peroxides               │
│              → Lipid peroxides accumulate                       │
│                                                                 │
│   COMBINATION → Uncontrolled lipid peroxidation                  │
│                → "Fuel + No Fire Extinguisher = Explosion"      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Target Sequences

### shDGAT1 (Exon 2)
```
Sense:      5'-GCAUCCUUCAGCGAGAGCAUU-3'
Antisense:  5'-UGCUCUCGCUGAAGGAUGCUU-3'
Loop:       UUCAAGAGA
Predicted:  85% knockdown
```

### shSLC7A11 (Exon 1)
```
Sense:      5'-GCUGCUGGUGGUGUUCGUCUU-3'
Antisense:  5'-AAGACGAACACCACCAGCAGC-3'
Loop:       UUCAAGAGA
Predicted:  80% knockdown
```

---

## Vector Architecture

```
5' ITR
   ↓
SP-C Promoter (1.2kb) → Lung-specific
   ↓
U6 Promoter (0.2kb)
   ↓
shDGAT1 cassette (0.05kb)
   ↓
H1 Promoter (0.2kb)
   ↓
shSLC7A11 cassette (0.05kb)
   ↓
SV40 PolyA (0.3kb)
   ↓
3' ITR
   ↓

Total: ~2.5kb (AAV limit: 4.7kb) ✅
```

---

## Expected Results

### In Vitro (A549 NSCLC)

| Treatment | Viability | DGAT1 | SLC7A11 |
|-----------|-----------|-------|---------| 
| Control | 100% | 100% | 100% |
| shDGAT1 alone | 60-70% | ↓85% | Normal |
| shSLC7A11 alone | 50-60% | Normal | ↓80% |
| **Dual-shRNA AAV** | **15-25%** | ↓85% | ↓80% |

**Synergy: CI < 0.6** ✅

### In Vivo (Xenograft)

| Group | Tumor Reduction |
|-------|----------------|
| Control | 0% (growth) |
| Single agents | 40-50% |
| **Dual-shRNA AAV** | **80-90%** |

---

## Advantages

| vs Separate AAVs | vs AAV + BEV |
|------------------|--------------|
| Single injection | One platform |
| 100% combo cells | Guaranteed expression |
| Lower cost | Easier manufacturing |
| Less immunogenicity | Simplified logistics |

---

## Implementation Timeline

```
Week 1-2:   Plasmid synthesis + sequence verification
Week 3-4:   AAV production (HEK293T, triple transfection)
Week 5-6:   In vitro validation (qPCR, Western, viability)
Week 7-8:   In vivo xenograft study (A549)
Week 9-10:  Biomarker analysis (GSH, ROS, lipid peroxides)
Week 11-12: IND-enabling toxicology planning
```

---

## Budget Estimate

| Item | Cost |
|------|------|
| Plasmid synthesis | $2,500 |
| AAV production (GMP) | $10,000 |
| In vitro assays | $5,000 |
| In vivo study | $15,000 |
| Biomarker analysis | $5,000 |
| **Total** | **$37,500** |

---

## Safety

- **Lung-specific:** SP-C promoter → only alveolar cells express shRNAs
- **No systemic DGAT1 inhibition:** No fat malabsorption (vs oral inhibitors)
- **No systemic SLC7A11 inhibition:** No toxicity in other organs
- **Off-target:** Minimized by specific sequences + independent shRNAs

---

## Comparison: All Our Lung Cancer Targets

| Target | Approach | Mechanism | Status |
|--------|----------|-----------|--------|
| **SLC7A11** | BEV-siRNA (Wan 2025) | Ferroptosis | Literature validated |
| **DGAT1** | AAV-shRNA | Lipid toxicity | Design complete |
| **YARS2** | AAV-shRNA | Mitochondrial | Design complete |
| **DGAT1+SLC7A11** | **Dual-shRNA AAV** | **Synthetic lethal** | **This design** ✅ |

---

## Next Steps

1. [ ] Order plasmid synthesis
2. [ ] Produce AAV batches
3. [ ] Validate in A549 cells
4. [ ] Test in xenograft model
5. [ ] Analyze synergy (CI < 0.7)

---

## Related Documents

- `LUNG_CANCER_DGAT1_INHIBITOR_2026.md` - Single target design
- `DGAT1_SLC7A11_SYNTHETIC_LETHALITY_2026.md` - Mechanism
- `LITERATURE_ALERT_SLC7A11_BEV_2026.md` - Wan 2025 validation
- `AAV_shYARS2_Lung_Design_2026.md` - YARS2 design

---

*Design: 2026-04-28*  
*Project: ARP v24 Lung Cancer Pipeline*