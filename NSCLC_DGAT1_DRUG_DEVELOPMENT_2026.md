# NSCLC Drug Development: DGAT1 Target
## Focused Drug Discovery Plan

**Date:** 2026-05-01  
**Target:** DGAT1 (Diacylglycerol O-acyltransferase 1)  
**Indication:** Non-Small Cell Lung Cancer (NSCLC)  
**Strategy:** PF14-siDGAT1 + Small Molecule Inhibitors

---

## Executive Summary

```
NSCLC에서 DGAT1는:
├── Lipid metabolism reprogramming의 핵심 효소
├── YAP/TEAD 경로와 연결
├── Aggressive tumor의 lipid droplet 축적 담당
└── 타겟 억제 = 종양 세포 사멸 (lipid toxicity)

개발 전략:
├── PF14-siDGAT1 (siRNA 전달) → 직접 KD
├── DGAT1 저분자 억제제 → 약물 개발
└── 조합 요법 (ferroptosis 유도)

현재 상태:
├── ChEMBL: 1 record (DGAT1)
├── Lead compounds: 8개 생성됨
├── XAI Score: 0.631 (moderate confidence)
└── Development stage: Preclinical
```

---

## 1. DGAT1 Biology in NSCLC

### 1.1 Role of DGAT1

```
DGAT1 Function:
├── Triglyceride (TAG) synthesis
├── Diacylglycerol (DAG) → TAG conversion
├── Lipid droplet formation/storage
└── Energy homeostasis

In Cancer (NSCLC):
├── ↑ DGAT1 expression in aggressive tumors
├── YAP/TEAD pathway activates DGAT1 transcription
├── Lipid droplet accumulation = Warburg effect extension
├── DGAT1 inhibition → lipid toxicity → apoptosis
└── Combination with ferroptosis = synthetic lethality
```

### 1.2 DGAT1-SLC7A11 Connection

```
DGAT1 + SLC7A11 Synthetic Lethality:

DGAT1 inhibition:
├── TAG synthesis ↓
├── DAG accumulation
├── ROS production ↑
└── Cell membrane damage

SLC7A11 inhibition (erastin):
├── Cystine uptake ↓
├── GSH synthesis ↓
├── Ferroptosis induction
└── Lipid ROS accumulation

COMBINATION EFFECT:
DGAT1i + SLC7A11i → Maximum lipid toxicity → Cancer cell death
```

### 1.3 YAP/TEAD-DGAT1 Axis

```
YAP/TEAD pathway:
├── Active in most aggressive NSCLC
├── TEAD transcription factors
└── Direct activation of DGAT1

THERAPEUTIC STRATEGY:
YAP/TEAD inhibitor (e.g., VT104)
     ↓
DGAT1 expression ↓
     ↓
TAG synthesis ↓
     ↓
Lipid droplet depletion → Apoptosis

COMBINATION:
YAP/TEADi + DGAT1i = Enhanced tumor suppression
```

---

## 2. Drug Development Strategies

### 2.1 Strategy 1: siRNA (PF14-siDGAT1)

```
Delivery: PF14 peptide (lungs-specific)
Target: DGAT1 mRNA
Mechanism: Knockdown of DGAT1 expression

ADVANTAGES:
├── High specificity (only DGAT1)
├── Rapid effect
├── Reversible
└── PF14 = lung-targeted delivery

LIMITATIONS:
├── Short duration (days)
├── Requires repeated dosing
├── Delivery optimization needed
└── N/P ratio: 1-4 (external review corrected)

PROTOCOL:
├── PF14 + siDGAT1 complexes
├── N/P ratio: 2:1
├── Intratracheal administration
├── In vitro: A549 cells
└── Readout: qPCR, Western blot, viability
```

### 2.2 Strategy 2: Small Molecule Inhibitors

