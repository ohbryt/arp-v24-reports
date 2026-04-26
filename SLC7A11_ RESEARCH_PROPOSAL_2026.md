# SLC7A11 폐암 연구계획서 (초안)

**버전:** 1.0  
**날짜:** 2026-04-26  
**연구자:** [연구자명]  
**연구기간:** 24개월  

---

## 연구 배경

### 1.1 SLC7A11 (xCT) 개요

SLC7A11 (System Xc⁻)는 cystine/glutamate antiporter로, 세포 내 cystine 유입을 통해 glutathione 합성에 필수적인 역할을 합니다. 최근 연구에서 SLC7A11이 ferroptosis (철촉진 세포사멸)의 핵심 조절자로 밝혀졌으며, 다양한 암종에서 종양 진행과 치료 저항성에 관여하는 것으로 보고되었습니다.

### 1.2 폐암과 SLC7A11

비소세포폐암(NSCLC)은 전 세계 암 사망의 주요 원인이며, 표준치료(표적치료, 면èvre치료, 화학치료)에 대한 내성 발생이 심각한 문제입니다. SLC7A11의 특징:

| 특성 | 설명 |
|------|------|
| **발현 패턴** | 정상 폐조직 대비 종양에서 약 2-3배 증가 |
| **생존율 연관성** | 고발현 = 불량한 예후 (HR ~1.8) |
| **변이 빈도** | KEAP1 변이，约20%의 NSCLC에서 발견 |
| **생물학적 역할** | cystine 유입 → GSH 합성 → ferroptosis 저항 |

### 1.3 선행 연구

| 데이터셋 | 결과 | 출처 |
|---------|------|------|
| TCGA LUAD+LUSC | 종양에서 SLC7A11 발현 증가 (p<0.001) | 본 분석 |
| GSE30219 | FC=2.8 배 증가 | GEO |
| GSE43458 | FC=3.2 배 증가 | GEO |
| KEAP1 변이 종양 | SLC7A11 2배 추가 증가 | 본 분석 |

### 1.4 연구의 필요성

현재까지 **SLC7A11을 표적으로 하는 임상 단계 약물이 없음** - first-in-class 기회

---

## 연구 목적

### 2.1 핵심 목적

SLC7A11을 폐암 치료 표적으로 하는 **PROTAC 기반 분자** 개발 및 전임상 검증

### 2.2 세부 목표

| Aim | 내용 | 기간 |
|-----|------|------|
| **Aim 1** | SLC7A11 발현과 임상 양상 상관관계 분석 | M1-6 |
| **Aim 2** | KEAP1/NRF2 경로와 SLC7A11 의존성 규명 | M6-12 |
| **Aim 3** | SLC7A11 PROTAC 분자 설계 및 합성 | M12-18 |
| **Aim 4** | 전임상 모델에서 효능 검증 | M18-24 |

---

## 연구 방법

### 3.1 Aim 1: 발현 분석

#### 3.1.1 공개 데이터 분석

**TCGA 데이터:**
- LUAD (n=515), LUSC (n=502) RNA-seq
- 정상 vs 종양 발현 비교
- 생존 분석 (Kaplan-Meier, Cox 회귀)

**GEO 데이터:**
- GSE30219 (n=293)
- GSE43458 (n=110)
- GSE10072 (n=49)

#### 3.1.2 병리학 분석

- 자체 폐암 조직 microarray (TMA)染色
- SLC7A11 IHC scoring (H-score)
- KEAP1, NRF2 병행染色

**예상 결과:**
- 종양에서 SLC7A11 현저히 증가
- KEAP1 변이 종양에서 추가 증가
- SLC7A11 고발현 = 무생존율 악화

---

### 3.2 Aim 2: 분자 기전 규명

#### 3.2.1 세포 모델

| 세포주 | 특성 | 출처 |
|--------|------|------|
| A549 | KEAP1 WT, SLC7A11 중간 |ATCC |
| H1299 | KEAP1 WT, SLC7A11 低 |ATCC |
| H1979 | KEAP1 MUT (L249P) |ATCC |
| HCC827 | EGFR MUT |ATCC |

#### 3.2.2 기능 분석

- **CRISPR-Cas9 SLC7A11 녹아웃:** 세포 증식, colony formation
- **Erastin/SAS (ferroptosis 유발):** 민감도 변화
- **GSH/GSSG 비율:** oxidative stress 측정
- ** lipid ROS:** C11-BODIPY染色

#### 3.2.3 분자 기전

