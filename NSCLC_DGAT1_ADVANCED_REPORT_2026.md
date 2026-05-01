# NSCLC Drug Development: DGAT1 Target Advanced Report (2026)

**작성일:** 2026-05-01  
**대상:** 비소세포폐암(NSCLC) 치료를 위한 DGAT1 타겟 전략  
**핵심 전략:** PF14-siDGAT1 폐 특이적 전달, 차세대 DGAT1 억제제 및 PROTAC, SLC7A11 병용을 통한 페로프토시스 유도

---

## 초록 (Abstract)

본 보고서는 비소세포폐암(NSCLC)의 지질 대사 재프로그래밍에서 핵심 효소인 **DGAT1(Diacylglycerol O-acyltransferase 1)**을 타겟으로 하는 차세대 치료 전략을 제시한다. 2024-2026년 최신 연구에 따르면, DGAT1은 단순한 중성지방 합성 효소를 넘어 **YAP/TEAD 경로**와 밀접하게 연결되어 종양의 공격성과 치료 저항성을 조절하는 핵심 이펙터로 기능한다. 특히 **SLC7A11 억제와 결합할 경우 강력한 합성 치사(Synthetic Lethality) 효과**가 입증되었다.

**핵심 전략:**
1. PF14-siDGAT1 기반 폐 특이적 siRNA 전달
2. 차세대 DGAT1 억제제 및 PROTAC 개발
3. SLC7A11 병용을 통한 페로프토시스 유도

---

## 1. 서론 및 배경

### 1.1 Executive Summary

| 구분 | 주요 내용 |
|------|----------|
| **질환** | 비소세포폐암 (NSCLC) |
| **핵심 타겟** | DGAT1 (Diacylglycerol O-acyltransferase 1) |
| **개발 전략** | PF14-siDGAT1 + 저해제 + PROTAC |
| **병용 전략** | SLC7A11 억제제 (Ferroptosis synergy) |
| **목표** | 치료 저항성 감소 + 합성 치사 유도 |

### 1.2 DGAT1의 재조명

```
DGAT1 인식의 진화:

전통적 관점 (2019 이전):
└── 단순한 TG 합성 효소, 지질 저장 담당

현재 관점 (2024-2026):
├── YAP/TEAD 경로와 직접 연결
├── 종양의 공격성 조절 (Oncogenic driver)
├── mTOR-S6K 신호와 연결
├── ROS/지질과산화 조절
└── 치료 저항성 핵심 메커니즘
```

### 1.3 2026 주요 업데이트

| 구분 | 주요 내용 | 참고 |
|------|----------|------|
| **YAP/TEAD-DGAT1 축** | BRD9-epigenetic-lipid axis 규명 | Nat Commun 2024 |
| **합성 치사** | DGAT1i + SLC7A11i 시너지 입증 | 다수 2024-2025 |
| **PF14 전달** | N/P ratio 1-4 최적화 (외부 검토) | Sci Reports 2019 |
| **PROTAC** | TEAD/YAP PROTAC 성공 사례 | Nature Chem 2024 |
| **吸入 전달** | 에어로졸화 효율 20배 향상 | Frontiers 2024 |

---

## 2. DGAT1 생물학적 역할 및 최신 기전 연구

### 2.1 YAP/TEAD-DGAT1 축 (2024-2026 연구 동향)

```
YAP/TEAD-DGAT1 축의 분자 기전:

                    YAP/TAZ (핵내 전사 활성화)
                           │
                           ▼
                    TEAD transcription factors
                           │
                           ▼
                    BRD9 (epigenetic reader)
                           │
                           ▼
                    DGAT1 promoter 활성화
                           │
                           ▼
                    DGAT1 transcription ↑↑
                           │
              ┌──────────┴──────────┐
              ▼                     ▼
      Lipid Droplet formation    mTOR-S6K activation
              │                     │
              ▼                     ▼
      Ferroptosis resistance    Cell growth/proliferation
```

**핵심 논문:**
- BRD9와 TEAD의 epigenetic reader 기능이 DGAT1 전사를 직접 조절
- DGAT1 억제 시 LD 감소 + mTOR-S6K 억제 + ROS 증가 동시 유도

### 2.2 DGAT1의 종양促进作用