```
Known DGAT1 Inhibitors:

| Compound | IC50 | Selectivity | Stage |
|----------|------|-------------|--------|
| **T863** | ~10μM | DGAT1 selective | Natural product |
| **A922500** | ~13nM | DGAT1 selective | Preclinical |
| **PF-06450309** | ~8nM | DGAT1 selective | Preclinical |
| **DGAT1i 34-11** | ~100nM | DGAT1 > DGAT2 | Preclinical |

Our Generated Leads (from MRL):
| SMILES | Reward | Synthesizability |
|--------|--------|-------------------|
| `CC(C)c1ccc(cc1)C(=O)O` | 0.797 | 0.75 |
| `c1ccc(cc1)C(=O)Nc2ccccc2O` | 0.788 | 0.75 |
| `CC(=O)Oc1ccccc1C(=O)NCCN` | 0.784 | 0.75 |

NEXT STEPS:
1. Purchase/commercial DGAT1 inhibitors (A922500)
2. Test in NSCLC cell lines (A549, H1299, PC9)
3. Optimize our generated leads
4. PROTAC design for DGAT1 degradation
```

### 2.3 Strategy 3: PROTAC Design

```
PROTAC for DGAT1:

PROTAC = DGAT1 ligand + E3 ligase ligand + Linker

DGAT1 LIGANDS:
├── A922500 derivative
├── T863 derivative
└── Our MRL leads

E3 LIGASE LIGANDS:
├── Pomalidomide (CRBN)
├── VHL ligand
└── MDM2 ligand

LINKER:
├── PEG linker (3-6 units)
├── Alkyl chain
└── Click chemistry compatible

DESIGN CONSIDERATIONS:
├── DGAT1 degradation > inhibition (complete knockout)
├── Reversible (washout恢复)
└── Catalytic mechanism (substoichiometric)

PROTAC ADVANTAGES:
├── Event-driven pharmacology
├── Lower dose possible
├── Overcome resistance
└── Targeted protein degradation
```

---

## 3. Target Validation Data

### 3.1 Literature Support

```
KEY PAPERS:
1. "Lipid metabolism gene-wide profile and survival signature of lung adenocarcinoma"
   → DGAT1 associated with survival
   
2. "Tumor cell-specific loss of GPX4 reprograms triacylglycerol metabolism"
   → TAG metabolism reprogramming in cancer
   
3. "YAP/TEAD-activated TAG synthesis and peroxidation in lipid droplets"
   → YAP/TEAD-DGAT1 axis discovery

DATABASE EVIDENCE:
├── TCGA: DGAT1 high in aggressive NSCLC
├── CCLE: DGAT1 essential in some lung cancer lines
└── CRISPR: DGAT1 dependency in lipid-addicted tumors
```

### 3.2 ChEMBL Bioactivity

```
Target: CHEMBL2176848 (DGAT1)
Records: 1

Known Inhibitors:
├── A922500: IC50 = 13nM (DGAT1)
├── PF-06424439: IC50 = 8nM (DGAT1, not DGAT2)
└── T863: IC50 = ~10μM (natural product)
```

---

## 4. Experimental Plan

### 4.1 In Vitro Validation

```
PHASE 1: Target Validation (Week 1-4)

Cell Lines:
├── A549 (KRAS mutant)
├── H1299 (p53 null)
├── PC9 (EGFR mutant)
└── H460 (KRAS mutant)

EXPERIMENTS:

1. DGAT1 expression:
   □ qPCR: DGAT1 mRNA levels
   □ Western blot: DGAT1 protein
   □ Lipid droplet stain (BODIPY)

2. DGAT1 knockdown (siRNA):
   □ Lipid droplet quantification
   □ Cell viability (CCK-8)
   □ Apoptosis assay (caspase 3/7)
   □ ROS measurement

3. DGAT1 inhibitors:
   □ A922500 dose-response (0.1-100μM)
   □ T863 dose-response
   □ Combination with erastin (SLC7A11i)

4. Combination effect:
   □ DGAT1i + SLC7A11i (erastin)
   □ DGAT1i + YAP/TEADi (VT104)
   □ DGAT1i + standard of care (cisplatin)
```

### 4.2 In Vivo Validation

