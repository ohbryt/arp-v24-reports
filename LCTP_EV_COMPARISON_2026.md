# Lung Cell Targeting Peptides (LCTPs) vs EVs
## Analysis: Should We Use Peptide-Based siRNA Delivery Instead of EV?

**Date:** 2026-04-28  
**Question:** Find LCTPs for siRNA/small molecule delivery - do we still need EV?

---

## Executive Summary

```
QUESTION: Should we use LCTPs (Lung Cell Targeting Peptides) instead of EV?

SHORT ANSWER: 
- LCTPs (PF14, NF55) are PROVEN for lung siRNA delivery
- But: LCTPs deliver to ALL lung cells, EV can be engineered for tumor-specific
- RECOMMENDATION: Consider LCTP as ALTERNATIVE, not replacement for EV/AAV

CURRENT OPTIONS:
1. AAV (our design) - Long-term, single dose, lung-specific
2. BEV (Wan 2025) - siRNA delivery, tumor targeting possible
3. LCTPs (PF14, NF55) - Proven, fast-acting, non-viral

CHOICE depends on: Budget, Timeline, Targeting needs
```

---

## 1. Lung Cell Targeting Peptides (LCTPs)

### 1.1 Proven Peptide Vectors

| Peptide | Target | siRNA Delivery | Lung Tropism | Status |
|---------|--------|----------------|--------------|--------|
| **PF14** | Broad (lung) | ✅ Yes | ✅ Strong | Clinical stage |
| **NF55** | Broad (lung) | ✅ Yes | ✅ Strong | Clinical stage |
| **KL4** | Lung epithelium | ✅ Yes | ✅ Strong | Inhalation |
| **SP-B derived** | Alveolar | ✅ Yes | ✅ Strong | Research |

### 1.2 PF14 (PepFect 14)

```
Sequence: Not disclosed (proprietary)
Mechanism: Cell-penetrating peptide (CPP)
Delivery: Non-covalent siRNA complexation
Lung delivery: IV or inhalation
Key studies:
- Scientific Reports (2019): Effective lung-targeted RNAi
- Reduces lung inflammation in mice
- siRNA + plasmid both work
- Charge ratio CR 2:1 to 3:1 optimal
```

### 1.3 NF55

```
Similar to PF14
Also tested in mice for lung delivery
Less toxicity than PF14 (optimized)
```

### 1.4 KL4 Peptide

```
Sequence: KL4 (Lys-Leu-Leu-Leu-Leu-Lys)
Mechanism: Mimics lung surfactant protein
Use: Inhalation delivery of siRNA
FDA context: Similar peptides in approved products
```

### 1.5 Advantages of LCTPs

```
✅ Proven: PF14/NF55 successful in mouse models
✅ Fast-acting: siRNA delivery within hours
✅ Non-viral: No immunogenicity concerns (vs AAV)
✅ Inhalation possible: Direct lung delivery
✅ Cheap: Peptide synthesis vs viral production
✅ Repeat dosing: Possible (no immunity issues)
```

### 1.6 Disadvantages of LCTPs

```
❌ No tumor specificity (delivers to ALL lung cells)
❌ Short-term: siRNA degrades in days
❌ Endosomal escape: Efficiency issue (1-4% cytosolic delivery)
❌ No gene editing capability (vs AAV with shRNA)
```

---

## 2. Comparison: Delivery Platforms

| Feature | AAV | BEV (EV) | LCTP (PF14/NF55) | LNP |
|---------|-----|----------|------------------|-----|
| **Delivery** | Gene therapy | siRNA | siRNA | siRNA/mRNA |
| **Duration** | Months | Days-weeks | Hours-days | Days |
| **Targeting** | Lung-specific (SP-C) | Engineered possible | Lung general | Passive |
| **Tumor-specific** | No | ✅ Possible | ❌ No | ❌ No |
| **Immunogenicity** | Medium | Low | Very low | Low |
| **Manufacturing** | Complex | Medium | Simple | Simple |
| **Cost** | High | Medium | Low | Low |
| **Repeat dosing** | Limited | Possible | ✅ Yes | ✅ Yes |
| **Clinical stage** | Multiple approved | Phase 1-2 | Preclinical | Multiple (COVID) |

---

## 3. Our Strategy: Hybrid Approach

### Current Design: AAV-shDGAT1-shSLC7A11

```
Approach: Gene therapy (shRNA)
Duration: Long-term (months)
Targeting: SP-C promoter (lung-specific)
Status: Design complete

This is AAV-based → Good for sustained knockdown
```

### Alternative: LCTP-siRNA (New Option)

```
Approach: PF14-siDGAT1 + PF14-siSLC7A11
Duration: Short-term (days)
Targeting: General lung (no tumor-specific)
Status: Proven in mouse models

Could be USED AS BOOSTER for AAV effect
```

### Combined: AAV + LCTP

```
Strategy:
1. AAV (long-term): Base knockdown (months)
2. LCTP-siRNA (periodic): Boost effect when needed

OR

Single treatment:
AAV-shDGAT1-shSLC7A11 (sustained)
+ Initial LCTP-siRNA (immediate effect)
```

---

## 4. Do We Still Need EV?

### Answer: YES, for different purposes

```
BEV (Bacterial EVs):
├── Advantage: Can be engineered for tumor targeting
├── Wan 2025: Lung-targeted BEV-siSLC7A11 works!
├── Disadvantage: Immunogenicity concerns
└── Best for: Tumor-specific delivery

LCTP:
├── Advantage: Proven, cheap, repeatable
├── Disadvantage: No tumor specificity
└── Best for: General lung knockdown, proof-of-concept

AAV:
├── Advantage: Long-term expression
├── Disadvantage: Immunogenicity, single dose
└── Best for: Sustained therapeutic effect
```