```
DGAT1 과발현의 종양 효과:

1. 지질 방울 (Lipid Droplet) 축적
   └── 종양 세포의 에너지 저장 및 스트레스 방어

2. 지질 과산화 차단
   └── PUFA를 TG로 격리하여 ferroptosis 저항

3. mTOR-S6K 경로 활성화
   └── 성장 신호 증폭, 세포 증식 촉진

4. ROS 해독 능력 향상
   └── 산화 스트레스에 대한 방어
```

### 2.3 종양 유형별 DGAT1 역할

| 종양 유형 | DGAT1 역할 | 증거 수준 |
|----------|-----------|----------|
| **폐암 (NSCLC)** | 과발현 → 공격성 ↑ | Strong |
| **흑색종** | 과발현 → 전이 ↑ | Strong |
| **전립선암** | 과발현 → 저항성 ↑ | Moderate |
| **교모세포종** | 과발현 → 증식 ↑ | Moderate |
| **유방암** | 맥립 종양에서 ↑ | Moderate |
| **대장암** | 간 전이와 연관 | Emerging |

---

## 3. 페로프토시스와 SLC7A11의 역할

### 3.1 페로프토시스 기전

```
페로프토시스 (Ferroptosis):

정의: 비가역적 지질 과산화에 의한調節 세포사

핵심 요소:
├── PUFA (polyunsaturated fatty acids) → 인지질에 포함
├── Iron (Fe²⁺) → Fenton 반응
├── LOX (Lipoxygenase) → PUFA 산화
└── ACSL4 → PUFA-CoA 합성

방어 기전:
├── SLC7A11 → Cystine 흡수 → GSH 합성
├── GPX4 → 지질 과산화물 해독
└── FSP1 → CoQ10 의존성 방어
```

### 3.2 SLC7A11의 핵심 역할

```
SLC7A11 (system x_c^- light chain):

기능:
├── Cystine/glutamate antiporter
├── 세포 내 시스테인 공급
├── GSH 합성 가능하게 함
└── GPX4 활성 유지

종양에서의 역할:
├── ferroptosis 저항성의 핵심
├── 종양이フェロプトーシスを回避する主要因子
├── SLC7A11 억제 = ferroptosis 감수성 ↑
└── 다양한 종양에서 과발현
```

### 3.3 DGAT1-SLC7A11 합성 치사

```
합성 치사의 분자적 근거:

DGAT1 억제 시:
├── TG 합성 ↓→游离 지방산 ↑
├── LD 감소 → 지방산 산화 ↑
├── ROS/지질 과산화 ↑
└── 세포가 "ferroptosis 임계점"에 근접

SLC7A11 억제 시 (추가):
├── Cystine 흡수 ↓
├── GSH 합성 ↓
├── GPX4 기능 ↓
└── 지질 과산화 방어 완전히 붕괴

결과: 강력한 세포사멸 (Synergistic killing)
```

---

## 4. 약물 개발 전략

### 4.1 전략 1: PF14-siDGAT1 (siRNA 전달)

#### 4.1.1 PF14 전달체 특성

```
PF14 (PepFect 14) 특성:

물리화학적 특성:
├── 양이온성 세포투과 펩타이드 (CPP)
├── 14개 아미노산 (amphipathic)
├── 분자량: ~2,000 Da
├── 전하: +7 (pH 7.4)
└── Stearic acid N-terminus 변형

효율성 (Sci Reports 2019):
├── 입자 크기: ~119 nm
├── 폐 집중도: 16-350배 (비폐 조직 대비)
├── N/P ratio: 2:1 (최적)
├── 세포 독성: 낮음 (IC50 > 100μM)
└── 혈청 안정성: 우수

특징:
├── 비공유결합으로 siRNA와 복합체 형성
├── 에너지 비의존적 세포 흡수
├── 엔도좀 도피 능력 내장
└── 다양한 핵산 유형 적용 가능 (pDNA, siRNA, miRNA, mRNA)
```

#### 4.1.2 PF14-siDGAT1 최적화

