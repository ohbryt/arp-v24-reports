# Novel Metabolic Pipeline for Refractory Cancer
## Beyond FASN: DGAT1, YARS2 → New Mechanisms

**Date:** 2026-04-24  
**Company:** Brown Biotech-style Pipeline  
**Focus:** Refractory Cancer (难治性癌)  
**Strategy:** Novel Mechanisms Beyond FASN  

---

## Executive Summary

| Tier | Target | Approach | Timeline | Priority |
|------|--------|----------|----------|----------|
| **Tier 1** | **CD36** | Antibody/small molecule | 2-3 years | ⭐⭐⭐⭐⭐ |
| **Tier 1** | **ATGL** | Activator (not inhibitor!) | 3-4 years | ⭐⭐⭐⭐ |
| **Tier 2** | **GPX4** | Inhibitor | 3-4 years | ⭐⭐⭐⭐ |
| **Tier 2** | **ACSL4** | Inhibitor | 3-4 years | ⭐⭐⭐ |
| **Tier 3** | **MRPL45** | Mitochondrial translation | 4-5 years | ⭐⭐⭐ |
| **Tier 3** | **LIPIN1** | Modulator | 5+ years | ⭐⭐ |

---

## Why FASN is Not Enough

| Issue | FASN | Implication |
|-------|------|------------|
| **Competition** | Already in Phase 2 | Limited differentiation |
| **Efficacy** | Cytostatic, not cytotoxic | Not curative |
| **Resistance** | Rapid emergence | Short duration of response |
| **Biomarker** | FASN expression | Limited patient selection |

**Need:** Novel mechanisms that FASN inhibitors cannot address

---

## Part 1: Lipid Droplet Biology (핵심 신개념)

### Why Lipid Droplets Matter

```
┌─────────────────────────────────────────────────────────────┐
│                    LIPID DROPLET (LD) in CANCER                │
├─────────────────────────────────────────────────────────────┤
│  Nutrient Restriction Survival                                 │
│  ├── LD stores fatty acids for energy                        │
│  ├── Protects from lipotoxicity                             │
│  └── Enables metastasis under starvation                     │
│                                                              │
│  Cancer Stem Cell (CSC) Maintenance                          │
│  ├── CSCs have MORE LDs than bulk tumor cells              │
│  ├── LDs fuel stemness properties                          │
│  └── LD depletion → CSC differentiation → therapy sensitive │
│                                                              │
│  Therapy Resistance                                          │
│  ├── LDs sequester chemotherapeutic drugs                   │
│  ├── Provide energy for drug efflux pumps                   │
│  └── Enable EMT (epithelial-mesenchymal transition)         │
└─────────────────────────────────────────────────────────────┘
```

### The DGAT1 Problem (and Solution)

```
DGAT1 INHIBITION PROBLEM:
├── DGAT1 blocks LD formation
├── But: DGAT1 also essential for intestinal fat absorption
├── Result: Severe GI toxicity (diarrhea, malabsorption)
└── Conclusion: NOT VIABLE as systemic drug

ATGL ACTIVATION SOLUTION:
├── ATGL degrades existing LDs (lipolysis)
├── Not essential for LD formation (only degradation)
├── ATGL knockout mice: Viable (unlike DGAT1 KO)
└── Conclusion: BETTER SAFETY PROFILE
```

---

## Part 2: CD36 - The Fatty Acid Gateway

### Why CD36 is a Prime Target

| Feature | CD36 |
|---------|------|
| **Role** | Primary fatty acid transporter on cell surface |
| **CSC expression** | CD36+ cells = tumor-initiating cells |
| **Function** | Uptake of exogenous fatty acids for lipid metabolism |
| **Knockout effect** | Loss of tumor-initiating capacity |
| **Therapeutic window** | Normal tissues less dependent than tumors |

### Evidence

| Study | Finding |
|-------|---------|
| Pc | CD36+ cells in oral cancer = stem cell population |
| Nathanson et al. | CD36 is required for metastasis |
| preclinical | Anti-CD36 antibodies block tumor initiation |

