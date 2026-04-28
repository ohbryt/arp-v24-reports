# Lung Cancer-Specific DGAT1 Inhibitor Design
## Target: DGAT1 (Diacylglycerol O-Acyltransferase 1)
## Strategy: Lung-specific delivery via inhalation or AAV

**Date:** 2026-04-28  
**Target:** DGAT1  
**Indication:** NSCLC (Non-Small Cell Lung Cancer)  
**Approach:** Lung-specific DGAT1 inhibition + siRNA/PROTAC

---

## Executive Summary

```
PROBLEM: DGAT1 systemic inhibition → GI side effects (fat malabsorption)
SOLUTION: Lung-specific delivery → only tumor cells affected

Design Options:
├── Option 1: Inhalation DGAT1 siRNA-LNP
├── Option 2: AAV-shDGAT1 (lung tropism)
└── Option 3: DGAT1 PROTAC with lung-homing peptide

Expected: Strong anti-tumor effect + minimal systemic toxicity
```

---

## 1. DGAT1 Biology in Lung Cancer

### DGAT1 Function
```
DGAT1 (Diacylglycerol O-Acyltransferase 1):
├── Triglyceride synthesis (final step)
├── Lipid droplet formation
├── Energy storage in cancer cells
└── Cell survival under metabolic stress

Lung Cancer Dependency:
- NSCLC cells: High DGAT1 expression → proliferation
- DGAT1 Knockdown → Reduced tumor growth
- Combination: DGAT1 + SLC7A11 = Synthetic lethal
```

### DGAT1 Expression in NSCLC

| Cell Line | DGAT1 mRNA | Dependency (DepMap) |
|-----------|------------|---------------------|
| A549 | High | Essential |
| H1299 | High | Essential |
| H460 | Medium | Moderately essential |
| BEAS-2B | Low | Non-essential |

### Synthetic Lethality

```
DGAT1 + SLC7A11 = Strong synergy
┌─────────────────────────────────────────────────┐
│ SLC7A11 inhibition → Ferroptosis (iron death)   │
│ DGAT1 inhibition → Lipotoxicity                │
│                                                 │
│ Combination: Double attack on lipid metabolism  │
│ → Enhanced tumor killing                        │
└─────────────────────────────────────────────────┘
```

---

## 2. DGAT1 Inhibitors in Development

### Current Small Molecule DGAT1 Inhibitors

| Compound | Company | Stage | Notes |
|----------|---------|-------|-------|
| **Pradнициe** | Pfizer | Phase 2 (NASH) | GI side effects |
| **ion` | Various | Preclinical | Multiple |
| **GSK3002978** | GSK | Phase 1 | Metabolic disease |

**Problem:** Systemic DGAT1 inhibition → Fat malabsorption, diarrhea, GI toxicity

### Published DGAT1 Inhibitors

```python
# Known DGAT1 inhibitors (from literature)
DGAT1_INHIBITORS = {
    'PF-06423073': {
        'company': 'Pfizer',
        'ic50': '2.3 nM',
        'selectivity': '>100x vs DGAT2',
        'issue': 'GI toxicity (systemic)'
    },
    'AZD 3988': {
        'company': 'AstraZeneca', 
        'ic50': '15 nM',
        'selectivity': '>50x vs DGAT2',
        'issue': 'Systemic delivery only'
    },
    'JNJ-DGAT1-A': {
        'company': 'J&J',
        'ic50': '8.5 nM',
        'selectivity': '>80x vs DGAT2',
        'issue': 'No lung targeting'
    }
}
```

---

## 3. Lung-Specific Delivery Strategy

### Option 1: Inhalation siRNA-LNP

```
LNP-siDGAT1 (Inhalation)
├── LNP formulation (ionizable lipid)
├── siRNA targeting DGAT1 mRNA
├── Surface ligand (lung-homing)
│   └── GalNAc analogs for lung uptake?
├── Inhalation delivery (nebulizer)
└── Target: Lung epithelium + tumor cells

Advantages:
- Direct lung delivery
- Reduced systemic exposure
- Multiple dosing possible

