# Colorectal Cancer (CRC) Drug Discovery Report
## ARP v24 Research Pipeline

**Generated:** 2026-04-24  
**Disease:** Colorectal Cancer (CRC, 대장암)  
**Type:** Gastrointestinal Cancer  
**Epidemiology:** World 3rd most common cancer (~1.9M cases/year)  
**Researcher:** ARP v24 + Groq LLM  

---

## 1. Executive Summary

대장암은 세계에서 3번째로 흔한 암으로, 매년 약 190만 명의 환자가 발생합니다.

### 생존율

| Stage | 5-Year Survival |
|-------|----------------|
| I | ~90% |
| II | ~80% |
| III | ~70% |
| IV | ~15% |

### 핵심 타겟 (ARP v24 Pipeline)

| Rank | Target | Score | Drug Candidates |
|------|--------|-------|-----------------|
| 1 | **EGFR** | 0.503 | Cetuximab, Panitumumab |
| 2 | **ALK** | 0.503 | Crizotinib |
| 3 | **MET** | 0.503 | Capmatinib |
| 4 | **KRAS** | 0.503 | Sotorasib |
| 5 | **CD274** | 0.503 | Pembrolizumab |

---

## 2. 핵심 타겟 및 약물 개발 현황

### 2.1 EGFR (Epidermal Growth Factor Receptor)

**발현:** 70-80% (종양에서 높음)  
**기능:** 세포 증식, 혈관新生儿, 종양 진행

#### 항체 기반 억제제

| 약물 | Company | 상태 | 적응증 |
|------|---------|------|-------|
| **Cetuximab** | Merck | ✅ 승인 | RAS wild-type |
| **Panitumumab** | Amgen | ✅ 승인 | RAS wild-type |

### 2.2 VEGF/VEGFR (혈관新生 억제)

**기능:** 종양 혈관 차단, 영양 공급 차단

| 약물 | Company | 상태 | 특징 |
|------|---------|------|------|
| **Bevacizumab** | Roche | ✅ 승인 | 1차 치료 |
| **Ramucirumab** | Eli Lilly | ✅ 승인 | 2차 치료 |
| **Regorafenib** | Bayer | ✅ 승인 | 3차 치료 (multi-kinase) |

### 2.3 MSI-H (MicroSatellite Instability-High)

**빈도:** ~15% (특히 우측 결장, Lynch 증후군)  
**특성:** 면역 치료 반응율 높음 (40-50%)

#### 면역检查点 억제제

| 약물 | Company | 상태 | 반응율 |
|------|---------|------|--------|
| **Pembrolizumab** | MSD | ✅ 승인 | ~50% |
| **Nivolumab** | BMS | ✅ 승인 | ~45% |
| **Ipilimumab** | BMS | ✅ 승인 | ~40% |

### 2.4 BRAF V600E

**빈도:** ~10% (예후不良)  
**특성:** melanocytic 표현, 내성 많음

| 약물 | 조합 | Company | 상태 |
|------|------|---------|------|
| **Encorafenib** | +Cetuximab+Binimetinib | Pfizer | ✅ 승인 (2020) |

### 2.5 KRAS

**빈도:** ~40% (KRAS 돌연변이)  
**특성:** EGFR 억제제에 내성

| 상태 | 약물 | 반응 |
|------|------|------|
| **KRAS野生형** | Cetuximab/Panitumumab | ✅ 반응 |
| **KRAS 돌연변이** | EGFR 억제제 | ❌ 무응답 |
| **KRAS G12C** | Sotorasib/Adagrasib | ✅ 승인 |

### 2.6 Wnt 경로

**기전:** APC 돌연변이 → β-catenin 축적 → 종양 진행  
**연구중 타겟:**

| 타겟 | 화합물 | 단계 |
|------|--------|------|
| **Porcupine** | ETC-1922149 | Phase 1 |
| **Tankyrase** | G007-LK | 전임상 |

---

## 3. 화학요법 (Chemotherapy)

### 3.1 표준 치료제

| 약물 | 조합 | Company | 상태 |
|------|------|---------|------|
| **5-Fluorouracil (5-FU)** | Leucovorin | generic | ✅ 승인 |
| **Oxaliplatin** | FOLFOX | generic | ✅ 승인 |
| **Irinotecan** | FOLFIRI | generic | ✅ 승인 |
| **Capecitabine** | 경구 | Roche | ✅ 승인 |

### 3.2 표준 조합 요법

| 조합 | 구성 | 용도 |
|------|------|------|
| **FOLFOX** | 5-FU + Leucovorin + Oxaliplatin | 1차 치료 |
| **FOLFIRI** | 5-FU + Leucovorin + Irinotecan | 2차 치료 |
| **CAPOX** | Capecitabine + Oxaliplatin | 1차 치료 |
| **FOLFOXIRI** | 5-FU + Oxaliplatin + Irinotecan | 전이성 |

---

## 4. 조합 요법 (Combination Therapy)

### 4.1 승인된 조합

| 조합 | Company | 상태 | 적응증 |
|------|---------|------|-------|
| **FOLFOX + Bevacizumab** | Roche | ✅ | 1차 치료 |
| **FOLFIRI + Bevacizumab** | Roche | ✅ | 2차 치료 |
| **FOLFOX + Cetuximab** | Merck | ✅ | RAS wild-type |
| **Pembrolizumab + Chemo** | MSD | ✅ | MSI-H 1차 |

