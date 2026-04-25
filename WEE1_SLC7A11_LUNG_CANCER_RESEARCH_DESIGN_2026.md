# Research Design: WEE1 + SLC7A11 Inhibition for Lung Cancer
## Synthetic Lethal Ferroptosis Strategy

**Date:** 2026-04-25  
**Strategy:** WEE1 inhibitor (AZD1775) + SLC7A11 inhibition → Ferroptosis  
**Indication:** KRAS-mutant NSCLC, KEAP1/NRF2-mutant NSCLC  
**Rationale:** Manus AI report + literature confirmation (8 papers WEE1+lung, 4 papers WEE1+ferroptosis)

---

## Executive Summary

| Element | Design |
|---------|--------|
| **Hypothesis** | WEE1 inhibition + SLC7A11 inhibition = synthetic lethal ferroptosis in NSCLC |
| **Primary Target** | KRAS-mutant NSCLC, KEAP1/NRF2-mutant NSCLC |
| **Combination** | AZD1775 (WEE1i) + SLC7A11i (sulfasalazine or novel) |
| **Mechanism** | G2/M checkpoint abrogation + GSH depletion → lipid peroxidation → ferroptosis |
| **Expected Outcome** | Synergistic tumor inhibition, overcame PD-1 resistance |

---

## 1. Scientific Background

### 1.1 WEE1 in Cancer

```
WEE1 Role:
├── G2/M checkpoint regulation (DNA damage response)
├── p53-independent survival mechanism
├── KRAS-mutant NSCLC: WEE1 dependence ↑ (文献 8건)
└── AZD1775 (MK-1775): Phase 2 clinical WEE1 inhibitor
```

### 1.2 SLC7A11 in Ferroptosis

```
SLC7A11 (xCT):
├── System Xc- subunit: cystine/glutamate antiporter
├── Provides cystine for GSH synthesis
├── NSCLC: Nrf2 pathway → SLC7A11 overexpression
├── KEAP1/NRF2 mutation (~20% NSCLC) → targetable
└── Inhibition → GSH depletion → GPX4 inactivation → ferroptosis
```

### 1.3 Synthetic Lethal Mechanism

```
WEE1i + SLC7A11i → FERROPTOSIS

Step 1: WEE1 Inhibition (AZD1775)
├── G2 checkpoint abrogation
├── Premature mitotic entry
├── Replication stress accumulation

Step 2: SLC7A11 Inhibition
├── GSH synthesis blockade
├── GPX4 cofactor depletion
├── Lipid ROS accumulation

Step 3: Combined Effect
├── Checkpoint stress + oxidative stress
├── Iron-dependent lipid peroxidation
└── Ferroptosis (not apoptosis)

Result: Synthetic lethal - normal cells survive, cancer cells die
```

---

## 2. Research Questions

### Primary Question
**Does WEE1 inhibition (AZD1775) synergize with SLC7A11 inhibition to induce ferroptosis in KRAS-mutant and KEAP1/NRF2-mutant NSCLC?**

### Secondary Questions

| Q# | Question |
|----|----------|
| Q1 | What is the optimal combination ratio of AZD1775:SLC7A11i? |
| Q2 | Which mutation background (KRAS, KEAP1/NRF2, TP53) shows best synergy? |
| Q3 | Is ferroptosis the primary cell death mechanism or is there apoptosis? |
| Q4 | Does combination enhance immunogenic cell death (ICD)? |
| Q5 | Can this overcome PD-1 inhibitor resistance? |

---

## 3. Experimental Design

### Phase 1: In Vitro Validation (Months 1-6)

#### 3.1 Cell Line Panel

| Cell Line | KRAS | KEAP1/NRF2 | TP53 | Source |
|-----------|------|------------|------|--------|
| **A549** | KRAS G12S | WT | mut | ATCC |
| **H1299** | WT | WT | null | ATCC |
| **H358** | KRAS G12C | WT | mut | ATCC |
| **H441** | KRAS G12D | mut | mut | ATCC |
| **Calu-3** | WT | WT | mut | ATCC |
| **H2122** | KRAS G12C | mut | mut | ATCC |
| **H1979** | WT (EGFR L858R) | WT | mut | ATCC |
| **PC9** | WT | WT | WT | JCRB |

#### 3.2 Drug Preparation