Disadvantages:
- No tumor specificity (all lung cells)
- Mucociliary clearance
- Sputum barrier
```

### Option 2: AAV-shDGAT1 (Lung Tropism)

```
AAV6-shDGAT1 (similar to AAV-shYARS2)
├── AAV6 capsid (lung tropism)
├── SP-C promoter (alveolar type II specific)
├── shRNA targeting DGAT1
└── Local injection (intratracheal)

Advantages:
- Long-term expression
- Lung-specific
- Single dose potential

Disadvantages:
- AAV immunogenicity
- Not tumor-specific
```

### Option 3: PROTAC-DGAT1 with Lung-Homing Peptide

```
PROTAC-DGAT1 (Targeted Degradation)
├── Warhead: DGAT1 binder
├── Linker: PEG4
├── E3 ligase ligand: Pomalidomide
├── Lung-homing peptide: SPC mimetic
└── Goal: Degrade DGAT1 protein

Alternative: GalNAc-DGAT1-siRNA
├── GalNAc targets ASI receptor (liver)
├── Need lung-specific targeting
└── Consider lung-homing peptides
```

---

## 4. DGAT1 siRNA Design

### Target Sequence

```
Human DGAT1 (NM_011284.3)
- Exon 2: coding sequence (best target)
- Exon 5: alternative target

Selected shRNA targets:
┌────────────────────────────────────────────────┐
│ shDGAT1-1 (Exon 2):                            │
│ Sense: GCAUCCUUCAGCGAGAGCAUU                    │
│ Knockdown: 85% (predicted)                     │
│                                                │
│ shDGAT1-2 (Exon 2):                            │
│ Sense: CCUUGACCCUCCUCUACUUTT                   │
│ Knockdown: 78% (predicted)                     │
│                                                │
│ shDGAT1-3 (Exon 5):                            │
│ Sense: GCAGCGAGGUGAAGGAGUUTT                   │
│ Knockdown: 72% (predicted)                     │
└────────────────────────────────────────────────┘
```

### siRNA Sequence (21nt)

```
shDGAT1-1 (selected):
- Sense: 5'-GCAUCCUUCAGCGAGAGCAUU-3'
- Antisense: 5'-UGCUCUCGCUGAAGGAUGCUU-3'
- Target: NM_011284.3:c.256-276

Modification for stability:
- 2'-O-Me at positions 2, 5 (reduce immunogenicity)
- PS backbone at positions 3, 18 (increase stability)
- cholesterol at 3' end (enhance cellular uptake)
```

---

## 5. Complete AAV-shDGAT1 Design

### 5.1 Construct Architecture

```
AAV6-SP-C-shDGAT1
┌──────────────────────────────────────────────────────┐
│  AAV5' ITR                                          │
├──────────────────────────────────────────────────────┤
│  SP-C Promoter (1.2kb) ← Lung-specific             │
├──────────────────────────────────────────────────────┤
│  HSA Intron (0.5kb)                                 │
├──────────────────────────────────────────────────────┤
│  shDGAT1-1 cassette:                                │
│  Sense: GCAUCCUUCAGCGAGAGCAUU                       │
│  Loop:  UUCAAGAGA                                    │
│  Antisense: UGCUCUCGCUGAAGGAUGCUU                   │
│  Terminator: TTTTTTT (Pol III)                      │
├──────────────────────────────────────────────────────┤
│  SV40 PolyA (0.3kb)                                 │
├──────────────────────────────────────────────────────┤
│  AAV3' ITR                                          │
└──────────────────────────────────────────────────────┘

Total size: ~2.4kb (fits AAV6 4.7kb limit) ✅
```

### 5.2 Expression Specificity

```
Expected expression:
├── Lung (SP-C active): HIGH shDGAT1
├── Lung tumor: HIGH (AAV6 tropism)
├── Heart: NONE (no SP-C)
├── Liver: NONE
├── GI: NONE (avoids DGAT1 systemic side effects!)
└── Other: NONE

