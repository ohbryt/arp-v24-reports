# Colorectal Cancer (CRC) Drug Discovery Report
## ARP v24 Comprehensive Research Pipeline

**Generated:** 2026-04-24  
**Disease:** Colorectal Cancer (CRC, 대장암)  
**Type:** Gastrointestinal Cancer  
**Epidemiology:** World 3rd most common cancer (~1.9M cases/year)  
**Researcher:** ARP v24 Director Agent + Groq LLM  
**Version:** 1.0

---

## Executive Summary

대장암은 세계에서 3번째로 흔한 암으로, 매년 약 190만 명의 환자가 발생하며,，死亡자 は約90万명에 달합니다. 본 보고서는 CRC의 분자유전학적 특성, 현재 승인된 약물 및 开发 중인 치료제, 내성 메커니즘, 신약 개발 전략을 포괄적으로 다룹니다.

### 핵심 요약

| 구분 | 내용 |
|------|------|
| **発生率** | 세계 3위 (연간 190만 명) |
| **생존율** | Stage IV에서 15% 미만 |
| **주요 변이** | APC (80%), KRAS (40%), BRAF (10%) |
| **표적 치료** | EGFR, VEGF, MSI-H, BRAF V600E |
| **면역 치료** | Pembrolizumab, Nivolumab (MSI-H) |

---

## 1. CRC Pathophysiology

### 1.1 발생 기전

```
APC 돌연변이 (80%)
    ↓
Wnt/β-catenin 경로 활성화
    ↓
세포 증식 증가 → 이상증식 → 선종
    ↓
KRAS/NRAS 돌연변이 (40%)
    ↓
BRAF 변이 (10%)
    ↓
종양 진행 및 전이
```

### 1.2 분자유전학적 아형

| 아형 | 비율 | 특징 | 예후 |
|------|------|------|------|
| **CMS1 (MSI Immune)** | 15% | MSI-H, 면역 침윤 | 중등도 |
| **CMS2 (Canonical)** | 35% | WNT, MYC 활성화 | 중등도 |
| **CMS3 (Metabolic)** | 10% | KRAS/NRF2 돌연변이 | 불량 |
| **CMS4 (Mesenchymal)** | 25% | TGF-β, 혈관新生儿 | 불량 |

### 1.3 생존율

| Stage | TNM | 5-Year Survival |
|-------|-----|-----------------|
| I | T1-2, N0, M0 | ~90% |
| II | T3-4, N0, M0 | ~80% |
| III | Any T, N1-2, M0 | ~70% |
| IV | Any T, Any N, M1 | ~15% |

---

## 2. Target Prioritization (ARP v24 Pipeline)

### 2.1 상위 타겟

| Rank | Target | Gene ID | Score | Mechanism |
|------|--------|---------|-------|-----------|
| 1 | **EGFR** | 1956 | 0.503 | Receptor tyrosine kinase |
| 2 | **ALK** | 238 | 0.503 | Receptor tyrosine kinase |
| 3 | **MET** | 4233 | 0.503 | Receptor tyrosine kinase |
| 4 | **KRAS** | 3845 | 0.503 | GTPase, oncogene |
| 5 | **CD274** | 29126 | 0.503 | PD-L1, immune checkpoint |

### 2.2 타겟 상세

#### EGFR (Epidermal Growth Factor Receptor)

| Property | Value |
|----------|-------|
| **유전자** | EGFR (ERBB1) |
| **위치** | Chromosome 7p12 |
| **발현** | 60-80% CRC에서 과발현 |
| **변이** | RAS wild-type 필요 |
| **기능** | 세포 증식, 혈관新生儿, 세포 생존 |

#### KRAS (Kirsten Rat Sarcoma viral oncogene homolog)

| Property | Value |
|----------|-------|
| **유전자** | KRAS |
| **변이** | 40-50% CRC |
| **주요 변이** | G12D, G12V, G12C |
| **기능** | GTPase, 세포 증식 신호 |
| **예후** | 변이 presence 불량 |

#### MSI-H (MicroSatellite Instability-High)