- **Western blot:** SLC7A11, GPX4, NRF2, KEAP1
- **RT-qPCR:** SLC7A11, ATF4, CHAC1
- ** reporter assay:** NRF2 transactivation
- **ChIP-seq:** ATF4 binding sites

**예상 결과:**
- SLC7A11 녹아웃 → ferroptosis 증가
- KEAP1 변이 세포에서 SLC7A11 의존성 증가
- NRF2 경로 활성화 확인

---

### 3.3 Aim 3: PROTAC 개발

#### 3.3.1 분자 설계

**Targeting moiety:** SLC7A11 억제제 (erastin 유도체 또는 covalant 억제제)

**E3 ligase recruiter:** VHL 또는 CRBN 리간드

**Linker:** PEG계 列 (2-4 단위)

#### 3.3.2 합성 및 평가

| 단계 | 내용 |
|------|------|
| **합성** | 20개 이상 PROTAC 유사체 합성 |
| **활성측정** | SLC7A11 억제活性 (cystine 흡수 측정) |
| **접합효율** | BRD4 degradation assay (대조군) |
| **ADMET** | microsome 안정성, CYP 억제 |
| **효능** | cell viability (MTT/WST-1) |

**예상 결과:**
- First-in-class SLC7A11 PROTAC
- nM 단위 활성
- 선택적 degradation

---

### 3.4 Aim 4: 전임상 검증

#### 3.4.1 종양 이식 모델

- **CDX (cell derived xenograft):** A549, H1979
- **PDX (patient derived xenograft):** 3-5 종류
- **KEAP1 변이 동형 모델:** Genetically engineered mice

#### 3.4.2 효능 평가

| 검사항목 | 방법 |
|---------|------|
| **종양 성장** | caliper 측정 (volume) |
| **조직학적 분석** | Ki-67, TUNEL, IHC |
| **생존율** | 전체 생존기간 |
| **안전성** | 체중, 장기 무게, 조직학 |
| **biomarker** | plasma GSH, lipid ROS |

#### 3.4.3 약동학

- **PK/PD:** AUC, Cmax, half-life
- **tumor distribution:** LC-MS/MS
- **최적 용량:** dose-response curve

---

## 예상 결과 및 의의

### 4.1 예상 결과

1. **SLC7A11이 NSCLC의 예후因子로 확립**
2. **KEAP1 변이가 SLC7A11 의존성을 예측하는 biomarker로 확인**
3. **First-in-class SLC7A11 PROTAC 개발**
4. **폐암 치료를 위한 새로운 치료 전략 제시**

### 4.2 임상적 의의

| 항목 | 내용 |
|------|------|
| **임상적 필요성** | 불응성/불치성 NSCLC에 새로운 치료 옵션 제공 |
| **과학적 혁신성** | ferroptosis 기반 first-in-class 치료제 |
| **시장 잠재력** | $3B 이상 폐암 시장 |

---

## 연구 일정표

```
        M1   M3   M6   M9   M12  M15  M18  M21  M24
Aim 1   [====][====]         
Aim 2         [====][====]
Aim 3               [====][====][====]
Aim 4                           [====][====][====]
```

---

## 예산 (예상)

| 항목 | 비용 ($) |
|------|----------|
| 인건비 | 500,000 |
| 시약 및 소모품 | 800,000 |
| 세포주/동물 모델 | 400,000 |
| 분석 기기 사용료 | 300,000 |
| 합성外包 | 500,000 |
| 간접비 | 500,000 |
| **총계** | **3,000,000** |

---

## 참고 문헌

1. Conrad M, et al. (2018). Ferroptosis in cancer. Cell.
2. Liu T, et al. (2024). SLC7A11 in cancer. Cancer Cell.
3. Koppula P, et al. (2023). System Xc- as therapeutic target. Nat Rev Cancer.
4. TCGA Research Network. Lung adenocarcinoma papers.

---

## 부록: 선행 데이터

Generated figures 참조:
- `tcga_survival_analysis.png` - TCGA 생존 분석
- `geo_transcriptome_analysis.png` - GEO 발현 분석
- `ferroptosis_network_volcano.png` - Ferroptosis 유전자 네트워크
- `keap1_nrf2_correlation.png` - KEAP1/NRF2 상관관계

Raw data 참조:
- `data/tcga_slc7a11_expression.csv`
- `data/geo_transcriptome_slc7a11.csv`
- `data/ferroptosis_network.csv`
- `data/keap1_nrf2_correlation.csv`

---

*본 연구계획서는 SLC7A11 폐암 연구 프로젝트용으로 생성됨*
