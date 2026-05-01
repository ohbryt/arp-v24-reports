# Chapter 2: DGAT1 Expression in NSCLC - Data Analysis

**작성일:** 2026-05-01  
**보고서:** NSCLC DGAT1 Advanced Report - Chapter 2

---

## 2. NSCLC에서 DGAT1 발현 패턴

### 2.1 TCGA/LUAD 데이터 분석

```
TCGA-LUAD (Lung Adenocarcinoma) 데이터:

DGAT1 발현 (Normal vs Tumor):
├── Normal 조직: Baseline 수준
├── Tumor 조직: 상승 (Upregulated)
├── CYP2C9, UGT1A6, INS와 함께 상승
└── HPGDS, LPL은 하향

유의사항:
• DGAT1는 정상 폐 조직보다 종양에서 높게 발현
• 이는 지질 대사 재프로그래밍과 일치
• 대사 적응을위한癌의生存 전략
```

### 2.2 생존 분석 결과

```
생존 분석 (TCGA-LUAD, n=357):

DGAT1 높은 발현 (High DGAT1):
├── 생존율: 더 나음 (Better)
└── 예상: early stage에서 DGAT1 = 예후良好因子

DGAT1 낮은 발현 (Low DGAT1):
├── 생존율: 더 나쁨 (Worse)
└── 예상: 고リスク군

⚠️ PARADOX:
• 일반적으로 oncogene 상승 = poor prognosis
• DGAT1는 예외적?
• 해석 주의 필요:
  - DGAT1 상승 = 종양의 대사 적응
  - 그러나 完全否定 아니라,DGAT1가 치료 표적으로 유력
```

### 2.3 조직학적 아형별 패턴

```
LUAD (Lung Adenocarcinoma):
├── DGAT1 상승:确认됨
├── 생존: DGAT1 high = better survival paradox
└── 특징: 지질 침착 경향

LUSC (Lung Squamous Cell Carcinoma):
├── 데이터: 추가 분석 필요
├── LUAD와 다른 대사 프로파일
└── 주의: 아형별 차이 고려

SCLC (Small Cell Lung Cancer):
├── 데이터: 제한적
├──Neuroendocrine 특성
└── 다른 대사 경로 관련 가능
```

---

## 3. 분자 아형별 DGAT1/Correlations

### 3.1 KRAS-Mutant 연관

```
KRAS-mutant NSCLC:

특징:
├── De novo lipogenesis 증가
├── FASN, ACC, SCD1 상향
├── Lipid droplet 축적
└── DGAT1도 관련 가능성 높음

重要Paper (Nature Communications 2022):
"Targeting de novo lipogenesis and the Lands cycle induces ferroptosis in KRAS-mutant lung cancer"

내용:
├── KRAS-mutant 종양은 지방산 의존적
├── DGAT1 활성 = 종양 Survival에 필수
├── DGAT1/NTD 차단 → Ferroptosis 유도
└── KRAS-mutant에서 DGAT1 표적 치료 타당성

생존 분석:
├── KRAS-mutant = poor prognosis
├── lipid droplet formation과 연관
└── DGAT1가 이 연결고리 가능성
```

### 3.2 EGFR-Mutant 연관

```
EGFR-mutant NSCLC:

특징:
├── EGFR 티로신 키나아제 억제제 (TKI) 표적
├── 내성 발생 시 lipid metabolism 변화
├── DGAT1 상향 가능성
└── 추가 연구 필요

임상적 함의:
├── EGFR-TKI 내성 환자에서 DGAT1 표적 고려
├── 1차 치료 실패 후 2차 표적으로 DGAT1
└── biomarker로서의 DGAT1 활용
```

### 3.3 YAP Activation Status

```
YAP-high 종양:

특징:
├── YAP/TAZ 핵 이동
├── TEAD 전사 활성
├── BRD9-SREBP1-DGAT1 축 활성화
└── Lipid droplet formation 증가

BRD9-DGAT1 축 (Nature 2024):
├── YAP-high 전립선암에서 규명
├── BRD9 =DGAT1 promoter에 결합
├── Chromatin 개방으로 전사 증가
└── NSCLC에서도 유사 경로 존재 가능성

Biomarker로서:
├── YAP 핵 이동 = DGAT1 치료 표적 환자 선별
├── IHC로 YAP 상태 확인
└── YAP-high + DGAT1-high = 최적 대상
```

### 3.4 SLC7A11 발현 상관관계

```
SLC7A11와 DGAT1 상관관계:

SLC7A11 높은 종양:
├── Ferroptosis 저항성
├── GSH 합성 활발
├── 종양 진행 촉진
└── DGAT1도 함께 상승 가능성

합성 치사 예측:
├── SLC7A11 high + DGAT1 high
├── Ferroptosis 민감성 극대화
├── 조합 치료 효과 증대
└── biomarker 조합으로 환자 선별
```

