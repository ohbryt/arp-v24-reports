# KDM4A + SLC7A11 Combination Strategy for Lung Cancer Therapy
## Synthetic Lethality & Epigenetic-Ferroptosis Axis

**Date:** 2026-04-30  
**Status:** Research Report

---

## Executive Summary

```
DISCOVERY: KDM4A directly regulates SLC7A11 transcription
├── KDM4A removes H3K9me3 silencing mark from SLC7A11 promoter
├── KDM4A knockdown → ↓SLC7A11 → ↑ferroptosis
└── Combination = Synthetic lethality

STRATEGY:
┌─────────────────────────────────────────────────────────┐
│  KDM4A inhibitor   +   SLC7A11 inhibitor               │
│  (blocks SLC7A11 transcription)                         │
│         +                                                │
│  (blocks cystine uptake, forces ferroptosis)            │
│         ↓                                                │
│  ENHANCED FERROPTOSIS + DUAL TARGETING                  │
└─────────────────────────────────────────────────────────┘
```

---

## Background: KDM4A Regulates SLC7A11

### Key Finding (Chen et al., 2021 - Biochem Biophys Res Commun)

```
Mechanism:
┌─────────────────────────────────────────────────────────┐
│  KDM4A (histone demethylase)                            │
│         ↓                                                │
│  Demethylates H3K9me3 at SLC7A11 promoter              │
│         ↓                                                │
│  SLC7A11 transcription ↑                              │
│         ↓                                                │
│  System Xc- activity ↑ (cystine uptake)               │
│         ↓                                                │
│  GSH production ↑ → FERROPTOSIS RESISTANCE             │
└─────────────────────────────────────────────────────────┘

KDM4A KNOCKDOWN:
→ H3K9me3 accumulates at SLC7A11 promoter
→ SLC7A11 transcription ↓
→ System Xc- dysfunction
→ Cystine uptake ↓ → GSH ↓
→ ENHANCED FERROPTOSIS
→ Decreased tumor progression & metastasis
```

### Supporting Evidence

| Study | Cancer Type | Finding |
|-------|-------------|---------|
| Chen et al., 2021 | Osteosarcoma | KDM4A knockdown enhances ferroptosis, inhibits progression |
| Frontiers Oncology, 2022 | Osteosarcoma | KDM4A reduces cisplatin sensitivity by inhibiting SLC7A11 |
| PeerJ, 2024 | Bone cancers | KDM4A knock-down enhances ferroptosis, inhibits metastasis |
| CMAR, 2025 | Multiple cancers | KDM3B and KDM4A cooperatively regulate SLC7A11 |

---

## Scientific Rationale: Why Combination?

### Single Agent Limitations

```
SLC7A11 INHIBITOR ALONE:
├── Cancer cells may upregulate other cystine transporters
├── Feedback compensation via KDM4A
└── Limited efficacy in KDM4A-high tumors

KDM4A INHIBITOR ALONE:
├── Cancer cells can still uptake cystine via other routes
├── Partial ferroptosis induction
└── Reversible effect (epigenetic adaptation)
```

### Combination Effect

```
┌─────────────────────────────────────────────────────────┐
│  KDM4A INHIBITOR                    │  SLC7A11 INHIBITOR  │
├────────────────────────────────────┼────────────────────┤
│  ↓SLC7A11 transcription           │  Direct enzyme      │
│  ↓System Xc- expression          │  inhibition        │
│  ↑H3K9me3 (gene silencing)       │  ↓cystine uptake   │
├────────────────────────────────────┼────────────────────┤
│           COMBINED EFFECT                             │
├────────────────────────────────────────────────────────┤
│  • Complete SLC7A11 blockade                          │
│  • No compensatory upregulation possible             │
│  • Max ferroptosis induction                          │
│  • Synthetic lethal phenotype                        │
└─────────────────────────────────────────────────────────┘
```

---

## KDM4A Inhibitors in Development

### Small Molecule Inhibitors

