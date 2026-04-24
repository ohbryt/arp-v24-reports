# NSCLC (Non-Small Cell Lung Cancer) Drug Discovery Report
## ARP v24 Research Pipeline

**Generated:** 2026-04-24  
**Disease:** NSCLC (Non-Small Cell Lung Cancer)  
**Type:** Lung Cancer (85% of all lung cancers)  
**Researcher:** ARP v24 + Groq LLM  

---

## 1. Executive Summary

NSCLC (Non-Small Cell Lung Cancer, 비소세포성 폐암)은 폐암의 약 85%를 차지하며, 상피세포에서 발생하는 악성 종양입니다.

### 치료 적응증

| 적응증 | 비율 | 예후 |
|--------|------|------|
| **adenocarcinoma** | ~40% | 중등도 |
| **squamous cell carcinoma** | ~25-30% | 중등도 |
| **large cell carcinoma** | ~10-15% | 불량 |

### 핵심 타겟 (ARP v24 Pipeline)

| Rank | Target | Score | Drug Candidates |
|------|--------|-------|-----------------|
| 1 | **EGFR** | 0.503 | Gefitinib, Erlotinib, Osimertinib |
| 2 | **ALK** | 0.503 | Crizotinib, Alectinib, Lorlatinib |
| 3 | **MET** | 0.503 | Capmatinib, Tepotinib |
| 4 | **KRAS** | 0.503 | Sotorasib, Adagrasib |
| 5 | **CD274 (PD-L1)** | 0.503 | Pembrolizumab, Atezolizumab |

---

## 2. 핵심 타겟 및 약물 개발 현황

### 2.1 EGFR (Epidermal Growth Factor Receptor)

**변이:** 30-40% (특히 비흡연자, 여성, 아시아인)  
**기능:** 세포 증식 및 생존 신호 전달

#### 티로신 키나아제 억제제 (TKI)

| 약물 | 세대 | Company | 상태 |
|------|------|---------|------|
| **Gefitinib** | 1세대 | AstraZeneca | ✅ 승인 |
| **Erlotinib** | 1세대 | Roche | ✅ 승인 |
| **Afatinib** | 2세대 | Boehringer | ✅ 승인 |
| **Osimertinib** | 3세대 | AstraZeneca | ✅ 1차 치료 approved |
| **Mobocertinib** | 3세대 | Takeda | 승인 (2021, 후퇴) |

**Osimertinib 권장:**
- 1차 치료 표준
- T790M 내성 돌연변이 효과적
- 뇌척삭질知道她有效

### 2.2 ALK (Anaplastic Lymphoma Kinase)

**변이:** 3-7%  
**Fusion:** EML4-ALK (echinoderm microtubule-associated protein-like 4)

#### ALK 억제제

| 약물 | Company | 상태 | 특징 |
|------|---------|------|------|
| **Crizotinib** | Pfizer | ✅ 승인 | 1차 치료 |
| **Ceritinib** | Novartis | ✅ 승인 | 2차 치료 |
| **Alectinib** | Roche | ✅ 승인 | 1차 치료, 뇌전이 효과 |
| **Brigatinib** | Ariad/Takeda | ✅ 승인 | 내성 극복 |
| **Lorlatinib** | Pfizer | ✅ 승인 | G1202R 내성, 뇌효과 |

### 2.3 ROS1

**변이:** 1-2%  
**Fusion:** GOPC-ROS1 (CMTI)

#### ROS1 억제제

| 약물 | Company | 상태 |
|------|---------|------|
| **Crizotinib** | Pfizer | ✅ 승인 |
| **Entrectinib** | Roche | ✅ 승인 |
| **Lorlatinib** | Pfizer | Phase 2 |

### 2.4 KRAS G12C

**변이:** 25-30% ( historically "undruggable" )  
**突破:** 2021-2022 covalent 억제제 승인

#### KRAS G12C 억제제

| 약물 | Company | 상태 | 승인일 |
|------|---------|------|--------|
| **Sotorasib (AMG 510)** | Amgen | ✅ FDA 승인 | 2021.05 |
| **Adagrasib (MRTX849)** | Mirati | ✅ FDA 승인 | 2022.12 |

**내성 메커니즘:**
- KRAS G12D/V 돌연변이 → 다음 세대 억제제 개발 중
- RTK reactivation → 조합 요법 필요

### 2.5 MET (Mesenchymal-Epithelial Transition)

**변이/amplification:** 3-5%  
**기능:** 상피-간엽 전환, 종양 침투

#### MET 억제제

| 약물 | Company | 상태 | 적응증 |
|------|---------|------|-------|
| **Capmatinib** | Novartis | ✅ FDA 승인 | MET amplification |
| **Tepotinib** | Merck | ✅ FDA 승인 | MET exon 14 skipping |
| **Savolitinib** | AstraZeneca/HutchMed | 개발중 | 중국 승인 |

---

## 3. 면역항암제 (Immune Checkpoint Inhibitors)

### 3.1 PD-1/PD-L1 억제제