```
PHASE 2: In Vivo Efficacy (Week 5-12)

Mouse Model:
├── A549 xenograft (nude mice)
├── Patient-derived xenograft (PDX) if available
└── KRAS-driven autochthonous model (LSL-Kras;Trp53fl/fl)

TREATMENT GROUPS:
├── Control (vehicle)
├── PF14-siDGAT1 (intratracheal, 3x/week)
├── A922500 (oral, daily)
├── Combination (PF14-siDGAT1 + A922500)
└── Positive control (cisplatin)

READOUTS:
├── Tumor volume (biweekly)
├── Body weight
├── Survival
├── Histology (H&E, Ki67, TUNEL)
├── Lipid droplet quantification
└── Biomarkers (DGAT1, SLC7A11, GSH, ROS)
```

### 4.3 Biomarkers

```
PATIENT SELECTION BIOMARKERS:
├── High DGAT1 expression (IHC)
├── High lipid droplet content (Oil Red O)
├── YAP nuclear localization
├── Low SLC7A11 (ferroptosis sensitive)
└── KRAS mutant status

RESPONSE BIOMARKERS:
├── Plasma TAG levels
├── Lipid droplet count
├── ROS markers (C11-BODIPY)
├── GSH/GSSG ratio
└── Ferrotosis markers (GPX4, PTGS2)
```

---

## 5. Drug Discovery Pipeline

### 5.1 Virtual Screening

```
STEP 1: Fragment-based Design
├── Use T863 as fragment
├── Grow into DGAT1 active site
└── Focus: Carboxylic acid interactions

STEP 2: Our MRL Leads Optimization
├── Lead 1: `CC(C)c1ccc(cc1)C(=O)O` (MW ~164)
│   └── Add lipophilic groups, increase MW to 300-500
├── Lead 2: `c1ccc(cc1)C(=O)Nc2ccccc2O`
│   └── Optimize H-bond donors/acceptors
└── Lead 3: `CC(=O)Oc1ccccc1C(=O)NCCN`
    └── Improve cell permeability

STEP 3: PROTAC Design
├── Linker length optimization
├── E3 ligase selection (CRBN vs VHL)
└── Cell permeability assessment
```

### 5.2 ADMET Optimization

```
ORAL DELIVERY (for systemic DGAT1i):
├── Caco-2 permeability: >10-6 cm/s
├── Microsomal stability: CLint <15 μL/min/mg
├── CYP inhibition: IC50 >10μM (major CYPs)
└── Solubility: FaSSIF >100μM

INHALATION DELIVERY (PF14-siDGAT1):
├── Particle size: 1-5 μm (alveolar deposition)
├── Aerodynamic stability
├── Lung tissue penetration
└── Mucociliary clearance avoidance
```

---

## 6. Combination Strategies

### 6.1 Rational Combinations

```
COMBINATION 1: DGAT1i + SLC7A11i
├── Mechanism: Synthetic lethality
├── Evidence: Strong preclinical
└── Priority: HIGH

COMBINATION 2: DGAT1i + YAP/TEADi
├── Mechanism: Enhanced lipid metabolism disruption
├── Evidence: YAP/TEAD activates DGAT1
└── Priority: HIGH

COMBINATION 3: DGAT1i + Cisplatin
├── Mechanism: DNA damage + metabolic stress
├── Evidence: Moderate
└── Priority: MEDIUM

COMBINATION 4: DGAT1i + Anti-PD1
├── Mechanism: Immunogenic cell death
├── Evidence: Emerging
└── Priority: MEDIUM

COMBINATION 5: DGAT1i + mTORi
├── Mechanism: Dual metabolic inhibition
├── Evidence: Moderate
└── Priority: LOW-MEDIUM
```

### 6.2 Triple Combination

```
DGAT1i + SLC7A11i + Immune Checkpoint

RATIONALE:
├── Metabolic stress → immunogenic cell death
├── Ferroptosis → DAMPs release
├── Antigen presentation ↑ → T cell activation
└── Anti-PD1 → T cell response enhancement

PRECLINICAL PLAN:
1. DGAT1i + SLC7A11i → Tumor metabolic disruption
2. Immunogenic cell death → DAMPs release
3. Anti-PD1 → Enhance T cell infiltration
4. Complete tumor eradication?

POTENTIAL FOR CURE:
├── Immunogenic cell death mechanism
├── Memory T cell formation
└── Long-term protection
```

---

## 7. Development Timeline