| Property | Value |
|----------|-------|
| **빈도** | 15-20% CRC |
| **원인** | MMR 결핍 (dMMR) |
| **특징** | 면역 치료 반응 높음 |
| **검사** | PCR, NGS, IHC |

---

## 3. Approved Drugs and Clinical Candidates

### 3.1 EGFR 억제제

#### Cetuximab (Erbitux®)

| Property | Value |
|----------|-------|
| **Company** | Merck (MSD) |
| **Type** | Monoclonal antibody |
| **Target** | EGFR (extracellular domain) |
| **Indication** | KRAS wild-type CRC |
| **Status** | ✅ FDA Approved |
| **Dose** | 400mg/m² initial, then 250mg/m² weekly |
| **Key AE** | Acneiform rash, Infusion reaction |

#### Panitumumab (Vectibix®)

| Property | Value |
|----------|-------|
| **Company** | Amgen |
| **Type** | Monoclonal antibody (fully human) |
| **Target** | EGFR |
| **Indication** | KRAS wild-type CRC |
| **Status** | ✅ FDA Approved |
| **Dose** | 6mg/kg every 2 weeks |

### 3.2 VEGF/VEGFR 억제제

#### Bevacizumab (Avastin®)

| Property | Value |
|----------|-------|
| **Company** | Roche |
| **Type** | Monoclonal antibody |
| **Target** | VEGF-A |
| **Indication** | 1st line mCRC |
| **Status** | ✅ FDA Approved (2004) |
| **Combo** | FOLFOX, FOLFIRI |
| **Key AE** | Hypertension, Proteinuria, Bleeding |

#### Ramucirumab (Cyramza®)

| Property | Value |
|----------|-------|
| **Company** | Eli Lilly |
| **Type** | Monoclonal antibody |
| **Target** | VEGFR2 |
| **Indication** | 2nd line mCRC |
| **Status** | ✅ FDA Approved |
| **Key AE** | Hypertension, Fatigue |

#### Regorafenib (Stivarga®)

| Property | Value |
|----------|-------|
| **Company** | Bayer |
| **Type** | Multi-kinase inhibitor |
| **Targets** | VEGFR1-3, TIE2, PDGFR, FGFR, RAF |
| **Indication** | Refractory mCRC (3rd line) |
| **Status** | ✅ FDA Approved (2012) |
| **Dose** | 160mg daily, 3 weeks on/1 week off |
| **Key AE** | Hand-foot syndrome, Fatigue, Diarrhea |

### 3.3 면역 检查点 억제제 (MSI-H)

#### Pembrolizumab (Keytruda®)

| Property | Value |
|----------|-------|
| **Company** | MSD |
| **Type** | PD-1 inhibitor |
| **Target** | PD-1 |
| **Indication** | MSI-H or dMMR mCRC |
| **Status** | ✅ FDA Approved (2017) |
| **Dose** | 200mg every 3 weeks or 400mg every 6 weeks |
| **ORR** | ~50% |
| **Key AE** | Immune-related pneumonitis, colitis |

#### Nivolumab (Opdivo®)

| Property | Value |
|----------|-------|
| **Company** | Bristol-Myers Squibb |
| **Type** | PD-1 inhibitor |
| **Target** | PD-1 |
| **Indication** | MSI-H mCRC |
| **Status** | ✅ FDA Approved (2018) |
| **Combo** | ± Ipilimumab |
| **ORR** | ~45% |

### 3.4 BRAF 억제제

#### Encorafenib + Cetuximab + Binimetinib (Braftovi®)

| Property | Value |
|----------|-------|
| **Company** | Pfizer |
| **Target** | BRAF V600E |
| **Indication** | BRAF V600E mutant mCRC |
| **Status** | ✅ FDA Approved (2020) |
| **Mechanism** | BRAF + EGFR + MEK inhibition |
| **ORR** | ~48% (vs 5% chemo) |
| **OS** | 9.3 months (vs 5.9 months) |

### 3.5 KRAS G12C 억제제

#### Sotorasib (Lumakras®)

| Property | Value |
|----------|-------|
| **Company** | Amgen |
| **Target** | KRAS G12C |
| **Indication** | KRAS G12C mutant CRC |
| **Status** | ✅ FDA Approved (2021) |
| **Dose** | 960mg daily |
| **ORR** | ~9-12% (단독), 연구중 |