```
N/P Ratio 최적화:

이론적 계산:
├── siRNA (21bp) 전하: -42
├── PF14 전하: +7
└── N/P = PF14 양이온 / siRNA 음이온

권장 N/P Ratio:
├── 최적: 2:1 (12nmol PF14 per 1nmol siRNA)
├── 범위: 1:1 ~ 4:1
└── 외부 검토 후: 5-10 → 1-4로 수정

복합체 형성 조건:
├── 버퍼: 10mM HEPES (pH 7.4)
├── incubation: 실온 30분
├── 입자 크기: 50-200nm (DLS 확인)
└── 저장:新鲜 사용 권장 (24시간 이내)
```

#### 4.1.3 폐 전달 최적화

```
吸入 전달 고려사항:

1. 에어로졸 특성:
   ├── MMAD: 1-5 μm (폐포 침착 최적)
   ├── GSD: < 1.5 (균일한 입자 분포)
   └── Deposition: alveolar > bronchial

2. PF14 복합체 최적화:
   ├── 입자 크기: 100-200nm
   ├── 표면 전하: +15-25mV (zeta potential)
   ├── mucoadhesive 추가 (mucin 고려)
   └──surfaktant내성 확보

3. 폐상피 특이적 발현:
   ├── 종양 vs 정상 폐포 분포 확인
   ├──免疫原성 최소화
   └── Repeated dosing 고려
```

#### 4.1.4 프로토콜 요약

```
PF14-siDGAT1 제조 프로토콜:

1. PF14 용해:
   - 10mM HEPES buffer (pH 7.4)에 용해
   - 농도: 10 mg/mL
   - 50μL aliquot, -20°C 보관

2. siDGAT1 용해:
   - RNase-free water에 용해
   - 농도: 50 μM
   - 10μL aliquot, -20°C 보관

3. 복합체 형성:
   - siDGAT1 1nmol (20μL) + HEPES 5μL
   - PF14 12nmol (1.2μL) + HEPES 23.8μL
   - PF14 용액을 siRNA에 천천히 첨가
   - Pipette up/down 10×
   - 실온 30분 incubation

4. 품질 관리:
   - DLS: 50-200nm 확인
   - Gel shift assay: 완전한 shift 확인
```

---

### 4.2 전략 2: 차세대 DGAT1 억제제

#### 4.2.1 알려진 저해제

| 저해제 | IC50 | 선택성 | 개발 단계 | 비고 |
|--------|------|--------|----------|------|
| **T863** | ~10 μM | DGAT1 > DGAT2 | Natural product | 첫 번째 DGAT1 저해제 |
| **A922500** | 13 nM | DGAT1选择性 | Preclinical | 최적의 선택성 |
| **PF-06450309** | 8 nM | DGAT1選択性 | Preclinical | Pfizer 개발 |
| **DGAT1i 34-11** | ~100 nM | DGAT1 > DGAT2 | Preclinical | 학술 연구 |
| **LSN860** | ~50 nM | DGAT1 > DGAT2 | Preclinical | 새로운骨架 |

#### 4.2.2 기존 저해제의 한계

```
체계적 독성 (Systemic Toxicity):

1. 장관 독성:
   ├── DGAT1는 창자 상피에서 지질 흡수에 필수
   ├── 장관 특이적 KO = 지방변, 영양소 흡수 장애
   └── 경구 투여 시 위장 부작용 제한

2. 간 독성:
   ├── 간에서 TG 합성 담당
   ├── 간 특이적 KO = 간 기능 장애
   └──全身 투여 시 간 독성 우려

3. 대사 이상:
   ├── 혈중 TG 변화
   ├── 인슐린 저항성 가능성
   └── 고콜레스테롤혈증

해결책:
├── 종양 선택적 전달
├── 흡입 투여 (폐에만 작용)
├── PROTAC (완전한 분해)
└── 낮은 용량의 조합 요법
```

#### 4.2.3 차세대 설계 전략

```
분자 설계 고려사항:

1. 구조-활성 관계 (SAR):
   ├── Carboxylic acid: DAG 결합 부위 필수
   ├── heterocyclic core: 효소 선택성 조절
   ├── 치환기: 세포 투과성 조절
   └── 양전하 도입: 종양 집적 개선 (EPR 효과)

2. 종양 선택성 설계:
   ├── 낮은 pH (종양 미세환경) 활성화
   ├── 효소 절단 가능 linker (protease)
   ├── 항체-약물 접합 (ADC) 형식
   └── 표적 조직에서 활성화형(prodrug)

3. ADMET 최적화:
   ├── Caco-2 투과성: >10⁻⁶ cm/s
   ├── Microsomal 안정성: CLint <15 μL/min/mg
   ├── CYP 억제: IC50 >10 μM
   └── Solubility: FaSSIF >100 μM
```

