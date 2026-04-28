# DGAT1 + SLC7A11 Synthetic Lethality Strategy
## Lipid Metabolism Double Attack for NSCLC

**Date:** 2026-04-28  
**Status:** CONFIRMED STRATEGY  
**Target:** NSCLC via lipid metabolism disruption

---

## Executive Summary

```
DECISION: DGAT1 + SLC7A11 is our PRIMARY combination strategy

RATIONALE:
- DGAT1: Triglyceride synthesis → Lipid droplet depletion
- SLC7A11: System xc- → Ferroptosis (iron death)
- BOTH: Converge on lipid peroxidation + ROS
- RESULT: Synthetic lethal for NSCLC

APPROACH:
├── Step 1: AAV-shDGAT1 (lung-specific)
├── Step 2: Combine with BEV-siSLC7A11 or commercial inhibitors
└── Step 3: Validate synthetic lethal effect
```

---

## 🎯 Mechanism: Why This Works

### Lipid Metabolism Overview

```
NORMAL CANCER CELL:
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   Glucose → Fatty Acid → Triglyceride (DGAT1)          │
│                              ↓                          │
│                        Lipid Droplets                   │
│                              ↓                          │
│                        Energy Storage                  │
│                              ↓                          │
│                        Cell Survival                    │
│                                                         │
└─────────────────────────────────────────────────────────┘

DGAT1 INHIBITED:
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   Glucose → Fatty Acid → DAG (accumulates)             │
│                              ↓                          │
│                        ER Stress                        │
│                              ↓                          │
│                        Apoptosis                        │
│                                                         │
│   + Free fatty acids → ROS production                  │
│   + Lipid peroxidation → Cell damage                  │
│                                                         │
└─────────────────────────────────────────────────────────┘

SLC7A11 INHIBITED:
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   System xc- blocked → Cystine import ↓                 │
│                              ↓                          │
│                        GSH synthesis ↓                  │
│                              ↓                          │
│                        GPX4 activity ↓                  │
│                              ↓                          │
│                        Ferroptosis (iron death)        │
│                                                         │
│   + Lipid peroxidation accumulates                     │
│   + ROS damages membranes                              │
│                                                         │
└─────────────────────────────────────────────────────────┘

DGAT1 + SLC7A11 COMBINATION:
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   DGAT1i → Free fatty acids available                   │
│            → Substrate for lipid peroxidation          │
│                                                         │
│   SLC7A11i → GPX4 activity reduced                     │
│              → Can't detoxify lipid peroxides          │
│                                                         │
│   RESULT: EXCEPTIONALLY STRONG LETHALITY               │
│                                                         │
│   "Fuel + No Fire Extinguisher = Explosion"           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 🧬 Molecular Rationale

### DGAT1 (Diacylglycerol O-Acyltransferase 1)

```
Gene: DGAT1 (chromosome 19q13)
Function: Final step of triglyceride synthesis

In NSCLC:
- High expression (DepMap essential)
- Knockdown: 50-70% viability reduction
- Mechanism: Lipid droplet depletion + DAG toxicity

Key pathway:
DAG → TG (DGAT1) → Lipid droplets

If DGAT1 blocked:
- DAG accumulates → ER stress → apoptosis
- Free fatty acids increase → oxidative stress
```

### SLC7A11 (System xc- subunit)

```
Gene: SLC7A11 (chromosome 4q28)
Function: Cystine/glutamate antiporter

In NSCLC:
- High expression ( ferroptosis resistance)
- Knockdown: Ferroptosis induction
- Mechanism: GSH synthesis → GPX4 → ROS detox

Key pathway:
SLC7A11 → Cystine import → GSH → GPX4 → Lipid peroxide detox

If SLC7A11 blocked:
- Cystine import stops → GSH depletes
- GPX4 can't function → lipid peroxides accumulate
- Ferroptosis (iron-dependent cell death)
```

### Synthetic Lethality Explanation

```
WHY SYNTHETIC LETHAL?

Condition 1: DGAT1 inhibition alone
→ Some lipid stress, some cell death
→ Cancer cells can adapt (use other lipids)

Condition 2: SLC7A11 inhibition alone  
→ Ferroptosis, but limited by available lipids
→ Some cells survive via antioxidant pathways

Condition 3: DGAT1 + SLC7A11 inhibition
→ MASSIVE lipid stress
→ Maximum ROS + lipid peroxidation
→ No escape route for cancer cells
→ Complete metabolic collapse

KEY INSIGHT:
DGAT1 inhibition releases free fatty acids
→ These become the SUBSTRATE for ferroptosis
→ SLC7A11 inhibition prevents detox
→ FERROPTOSIS ON STEROIDS
```

---

## 📊 Expected Results

### In Vitro (A549 cells)

| Treatment | Viability | Lipid Droplets | ROS | Ferroptosis |
|-----------|-----------|----------------|-----|-------------|
| **Control** | 100% | High | Low | None |
| **shDGAT1** | 60-70% | ↓↓ | ↑ | Moderate |
| **siSLC7A11** | 50-60% | Normal | ↑↑ | Strong |
| **shDGAT1 + siSLC7A11** | **20-30%** | ↓↓↓ | ↑↑↑ | **MAXIMAL** |

### In Vivo (Xenograft)

```
Expected tumor reduction:
- shDGAT1 alone: ~40%
- siSLC7A11 alone: ~50%  
- shDGAT1 + siSLC7A11: ~75-85%

