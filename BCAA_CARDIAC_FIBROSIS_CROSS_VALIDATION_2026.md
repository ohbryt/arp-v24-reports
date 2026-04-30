# BCAA Metabolism Deep-Dive: Cardiac Fibrosis Cross-Validation
## ARP Research Coordination

**Date:** 2026-04-30  
**Status:** Research In Progress  
**Paper:** Yao et al. 2026 - Dietary intake and BCAA metabolism regulate pulmonary fibrosis through KDM4A-mediated epigenetic remodeling

---

## Research Status

### Tier System

| Tier | Type | File | Status |
|------|------|------|--------|
| 1 | PDF (Full-text) | papers/yao-2026-dietary-intake-and-bcaa-metabolism.pdf | ⚠️ NOT POSSESSED |
| 2 | Source (Abstract summary) | sources/yao-2026-dietary-intake-and-bcaa-metabolism.md | ✅ Complete |
| 3 | Wiki (ARQ 8 + Brown Biotech mapping) | Cardiology/yao-2026-dietary-intake-and-bcaa-metabolism.md | ✅ Complete |
| Index | Navigation | index.md - Cardiology section | ✅ Complete |
| Notion | Sync | Status: Inbox → Synced-to-Vault | ✅ Complete |

---

## Core Takeaway

### 3-Tier Node Validation

```
BCAA Metabolism Pathway (3 핵심 nodes):

┌─────────────────────────────────────────────────────────┐
│  BCAT2 (Branched-chain aminotransferase 2)             │
│  ├── Cytosolic BCAA catabolism                          │
│  └── Expressed in fibroblasts, kidney                   │
├─────────────────────────────────────────────────────────┤
│  SLC7A5 (LAT1 - Large neutral amino acid transporter) │
│  ├── Cell surface transporter for BCAAs                  │
│  ├── Expressed in proliferating cells, cancer           │
│  └── DRUG TARGET: JPH203/Nanvuranlat in cancer trials │
├─────────────────────────────────────────────────────────┤
│  KDM4A (Histone demethylase)                            │
│  ├── H3K9me3 demethylase                                │
│  ├── Epigenetic regulation of fibrosis genes            │
│  └── ALSO regulates SLC7A11 (our target!)              │
└─────────────────────────────────────────────────────────┘
```

### Cross-Organ Hypothesis: Lung ↔ Heart Fibrosis

```
Evidence for BCAA pathway cross-organ fibrosis:

LUNG FIBROSIS (This paper - Yao 2026):
BCAA intake → BCAT2/SLC7A5 → KDM4A → H3K9me3 demethylation → Pulmonary fibrosis

↓ parallel mechanism

HEART FIBROSIS (Our targets):
BCAA dysregulation → BCAT2/SLC7A5 → KDM4A → Cardiac fibrosis
                  → Or similar epigenetic pathway?

HYPOTHESIS:
├── KDM4A inhibitors may work for BOTH lung AND heart fibrosis
├── SLC7A5 blockade (JPH203) may have anti-fibrotic effects in both organs
└── BCAT2 inhibition → reduced BCAA flux → less KDM4A activation
```

---

## Immediate Reposition Candidates

### JPH203 / Nanvuranlat (SLC7A5 Inhibitor)

```
ORIGINAL INDICATION:
├── Cancer (Phase 1/2 clinical trials)
├── SLC7A5 (LAT1) positive cancers
└── Mechanism: Blocks leucine uptake → mTORC1 inhibition → anti-cancer

REPOSITION POTENTIAL:
├── IPF (Interstitial Pulmonary Fibrosis)
├── Cardiac fibrosis
└── Rationale: Reduce BCAA flux → reduce KDM4A activation → anti-fibrotic

ADVANTAGE:
├── Already in cancer clinical trials → safety profile known
├── Repurposing potential = faster translation
└── Could combine with our DGAT1/SLC7A11 strategy
```

### Alternative: JPH203 (Cancer) vs Nanvuranlat (Japan)

```
JPH203 (USA):
├── Sponsor: Various
├── Phase: Phase 1/2 in cancer
└── Patent: US patents

Nanvuranlat (Japan):
├── Sponsor: Kyorin Pharmaceutical (Japan)
├── Phase: Cancer trials in Japan
└── Status: Active development
```

---

## Recommended Follow-ups (ARQ Q5 Criteria)

### Priority 1: Immediate (1 week)