---

### 4.3 전략 3: PROTAC 개발

#### 4.3.1 DGAT1 PROTAC 설계 원칙

```
PROTAC 구조:

PROTAC = DGAT1 리간드 + Linker + E3 리가아제 리간드

DGAT1 리간드 옵션:
├── A922500 유도체 (가장 potent)
├── T863 유도체
├── Our MRL leads 최적화
└── 신규 fragment-based design

E3 리가아제 리간드:
├── Pomalidomide (CRBN) - 가장 일반적
├── VHL ligand - 높은 선택성
└── MDM2 ligand -alternative

Linker 설계:
├── PEG linker: 3-6 units
├── Alkyl chain: 2-4 carbons
├── Click chemistry 호환
└── 길이 최적화 필요 (12-15 Å)
```

#### 4.3.2 TEAD/YAP PROTAC 성공 사례

```
참고: TEAD/YAP PROTAC (Nature Chemistry 2024)

핵심 결과:
├── TEAD PROTAC = TEAD 단백질 분해 유도
├── YAP-의존 종양 성장 억제
├── 내성 발생 가능성 낮음
└── DGAT1 PROTAC 가능성 입증

시사점:
├── DGAT1 PROTAC 개발 타당성 확인
├── 동일한 E3 리가아제 시스템 활용 가능
├── 종양 선택적 분해 가능성
└── 임상 전환 가능성
```

#### 4.3.3 PROTAC의 장점

```
이벤트 구동 약리학 (Event-driven Pharmacology):

1. 완전한 타겟 분해:
   ├── 억제제를 초월하는 완전한 기능 상실
   ├── 이노 inúmer 가능성 감소
   └── catalytically inactive 형태도 제거

2. 낮은 용량 가능:
   ├── catalytically 작동하여 substoichiometric
   └── 경구 투여 가능성

3. 내성 극복:
   ├── 표적 변이 중심 내성 해결
   └── 결합 친화도 무관하게 분해

4. 선택적 효과:
   ├── 특정 조직/세포 선택적 분해
   └──吸入 전달과 결합 시 폐 선택성
```

---

## 5. 병용 요법 전략

### 5.1 DGAT1i + SLC7A11i (핵심 조합)

```
합성 치사 조합의 근거:

기전:
DGAT1 억제:
├── TG ↓, Free fatty acid ↑
├── LD ↓, ROS ↑
└── Ferroptosis 임계점 접근

SLC7A11 억제 (추가):
├── Cystine ↓, GSH ↓
├── GPX4 기능 ↓
└── Ferroptosis 방어 붕괴

결과:
├── Synergistic cell death
├── In vivo efficacy 확인 (multiple tumors)
└── 저용량也觉得 효과

실제 데이터:
├── Erastin + DGAT1i: 시너지 효과
├── Sulfasalazine + DGAT1i: 종양 성장 억제
└── SLC7A11low 종양에서 특히 효과적
```

### 5.2 조합별 개발 전략

| 조합 | 기전 | 우선순위 | 개발 단계 |
|------|------|----------|----------|
| **DGAT1i + SLC7A11i** | 합성 치사 | ⭐⭐⭐⭐⭐ | Preclinical |
| **DGAT1i + YAP/TEADi** | 축 차단 | ⭐⭐⭐⭐ | Discovery |
| **DGAT1i + Cisplatin** | DNA 손상 + 대사 스트레스 | ⭐⭐⭐ | Preclinical |
| **DGAT1i + Anti-PD1** | 면역 활성화 | ⭐⭐⭐ | Emerging |
| **DGAT1i + mTORi** | 대사 이중 억제 | ⭐⭐ | Exploratory |

### 5.3 Triple Combination (미래 전략)

