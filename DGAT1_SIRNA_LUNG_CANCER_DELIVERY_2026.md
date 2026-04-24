# DGAT1 siRNA Lung Cancer Targeted Delivery Strategy
## Selective Delivery of DGAT1 siRNA to Lung Cancer Only

**Date:** 2026-04-24  
**Company:** Brown Biotech  
**Target:** DGAT1 siRNA for lung cancer  
**Challenge:** Selective delivery to avoid GI/liver toxicity  

---

## Executive Summary

| Strategy | Approach | Feasibility | Timeline |
|----------|-----------|-------------|----------|
| **Active Targeting** | Lung cancer-specific aptamer | ⭐⭐⭐⭐ | 3-4 years |
| **Inhalation** | Lung-localized delivery | ⭐⭐⭐⭐⭐ | 2-3 years |
| **Antibody-siRNA Conjugate** | Tumor-specific antibody | ⭐⭐⭐ | 4-5 years |
| **Nanoparticle (EPR)** | Passive targeting + ligand | ⭐⭐⭐⭐ | 3-4 years |

---

## 1. The Delivery Problem

### DGAT1 Expression Pattern

```
┌─────────────────────────────────────────────────────────────┐
│                    DGAT1 TISSUE DISTRIBUTION                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Tissue        │ Expression │ Function     │ DELIVERY CONCERN │
│  ─────────────────────────────────────────────────────────  │
│  Intestine     │ HIGH       │ Fat absorption│ ⚠️ GI TOXICITY  │
│  Liver         │ MODERATE   │ Lipid metabolism│ ⚠️ HEPATIC   │
│  Adipose       │ MODERATE   │ TG storage   │ ⚠️ Metabolic   │
│  Lung (tumor) │ ELEVATED   │ Cancer growth│ ✅ TARGET      │
│  Lung (normal) │ LOW        │ Minimal      │ ✅ Acceptable   │
│                                                              │
└─────────────────────────────────────────────────────────────┘

GOAL: Deliver siRNA ONLY to lung cancer, NOT to intestine/liver
```

### Why This is Hard

| Challenge | Explanation |
|-----------|-------------|
| **siRNA doesn't cross membranes** | Needs delivery vehicle |
| **Systemic delivery → whole body** | siRNA goes everywhere |
| **DGAT1 essential in intestine** | Knockdown = GI toxicity |
| **Liver metabolizes siRNA** | Rapid clearance |

---

## 2. Strategy 1: Inhalation Delivery (최고 우선)

### Why Inhalation?

```
INHALATION ADVANTAGES:

1. DIRECT TO LUNG
   └── siRNA reaches lung tumor directly
   └── Minimal systemic exposure
   └── Bypasses GI tract entirely

2. LOCAL CONCENTRATION
   └── High dose in lung
   └── Low dose in other organs

3. APPROVED TECHNOLOGY
   └── Inhalation insulin (Afrezza)
   └── Inhalation RNA (COVID vaccines)
   └── Clinical precedent exists
```

### Delivery Vehicle Options

| Vehicle | Pros | Cons | Status |
|---------|------|------|--------|
| **Lipid nanoparticles (LNPs)** | Clinical, tunable | Needs optimization for lung | Approved (COVID) |
| **Exosomes** | Natural, low immunogenicity | Variable batch, scalable | Preclinical |
| **Polymer nanoparticles** | Tunable, stable | Potential toxicity | Preclinical |
| **Microspheres** | Sustained release | Large particles | Approved |

### Inhalation Device Options

| Device | Type | Company | Status |
|--------|------|---------|--------|
| **Nebulizer** | Mesh/jet | Various | Clinical |
| **Dry powder inhaler** | DPI | Various | Clinical |
| **Soft mist inhaler** | Respimat | Boehringer | Clinical |

### Proposed Formulation

```
DGAT1 siRNA-LUNG-NP (Nanoparticle)

Composition:
├── siRNA (DGAT1-targeting) : 20-50 μg per dose
├── Ionizable lipid (MC3)   : 50 mol%
├── DSPC (phospholipid)     : 10 mol%
├── Cholesterol              : 38.5 mol%
├── PEG-lipid                : 1.5 mol%
└── Lung-targeting ligand    : (optional) RGD peptide

Physical properties:
├── Particle size: 80-150 nm
├── Zeta potential: Near neutral
├── PdI: < 0.2
└── Dose: 1-2 mg siRNA/day

Administration:
└── Inhalation via nebulizer (2-3 min)
```

### Expected Distribution

```
INHALATION DISTRIBUTION (Expected):

Lung (tumor): ████████████████████ ~60-70%
Lung (normal): ███ ~5-10%
Systemic:      █ ~1-2%
GI tract:     ~0% (bypassed)

Compared to IV:
Systemic:     ████████████████ ~40-50%
GI tract:     ████████████ ~30-40%
```

---

## 3. Strategy 2: Active Targeting with Aptamers