```
Cardiac fibrosis multi-omics validation:

TASK:
├── Extract BCAT2, SLC7A5, KDM4A expression from our 11 cardiac fibrosis files
├── Compare lung vs heart expression patterns
├── Cross-organ mechanism 1st-pass validation

FILES TO ANALYZE:
└── ~/openclaw/workspace/arp-v24/cardiac_fibrosis_*.json or equivalent

OUTPUT:
├── Expression heatmap (lung vs heart)
├── Correlation with fibrosis markers
└── Go/No-Go for Priority 2
```

### Priority 2: Near-term (1 month)

```
NSCLC tumor-stroma-fibroblast BCAA pathway + JPH203 + YARS2 combo:

TASK:
├── Build BCAA pathway in tumor-stroma-fibroblast co-culture model
├── Add JPH203 (SLC7A5 inhibitor) to existing YARS2 strategy
├── In silico combo validation

RATIONALE:
├── Fibroblasts supply BCAAs to cancer cells
├── SLC7A5 on cancer cells take up BCAAs
├── KDM4A activation in cancer cells drives ferroptosis resistance
├── Triple combo: JPH203 (BCAA) + PF-543106 (DGAT1) + YARS2 siRNA (mitochondrial)

OUTPUT:
├── Pathway diagram with drug targets
├── In silico efficacy prediction
└── Proposal for wet validation
```

### Priority 3: Long-term (3 months)

```
External collaboration proposal:

EXPERIMENT: Bleomycin-induced pulmonary fibrosis in mice
├── Group 1: Wild-type control
├── Group 2: BCAT2 knockout
├── Group 3: KDM4A knockout
├── Group 4: BCAT2 + KDM4A double knockout (rescue experiment)

READOUTS:
├── Lung fibrosis markers (hydroxyproline, α-SMA)
├── BCAA pathway metabolites
├── KDM4A activity (H3K9me3 levels)
├── Cross-organ: Cardiac fibrosis markers

RATIONALE FOR EPISTASIS:
├── If BCAT2 acts upstream of KDM4A:
│   └── Single KO should show phenotype; Double KO should NOT rescue
├── If BCAT2 and KDM4A are parallel:
│   └── Double KO should show ADDITIVE or SYNERGISTIC effect
```

---

## Limitations

### Current Status: Abstract-Only

```
LIMITATION:
├── Full Nature paper NOT in possession
├── Only abstract available
├── Cannot extract quantitative metrics

IF PDF OBTAINED:
├── Update sources/ with quantitative data
├── Enhance wiki with figures and tables
├── Update ARQ with specific numbers

POTENTIAL ACCESS ROUTES:
├── University library (Yonsei Severance SAB)
├── Author requests
├── ResearchGate
├── Contact corresponding author
```

---

## Integration with Our Research

### Existing Work to Connect

```
CONNECTIONS:

1. KDM4A-SLC7A11 (already in our pipeline):
   └── KDM4A also regulates SLC7A11 → links BCAA pathway to ferroptosis

2. DGAT1 + YARS2:
   └── YARS2 = mitochondrial translation
   └── JPH203 = BCAA transport
   └── Synergy: BCAA blockade + mitochondrial disruption

3. PF14-YARS2 siRNA:
   └── Add JPH203 for triple combo potential
```

### Multi-Target Strategy Map

```
                    BCAAs (dietary intake)
                           ↓
                    BCAT2 (cytosolic)
                           ↓
              ┌───────────┴───────────┐
              ↓                       ↓
        SLC7A5 (LAT1)           KDM4A (epigenetic)
              ↓                       ↓
     ┌───────┴───────┐         ┌─────┴─────┐
     ↓               ↓         ↓           ↓
  mTORC1         SLC7A11    Lung       Heart
  activation    (ferroptosis fibrosis  fibrosis
     ↓           resistance)
     ↓               ↓
  Cancer         Ferroptosis
  growth         + Cancer

OUR DRUG TARGETS:
├── JPH203/Nanvuranlat → SLC7A5 inhibitor (clinical)
├── KDM4A inhibitor → in development
├── PF-543106 → DGAT1 inhibitor (our current)
└── YARS2 siRNA → mitochondrial translation (our current)
```

---

## Action Items

```
IMMEDIATE:
□ Upload Yao 2026 PDF if available
□ Check our cardiac fibrosis multi-omics files for BCAT2/SLC7A5/KDM4A

1-WEEK:
□ Run expression analysis on 11 cardiac fibrosis files
□ Cross-organ validation

1-MONTH:
□ Build NSCLC tumor-stroma-fibroblast BCAA model
□ Add JPH203 to existing drug combo proposal

3-MONTH:
□ Draft external collaboration proposal
□ Bleomycin BCAT2/KDM4A double KO experiment design
```

---

*Document: arp-v24/BCAA_CARDIA C_FIBROSIS_CROSS_VALIDATION_2026.md*  
*Created: 2026-04-30*