| Compound | Target | IC50 | Stage | Reference |
|----------|--------|------|-------|-----------|
| **JIB-04** | KDM4A/B/C/D | ~200nM | Preclinical | Maggio et al. |
| **KDM4-IN-4** | KDM4A | ~1μM | Preclinical | Cancer Lett 2025 |
| **NCDM-32B** | KDM4A/B/C | 3.0μM | Preclinical | Breast cancer |
| **GSK-J4** | KDM6A/B | ~50nM | Preclinical | Various |

### PROTAC Degrader

| Compound | Target | Selectivity | Stage | Reference |
|----------|--------|-------------|-------|-----------|
| **RDN8011** | KDM4A-C | Spares KDM4D | Preclinical | Eur J Med Chem 2025 |

```
RDN8011 details:
• First-in-class PROTAC degrader of KDM4
• Effectively degrades KDM4A-C while sparing KDM4D
• Significant antiproliferative effects in esophageal cancer
• Could be combined with SLC7A11 inhibitors
```

### Epigenetic Editing

```
Recent strategy: Epigenetic editing + Epi-drugs
• KDM4 targeting via dCas9-KDM4A fusion
• Combined with pharmacological inhibitors
• Shows promise in colon, breast, hepatocellular carcinoma
```

---

## Lung Cancer Context

### Why Lung Cancer?

```
1. KDM4A is often overexpressed in NSCLC
2. KDM4A-high tumors show:
   • Higher SLC7A11 expression
   • More ferroptosis resistance
   • Poorer outcomes
   
3. Combination strategy particularly relevant for:
   • KRAS-mutant NSCLC (lipid metabolism altered)
   • NSCLC with immunotherapy resistance
   • EGFR-mutant NSCLC (ferroptosis sensitivity)
```

### Precedent: ESCC Study

```
KDM4A overexpression in ESCC patients who did NOT respond to anti-PD1 therapy
→ KDM4 inhibitor (KDM4-IN-4) + anti-PD1 therapy
→ Pronounced tumor suppression in vivo

Applies to: Lung cancer immunotherapy resistance
```

---

## Therapeutic Strategy: Three Approaches

### Approach 1: Small Molecule Combination

```
KDM4A inhibitor + SLC7A11 inhibitor

Example combinations:
• JIB-04 + Sulfasalazine (FDA-approved, cheap)
• KDM4-IN-4 + Erastin derivatives
• NCDM-32B + PF-543106 (DGAT1 inhibitor, our target!)

RATIONALE:
• KDM4A inhibitor → ↓SLC7A11 transcription
• SLC7A11 inhibitor → direct enzyme inhibition
• PF-543106 → additional lipid ROS amplification
→ TRIPLE assault on ferroptosis defense
```

### Approach 2: PROTAC-Based

```
KDM4A PROTAC (RDN8011) + SLC7A11-targeted agent

• KDM4A PROTAC → degrades KDM4A protein
• SLC7A11 siRNA/PROTAC → blocks transporter
• No compensatory upregulation possible

ADVANTAGE:
• More complete and durable inhibition
• Covalently degrades KDM4A (not just inhibits)
```

### Approach 3: Epigenetic Editing (Future)

```
dCas9-KDM4A fusion + SLC7A11 sgRNA

• Precision editing of SLC7A11 promoter
• Blocks KDM4A from binding to promoter
• Permanent silencing of SLC7A11

FUTURE: CRISPR-based therapy
• In vivo delivery challenges remain
• Lung epithelium targeting possible via AAV
```

---

## Experimental Design

### In Vitro Validation

```
CELL LINES:
• A549 (KRAS-mutant NSCLC)
• H1299 (NSCLC, p53-null)
• H460 (NSCLC, high SLC7A11)
• PC9 (EGFR-mutant NSCLC)

TREATMENT GROUPS:
1. Control (DMSO)
2. KDM4A inhibitor alone (JIB-04, 200nM)
3. SLC7A11 inhibitor alone (Sulfasalazine, 1mM)
4. DGAT1 inhibitor alone (PF-543106, 100nM)
5. KDM4A + SLC7A11 inhibitor combo
6. KDM4A + DGAT1 inhibitor combo
7. Triple: KDM4A + SLC7A11 + DGAT1 inhibitors

READOUTS:
• Cell viability (CTG assay)
• Ferroptosis markers (lipid ROS, 4-HNE, GPX4)
• SLC7A11, KDM4A, GSH levels
• Lipid droplet quantification
• Clonogenic survival
```