| 약물 | 타겟 | Company | 상태 | 적응증 |
|------|------|---------|------|-------|
| **Pembrolizumab** | PD-1 | MSD | ✅ 승인 | 1차 치료 (PD-L1≥1%) |
| **Nivolumab** | PD-1 | BMS | ✅ 승인 | 2차 치료 |
| **Atezolizumab** | PD-L1 | Roche | ✅ 승인 | 1차 치료 |
| **Durvalumab** | PD-L1 | AstraZeneca | ✅ 승인 | Stage III 유지요법 |
| **Cemiplimab** | PD-1 | Regeneron | ✅ 승인 | 2차 이후 |

### 3.2 조합 요법 현황

| 조합 | Company | 상태 | 비고 |
|------|---------|------|------|
| **Osimertinib + Pembrolizumab** | AstraZeneca/MSD | Phase 3 | 부작용 증가 |
| **Chemo + Pembro** | MSD | ✅ 승인 | 1차 치료 표준 |
| **Chemo + Atezolizumab + Bevacizumab** | Roche | ✅ 승인 | |

---

## 4. 내성 메커니즘 및 극복 전략

### 4.1 EGFR 내성 메커니즘

| 내성 메커니즘 | 비율 | 극복 전략 |
|--------------|------|-----------|
| **T790M 돌연변이** | ~50% | Osimertinib (3세대) |
| **C797S 돌연변이** | ~15% | 4세대 TKI (EAI-045, BLU-945) |
| **MET amplification** | ~5-10% | EGFR + MET 조합 |
| **HER2 amplification** | ~2-5% | HER2 antibody-drug conjugate |
| **SCLC transformation** | ~10% | Chemotherapy |

### 4.2 ALK 내성 메커니즘

| 내성 메커니즘 | 극복 전략 |
|--------------|-----------|
| **G1202R 돌연변이** | Lorlatinib |
| **L1196M** | Alectinib, Brigatinib |
| **Multiple mutations** | 2세대 ALK 억제제 조합 |

### 4.3 KRAS G12C 내성

- **On-target resistance:** KRAS 돌연변이 확대
- **Off-target resistance:** RTK reactivation → SHP2 억제제 조합
- **Adaptive resistance:** Autophagy → Hydroxychloroquine 조합

---

## 5. NAMs 검증 전략

### 5.1 In Vitro

| Assay | Model | Readout |
|-------|-------|---------|
| **세포 증식** | NSCLC cell lines (PC9, H1975) | IC50 |
| ** apoptosis** | TUNEL, caspase activation | Annexin V |
| **신호 경로** | Western blot | pEGFR, pAKT, pERK |
| **3D organoid** | Patient-derived | Organoid viability |

### 5.2 In Vivo

| Model | 유발 방법 | 평가 지표 |
|-------|----------|-----------|
| **CDX** | Cell line xenograft | 종양 크기 |
| **PDX** | Patient-derived | 종양 감소율 |
| **GEMM** | KRAS/EGFR突变 | 생존율 |
| **syngeneic** | LLC model | 면역 반응 |

### 5.3 임상 전 生物標識

| Biomarker | 측정법 | 임상적 의의 |
|-----------|--------|-------------|
| **PD-L1** | IHC | 면역 치료 반응 예측 |
| **TMB** | NGS | 면역 치료 반응 예측 |
| **ctDNA** | droplet digital PCR | 치료 반응 모니터링 |
| **EGFR mutation** | PCR/NGS | TKI 반응 예측 |

---

## 6. 결론 및 권고

### 6.1 가장 유망한 타겟

| 타겟 | 약물 | 개발 단계 | 권장 |
|------|------|----------|------|
| **EGFR** | Osimertinib | 임상 | ⭐⭐⭐ 1차 치료 표준 |
| **KRAS G12C** | Sotorasib/Adagrasib | 임상 | ⭐⭐⭐ 최근 승인 |
| **ALK** | Alectinib/Lorlatinib | 임상 | ⭐⭐⭐ 1차 치료 |
| **MET** | Capmatinib/Tepotinib | 임상 | ⭐⭐ MET 변이 |
| **PD-L1** | Pembrolizumab | 임상 | ⭐⭐⭐ 1차 치료 |

### 6.2 개발 전략

```
1. 단기 (1-2년):
   - EGFR 3세대 + 면역 치료 조합
   - KRAS G12C + SHP2 억제제
   - MET TKI + EGFR 억제제

2. 중기 (3-5년):
   - 4세대 EGFR TKI (C797S)
   - KRAS G12D/V 억제제
   - Multi-target TKI

3. 장기 (5년+):
   - 개인별 맞춤 치료
   - early detection + intervention
   - 항암-vaccine 조합
```

### 6.3 핵심 인사이트

> **NSCLC 치료는 맞춤 의료 시대로:**
> 1. 유전자 변이 확인이 필수
> 2. TKI + 면역 치료 조합이 표준
> 3. 내성 극복을 위한 차세대 억제제 개발 중
> 4. KRAS G12C는 2021-2022년 가장 큰突破

---

## 7. References

1. Soria JC, et al. Osimertinib in EGFR T790M-positive NSCLC. N Engl J Med. 2017
2. Skoulidis F, et al. KRAS G12C inhibition with sotorasib. N Engl J Med. 2021
3. Mok TS, et al. Alectinib vs crizotinib in ALK-positive NSCLC. N Engl J Med. 2017
4. Reck M, et al. Pembrolizumab vs chemotherapy in PD-L1-positive NSCLC. N Engl J Med. 2016

---

*Report generated by ARP v24 Research Pipeline · 2026-04-24*