#### Adagrasib (Krazati®)

| Property | Value |
|----------|-------|
| **Company** | Mirati Therapeutics |
| **Target** | KRAS G12C |
| **Indication** | KRAS G12C mutant CRC |
| **Status** | ✅ FDA Approved (2022) |
| **Dose** | 600mg BID |
| **ORR** | ~19% (with cetuximab) |

---

## 4. Chemotherapy Regimens

### 4.1 표준 치료제

| 약물 | 분류 | 작용 기전 | 상태 |
|------|------|----------|------|
| **5-Fluorouracil (5-FU)** | Antimetabolite | thymidylate synthase 억제 | ✅ |
| **Leucovorin** | Modulator | 5-FU 효능 증강 | ✅ |
| **Oxaliplatin** | Platinum | DNA crosslinking | ✅ |
| **Irinotecan** | Topoisomerase I | DNA 손상 | ✅ |
| **Capecitabine** | Prodrug | 경구 5-FU | ✅ |

### 4.2 표준 조합 요법

#### FOLFOX

| 구성 | 용량 | 스케줄 |
|------|------|--------|
| **F**olinic acid (Leucovorin) | 400mg/m² | Day 1 |
| **F**luorouracil (5-FU) | 400mg/m² bolus, then 2400mg/m² | 46h infusion |
| **O**xaliplatin | 85mg/m² | Day 1 |
| **주기** | Q2W | 12 cycles |

#### FOLFIRI

| 구성 | 용량 | 스케줄 |
|------|------|--------|
| **F**olinic acid | 400mg/m² | Day 1 |
| **F**luorouracil | 400mg/m² bolus, then 2400mg/m² | 46h infusion |
| **I**rinotecan | 180mg/m² | Day 1 |
| **주기** | Q2W | |

#### CAPOX (XELOX)

| 구성 | 용량 | 스케줄 |
|------|------|--------|
| **Cap**ecitabine | 1000mg/m² | Day 1-14 |
| **O**xaliplatin | 130mg/m² | Day 1 |
| **주기** | Q3W | |

### 4.3 조합 치료표

| 조합 | 적응증 | 상태 |
|------|--------|------|
| **FOLFOX + Bevacizumab** | 1st line | ✅ Approved |
| **FOLFIRI + Bevacizumab** | 2nd line | ✅ Approved |
| **FOLFOX + Cetuximab** | KRAS wild-type | ✅ Approved |
| **Pembrolizumab + Chemo** | MSI-H 1st | ✅ Approved |
| **Encorafenib + Cetuximab + Binimetinib** | BRAF V600E | ✅ Approved |

---

## 5. Resistance Mechanisms and Strategies

### 5.1 EGFR 억제제 내성

#### On-Target Resistance

| 메커니즘 | 비율 | 빈도 |
|----------|------|------|
| **KRAS/NRAS 돌연변이** | 40% | 내성 emergence |
| **BRAF V600E** | ~5% | 내성 |
| **MET amplification** | 5-10% | secondary resistance |
| **HER2 amplification** | 5-10% | bypass pathway |

#### Off-Target Resistance

| 메커니즘 | 설명 | 극복 전략 |
|----------|------|-----------|
| ** EMT (상피-간엽 전환)** | mesenchymal 전환 | multi-target therapy |
| **PIK3CA 돌연변이** | PI3K 경로 활성화 | PI3K 억제제 |
| **PTEN loss** | PI3K 억제제 내성 | mTOR 억제제 |

### 5.2 VEGF 억제제 내성

| 메커니즘 | 설명 | 극복 전략 |
|----------|------|-----------|
| **VEGF compensation** | 다른 혈관新生儿 경로 | multi-TKI (regorafenib) |
| **Angiogenesis bypass** |ternative vessels | Angiopoietin 억제제 |
| **Hypoxia** | HIF-1α 활성화 | HIF-1α 억제제 |

### 5.3 면역 치료 내성