### Development Strategy

| Approach | Compound | Stage |
|----------|---------|-------|
| **Antibody** | Anti-CD36 mAb | Preclinical |
| **Small molecule** | Sulfatide analogs | Preclinical |
| **siRNA** | CD36-targeted nanoparticles | Early preclinical |

**Recommended:** Partner with antibody developer or in-license existing IP

---

## Part 3: ATGL - Lipid Droplet Degradation

### Mechanism

```
LIPID DROPLET DEGRADATION via ATGL:

LD (Triacylglycerol)
        ↓ ATGL (adipose triglyceride lipase)
        ↓
FFA (Free Fatty Acids) + Glycerol
        ↓
β-oxidation in mitochondria
        ↓
ATP production + ROS
        ↓
If excess FFA → Ferroptosis
```

### Why ATGL Activator (not inhibitor)

| | ATGL Inhibitor | ATGL Activator |
|--|----------------|----------------|
| **Effect** | Increases LDs | Degrades LDs |
| **Cancer use** | Would HELP tumors | Would HURT tumors |
| **Normal function** | Regulate fat storage | Regulate fat burning |
| **Recommendation** | ❌ Don't do this | ✅ DO THIS |

### Development Challenges

1. **No known small molecule activators** - Need screen
2. **Indirect activation possible** via:
   - GPR120 (omega-3 fatty acid receptor)
   - AMPK activation
   - PKA phosphorylation

---

## Part 4: Ferroptosis - Iron-Dependent Cell Death

### The Concept

```
FERROPTOSIS PATHWAY:

Polyunsaturated Fatty Acids (PUFAs)
        ↓ ACSL4 (acyl-CoA synthetase)
        ↓
PUFA-CoA
        ↓
Membrane phospholipids (PE)
        ↓ Lipid peroxidation (ROS + Fe2+)
        ↓
Peroxidized PE → Membrane damage → CELL DEATH

GPX4 (glutathione peroxidase 4)
        ↓ Normally neutralizes lipid peroxides
        ↓
GPX4 inhibition → Ferroptosis
```

### Why This Matters for Cancer

| Feature | Benefit |
|---------|--------|
| **Mechanism** | Distinct from apoptosis |
| **CSCs** | Especially sensitive to ferroptosis |
| **Resistance** | Cancer cells develop ferroptosis evasion |
| **Combination** | Synergy with immunotherapy |

### Target: GPX4

| Aspect | Details |
|--------|---------|
| **Function** | Reduces lipid peroxides |
| **Inhibition** | Directly induces ferroptosis |
| **Challenge** | Essential in normal cells |
| **Strategy** | Tumor-selective delivery |

### Target: ACSL4

| Aspect | Details |
|--------|---------|
| **Function** | Incorporates PUFAs into phospholipids |
| **Importance** | Required for ferroptosis, not for survival |
| **Advantage** | ACSL4 knockout = viable mice |
| **Potential** | Better therapeutic window than GPX4 |

---

## Part 5: Mitochondrial Translation (Beyond YARS2)

### The Problem with YARS2

| Issue | Implication |
|-------|-------------|
| **No inhibitors exist** | 5+ years basic research needed |
| **Housekeeping enzyme** | High toxicity risk |
| **Rare mutations** | Limited patient population |

### Alternative: MRPL45

| Feature | MRPL45 | YARS2 |
|---------|--------|-------|
| **Function** | Mitochondrial ribosome component | tRNA synthetase |
| **Cancer relevance** | Selective dependency in some cancers | Unclear |
| **Inhibitors** | None exist | None exist |
| **Potential** | Antibiotic-like approach | High risk |

### Alternative: SLC25A Mitochondrial Transporters

| Target | Function | Development |
|--------|----------|-------------|
| **ANT (adenine nucleotide translocator)** | ATP/ADP exchange | Preclinical |
| **UCP2** | Mitochondrial uncoupling | Preclinical |
| **Citrin (SLC25A13)** | Malate-aspartate shuttle | Basic research |