### 4.2 개발중 조합

| 조합 | 단계 | 타겟 |
|------|------|------|
| **Bevacizumab + Atezolizumab** | Phase 3 | VEGF + PD-L1 |
| **Cetuximab + Binimetinib** | Phase 2 | EGFR + MEK |
| **Regorafenib + Nivolumab** | Phase 1/2 | Multi + PD-1 |

---

## 5. 내성 메커니즘 및 극복 전략

### 5.1 EGFR 억제제 내성

| 내성 메커니즘 | 비율 | 극복 전략 |
|--------------|------|-----------|
| **KRAS/NRAS 돌연변이** | ~40% | RAS 돌연변이 검사 필수 |
| **MET amplification** | ~5-10% | MET 억제제 추가 |
| **HER2 amplification** | ~5-10% | Trastuzumab + Pertuzumab |
| **Epithelial-mesenchymal transition** | Variable | Multi-target therapy |

### 5.2 VEGF 억제제 내성

| 내성 메커니즘 | 극복 전략 |
|--------------|-----------|
| **VEGF compensation** | Regorafenib (multi-kinase) |
| **Angiogenesis bypass** | Angiopoietin 억제제 |
| **Hypoxia** | HIF-1α 억제제 |

### 5.3 면역 치료 내성

- **STK11 돌연변이** → 면역 치료 반응 低
- **WNT/β-catenin 활성화** → T-cell 침투阻碍
- **Treg infiltration** → 면역 억제 환경

---

## 6. NAMs 검증 전략

### 6.1 In Vitro 검증

| Assay | Model | Readout |
|-------|-------|---------|
| **Organoid** | Patient-derived organoid (PDO) | drug sensitivity |
| **Spheroid** | 3D tumor spheroid | viability |
| **Apoptosis** | TUNEL, caspase | Annexin V |
| **Migration** | Boyden chamber | cell migration |

### 6.2 In Vivo 검증

| Model | 유발 | 평가 |
|-------|------|------|
| **PDX** | Patient-derived | tumor regression |
| **Apc^Min mouse** | Apc mutation | intestinal tumors |
| **AOM/DSS** | Inflammation-induced | colitis-associated CRC |
| **MC38 syngeneic** | Mouse CRC | immune checkpoint response |

### 6.3 Predictive Biomarkers

| Biomarker | 방법 | 임상적 의의 |
|-----------|------|-------------|
| **MSI-H** | PCR/NGS | 면역 치료 반응 |
| **RAS status** | PCR/NGS | EGFR 억제제 반응 |
| **BRAF V600E** | PCR/NGS | 예후 예측 |
| **PD-L1** | IHC | 면역 치료 반응 |
| **ctDNA** | ddPCR/NGS | 치료 반응 모니터링 |

---

## 7. 결론 및 권고

### 7.1 가장 유망한 타겟

| 타겟 | 약물 | 개발 단계 | 권장도 |
|------|------|----------|--------|
| **MSI-H** | Pembrolizumab | ✅ 승인 | ⭐⭐⭐ |
| **BRAF V600E** | Encorafenib combo | ✅ 승인 | ⭐⭐⭐ |
| **KRAS G12C** | Sotorasib | ✅ 승인 | ⭐⭐⭐ |
| **VEGF** | Bevacizumab | ✅ 승인 | ⭐⭐⭐ |
| **EGFR** | Cetuximab | ✅ 승인 | ⭐⭐ (RAS野生형) |

### 7.2 개발 전략

```
1. 단기 (1-2년):
   - MSI-H → 면역 치료 (1차 치료 표준)
   - RAS wild-type → FOLFOX + Cetuximab
   - BRAF V600E → Encorafenib + Cetuximab + Binimetinib

2. 중기 (3-5년):
   - KRAS G12C + EGFR 조합
   - Wnt 경로 타겟 (Porcupine 억제제)
   - 항체-약물접합체 (ADC) 개발

3. 장기 (5년+):
   - 개인별 맞춤 치료 (유전체 검사 기반)
   - 조기 검진 + 면역 예방
   - 장점막 면역 강화
```

### 7.3 핵심 인사이트

> **CRC 치료의 핵심:**
> 1. **유전자 검사 필수** - RAS, MSI, BRAF
> 2. **MSI-H는 면역 치료** - Pembrolizumab/Nivolumab
> 3. **BRAF V600E는 조합 요법** - Encorafenib + EGFR + MEK
> 4. **VEGF는 혈관 차단** - Bevacizumab + Chemo
> 5. **조기 검진이 예후 좌우** - Colonoscopy 권장

---

## 8. References

1. Siegel RL, et al. Colorectal Cancer Statistics 2024. CA Cancer J Clin. 2024
2. Douillard JY, et al. Panitumumab + chemotherapy in CRC. J Clin Oncol. 2013
3. André T, et al. Pembrolizumab in MSI-H CRC. N Engl J Med. 2020
4. Kopetz S, et al. Encorafenib + Binimetinib in BRAF V600E CRC. N Engl J Med. 2019

---

*Report generated by ARP v24 Research Pipeline · 2026-04-24*