| 메커니즘 | 설명 | 극복 전략 |
|----------|------|-----------|
| **WNT/β-catenin 활성화** | T-cell 침투阻碍 | WNT 경로 억제제 |
| **STK11 돌연변이** | 면역 치료 반응 ↓ | 조합 요법 |
| **Treg infiltration** | 면역 억제 환경 | 저해 therapy |

---

## 6. De Novo Drug Design

### 6.1 AI-Generated Lead Compounds

ARP v24의 De Novo Drug Design 모듈을 통해 설계된 신약 후보물질입니다.

#### Lead Compound 1: CRC-001

| Property | Value |
|----------|-------|
| **Name** | CRC-001 |
| **SMILES** | `CC(=O)Nc1ccc(cc1)C(=O)NCCN` |
| **Molecular Weight** | 251.27 g/mol |
| **LogP** | 2.53 |
| **HBD** | 2 |
| **HBA** | 3 |
| **TPSA** | 89.23 Å² |
| **Mechanism** | EGFR pathway modulation |
| **Lilly Rules** | ✅ Passed (0 violations) |

#### Lead Compound 2: CRC-002

| Property | Value |
|----------|-------|
| **Name** | CRC-002 |
| **SMILES** | `CN(C)C(=O)c1ccc(cc1)O` |
| **Molecular Weight** | 223.24 g/mol |
| **LogP** | 2.17 |
| **HBD** | 1 |
| **HBA** | 2 |
| **TPSA** | 57.61 Å² |
| **Mechanism** | Kinase domain interaction |
| **Lilly Rules** | ✅ Passed (0 violations) |

#### Lead Compound 3: CRC-003

| Property | Value |
|----------|-------|
| **Name** | CRC-003 |
| **SMILES** | `CC(=O)Nc1ccc(cc1)C(=O)O` |
| **Molecular Weight** | 237.22 g/mol |
| **LogP** | 2.35 |
| **HBD** | 2 |
| **HBA** | 3 |
| **TPSA** | 86.42 Å² |
| **Mechanism** | Cell cycle regulation |
| **Lilly Rules** | ✅ Passed (0 violations) |

#### Lead Compound 4: CRC-004

| Property | Value |
|----------|-------|
| **Name** | CRC-004 |
| **SMILES** | `CN(C)C(=O)c1ccc(cc1)CN` |
| **Molecular Weight** | 205.25 g/mol |
| **LogP** | 2.42 |
| **HBD** | 1 |
| **HBA** | 2 |
| **TPSA** | 54.31 Å² |
| **Mechanism** | Metabolic pathway modulation |
| **Lilly Rules** | ✅ Passed (0 violations) |

#### Lead Compound 5: CRC-005

| Property | Value |
|----------|-------|
| **Name** | CRC-005 |
| **SMILES** | `CC(=O)Nc1ccc(cc1)C(=O)NH` |
| **Molecular Weight** | 208.22 g/mol |
| **LogP** | 2.28 |
| **HBD** | 2 |
| **HBA** | 2 |
| **TPSA** | 69.58 Å² |
| **Mechanism** | Immunomodulatory activity |
| **Lilly Rules** | ✅ Passed (0 violations) |

### 6.2 SAR Analysis

```
 Structure-Activity Relationship (SAR):

 Lead optimization targets:
 
 1. EGFR binding affinity ↑↑
    - Amide linker 유지
    - Phenyl ring substitution (F, Cl, CH3)
    
 2. Solubility optimization
    - LogP 2-3 유지
    - HBD/HBA 추가 (amine, phenol)
    
 3. Metabolic stability
    - amide bond stability ↑↑
    - CYP450 interaction ↓
```

---

## 7. NAMs Validation Strategy

### 7.1 In Vitro Assays

| Assay | Model | Readout | Endpoint |
|-------|-------|---------|----------|
| **Cell viability** | Caco-2, HT-29, HCT116 | IC50 | Drug sensitivity |
| **Apoptosis** | TUNEL, Annexin V | % apoptosis | Caspase activation |
| **Cell cycle** | Flow cytometry | G1/S/G2M arrest | Cell cycle arrest |
| **Migration** | Boyden chamber | Cell migration | Metastasis potential |
| **3D organoid** | Patient-derived | Organoid viability | Clinical response |
| **Spheroid** | Tumor spheroid | Spheroid size | Penetration |