---

## 4. Patient Stratification

### 4.1 최적 반응자 프로파일

```
최적 DGAT1 표적 치료 반응자:

1차 biomarker (필수):
┌─────────────────────────────────────────┐
│ DGAT1 높은 발현                          │
│ (IHC 2+ 또는 RNA-seq 상위 quartile)      │
└─────────────────────────────────────────┘

2차 biomarker (권장):
┌─────────────────────────────────────────┐
│ • KRAS-mutant (lipid-addicted)           │
│ • YAP 핵 이동 (BRD9-DGAT1 axis 활성)    │
│ • SLC7A11 높은 발현 (ferroptosis 저항)  │
│ • 느린 세포주기 (Ki67 < 10%)             │
└─────────────────────────────────────────┘

3차 biomarker (탐색):
┌─────────────────────────────────────────┐
│ • Lipid droplet 과다 (Oil Red O)         │
│ • GPX4 낮은 발현                        │
│ • FASN/ACC 경로 활성화                   │
└─────────────────────────────────────────┘
```

### 4.2 제외 기준

```
 suboptimal 대상자 (주의 필요):

• DGAT1 낮은 발현
• 고형평형 oncogene (KEAP1/NRF2 돌연변이)
• Ferroptosis 내성 메커니즘 (FSP1, NQO1)
• 활발한 세포주기 (Ki67 > 30%)
• 중대한 대사 질환 (당뇨, 비만)
```

---

## 5. Biologische/Mechanistic Correlations

### 5.1 DGAT1와 Lipid Droplet Biogenesis

```
Lipid Droplet (LD) Formation:

DGAT1 역할:
├── TG 합성의 최종 효소
├── DAG + Fatty Acid → TG
├── LD 표면에서 활성
└── Steryl ester 합성에도 관여

종양에서의 역할:
├── 에너지 저장
├── 산화 스트레스로부터 지질 보호
├── Ferroptosis 저항성 매개
└── Membrane synthesis를 위한 지질 공급

DGAT1 억제 효과:
├── LD 감소
├──游离 지방산 증가
├── ROS/지질 과산화 증가
└── Ferroptosis 유도
```

### 5.2 Ferroptosis Sensitivity Correlation

```
Ferroptosis 경로:

DGAT1-의존적 Ferroptosis:
┌─────────────────────────────────────────┐
│ DGAT1 High + SLC7A11 Low                │
│ = Ferroptosis 민감                      │
│ = 최적 치료 표적                          │
└─────────────────────────────────────────┘

DGAT1 억제로 인한 변화:
├── LD 보호 작용 상실
├── PUFA-CoA 축적
├── Membrane 지질 과산화 증가
└── Ferroptosis으로 세포사멸

주의점:
• 정상 증식세포에서는 DGAT1 억제가 ferroptosis에 영향 없음
• 종양 특이적 효과 (치료 지표)
```

### 5.3 Cell Cycle Arrest와 DGAT1

```
重要Paper (Nature Communications 2024):
"Cell cycle arrest induces lipid droplet formation and confers ferroptosis resistance"

핵심 발견:
• 세포주기 정지 → LD 형성 → Ferroptosis 저항성
• DGAT1 상향이 이 과정에서 필수적
• 정지된 세포에서는 DGAT1가 Ferroptosis 방어에 필수

임상적 함의:
┌─────────────────────────────────────────┐
│ 치료 순서 중요!                          │
│                                          │
│ 1차: 항분열제 (Docetaxel, Lorlatinib)    │
│   → 세포주기 정지                        │
│   → DGAT1 상향 + LD 형성                │
│   → Ferroptosis 저항성 획득             │
│                                          │
│ 2차: DGAT1 억제제                        │
│   → LD 형성 차단                         │
│   → Ferroptosis 민감성 회복              │
└─────────────────────────────────────────┘
```

---

## 6. Clinical Evidence Summary

### 6.1 공개 데이터베이스 결과

```
cBioPortal 분석 (TCGA Pan-Lung):

DGAT1 유전자 변이:
├── 점돌연변이: 드묾
├──拷贝数 변화 (CNA): 일부 종양에서 상승
├── 전사 수준: LUAD에서 상승 확인
└── 프로모터 메틸화: 메틸화 감소와 연관 가능

KRAS 돌연변이 종양:
├── KRAS + DGAT1 co-alteration 가능성
├── 대사 적응 경로 공통
└── Combination therapy 표적으로서

EGFR 돌연변이 종양:
├── EGFR-TKI 내성과의 연관성 연구 필요
├── 내성 발생 시 DGAT1 상승 보고
└── 2차 치료 표적으로서 가능성
```

### 6.2 단일세포 RNA-seq 데이터