| Drug | Source | Concentration Range |
|------|--------|-------------------|
| **AZD1775** | MedChem Express | 0.01 - 10 μM |
| **Sulfasalazine (SAS)** | Sigma-Aldrich | 0.1 - 10 mM |
| **Erastin** | MedChem Express | 0.01 - 10 μM |
| **Ferr-1** (ferroptosis inhibitor) | MedChem Express | 10 μM |
| **Z-VAD-FMK** (apoptosis inhibitor) | Selleckchem | 20 μM |

#### 3.3 Experimental Assays

**3.3.1 Viability Assay (Cell Titer Glow)**
```
- 96-well plate, 3,000 cells/well
- Drug treatment: 72h
- Combination matrix: 6x6 grid
- Calculate CI (Combination Index) by Chou-Talalay
```

**3.3.2 Ferroptosis Markers**

| Marker | Method | Time Points |
|--------|--------|-------------|
| **Lipid ROS** | C11-BODIPY 581/591 flow cytometry | 6h, 12h, 24h |
| **GSH** | GSH-Glo assay (Promega) | 6h, 12h, 24h |
| **GPX4 activity** | GPX4 assay kit (Abcam) | 24h |
| **Iron** | Iron Assay Kit (Abcam) | 24h |
| **4-HNE** | Western blot (MDA marker) | 24h |

**3.3.3 Cell Death Mechanism Confirmation**

```
Rescue Experiments:
├── +Ferr-1 (10 μM): Block ferroptosis
├── +Z-VAD-FMK (20 μM): Block apoptosis
├── +Necro-1 (10 μM): Block necroptosis
└── +DFO (100 μM): Iron chelation

Flow cytometry: PI/Annexin V
Confocal microscopy: C11-BODIPY + PI
```

**3.3.4 Molecular Markers (Western Blot/QPCR)**

| Target | Protein | mRNA |
|--------|---------|------|
| WEE1 pathway | p-WEE1, p-CDC2, Cyclin B1 | WEE1, CDC2 |
| SLC7A11 | SLC7A11, SLC3A2 | SLC7A11 |
| Ferroptosis | GPX4, SLC7A11, Nrf2 | GPX4, SLC7A11 |
| DNA damage | γH2AX, p-ATM, p-CHK1 | H2AX, ATM |
| Apoptosis | PARP cleavage, Caspase 3 | - |
| Loading control | β-actin, GAPDH | β-actin |

#### 3.4 Expected Results

```
Viability:
- CI < 0.7 = synergistic (at specific ratio)
- KRAS-mutant: Lower IC50 for both drugs
- KEAP1/NRF2-mutant: Higher SLC7A11 dependency

Ferroptosis confirmation:
- Lipid ROS ↑↑ with combination
- GSH ↓↓ with combination
- Ferr-1 rescue: viability restored >70%
- Z-VAD-FMK rescue: no protection
```

---

### Phase 2: Mechanistic Studies (Months 4-9)

#### 3.5 Metabolomics

```
Objective: Global metabolic changes upon combination treatment

Samples:
- Control (DMSO)
- AZD1775 alone
- SLC7A11i alone
- Combination

LC-MS/MS analysis:
├── GSH/GSSG ratio
├── Lipid species (PE, PC, PUFA)
├── TCA cycle intermediates
├── Amino acids
└── Nucleotides

Hypothesis:
- GSH depletion
- PE(20:4) accumulation (ferroptosis marker)
- TCA cycle disruption
```

#### 3.6 Proteomics (Phosphoarray)

```
Objective: Global phosphorylation changes

Phospho-Kinase Array (Human Phospho-Kinase Array, R&D Systems)
- 43 kinases simultaneously
- Compare single vs combination

Key expected changes:
- WEE1 pathway: inhibited
- DNA damage response: elevated
- mTOR pathway: suppressed
- AMPK: activated
```

#### 3.7 CRISPR Validation

```
Genome-wide CRISPR screen (Brunello library, 76,000 sgRNAs)

Screens:
1. AZD1775 resistance → identify sensitizers
2. SLC7A11i resistance → identify sensitizers
3. Combination → identify synergistic targets

Hit validation:
- Top 20 genes per screen
- Individual sgRNA validation
- Pathway enrichment (GO, KEGG)
```

#### 3.8 Immunogenic Cell Death (ICD) Assessment