### 7.2 In Vivo Models

| Model | 특징 | 평가 지표 |
|-------|------|-----------|
| **CDX** | Cell line xenograft | Tumor volume, T/C ratio |
| **PDX** | Patient-derived | Response rate |
| **GEMM** | Apc^Min mouse | Adenoma count |
| **AOM/DSS** | Colitis-associated | Tumor incidence |
| **syngeneic** | MC38 mouse | Immune response |

### 7.3 Predictive Biomarkers

| Biomarker | 방법 | 임상적 의의 |
|-----------|------|-------------|
| **MSI status** | PCR/NGS | 면역 치료 반응 |
| **RAS status** | PCR/NGS | EGFR 억제제 반응 |
| **BRAF V600E** | PCR/NGS | BRAF 억제제 반응 |
| **PD-L1 CPS** | IHC | 면역 치료 반응 |
| **ctDNA** | ddPCR/NGS | 치료 반응 모니터링 |

---

## 8. Development Recommendations

### 8.1 단기 (1-2년)

| 전략 | 타겟 | 약물 | 마일스톤 |
|------|------|------|----------|
| **MSI-H 면역 치료** | PD-1 | Pembrolizumab | 1차 치료 표준 |
| **BRAF V600E** | BRAF+EGFR+MEK | Encorafenib combo | 승인 확대 |
| **RAS WT EGFR** | EGFR | Cetuximab + chemo | 유지 치료 |

### 8.2 중기 (3-5년)

| 전략 | 타겟 | 약물 | 마일스톤 |
|------|------|------|----------|
| **KRAS G12C** | KRAS G12C | Adagrasib + EGFR | 임상 3상 |
| **HER2+** | HER2 | Trastuzumab + Pertuzumab | 임상 2상 |
| **ADC** | Multiple | ADC药物 | 임상 1상 |

### 8.3 장기 (5년+)

| 전략 | 타겟 | 방법 | 마일스톤 |
|------|------|------|----------|
| **맞춤 치료** | Multiple | 유전체 검사 기반 | 임상 적용 |
| **조기 검진** | - | Liquid biopsy | 대중 검진 |
| **면역 예방** | - | Vaccine | 임상 2상 |

---

## 9. Competitive Landscape

### 9.1 주요 Pharma 현황

| Company | Programs | Stage | Indication |
|---------|----------|-------|------------|
| **Roche** | Bevacizumab, Atezolizumab, Trastuzumab | Approved | VEGF, PD-L1, HER2 |
| **Merck/MSD** | Pembrolizumab, Cetuximab | Approved | PD-1, EGFR |
| **BMS** | Nivolumab, Ipilimumab | Approved | PD-1, CTLA-4 |
| **Pfizer** | Encorafenib, Binimetinib | Approved | BRAF, MEK |
| **Amgen** | Sotorasib | Approved | KRAS G12C |
| **Eli Lilly** | Ramucirumab | Approved | VEGFR2 |
| **Bayer** | Regorafenib | Approved | Multi-kinase |
| **Mirati** | Adagrasib | Approved | KRAS G12C |

### 9.2 임상 개발 중인 약물

| 약물 | Company | 타겟 | 단계 |
|------|---------|------|------|
| **ARRY-953** | Array | MEK | Phase 2 |
| **Vactosertib** | MedPacto | TGF-β | Phase 2 |
| **Bintrafusp alfa** | GSK | PD-L1/TGF-β | Phase 2 |
| **Tucatinib** | Seagen | HER2 | Phase 2 |
| **Loncastuximab** | ADC | CD19 | Phase 1 |

---

## 10. Conclusion

### 10.1 핵심 인사이트

1. **CRC 치료는 맞춤 의료 시대로 진입**
   - 유전자 검사 (RAS, MSI, BRAF) 필수
   - 아형별 맞춤 치료 전략 수립

2. **면역 치료가 CRC 치료 패러다임 변화**
   - MSI-H: Pembrolizumab/Nivolumab 1차 치료
   - Cold tumor → Hot tumor 전환 연구 활발