```
WEEK 1-4: In Vitro Validation
├── Cell lines obtained
├── DGAT1 expression confirmed
├── siRNA knockdown validated
└── Lead compound procured

WEEK 5-8: In Vitro Combination
├── DGAT1i + SLC7A11i synergy confirmed
├── DGAT1i + YAP/TEADi tested
├── Dose-response curves established
└── Biomarkers identified

WEEK 9-12: In Vivo Proof of Concept
├── Xenograft study initiated
├── PF14-siDGAT1 efficacy tested
├── A922500 efficacy tested
└── Combination benefit demonstrated

MONTH 4-6: Lead Optimization
├── PROTAC design initiated
├── ADMET optimization
└── IND-enabling studies

MONTH 7-12: Preclinical Development
├── GLP toxicology
├── PK/PD studies
├── Formulation development
└── IND preparation
```

---

## 8. Success Criteria

```
IN VITRO:
□ DGAT1 knockdown >70% (siRNA)
□ IC50 <10μM for lead compounds
□ Combination index <1 (synergy)
□ Ferroptosis markers elevated

IN VIVO:
□ Tumor growth inhibition >50% (single agent)
□ Tumor growth inhibition >80% (combination)
□ No significant body weight loss
□ Biomarkers validate mechanism

REGULATORY:
□ Sufficient preclinical data package
□ IND filing within 12 months
□ Clinical trial design finalized
```

---

## 9. Risks & Mitigations

```
RISK 1: DGAT1 inhibition toxicity (systemic)
MITIGATION:
├── Inhalation delivery (local)
├── Tissue-selective PROTAC
└──间歇性 dosing

RISK 2: Limited efficacy (single agent)
MITIGATION:
├── Combination therapy design
├── Patient selection biomarkers
└── Synthetic lethality approach

RISK 3: Resistance development
MITIGATION:
├── Multiple mechanisms (siRNA + small molecule)
├── Combination therapy
└── PROTAC for complete degradation

RISK 4: Off-target effects
MITIGATION:
├── DGAT1 selectivity screening
├── Metabolite profiling
└── Tissue-specific delivery
```

---

## 10. Resources Required

### Equipment
```
Cell culture: CO2 incubator, biosafety cabinet
Molecular biology: qPCR, Western blot
Imaging: Confocal microscopy (lipid droplets)
Animal: IVIS or similar for imaging
```

### Reagents
```
Cell lines: A549, H1299, PC9, H460
Compounds: A922500, T863, erastin, VT104
Antibodies: Anti-DGAT1, anti-GAPDH
Assay kits: CCK-8, Caspase-Glo, ROS detection
```

### Budget Estimate
```
Year 1: $150,000-200,000
├── Personnel (1 FTE): $80,000
├── Reagents: $30,000
├── Animal studies: $25,000
├── Outsourcing: $20,000
└── Contingency: $15,000
```

---

## 11. Next Steps

```
IMMEDIATE (This Week):
□ Order A922500 from supplier
□ Obtain NSCLC cell lines
□ Design PF14-siDGAT1 complexes
□ Literature deep-dive on DGAT1 in NSCLC

SHORT-TERM (Month 1):
□ Confirm DGAT1 expression in our cell lines
□ Test PF14-siDGAT1 in vitro
□ Test A922500 dose-response
□ Establish biomarkers

MEDIUM-TERM (Month 2-3):
□ Demonstrate synergy with SLC7A11i
□ In vivo xenograft study
□ Begin PROTAC design
□ Write publication/patent

LONG-TERM (Month 4-12):
□ IND-enabling studies
□ GLP toxicology
□ Clinical trial design
□ Partnering discussions
```

---

## References

```
1. Lung Cancer DGAT1 Pipeline Report (ARP v24, 2026-04-25)
2. DGAT1 SLC7A11 Synthetic Lethality Report
3. PF14-siDGAT1 Complete Protocol
4. YAP/TEAD-DGAT1 axis papers
5. ChEMBL: CHEMBL2176848
```

---

*Report: arp-v24/NSCLC_DGAT1_DRUG_DEVELOPMENT_2026.md*  
*Created: 2026-05-01*  
*Status: Ready for execution*