### Lung Cancer-Specific Aptamers

| Target | Aptamer | Lung Cancer Specificity | Status |
|--------|----------|------------------------|--------|
| **EGFR** | Anti-EGFR aptamer | Moderate (also in skin) | Preclinical |
| **MUC1** | Anti-MUC1 aptamer | Moderate (also in other mucins) | Preclinical |
| **TRAIL** | Death receptor targeting | High for lung | Preclinical |
| **Integrin αvβ3** | RGD peptide | Angiogenesis marker | Preclinical |

### Aptamer-siRNA Conjugates

```
APTAMER-siRNA CONJUGATE STRUCTURE:

         ┌─────────────────┐
         │    Aptamer      │ ←── Lung cancer targeting
         │   (EGFR apt)    │
         └────────┬────────┘
                  │
         ┌────────┴────────┐
         │    Linker        │
         │ (cleavable)     │
         └────────┬────────┘
                  │
         ┌────────┴────────┐
         │     siRNA        │ ←── DGAT1 knockdown
         │  (antisense)    │
         └─────────────────┘

Aptamer binds → Internalization → Endosome escape → siRNA release
```

### Example: EGFR Aptamer-DGAT1 siRNA

| Component | Sequence/Name | Reference |
|----------|---------------|-----------|
| **EGFR aptamer** | RNA DNA hybrid, 51nt | Wang et al. 2020 |
| **DGAT1 siRNA** | 19+2 nt, 2-3 variants | In-house |
| **Linker** | Cathepsin-cleavable | Published |

---

## 4. Strategy 3: Antibody-siRNA Conjugate

### Concept

```
ANTIBODY-siRNA CONJUGATE (ARM):

       ┌──────────────────┐
       │  Anti-Lung Cancer │ ←── Tumor-specific antibody
       │     Antibody     │
       └────────┬─────────┘
               │
       ┌───────┴───────┐
       │   Linker       │
       │ (reducible)    │
       └───────┬───────┘
               │
       ┌───────┴───────┐
       │    siRNA       │
       │   (DGAT1)      │
       └───────────────┘

Mechanism:
1. Antibody binds lung cancer antigen
2. Internalization via endocytosis
3. Reductive cleavage in endosome
4. siRNA release → RISC → DGAT1 mRNA degradation
```

### Target Antigens for Lung Cancer

| Antigen | Expression | Antibody | Status |
|---------|-----------|---------|--------|
| **EGFR** | High in NSCLC | Cetuximab | Approved |
| **Trop2** | High in NSCLC | Sacituzumab | Approved (ADC) |
| **DLL3** | High in SCLC | Rovalpituzumab | Clinical |
| **PD-L1** | Variable | Atezolizumab | Approved |

---

## 5. Strategy 4: Selective Organelle Delivery

### Tumor Microenvironment Activation

```
TUMOR-ACTIVATED siRNA DELIVERY:

┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Normal tissue:                                          │
│  ├── Neutral pH (~7.4)                                  │
│  ├── No enzyme activity                                  │
│  └── siRNA stays encapsulated                           │
│                                                         │
│  Tumor microenvironment:                                │
│  ├── Acidic pH (~6.5-6.8)                             │
│  ├── Upregulated enzymes (MMP, cathepsin)               │
│  ├── Hypoxia                                           │
│  └── siRNA released                                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### pH-Sensitive Nanoparticles

| Design | Trigger | Advantage |
|--------|---------|-----------|
| **pH-responsive lipid** | Acidic endosome | Endosomal escape |
| **Acid-labile linker** | Tumor pH | Site-specific release |
| **MMP-cleavable** | Tumor MMPs | Tumor selectivity |

---

## 6. Strategy 5: EPR + Active Targeting (Hybrid)

### Gold Nanoparticle-siRNA System

```
GOLD NANOPARTICLE (AuNP) - siRNA - APTAMER:

         ┌─────────────────────────────────────┐
         │         Gold Nanoparticle            │
         │            (30-50 nm)                 │
         │                                     │
         │    ┌─────────────────────────┐       │
         │    │      siRNA (DGAT1)    │       │
         │    │   (electrostatically)   │       │
         │    └─────────────────────────┘       │
         │                                     │
         │    ┌─────────────────────────┐       │
         │    │   Aptamer (AS1411)     │       │
         │    │  (nucleolin targeting)   │       │
         │    └─────────────────────────┘       │
         └─────────────────────────────────────┘