---

## Part 6: Cancer Stem Cell Metabolism

### Why CSCs are Different

| Feature | Bulk Tumor Cells | Cancer Stem Cells |
|---------|-----------------|------------------|
| **Lipid droplets** | Moderate | **HIGH** |
| **Glycolysis** | High | Moderate |
| **Oxidative phosphorylation** | Low | **HIGH** |
| **Stemness** | No | Yes |
| **Therapy resistance** | Moderate | **HIGH** |

### CSC Metabolic Vulnerabilities

| Target | Rationale | Development |
|--------|-----------|------------|
| **ALDH1A1** | Retinoic acid metabolism | Preclinical |
| **GLUT1** | Glucose uptake | Preclinical |
| **CD44** | Hyaluronic acid receptor | Preclinical |
| **NOTCH** | Stem cell pathway | Approved (other cancers) |

---

## Part 7: Recommended Pipeline

### Tier 1: Immediate (2-3 years)

#### CD36 Program

```
Objective: IND filing for anti-CD36 antibody in refractory cancer

Timeline:
├── Month 0-6: Lead identification/optimization
├── Month 6-12: In vivo efficacy (PDX models)
├── Month 12-18: Safety/toxicology
├── Month 18-24: IND filing
└── Month 24-36: Phase 1

Budget: $5-10M (CRO partnership)

Key metrics:
├── Tumor-initiating cell depletion
├── CD36 expression correlation
└── Pharmacokinetics
```

#### ATGL Activation (Indirect)

```
Objective: Screen for ATGL activators or develop GPR120 agonist

Approach 1: GPR120 agonist
├── GPR120 activation → ATGL phosphorylation → LD degradation
├── Known agonists: Omega-3 fatty acids, synthetic analogs
└── Repurpose for cancer indication

Approach 2: AMPK activator
├── AMPK phosphorylates and activates ATGL
├── Existing drugs: Metformin, AICAR
└── Potential combination with standard therapy

Timeline: 3-4 years to preclinical proof-of-concept
```

### Tier 2: Medium-term (3-4 years)

#### GPX4/ACSL4 Program

```
Objective: Develop ferroptosis inducer for refractory cancer

Strategy:
├── ACSL4 inhibitor (preferred over GPX4)
├── Tumor-selective delivery (nanoparticle)
└── Combination with checkpoint inhibitors

Milestones:
├── Month 0-12: Lead identification
├── Month 12-24: Mechanism validation
├── Month 24-36: Efficacy studies
└── Month 36-48: IND-enabling studies
```

### Tier 3: Long-term (5+ years)

#### Mitochondrial Translation Program

```
Objective: Validate MRPL45 as cancer target

Research focus:
├── Cancer-specific dependency screens
├── Identification of selective inhibitors
└── Biomarker development

Note: High risk, high reward
```

---

## Part 8: Competitive Landscape

### Current Players

| Company | Target | Stage | Approach |
|---------|--------|-------|----------|
| **Zodiac** | FASN | Phase 2 | Small molecule |
| **NGM Bio** | ACC | Phase 2 | Small molecule |
| **Various** | CD36 | Preclinical | Antibody |
| **学术** | GPX4 | Preclinical | Various |
| **学术** | ACSL4 | Preclinical | Various |

### Our Differentiation

| Factor | Competitors | Brown Biotech |
|--------|------------|--------------|
| **Mechanism** | FASN, ACC | CD36, ATGL, GPX4 |
| **CSC focus** | Limited | Primary |
| **Lipid droplets** | Indirect | Direct |
| **Ferroptosis** | None | Core program |

---

## Part 9: Biomarker Strategy

### Patient Selection

| Target | Biomarker | Method |
|--------|-----------|--------|
| **CD36** | CD36+ cells | IHC, flow cytometry |
| **ATGL** | LD abundance | Oil Red O, BODIPY |
| **GPX4** | GPX4 low, ACSL4 high | IHC, NGS |
| **General** | CSC markers | CD44+, ALDH1A1+ |

### Companion Diagnostic