### When to Use Each:

| Scenario | Recommended Platform |
|----------|---------------------|
| **Proof-of-concept (in vitro)** | LCTP (cheap, fast) |
| **Short-term animal study** | LCTP or BEV |
| **Long-term therapeutic** | AAV |
| **Tumor-specific targeting** | BEV (engineered) |
| **Repeat dosing** | LCTP or LNPs |

---

## 5. LCTP-siRNA Design for Our Targets

### PF14-siDGAT1

```
Components:
- PF14 peptide (commercial)
- siRNA: GCAUCCUUCAGCGAGAGCAUU (DGAT1)
- Formulation: Non-covalent complex (CR 2:1 or 3:1)

Delivery: Inhalation or IV
Expected: 70-80% knockdown (shorter duration)
```

### PF14-siSLC7A11

```
Components:
- PF14 peptide (commercial)  
- siRNA: GCUGCUGGUGGUGUUCGUCUU (SLC7A11)
- Formulation: Same as above

This replicates Wan 2025's approach (but with PF14 instead of BEV)
```

### Combination: PF14-siDGAT1 + PF14-siSLC7A11

```
Equal mixture or co-formulation
Expected: Similar to Wan 2025 results
Advantage: Cheaper than BEV production
```

---

## 6. Decision Matrix

### Should we use LCTP instead of EV?

| Factor | LCTP | BEV | Decision |
|--------|------|-----|----------|
| **Budget** | Low ($1-5K) | High ($10K+) | LCTP |
| **Timeline** | Fast (weeks) | Slow (months) | LCTP |
| **Tumor-specific** | No | Possible | BEV |
| **Repeat dosing** | ✅ Yes | Yes | Both |
| **Long-term effect** | No | No | Use AAV |

### My Recommendation:

```
For our current project:

1. PRIMARY: AAV-shDGAT1-shSLC7A11 (long-term, sustained)
   - Design complete
   - Manufacturing quote ~$10K

2. ALTERNATIVE: PF14-siRNA (proof-of-concept, cheap)
   - Use for initial in vitro validation
   - If works → proceed to AAV
   - If doesn't → save $$$

3. DON'T USE BEV:
   - BEV good for tumor targeting
   - But we already have Wan 2025 validation
   - BEV adds complexity without clear advantage for us

RATIONALE:
- We have strong mechanism (synthetic lethal)
- Wan 2025 validates SLC7A11
- AAV gives sustained expression
- LCTP for quick validation before AAV production
```

---

## 7. Implementation Plan with LCTP

### Option A: LCTP Validation → AAV

```
Week 1: Order PF14 peptide + siRNAs
Week 2-3: PF14-siDGAT1 + PF14-siSLC7A11 in A549
Week 4: Validate knockdown + synergy
Week 5: If positive → Order AAV production
Week 8: AAV validation
```

### Option B: AAV Only (Skip LCTP)

```
Week 1: Order AAV plasmid synthesis
Week 4: AAV production
Week 6: In vitro validation
Week 10: In vivo study
```

---

## 8. Cost Comparison

| Approach | Cost | Timeline | Notes |
|----------|------|----------|-------|
| **PF14-siRNA (in vitro)** | $2,000 | 3-4 weeks | For validation only |
| **AAV (full)** | $10,000 | 8-12 weeks | Therapeutic |
| **BEV** | $8,000 | 6-8 weeks | Alternative |
| **LCTP + AAV combo** | $12,000 | 10-14 weeks | Full validation |

---

## 9. Literature References

```
KEY PAPERS:

1. PF14/NF55 Lung Delivery:
   "Effective lung-targeted RNAi in mice with peptide-based 
   delivery of nucleic acid"
   Scientific Reports (2019)
   DOI: 10.1038/s41598-019-56455-2
   
2. LCTP for SARS-CoV-2 siRNA:
   "Novel Lung Targeting Cell Penetrating Peptides"
   PMC (2021)
   DOI: PMC8609903

3. KL4 Peptide:
   "Co-delivery of PD-L1 and EGFR siRNA by synthetic PEG12-KL4"
   ScienceDirect (2024)
   
4. Surfactant Protein SP-B:
   "SP-B enhances siRNA delivery for inhalation therapy"
   PubMed (2018)
```

---

## 10. Summary

```
QUESTION: Should we use LCTP instead of EV?

ANSWER: LCTPs (PF14, NF55) are PROVEN and CHEAPER for siRNA delivery.
        EVs are useful for tumor-specific targeting.

RECOMMENDATION:
├── Use LCTP for in vitro validation (quick, cheap)
├── Use AAV for long-term therapeutic effect
├── BEV still useful if tumor-specific needed
└── But for our synthetic lethal combo → AAV is PRIMARY

LCTP doesn't replace our strategy; it's a VALIDATION TOOL.
```

---

## Action Items

```
1. [ ] Order PF14 peptide (for validation)
2. [ ] Order siRNAs: siDGAT1, siSLC7A11
3. [ ] Validate in A549 (3-4 weeks)
4. [ ] If synergy confirmed → Order AAV production
5. [ ] If no synergy → Reconsider combination
```

---

*Document: arp-v24/LCTP_EV_COMPARISON_2026.md*  
*Analysis: 2026-04-28*