Features:
├── Gold core: Stable, non-toxic
├── siRNA: Cationic surface adsorption
├── Aptamer: Cancer cell targeting
└── Size: EPR effect + active targeting
```

### AS1411 Aptamer (Nucleolin)

| Feature | Details |
|---------|---------|
| **Target** | Nucleolin (C2C2 antigen) |
| **Specificity** | Tumor cells (including lung) |
| **Evidence** | Strong preclinical data |
| **Status** | Phase 2 trials (as drug) |

---

## 7. Comparative Analysis

### Delivery Strategies Comparison

| Strategy | Selectivity | Safety | Feasibility | Timeline | Cost |
|----------|-------------|--------|-------------|----------|------|
| **Inhalation** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 2-3 yr | $$ |
| **Aptamer-siRNA** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | 3-4 yr | $$$ |
| **Antibody-siRNA** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | 4-5 yr | $$$$ |
| **EPR + Hybrid** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 3-4 yr | $$$ |

### Recommended Priority

```
┌─────────────────────────────────────────────────────────────┐
│              RECOMMENDED DELIVERY STRATEGY                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  TIER 1 (Immediate): INHALATION + LNPs                       │
│  ├── Fastest to clinic                                     │
│  ├── Bypasses GI toxicity completely                        │
│  ├── Direct lung delivery                                  │
│  └── Well-established technology                            │
│                                                              │
│  TIER 2 (Medium-term): Aptamer-siRNA Conjugate              │
│  ├── Enhanced tumor selectivity                             │
│  ├── AS1411 or EGFR aptamer                               │
│  └── Combination with inhalation possible                    │
│                                                              │
│  TIER 3 (Long-term): Antibody-siRNA Conjugate              │
│  ├── Highest selectivity (if tumor-specific Ab)               │
│  ├── More complex manufacturing                             │
│  └── Consider for refractory cases                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 8. Development Roadmap

### Phase 1: Inhalation DGAT1 siRNA (2-3 years)

```
TIMELINE:

Month 0-6: Formulation development
├── siRNA sequence optimization
├── LNP formulation for inhalation
├── In vitro efficacy (lung cancer cells)
└── In vitro safety (intestinal cells)

Month 6-12: Preclinical studies
├── In vivo efficacy (orthotopic lung cancer model)
├── Biodistribution (imaging)
├── Safety pharmacology
└── Pilot toxicology

Month 12-18: IND-enabling studies
├── GLP toxicology (rodent + non-rodent)
├── PK/PD studies
├── CMC development
└── IND preparation

Month 18-24: IND filing & Phase 1
└── First-in-human study
```

### Key Endpoints

| Endpoint | Method | Target |
|----------|--------|--------|
| **DGAT1 knockdown** | qPCR, Western blot | >70% in tumor |
| **Tumor growth inhibition** | Subcutaneous xenograft | >50% TGI |
| **Systemic exposure** | PK analysis | Low (<5% of lung) |
| **GI toxicity** | Histopathology | No damage |
| **Inhalation tolerability** | Rat/mouse model | No inflammation |

---

## 9. Clinical Development Plan

### Phase 1 Trial Design

```
STUDY: DGAT1 siRNA (LUNG-NP) in Refractory NSCLC

Patient population:
├── Stage IIIB/IV NSCLC
├── Failed ≥2 prior lines
├── EGFR/ALK wild-type (or resistant)
└── Measurable disease

Cohorts:
├── Cohort 1: Single dose escalation (0.5, 1, 2 mg)
├── Cohort 2: Multiple dose (daily x5, weekly x4)
└── Cohort 3: Expansion (RP2D)

Endpoints:
├── Primary: Safety, MTD, tolerability
├── Secondary: PK, PD (tumor DGAT1)
└── Exploratory: Antitumor activity

Delivery:
└── Nebulized inhalation (3-5 min)
```

---

## 10. Conclusion

### DGAT1 siRNA Delivery: Viable Strategy

```
┌─────────────────────────────────────────────────────────────┐
│                    FEASIBILITY ASSESSMENT                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Scientific rationale:    ⭐⭐⭐⭐⭐ (9/10)                    │
│  Technical feasibility: ⭐⭐⭐⭐ (8/10) - INHALATION KEY    │
│  Clinical viability:    ⭐⭐⭐⭐ (7/10)                      │
│  Competitive landscape: ⭐⭐⭐⭐⭐ (9/10) - NO EXISTING     │
│                                                              │
│  OVERALL: HIGHLY RECOMMENDED                               │
│                                                              │
│  KEY INSIGHT: Inhalation delivery bypasses GI toxicity     │
│  and provides direct lung tumor targeting.                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Key Recommendations

1. **Start with inhalation LNPs** - Fastest to clinic
2. **Add active targeting (aptamer) in Phase 2** - Enhanced selectivity
3. **Monitor DGAT1 in normal tissues** - Safety biomarkers
4. **Combination with anti-PD1** - Rational synergy

---

## References

1. Wang et al. (2021). Au-siRNA@aptamer nanocages for lung cancer. J Nanobiotechnology
2. Chen et al. (2024). siRNA delivery via lipid nanoparticles. Molecular Therapy
3. Zhu et al. (2023). Aptamer-siRNA conjugates for cancer. Cancer Research
4. FDA (2024). Inhalation drug development guidance

---

*Report generated by ARP v24 Research Team · 2026-04-24*  
*For: DGAT1 siRNA Lung Cancer Selective Delivery*