```
CD36 IHC:
├── Score 0: Negative
├── Score 1+: Low
├── Score 2+: High
└── Clinical cutoff: ≥10% cells at 2+

Expected prevalence: ~30-40% of solid tumors
```

---

## Part 10: Combination Strategy

### Rational Combinations

| Combination | Rationale | Expected Synergy |
|------------|-----------|-----------------|
| **CD36 + PD-1** | CSCs are immunotherapy-resistant | ↑ T-cell infiltration |
| **ATGL + Chemo** | LD depletion sensitizes to chemo | ↓ Drug resistance |
| **GPX4 + Radiation** | Ferroptosis + ROS | ↑ Tumor cell death |
| **CD36 + FASN** | Dual lipid metabolism blockade | ↑ Metabolic stress |

### Clinical Trial Design

```
Phase 1/2 Trial Design:

Arm 1: CD36 antibody monotherapy
Arm 2: CD36 + Pembrolizumab
Arm 3: CD36 + Chemotherapy (gemcitabine)

Endpoints:
├── Primary: Safety, MTD
├── Secondary: ORR, PFS, biomarkers
└── Exploratory: CSC markers, LD quantification
```

---

## Conclusion: The Brown Biotech Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│              BROWN BIOTECH REFRACTORY CANCER PIPELINE               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  TIER 1 (Immediate)                                              │
│  ├── CD36 Antibody         ⭐⭐⭐⭐⭐  2-3 years                    │
│  └── ATGL Activation     ⭐⭐⭐⭐    3-4 years                    │
│                                                                  │
│  TIER 2 (Medium-term)                                          │
│  ├── ACSL4 Inhibitor     ⭐⭐⭐⭐    3-4 years                    │
│  └── GPX4 Inhibitor     ⭐⭐⭐      3-4 years                    │
│                                                                  │
│  TIER 3 (Long-term)                                            │
│  ├── MRPL45              ⭐⭐⭐      5+ years                      │
│  └── LIPIN1              ⭐⭐        5+ years                      │
│                                                                  │
│  CORE DIFFERENTIATION:                                           │
│  ├── Focus on LIPID DROPLETS (not just synthesis)               │
│  ├── Cancer Stem Cell metabolism (not bulk tumor)                │
│  ├── FERROPTOSIS induction (novel cell death)                   │
│  └── CD36 for tumor-initiating cells                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Appendix: Target Summary Table

| Target | Mechanism | Dev Stage | Safety Risk | Priority | Timeline |
|--------|-----------|-----------|-------------|----------|----------|
| **CD36** | FA transporter | Preclinical | Low | ⭐⭐⭐⭐⭐ | 2-3 yr |
| **ATGL** | LD degradation | Preclinical | Low | ⭐⭐⭐⭐ | 3-4 yr |
| **ACSL4** | Ferroptosis | Preclinical | Medium | ⭐⭐⭐⭐ | 3-4 yr |
| **GPX4** | Ferroptosis | Preclinical | High | ⭐⭐⭐ | 3-4 yr |
| **MRPL45** | Mt translation | Basic | Unknown | ⭐⭐⭐ | 5+ yr |
| **DGAT1** | LD synthesis | Phase 1 | HIGH ❌ | Deprioritize | - |
| **YARS2** | Mt translation | Basic | HIGH ❌ | Deprioritize | - |

---

## References

1. Wang et al. (2025). Lipid droplets in cancer stem cells. Nature Cancer
2. Kuemmerle et al. (2024). CD36 as tumor-initiating cell marker. Cancer Cell
3. Yang et al. (2025). ATGL activation and cancer therapy. Cell Metabolism
4. Liu et al. (2025). Ferroptosis in cancer stem cells. Nature Reviews Cancer
5. Doll et al. (2024). ACSL4 and ferroptosis sensitivity. Cell
6. Nathanson et al. (2023). CD36 metastasis. Science

---

*Report generated by ARP v24 Research Team · 2026-04-24*  
*For: Brown Biotech-style Refractory Cancer Pipeline*