```
If combination induces ICD → combination with PD-1

Markers:
- CALR exposure (flow cytometry)
- HMGB1 release (ELISA)
- ATP release (ENLITEN assay)
- DAMP secretion time course

Hypothesis:
- Combination → ICD → immune activation
- Then combine with anti-PD-1 for enhanced effect
```

---

### Phase 3: In Vivo Validation (Months 6-12)

#### 3.9 Xenograft Models

| Model | Background | Treatment Groups (n=8) |
|-------|-----------|------------------------|
| **A549** | KRAS G12S, TP53 mut | Vehicle, AZD1775, SLC7A11i, Combo |
| **H358** | KRAS G12C, TP53 mut | Vehicle, AZD1775, SLC7A11i, Combo |
| **H2122** | KRAS G12C, KEAP1 mut | Vehicle, AZD1775, SLC7A11i, Combo |

**Dosing:**
- AZD1775: 30 mg/kg PO QD (文献 based)
- Sulfasalazine: 200 mg/kg IP BID
- Combination: Same doses

**Endpoints:**
- Tumor volume (caliper) 3x/week
- Body weight 2x/week
- Survival
- Final tumor collection (IHC, metabolomics)

#### 3.10 PDX Models

| Patient | Mutation | Treatment Groups |
|---------|----------|-----------------|
| **PDX-1** | KRAS G12C, KEAP1 mut | Vehicle, AZD1775, SLC7A11i, Combo |
| **PDX-2** | KRAS G12D, TP53 mut | Vehicle, AZD1775, SLC7A11i, Combo |
| **PDX-3** | KEAP1 mut (KRAS WT) | Vehicle, AZD1775, SLC7A11i, Combo |

**Enrollment:** 3 patients per group (minimum)

#### 3.11 Immunocompetent Model (LLC1)

```
For combination with PD-1 study

C57BL/6 mice, LLC1 allograft

Groups:
1. Vehicle
2. AZD1775 (30 mg/kg)
3. SLC7A11i (equivalent dose)
4. Combo
5. Combo + Anti-PD-1 (200 μg, BIW)

Endpoints:
- Tumor growth
- Survival
- TIL analysis (flow cytometry)
- Cytokine panel (LEGENDplex)
```

---

### Phase 4: Combination with PD-1 (Months 10-15)

#### 3.12 Synergy with Immune Checkpoint Inhibition

```
Rationale: ICD induction → T cell activation → PD-1 response

In vitro:
- PBMC co-culture with tumor cells
- ELISPOT (IFN-γ)
- T cell proliferation (CFSE)
- Cytotoxicity assay (CD8+ T cell killing)

In vivo:
- LLC1 + anti-PD-1 combo study
- MC38 syngeneic model (if available)
```

**Expected Results:**
- Combo + PD-1 > Combo alone
- Increased CD8+/Treg ratio
- Elevated IFN-γ in tumor

---

## 4. Biomarker Strategy

### 4.1 Patient Selection Biomarkers

| Biomarker | Method | Population |
|-----------|--------|------------|
| **KEAP1/NRF2 mutation** | NGS (tissue/blood) | KEAP1 mut NSCLC |
| **SLC7A11 expression** | IHC (H-score) | High expression |
| **TP53 mutation** | NGS | All-comers |
| **KRAS mutation** | NGS | KRAS-mutant |
| **NRF2 target genes** | qPCR (NQO1, HMOX1) | Nrf2 activation |

### 4.2 Pharmacodynamic Markers

| Marker | Time | Sample |
|--------|------|--------|
| **p-WEE1 (S642)** | Day 1, 8 | Tumor biopsy |
| **γH2AX** | Day 1, 8 | Tumor biopsy |
| **GSH/GSSG ratio** | Day 1, 8, 15 | Plasma |
| **Lipid peroxides** | Day 1, 8, 15 | Plasma (MDA) |
| **4-HNE** | Day 1, 8 | Tumor biopsy |

---

## 5. Statistical Analysis

### 5.1 Sample Size Justification

```
In vitro:
- 3 biological replicates
- 2 technical replicates per experiment
- Power > 0.8 for 30% difference, α=0.05

In vivo:
- n=8 per group (80% power, 30% tumor growth inhibition)
- α=0.05, β=0.2
```

### 5.2 Primary Endpoints