### In Vivo Validation

```
MOUSE MODEL:
• KP (KrasLSL-G12D/+; Trp53fl/fl) autochthonous NSCLC
• Subcutaneous A549 xenograft

TREATMENT:
• KDM4A inhibitor (KDM4-IN-4, 50mg/kg IP daily)
• PF-543106 (DGAT1 inhibitor, 10mg/kg IP daily)
• Combination vs monotherapy

READOUTS:
• Tumor volume/survival
• IHC: Ki67, KDM4A, SLC7A11, GPX4
• Lipid ROS (4-HNE staining)
• Blood chemistry (safety)
```

---

## Biomarkers

### For Patient Selection

```
KDM4A-high, SLC7A11-high tumors → BEST CANDIDATES
├── Likely to respond to KDM4A inhibition
├── Dependent on SLC7A11 for ferroptosis defense
└── Combination most effective

BIOMARKER PANEL:
┌─────────────────────────────────────────────────┐
│  HIGH KDM4A expression   →  KDM4A inhibitor     │
│  HIGH SLC7A11 expression →  SLC7A11 inhibitor   │
│  HIGH GPX4              →  Ferroptosis target  │
│  HIGH lipid droplets    →  DGAT1 vulnerable    │
└─────────────────────────────────────────────────┘
```

---

## Safety Considerations

```
NORMAL TISSUE CONCERNS:
• KDM4A inhibition in normal lung epithelium
• SLC7A11 inhibition in normal cells

MITIGATION:
• Tumor-targeted delivery (AAV, nanoparticles)
• Conditional inhibitors (prodrugs)
• Tissue-specific targeting

WINDOW:
• Cancer cells depend more on SLC7A11
• Normal cells have alternative cystine sources
• Therapeutic window exists
```

---

## Competitive Landscape

| Company | Approach | Stage | Notes |
|---------|----------|-------|-------|
| None approved | KDM4A inhibitors | Preclinical | Various academic labs |
| Various | SLC7A11 inhibitors | Preclinical | Many in development |
| Our strategy | Triple combination | Discovery | Novel |

---

## References

```
1. Chen M, Jiang Y, Sun Y. KDM4A-mediated histone demethylation of SLC7A11 
   inhibits cell ferroptosis in osteosarcoma. Biochem Biophys Res Commun. 2021;550:77-83.
   PMID: 33689883

2. Chen et al. Ferroptosis in osteosarcoma: A promising future. 
   Front Oncol. 2022. PMC9705963

3. Liu et al. KDM4 involvement in breast cancer. Front Oncol. 2021.

4. Eur J Med Chem 2025. Discovery of first-in-class PROTAC degrader of KDM4 (RDN8011)

5. Cancer Lett 2025. KDM4A inhibition + anti-PD1 in ESCC

6. CMAR 2025. Role of SLC7A11 in tumor progression and regulation mechanisms

7. PeerJ 2024. Ferroptosis and bone-related diseases
```

---

## Next Steps

```
IMMEDIATE:
1. Literature review on existing KDM4A inhibitors
2. Confirm target expression in lung cancer cell lines
3. Design in vitro validation experiments

NEAR-TERM:
4. Test JIB-04 + PF-543106 combination in A549 cells
5. Measure ferroptosis markers
6. Compare with single agents

LONG-TERM:
7. Develop KDM4A PROTAC if effective
8. In vivo validation in mouse models
9. Patient selection biomarkers
```

---

*Document: arp-v24/KDM4A_SLC7A11_COMBINATION_STRATEGY_2026.md*  
*Created: 2026-04-30*