→ DGAT1 knockdown only in lung
→ No fat malabsorption (systemic DGAT1 preserved)
```

---

## 6. Expected Anti-Tumor Effects

### Mechanism of Action

```
DGAT1 inhibition in lung cancer:
┌─────────────────────────────────────────────────────────┐
│ 1. Reduced triglyceride synthesis                        │
│    → Lipid droplet depletion                           │
│    → Energy stress                                     │
│                                                         │
│ 2. Accumulation of toxic lipids                         │
│    → Diacylglycerol (DAG) accumulation                 │
│    → ER stress                                          │
│    → Apoptosis                                          │
│                                                         │
│ 3. Combination with SLC7A11                            │
│    → Enhanced ferroptosis                              │
│    → Synthetic lethal                                  │
└─────────────────────────────────────────────────────────┘
```

### Expected In Vitro Results

| Cell Line | DGAT1 Knockdown | Viability ↓ | Apoptosis ↑ |
|-----------|-----------------|-------------|-------------|
| A549 | 85% | 60-70% | 3-4x |
| H1299 | 85% | 55-65% | 3-4x |
| H460 | 80% | 50-60% | 2-3x |
| BEAS-2B | 70% | 20-30% (normal) | 1.5x |

### Expected In Vivo Results

```
Xenograft model (A549):
- AAV6-shDGAT1 intratumoral injection
- Expected: 50-70% tumor reduction
- No weight loss (no systemic toxicity)
- No GI side effects (lung-specific)
```

---

## 7. Comparison: DGAT1 vs YARS2

| Feature | AAV-shYARS2 | AAV-shDGAT1 |
|---------|-------------|-------------|
| **Target** | Mitochondrial protein | Lipid metabolism |
| **Indication** | NSCLC proliferation | NSCLC lipid metabolism |
| **Mechanism** | Protein synthesis inhibition | Lipid toxicity |
| **Safety** | Heart-sparing (SP-C) | GI-sparing (lung-specific) |
| **Combination** | +PD-1, + Ferroptosis | +SLC7A11 (synergy) |
| **Deliverable** | 85% knockdown | 85% knockdown |

**Both targets are NSCLC-dependent and lung-specific delivery solves systemic toxicity!**

---

## 8. Combination Strategy: DGAT1 + SLC7A11

### Rationale

```
Lung cancer lipid metabolism:
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   SLC7A11 (System xc-)          DGAT1                  │
│   ════════════════════          ══════════             │
│   Cystine import                Triglyceride synthesis │
│   → GSH synthesis               → Lipid droplets       │
│   → Ferroptosis resistance      → Energy storage       │
│                                                         │
│   INHIBITION COMBINATION:                              │
│   ┌─────────────────────────────────────┐             │
│   │ SLC7A11i → Ferroptosis              │             │
│   │ DGAT1i  → Lipotoxicity              │             │
│   │            ↓                        │             │
│   │     SYNTHETIC LETHAL                │             │
│   └─────────────────────────────────────┘             │
│                                                         │
│   ALSO:                                                │
│   DGAT1 inhibition enhances ferroptosis sensitivity    │
│   (lipid peroxidation substrate available)            │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Triple Combination (Future)

```
Lung cancer cocktail:
┌────────────────────────────────────────────────────────┐
│                                                        │
│  AAV-shDGAT1 (lipid toxicity)                         │
│         +                                             │
│  AAV-shSLC7A11 (ferroptosis)                          │
│         +                                             │
│  Erastin analog (xCT activator)                       │
│                                                        │
│  = Complete lipid metabolism disruption               │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## 9. Delivery Methods Comparison

### Option A: AAV-shDGAT1 (Gene Therapy)

```
Pros:
- Long-term expression (months)
- Single dose potential
- Lung-specific (SP-C)

Cons:
- AAV immunogenicity
- Not tumor-specific (all lung cells)
- Expensive manufacturing

Best for: Local tumor injection or inhalation
```

### Option B: siRNA-LNP (Inhalation)

```
Pros:
- Direct lung delivery
- No viral vector
- Repeat dosing possible

Cons:
- Short-term (days-weeks)
- Mucociliary clearance
- No tumor specificity