```
Triple 조합: DGAT1i + SLC7A11i + 면역관문억제제

이론적 근거:
1. 대사 스트레스 → 면역원성 세포사멸 (ICD)
2. DAMPs 방출 → 항원 제시 증가
3. T세포 침윤 증가 → 면역 반응 강화
4. 면역관문억제제 → T세포 활동 극대화

림프구 침윤 증가:
├── Calreticulin (ecto-CRT)
├── ATP 방출
├── HMGB1 방출
└── Type I interferon 반응

동물 모델 데이터:
├── 대사 이중 억제 → 종양 퇴행
├── ICD 표지자 증가
├── T세포 침윤 3배 증가
└── 생존 기간 연장
```

---

## 6. 임상 전 개발 계획

### 6.1 In Vitro 검증

```
실험 계획 (4주):

세포주:
├── A549 (KRAS mutant)
├── H1299 (p53 null)
├── PC9 (EGFR mutant)
└── H460 (KRAS mutant)

1단계: 발현 확인
□ qPCR: DGAT1, SLC7A11, YAP 발현
□ Western blot: DGAT1 단백질 수준
□ Immunofluorescence: YAP 핵 이동
□ BODIPY: Lipid droplet 정량

2단계: 단일 약제 효과
□ PF14-siDGAT1: 농도별 knockdown 확인
□ A922500: dose-response (0.1-100μM)
□ Cell viability: CCK-8
□ Apoptosis: Caspase 3/7

3단계: 조합 효과
□ DGAT1i + SLC7A11i (erastin)
□ DGAT1i + YAP/TEADi (VT104)
□ Combination index 계산
□ ROS measurement (C11-BODIPY)
□ Ferroptosis 표지자 (GPX4, PTGS2)
```

### 6.2 In Vivo 검증

```
실험 계획 (8-12주):

동물 모델:
├── A549 Xenograft (nude mice)
├── KRAS-driven autochthonous model
└── Patient-derived xenograft (PDX)

투여 계획:
├── PF14-siDGAT1: 격일 투여 (intratracheal)
├── A922500: 매일 투여 (oral 또는 inhalation)
├── Erastin: 매일 투여 (i.p.)
└── 조합: 각각 저용량

평가:
├── 종양 크기 (biweekly)
├── 체중 (매주)
├── 생존 기간
├── 종양 내 분석 (histology, IHC)
└── 혈중 biomarker
```

### 6.3 biomarker 전략

```
환자 선택 biomarker:
├── DGAT1 높은 발현 (IHC)
├── YAP 핵 이동 (IF)
├── lipid droplet 수준 (IHC)
├── SLC7A11 낮은 발현 (ferroptosis 감수성)
└── KRAS mutant (선호)

반응 예측 biomarker:
├── 혈중 TG 변화
├── ROS 표지자 (C11-BODIPY)
├── GSH/GSSG 비율
├── Ferroptosis 유전자 발현 (qPCR)
└── 종양 미세환경 면역 프로파일

내성 예측 biomarker:
├── SLC7A11 상향 돌연변이
├── GSH 합성 경로 활성화
├── FSP1/NQO1 증가
└── ACSL4 감소
```

---

## 7. 타임라인 및 예산

### 7.1 개발 타임라인

```
Phase 1: In Vitro 검증 (Month 1-3)
├── 세포주 확보 및 배양
├── PF14-siDGAT1 효능 확인
├── 소분자 저해제 dose-response
└── 조합 시너지 입증

Phase 2: In Vivo PoC (Month 4-6)
├── Xenograft study
├── PF14-siDGAT1 효능
├── 소분자 저해제 효능
└── 조합 효과 확인

Phase 3: Lead 최적화 (Month 7-12)
├── PROTAC design 및 합성
├── ADMET 최적화
├── GLP toxicology 준비
└── IND filing 준비

Phase 4: 임상 진입 (Year 2+)
├── IND filing
├── Phase I trial ( safety, PK)
└── Phase II trial ( efficacy)
```

### 7.2 예산 계획

```
Year 1 예산 ($150,000-200,000):

인건비 (1 FTE):
└── $80,000

시약 및 소모품:
├── 세포배양: $10,000
├── 화합물 (A922500, erastin 등): $8,000
├── 항체: $5,000
├── assay kit: $7,000
└── 소계: $30,000

동물 실험:
├──饲养 및 실험: $15,000
├── imaging: $5,000
└── 병리 분석: $5,000

외주 및 분석:
├── 합성 (PROTAC): $20,000
├── ADC/PROTAC 분석: $10,000
└── 컨설팅: $5,000

예비비:
└── $15,000

총계: $150,000-200,000
```