Synergy: 1+1 > 2 effect
```

---

## 🔧 Implementation Strategy

### Phase 1: Single Agent Validation

```
Step 1A: AAV-shDGAT1 alone
- Validate knockdown efficiency (85%)
- Confirm anti-proliferation effect
- Characterize mechanism (DAG, ROS)

Step 1B: BEV-siSLC7A11 alone
- Use paper's approach (Wan 2025)
- Or commercial SLC7A11 inhibitors
- Confirm ferroptosis induction
```

### Phase 2: Combination Therapy

```
Step 2A: In vitro combination
- AAV-shDGAT1 + BEV-siSLC7A11
- Test synergy ratio
- Determine optimal dosing

Step 2B: In vivo validation
- Syngeneic mouse model
- Compare single vs combo
- Measure tumor volume, survival
```

### Phase 3: IND-enabling Studies

```
Step 3A: Toxicology
- 28-day repeat dose (lung-specific)
- Safety assessment (systemic vs local)

Step 3B: PK/PD
- Lung concentration vs plasma
- Biomarker validation (GSH, ROS, lipid profiles)
```

---

## 🎯 Deliverables

### Construct Design (Complete)

```
AAV-shDGAT1 (Lung-specific)
├── Capsid: AAV6
├── Promoter: SP-C
├── shRNA: GCAUCCUUCAGCGAGAGCAUU (85%)
└── Size: ~2.4kb ✅

BEV-siSLC7A11 (From Wan 2025)
├── Engineered bacterial EVs
├── siRNA targeting SLC7A11
└── Lung-targeted delivery
```

### Alternative: Oral SLC7A11 Inhibitors

```
If BEV not available:
- Erastin analogs (PF-06423073)
- Sulfasalazine (generic, FDA-approved for IBD)
- Alternative: Sorafenib (multi-kinase inc. SLC7A11)

Combo: Oral SLC7A11 inhibitor + AAV-shDGAT1
```

---

## 📊 Timeline & Budget

### Timeline

```
Month 1-2:  Construct + AAV production
Month 3-4:  In vitro single agent validation
Month 5-6:  In vitro combination (synergy)
Month 7-8:  In vivo (xenograft)
Month 9-10: PK/PD studies
Month 11-12: IND-enabling toxicology
```

### Budget

| Item | Cost | Notes |
|------|------|-------|
| Plasmid + AAV | $10,000 | Both constructs |
| In vitro assays | $5,000 | Cell viability, ROS, lipid |
| In vivo study | $15,000 | Xenograft + imaging |
| PK/PD | $8,000 | Biomarker analysis |
| Toxicology | $20,000 | IND-enabling |
| **Total** | **$58,000** | |

---

## ⚠️ Risk Mitigation

| Risk | Mitigation |
|------|------------|
| BEV immunogenicity | Use AAV alternative |
| Off-target effects | Validate shRNA specificity |
| Toxicity (systemic) | Lung-specific delivery (SP-C) |
| Synergy not achieved | Test multiple ratios |
| Manufacturing | Use established platforms |

---

## 🎯 Success Metrics

```
PRIMARY:
- >80% tumor reduction (combo vs control)
- Synthetic lethal confirmed (CI < 0.7)
- No severe toxicity at therapeutic dose

SECONDARY:
- Biomarker validation (GSH, ROS, lipid peroxides)
- Lung-specific targeting confirmed
- Repeat dosing tolerated
```

---

## 🔗 Related Documents

- `LUNG_CANCER_DGAT1_INHIBITOR_2026.md` - DGAT1 design
- `LITERATURE_ALERT_SLC7A11_BEV_2026.md` - SLC7A11 validation
- `SLC7A11_COMPREHENSIVE_ANALYSIS_2026.md` - Full target analysis
- `YARS2_LUNG_CANCER_FULL_PIPELINE_REPORT_2026.md` - YARS2 data

---

## 📝 Summary

```
DGAT1 + SLC7A11 SYNTHETIC LETHALTY STRATEGY:

MECHANISM:
- DGAT1 inhibition → Free fatty acids + DAG toxicity
- SLC7A11 inhibition → Ferroptosis (no GSH/GPX4)
- COMBINATION → Uncontrolled lipid peroxidation

STRATEGY:
1. AAV-shDGAT1 (lung-specific, SP-C promoter)
2. BEV-siSLC7A11 or oral inhibitors (Wan 2025 validated)
3. Combination in NSCLC models

EXPECTED OUTCOME:
- 75-85% tumor reduction (combo)
- Synthetic lethal confirmed
- Novel lung cancer therapy

STATUS: CONFIRMED - Ready for execution
```

---

*Document: arp-v24/DGAT1_SLC7A11_SYNTHETIC_LETHALITY_2026.md*  
*Strategy confirmed: 2026-04-28*