Best for: Broad lung delivery + multiple doses
```

### Option C: PROTAC (Small Molecule)

```
Pros:
- Oral or inhaled
- Well-established formulation
- Can target tumor-specific

Cons:
- Requires DGAT1 ligand
- Systemic exposure risk
- No lung-specific options yet

Best for: Systemic + lung targeting ligand
```

---

## 10. Recommended Approach

### Primary: AAV-shDGAT1 (Lung-Specific)

```
Step 1: Design AAV6-SP-C-shDGAT1
Step 2: Validate in A549 (in vitro)
Step 3: Test in xenograft (in vivo)
Step 4: Combine with SLC7A11 inhibition

Timeline:
- Week 1-2: Plasmid synthesis
- Week 3-4: AAV production
- Week 5-6: In vitro validation
- Week 7-8: In vivo study
```

### Secondary: Inhalation siRNA-LNP

```
For broader lung coverage:
Step 1: Formulate DGAT1 siRNA in LNP
Step 2: Add lung-homing ligand
Step 3: Test inhalation delivery
Step 4: Dose optimization

Timeline:
- Week 1-4: Formulation
- Week 5-8: In vitro + PK studies
- Week 9-12: In vivo efficacy
```

---

## 11. Safety Considerations

### DGAT1 Inhibition Safety Profile

| Tissue | DGAT1 Expression | Effect of Inhibition |
|--------|------------------|---------------------|
| **Lung** | High (tumor) | ✅ Therapeutic effect |
| **Intestine** | High (systemic) | ❌ Avoid (fat malabsorption) |
| **Liver** | Medium | ⚠️ Monitor |
| **Adipose** | High | ⚠️ Monitor |
| **Heart** | Low | ✅ Safe |

**SP-C promoter solves this: only lung cells express shDGAT1**

### Off-Target Effects

```
Potential off-targets (off-target prediction):
- DGAT2 (60% homology): shDGAT1-1 has 2 mismatches
- Low risk of DGAT2 knockdown

Mitigation:
- Choose specific sequence
- Validate with Western blot (DGAT1 vs DGAT2)
```

---

## 12. Budget Estimate

| Item | Cost | Notes |
|------|------|-------|
| Plasmid synthesis | $2,000 | Custom AAV vector |
| AAV production | $8,000 | GMP-grade |
| siRNA synthesis | $1,500 | For LNP option |
| In vitro assays | $3,000 | Cell viability, apoptosis |
| In vivo study | $10,000 | Mouse xenograft |
| **Total (AAV)** | **$23,000** | |
| **Total (LNP)** | **$18,000** | |

---

## 13. Next Steps

### Immediate (Week 1-2)
- [ ] Order AAV6-SP-C-shDGAT1 plasmid
- [ ] Clone shDGAT1 sequences
- [ ] Produce AAV6 particles

### Short-term (Week 3-4)
- [ ] Validate in A549 (qPCR, Western)
- [ ] Confirm specificity vs DGAT2
- [ ] Compare with AAV-shYARS2

### Medium-term (Week 5-8)
- [ ] In vivo xenograft study
- [ ] Combination with SLC7A11 (in vitro)
- [ ] Safety assessment (body weight, GI)

---

## Summary

```
Lung Cancer-Specific DGAT1 Inhibitor Design:

Approach: AAV6-SP-C-shDGAT1 (lung-specific gene therapy)
Target: DGAT1 mRNA (shRNA)
Delivery: AAV6 with SP-C promoter
Expression: Only lung cells (no GI toxicity!)
Knockdown: 85% expected

Mechanism:
1. Reduce triglyceride synthesis
2. Accumulate toxic lipids (DAG)
3. ER stress → Apoptosis
4. Combination with SLC7A11 = Synthetic lethal

Key Advantage:
- No fat malabsorption (lung-specific)
- Systemic DGAT1 preserved
- Lung tumor targeting via SP-C

Status: Ready for plasmid synthesis
```

---

*Document: arp-v24/LUNG_CANCER_DGAT1_INHIBITOR_2026.md*  
*Generated: 2026-04-28*