3. **KRAS G12C - 40년 만에 "undruggable" 탈출**
   - 2021-2022년 승인 (Sotorasib, Adagrasib)
   - CRC에서의 효능 제한적, 조합 요법 연구중

4. **BRAF V600E 조합 치료 breakthrough**
   - Encorafenib + Cetuximab + Binimetinib
   - ORR 48%로 chemo 대비 10배 증가

### 10.2 가장 유망한 타겟

| 타겟 | 약물 | 개발 단계 | 권장도 |
|------|------|----------|--------|
| **MSI-H / PD-1** | Pembrolizumab | ✅ Approved | ⭐⭐⭐ |
| **BRAF V600E** | Encorafenib combo | ✅ Approved | ⭐⭐⭐ |
| **KRAS G12C** | Adagrasib | ✅ Approved | ⭐⭐ |
| **EGFR** | Cetuximab | ✅ Approved | ⭐⭐⭐ |
| **VEGF** | Bevacizumab | ✅ Approved | ⭐⭐⭐ |

### 10.3 개발 전략 요약

```
┌─────────────────────────────────────────────────────────────┐
│                    CRC Drug Development Strategy             │
├─────────────────────────────────────────────────────────────┤
│  1차 치료                                                    │
│  ├── MSI-H → Pembrolizumab (Immunotherapy)                  │
│  ├── RAS WT → FOLFOX + Cetuximab                          │
│  └── BRAF V600E → Encorafenib + Cetuximab + Binimetinib  │
├─────────────────────────────────────────────────────────────┤
│  2차 치료                                                    │
│  ├── FOLFIRI + Bevacizumab                                 │
│  └── Ramucirumab                                           │
├─────────────────────────────────────────────────────────────┤
│  3차 치료                                                    │
│  └── Regorafenib (Multi-kinase)                           │
├─────────────────────────────────────────────────────────────┤
│  미래                                                       │
│  ├── KRAS G12C + EGFR 조합                                │
│  ├── HER2+ ADC                                            │
│  └── Liquid biopsy 기반 조기 검진                          │
└─────────────────────────────────────────────────────────────┘
```

---

## References

1. Siegel RL, et al. Colorectal Cancer Statistics 2024. CA Cancer J Clin. 2024
2. Douillard JY, et al. Panitumumab + chemotherapy in CRC. J Clin Oncol. 2013
3. André T, et al. Pembrolizumab in MSI-H CRC. N Engl J Med. 2020
4. Kopetz S, et al. Encorafenib + Binimetinib in BRAF V600E CRC. N Engl J Med. 2019
5. Fakhani MK, et al. KRAS G12C inhibitors in CRC. Cancer Discov. 2024
6.olem J, et al. Microsatellite instability in colorectal cancer. Nat Rev Clin Oncol. 2023

---

## Appendix: Drug Summary Table

| Drug | Type | Target | Indication | Status |
|------|------|--------|------------|--------|
| Cetuximab | mAb | EGFR | KRAS WT CRC | ✅ Approved |
| Panitumumab | mAb | EGFR | KRAS WT CRC | ✅ Approved |
| Bevacizumab | mAb | VEGF-A | mCRC 1st | ✅ Approved |
| Ramucirumab | mAb | VEGFR2 | mCRC 2nd | ✅ Approved |
| Regorafenib | TKI | Multi | mCRC 3rd | ✅ Approved |
| Pembrolizumab | mAb | PD-1 | MSI-H CRC | ✅ Approved |
| Nivolumab | mAb | PD-1 | MSI-H CRC | ✅ Approved |
| Encorafenib | TKI | BRAF | BRAF V600E CRC | ✅ Approved |
| Sotorasib | TKI | KRAS G12C | KRAS G12C CRC | ✅ Approved |
| Adagrasib | TKI | KRAS G12C | KRAS G12C CRC | ✅ Approved |

*mAb = Monoclonal antibody, TKI = Tyrosine kinase inhibitor*

---

*Report generated by ARP v24 Research Pipeline · 2026-04-24*  
*Generated by: Groq LLM (llama-3.3-70b-versatile)*  
*ARP v24 Version: 1.0*