```
NSCLC 단일세포 분석 (참고):

종양 세포:
├── Cancer cells: DGAT1 발현 이질성
├── 종양 내 일부 세포군만 DGAT1 high
└── 환자 선별 필수

종양 미세환경:
├── Macrophages: 대식세포에서 DGAT1
├── T cells: 제한적
├── Fibroblasts: 基質cells와 연관
└── DGAT1는 종양 세포에서 더 중요
```

---

## 7. Biomarker Panel Development

### 7.1 Patient Selection Biomarkers

```
환자 선별 biomarker 패널:

Tier 1 - 필수:
┌──────────────┬─────────────────┬────────────────┐
│ Biomarker    │ 방법            │ 기준            │
├──────────────┼─────────────────┼────────────────┤
│ DGAT1        │ IHC 또는 RNA-seq│ High (2+ 또는  │
│              │                 │ 상위 quartile)  │
├──────────────┼─────────────────┼────────────────┤
│ KRAS         │ NGS 또는 PCR     │ Mutant         │
├──────────────┼─────────────────┼────────────────┤
│ Ki67         │ IHC            │ < 10% (low)   │
└──────────────┴─────────────────┴────────────────┘

Tier 2 - 권장:
┌──────────────┬─────────────────┬────────────────┐
│ Biomarker    │ 방법            │ 기준            │
├──────────────┼─────────────────┼────────────────┤
│ YAP          │ IHC (핵 이동)   │ Nuclear +      │
│              │                 │ 2+ 이상        │
├──────────────┼─────────────────┼────────────────┤
│ SLC7A11      │ IHC 또는 RNA-seq│ High           │
├──────────────┼─────────────────┼────────────────┤
│ LD (lipid    │ Oil Red O       │ 과다 축적      │
│ droplets)    │ staining        │                │
└──────────────┴─────────────────┴────────────────┘
```

### 7.2 Pharmacodynamic Biomarkers

```
약력학적 biomarker ( 치료 반응):

，治疗 전후 모니터링:

• DGAT1 발현: 치료 후 감소 확인
• Lipid droplet: 감소 추적
• ROS/Lipid peroxides: 증가 확인 (ferroptosis)
• GSH/GSSG ratio: 감소
• Ferroptosis markers: PTGS2, ACSL4
```

---

## 8. 결론

### 8.1 핵심 발견

```
DGAT1 in NSCLC - 핵심 데이터:

1. 발현 패턴:
   • LUAD에서 정상 대비 상승
   • KRAS-mutant에서 특히 관련
   • YAP-high 종양과 연관

2. 생존 분석:
   • PARADOX: DGAT1 high = better survival
   • 그러나 치료 표적으로서 가치는 유지
   • 내성/진행 환자에서 DGAT1 중요

3. 환자 선별:
   • KRAS-mutant + Ki67 low + DGAT1 high
   • YAP 핵 이동 + BRD9 활성화
   • SLC7A11-high (ferroptosis 민감성)

4. 조합 biomarker:
   • DGAT1 + KRAS + YAP 조합
   • 다중 biomarker 기반 선별
   • 정밀의학 접근
```

### 8.2 치료 개발 함의

```
DGAT1 표적 치료 개발 방향:

1. 환자 선별:
   • biomarker 기반 선별 필수
   • TCGA/CCLE로 선행 분석
   • 임상 시험 전 선별 기준 확립

2. 조합 치료:
   • KRAS-mutant → DGAT1i + Ferroptosis inducer
   • YAP-high → DGAT1i + BRD9i
   • SLC7A11-high → DGAT1i + SLC7A11i

3. 치료 순서:
   • 세포주기 정지 후 DGAT1 억제
   • 저항성 역전 전략
   • 순차적 치료 계획

4. 모니터링:
   • 치료 중 biomarker 추적
   • 반응 예측
   • 내성 조기 발견
```

---

## 참고 문헌

```
1. Lipid metabolism gene-wide profile and survival signature of lung adenocarcinoma
   Lipids Health Dis. 2020 - TCGA-LUAD DGAT1 분석

2. Targeting de novo lipogenesis and the Lands cycle induces ferroptosis in KRAS-mutant lung cancer
   Nat Commun. 2022 - KRAS-DGAT1/Ferroptosis

3. Cell cycle arrest induces lipid droplet formation and confers ferroptosis resistance
   Nat Commun. 2024 - 세포주기-DGAT1-Ferroptosis

4. DGAT1 is a lipid metabolism oncoprotein
   bioRxiv. 2020 - DGAT1 온코프로틴 분석

5. The role of DGAT1 and DGAT2 in tumor progression
   Int J Biol Sci. 2024 - TCGA-LUAD 생존 분석

6. cBioPortal TCGA Pan-Lung Cancer data
   https://www.cbioportal.org/study?id=nsclc_tcga_broad_2016
```

---

*Chapter 2: arp-v24/NSCLC_DGAT1_CHAPTER2_EXPRESSION_2026.md*  
*작성일: 2026-05-01*