| Endpoint | Analysis |
|----------|----------|
| **Cell viability** | IC50, CI (Chou-Talalay) |
| **Tumor growth** | Tumor volume, TGI%, mixed effects model |
| **Survival** | Kaplan-Meier, log-rank test |
| **Biomarkers** | Mixed ANOVA, time course analysis |

### 5.3 Statistical Software

- **R** (v4.2+): ANOVA, mixed effects, survival analysis
- **GraphPad Prism**: Figures, IC50
- **SPSS**: Clinical statistics

---

## 6. Timeline & Milestones

```
Month 1-3:   Study initiation, cell line procurement, drug preparation
Month 3-6:   In vitro viability + mechanism (Phase 1)
Month 4-9:   Metabolomics, proteomics, CRISPR (Phase 2)
Month 6-12:  In vivo efficacy (Phase 3)
Month 10-15: PD-1 combination studies (Phase 4)
Month 12:    Interim analysis, IND-enabling studies planning
Month 15:    Final report, publication, partner discussions
```

### Key Milestones

| Milestone | Target Date |
|-----------|-------------|
| **M1:** In vitro synergy confirmed | Month 6 |
| **M2:** Mechanism elucidated | Month 9 |
| **M3:** In vivo efficacy achieved | Month 12 |
| **M4:** PD-1 synergy demonstrated | Month 15 |
| **M5:** IND-enabling studies start | Month 18 |

---

## 7. Budget Estimate

| Category | Year 1 | Year 2 | Total |
|----------|--------|--------|-------|
| **Direct Costs** | | | |
| - In vitro assays | $80,000 | $30,000 | $110,000 |
| - Metabolomics/proteomics | $60,000 | $40,000 | $100,000 |
| - CRISPR screen | $50,000 | $20,000 | $70,000 |
| - In vivo studies | $120,000 | $150,000 | $270,000 |
| - PD-1 combination | $0 | $80,000 | $80,000 |
| **Subtotal** | $310,000 | $320,000 | $630,000 |
| **Indirect (15%)** | $46,500 | $48,000 | $94,500 |
| **Total** | $356,500 | $368,000 | $724,500 |

---

## 8. Risk Assessment & Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Synergy not reproduced** | Medium | High | Multiple cell lines, orthogonal assays |
| **Toxicity in vivo** | Medium | Medium | Start with low doses, monitor closely |
| **IC50 too high** | Low | High | SAR optimization, prodrug approach |
| **PD-1 combination fails** | Medium | Medium | Focus on biomarkers, alternative combinations |
| **Competitive entry** | High | Medium | Fast follow, novel indications |

---

## 9. Regulatory Considerations

### 9.1 Drug Status

| Drug | Status | Company |
|------|--------|---------|
| **AZD1775 (Adavosertib)** | Phase 2 (various cancers) | AstraZeneca |
| **Sulfasalazine** | Approved (IBD) | Generic |
| **SLC7A11i (novel)** | Pre-IND | Our IP |

### 9.2 IND-Enabling Studies

```
For novel SLC7A11i:
- Safety pharmacology (CV, CNS, respiratory)
- Genotoxicity (Ames, micronucleus)
- ADME (CYP inhibition/induction)
- PK/PD in rodents and NHPs
- GLP tox (14-day, 28-day)
```

---

## 10. Publication Plan

| Target | Journal | Timeline |
|--------|---------|----------|
| **Mechanism paper** | Cancer Research | Month 12 |
| **In vivo paper** | Clinical Cancer Research | Month 18 |
| **Combination with IO** | Nature Cancer / JITC | Month 24 |

---

## 11. Conclusion

This research design provides a comprehensive, milestone-driven approach to validate the **WEE1 + SLC7A11 synthetic lethal ferroptosis** strategy in lung cancer. 

**Key Strengths:**
- Strong scientific rationale (literature confirmed)
- Clear mechanistic hypothesis
- Synergy with PD-1 for combination potential
- Biomarker-driven patient selection

**Expected Outcome:**
- 2-3 years to first-in-human study
- Clear path to IND via 505(b)(1) or 505(b)(2)
- License-out potential to AZ/pfizer (WEE1) + immuno-oncology company

---

*Research Design by ARP v24*  
*Brown Biotech AI Drug Discovery Platform*  
*2026-04-25*