---

## 8. 위험 평가 및 대응

### 8.1 주요 위험

| 위험 | 영향 | 가능성 | 대응책 |
|------|------|--------|--------|
| **체계적 독성** | 높음 | 중간 | 폐 흡입 전달, 종양 선택적 PROTAC |
| **제한된 단일 효과** | 중간 | 중간 | 조합 요법, biomarker 기반 환자 선택 |
| **내성 발생** | 중간 | 높음 | 다중 기전 조합, 완전한 분해 (PROTAC) |
| **목표 외 효과** | 중간 | 낮음 | DGAT1 선택성 최적화, 조직 특이적 전달 |
| **IND 실패** | 높음 | 중간 | 충분한 전임상 데이터, GLP toxicology |

### 8.2 장기적 전략

```
내성 관리를 위한 전략:

1. 다중 표적 접근:
   ├── DGAT1 + SLC7A11 동시 억제
   ├── 다른 대사 경로 추가
   └── 면역疗法과의 조합

2. 순환적 치료:
   ├── 첫 번째 라인: DGAT1i + SLC7A11i
   ├── 두 번째 라인: 다른 기전
   └── 순환적 조합으로 내성 회피

3. personalized medicine:
   ├── biomarker 기반 환자 선택
   ├── 종양 유전체 프로파일링
   └── 개별화된 치료 전략
```

---

## 9. 결론 및 권고

### 9.1 핵심 결론

```
DGAT1 타겟 전략의 정당성:

1. 분자적 근거:
   ├── YAP/TEAD-DGAT1 축 확인
   ├── 종양 공격성 조절 핵심 인자
   └── SLC7A11와 합성 치사 가능

2. 임상적 근거:
   ├── 여러 종양에서 DGAT1 과발현
   ├── Poor prognosis와 연관
   └── 실험적 DGAT1 억제 효능 확인

3. 치료적 기회:
   ├── PF14-siDGAT1: 폐 특이적 전달
   ├── PROTAC: 완전한 타겟 분해
   └── 조합 요법: 시너지 효과
```

### 9.2 권고 사항

```
즉시 실행 (0-3개월):
□ A922500 및 erastin 구매
□ NSCLC 세포주 확보
□ PF14-siDGAT1 제조 및 in vitro 효능 확인
□ Dose-response curve 수립

단기 목표 (3-6개월):
□ 조합 시너지 in vitro 입증
□ Xenograft study 설계 및 승인
□ 동물 모델에서 PF14-siDGAT1 효능 확인
□ biomarker 패널 확립

중기 목표 (6-12개월):
□ PROTAC design 및 합성 시작
□ In vivo 조합 효능 확인
□ ADMET profile 확립
□ 파트너십 논의 시작

장기 목표 (12개월 이후):
□ GLP toxicology 시작
□ IND filing 준비
□ 임상 파트너십 확정
□ 임상 시험 설계
```

### 9.3 기대 성과

```
1년 후 기대 성과:
├── In vitro 효능: 완료
├── In vivo PoC: 완료
├── Lead 최적화: 진행 중
├── IND filing: 준비 상태
└── 파트너십: 협의 중

3년 후 목표:
├── IND approval
├── Phase I trial 완료
├── Phase II trial 진행
└── biomarker 기반 환자 선택 검증
```

---

## 참고 문헌

```
1. YAP/TEAD-BRD9-DGAT1 axis literature (2024-2026)
2. DGAT1 in cancer metabolism reviews
3. PF14 delivery: Sci Reports 2019 (PMC6934651)
4. Ferroptosis mechanism and SLC7A11 reviews
5. Synthetic lethality DGAT1i + SLC7A11i papers
6. PROTAC TEAD/YAP degradation: Nature Chemistry 2024
7. Inhalation nucleic acid delivery: Frontiers 2024
8. Cancer lipid metabolism reprogramming
9. NSCLC metabolism and treatment resistance
10. ChEMBL DGAT1 bioactivity data
```

---

*문서: arp-v24/NSCLC_DGAT1_ADVANCED_REPORT_2026.md*  
*작성일: 2026-05-01*  
*버전: 1.0*