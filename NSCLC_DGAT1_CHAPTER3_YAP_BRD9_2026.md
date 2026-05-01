# Chapter 3: YAP/TEAD-BRD9-DGAT1 축 (2024-2026)

**작성일:** 2026-05-01  
**보고서:** NSCLC DGAT1 Advanced Report - Chapter 3

---

## 3. YAP/TEAD-BRD9-DGAT1 Epigenetic 축

### 3.1 핵심 발견: BRD9가 중간체

```
⚠️ 중요 수정 (전문가 검토 반영):

기존 가설:
YAP/TEAD → DGAT1 직접 전사 활성화

수정된 기전:
YAP/TEAD → BRD9 → DGAT1 전사 활성화

증거 출처:
Cell Death & Disease 2026 (3주 전 발표)
"Aberrant activation of epigenetic BRD9-DGAT1 axis 
 promotes lipid droplets deposition and ferroptosis resistance 
 in YAP-high prostate cancer"
```

### 3.2 분자 기전 상세

```
YAP/TEAD-BRD9-DGAT1 축:

┌─────────────────────────────────────────────────────────┐
│ YAP (Yes-associated protein)                            │
│ ├── Hippo pathway downstream effector                   │
│ ├── 핵 이동 시 TEAD와 결합                              │
│ └── 종양 억제 신호 불응성                               │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ TEAD (TEA domain transcription factor)                  │
│ ├── YAP의 전사 파트너                                   │
│ ├── BRD9 프로모터에 결합                                │
│ └── BRD9 전사 활성화                                    │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ BRD9 (Bromodomain-containing protein 9)                 │
│ ├── SWI/SNF chromatin remodeling complex 구성원         │
│ ├── Epigenetic reader                                  │
│ ├── DGAT1 promoter에 결합                               │
│ ├── H3K4me3 및 크로마틴 접근성 증가                     │
│ └── SREBP1과 공점유 가능성                              │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ DGAT1 (Diacylglycerol O-acyltransferase 1)              │
│ ├── TG 합성 최종 효소                                   │
│ ├── Lipid droplet 생합성                                │
│ ├── Ferroptosis 저항성 매개                             │
│ └── 종양 형성 촉진                                       │
└─────────────────────────────────────────────────────────┘
```

### 3.3 BRD9의 역할

```
BRD9 (Bromodomain-containing protein 9):

기본 특성:
├── SWI/SNF chromatin remodeling complex 구성원
├── Bromodomain 보유 (acetyl-lysine 인식)
├── Epigenetic reader 기능
└── 전사 활성화/억제 조절

종양에서의 역할:
├── Enhancer-addicted 종양에서 핵심
├── 전립선암에서 dependency 확인
├── YAP-high 종양에서 특히 중요
└── DGAT1 전사에 필수적

약물 표적으로서:
├── BRD9 저해제 존재 (BI-7273, I-BRD9)
├── PROTAC degraders 개발 중
├── VT104 (YAP/TEAD 저해제)도 간접적 영향
└── DGAT1 조합 전략 가능
```

---

## 4. Lipid Droplet-Ferroptosis 연결

### 4.1 Lipid Droplet의 Ferroptosis 방어 기전

```
Lipid Droplet (LD) 방어 기전:

1. PUFA 격리 (Sequestration):
   ├── PUFA를 TG로 전환 → LD에 저장
   ├── Membrane 내游离 PUFA 감소
   └── Lipid peroxidation 기질 감소

2. Antioxidant organelle 기능:
   ├── LD 표면에서 항산화 반응
   ├── ROS 국소적 처리
   └── Organelle 보호

3. Membrane stability 유지:
   ├── Phospholipid turnover 조절
   ├── Membrane integrity 보존
   └── Ferroptosis threshold 상승

DGAT1 역할:
├── LD 생합성의 최종 단계
├── DAG + FA → TG (LD core)
├── LD 크기/수 조절
└── Ferroptosis 저항성의 핵심 매개체
```

### 4.2 DGAT1 억제 시 Ferroptosis 유도

```
DGAT1 억제 효과:

즉각적 효과:
├── TG 합성 ↓
├── LD 형성 ↓
├──游离 지방산 ↑
└── DAG 축적

2차 효과:
├── PUFA-CoA 축적
├── Membrane 지질 과산화 ↑
├── 4-HNE, MDA ↑
└── ROS 증폭

최종 효과:
├── Ferroptosis 유도
├── 세포사멸
└── 종양 억제

중요: 정상 증식세포에서는 DGAT1 억제가 ferroptosis에 영향 없음
→ 종양 선택적 효과 가능
```

---

## 5. NSCLC에서의 적용 가능성

### 5.1 전립선암에서 NSCLC로의 확장

```
전립선암 데이터 → NSCLC 확장:

공통점:
├── YAP 활성화 common in both cancers
├── Lipid metabolism 재프로그래밍
├── KRAS-mutant (NSCLC) vs AR-driven (전립선암)
└── Ferroptosis 저항성 공통

차이점:
├── 전립선암: AR signaling 중심
├── NSCLC: KRAS/EGFR/ALK driver
├── 대사 적응 경로 상이 가능
└── 검증 필요

검증 방법:
├── NSCLC 세포주에서 BRD9-DGAT1 상관관계
├── YAP 핵 이동과 DGAT1 발현 연관성
├── BRD9 저해제 효과 확인
└── ChIP-seq으로 BRD9-DGAT1 결합 확인
```

### 5.2 NSCLC에서 YAP 활성화 아형

```
NSCLC에서 YAP 활성화:

YAP-high NSCLC 특징:
├── Hippo pathway 비활성
├── 핵 내 YAP 축적
├── EMT (epithelial-mesenchymal transition)
├── 침습/전이 증가
├── 치료 저항성
└── Poor prognosis

KRAS와의 연관:
├── KRAS-mutant에서 YAP 활성화 common
├── KRAS → MAPK → YAP axis
├── KRAS와 YAP 공동 작용
└── Combined targeting 전략

Biomarker로서:
├── YAP 핵 이동 (IHC)
├── YAP target gene 발현 (CTGF, CYR61)
├── BRD9 발현
└── DGAT1 발현
```

---

## 6. 치료 전략: BRD9-DGAT1 축 타겟팅

### 6.1 BRD9 저해제

```
BRD9 저해제 옵션:

| 저해제 | 유형 | 상태 | 비고 |
|--------|------|------|------|
| **BI-7273** | 소분자 | 전임상 | BRD9 bromodomain 저해 |
| **I-BRD9** | 소분자 | 전임상 | 선택적 BRD9 저해 |
| **dBRD9** | PROTAC | 개발 중 | BRD9 분해 유도 |
| **VZ185** | PROTAC | 개발 중 | BRD9/BRD7 dual degrader |

효과:
├── DGAT1 전사 감소
├── LD 형성 억제
├── Ferroptosis 감수성 회복
└── 종양 성장 억제
```

### 6.2 YAP/TEAD 저해제

```
YAP/TEAD 저해제:

| 저해제 | 기전 | 상태 | 비고 |
|--------|------|------|------|
| **VT104** | TEAD palmitoylation 저해 | 임상 | 간접적 DGAT1 효과 |
| **IK-930** | TEAD 저해 | 임상 | YAP 의존 종양 |
| **TB-505** | TEAD antagonist | 전임상 | - |

간접적 효과:
├── YAP 억제 → BRD9 ↓ → DGAT1 ↓
├── 다단계 효과
├── 더 광범위한 전사 변화
└── 부작용 가능성

조합 전략:
├── VT104 + DGAT1i (이중 억제)
├── VT104 + Pradigastat
└── Sequential therapy 가능성
```

### 6.3 DGAT1 저해제 (직접)

```
DGAT1 직접 저해:

Pradigastat (LCQ908):
├── Novartis 개발
├── Phase II/III 완료 (대사 질환)
├── 임상 안전성 데이터 보유
├── 2026년 3월 ferroptosis paper에서 사용
└── Oncology repurposing 경로

기타 저해제:
├── A922500: 전임상, potency 높음
├── AZD7687: AstraZeneca, Phase I/II
├── T863: 도구 화합물
└── PF-06450309: Pfizer

장점:
├── 직접적 효과
├── BRD9 독립적 작용
├── LD 감소 직접 유도
└── Ferroptosis 즉각 유도
```

---

## 7. 조합 전략 설계

### 7.1 Triple Targeting: YAP-BRD9-DGAT1

```
Triple targeting 전략:

┌─────────────────────────────────────────────────────────┐
│ Level 1: YAP/TEAD 저해 (VT104)                          │
│ ├── 상위 경로 차단                                       │
│ ├── BRD9, DGAT1 외 다른 target도 영향                    │
│ └── 광범위한 전사 변화                                   │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ Level 2: BRD9 저해 (BI-7273 또는 PROTAC)                │
│ ├── 중간 단계 차단                                       │
│ ├── DGAT1 전사 특이적 억제                               │
│ └── Epigenetic modulation                               │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ Level 3: DGAT1 저해 (Pradigastat)                       │
│ ├── 최하위 경로 차단                                     │
│ ├── 직접적 LD 감소                                       │
│ └── Ferroptosis 유도                                     │
└─────────────────────────────────────────────────────────┘

최적 조합:
├── VT104 + Pradigastat (2중 차단)
├── BI-7273 + Pradigastat (BRD9 + DGAT1)
└── VT104 + Pradigastat + Anti-PD1 (3중)
```

### 7.2 SLC7A11 추가 조합

```
4중 조합 전략 (최대 효과):

YAP/TEAD 저해 (VT104)
    + BRD9 저해 (선택적)
    + DGAT1 저해 (Pradigastat)
    + SLC7A11 저해 (Erastin/Sulfasalazine)
    = Ferroptosis 극대화

기전:
├── YAP 억제 → BRD9 ↓ → DGAT1 ↓
├── DGAT1 억제 → LD ↓ → Ferroptosis 감수성 ↑
├── SLC7A11 억제 → GSH ↓ → GPX4 ↓
└── Ferroptosis 방어 완전 붕괴

주의:
├── 독성 증가 가능성
├── 순차적 투여 고려
├── 환자 선별 필수
└── Dose optimization 필요
```

---

## 8. 실험 검증 계획

### 8.1 In Vitro 검증

```
실험 계획 (NSCLC 세포주):

1단계: YAP-BRD9-DGAT1 축 확인
□ YAP 핵 이동 확인 (IF)
□ BRD9 발현 측정 (Western)
□ DGAT1 발현 측정 (qPCR, Western)
□ 상관관계 분석

2단계: BRD9-DGAT1 결합 확인
□ ChIP-qPCR: BRD9가 DGAT1 promoter에 결합하는지
□ ChIP-seq (선택적)
□ CRISPR KO: BRD9 KO → DGAT1 감소 확인

3단계: 저해제 효과
□ VT104: YAP/TEAD 저해 → BRD9, DGAT1 변화
□ BI-7273: BRD9 저해 → DGAT1 감소
□ Pradigastat: 직접 DGAT1 억제

4단계: Ferroptosis 검증
□ C11-BODIPY: Lipid peroxidation
□ Fer-1 구조 확인: Ferroptosis 기전 확인
□ 4-HNE, MDA 측정
□ Cell viability
```

### 8.2 In Vivo 검증

```
동물 실험 계획:

모델:
├── A549 Xenograft (KRAS-mutant)
├── YAP-high 종양 모델
└── Patient-derived xenograft (PDX)

군 배치:
├── Vehicle
├── VT104 alone
├── Pradigastat alone
├── VT104 + Pradigastat
├── Pradigastat + Anti-PD1
└── VT104 + Pradigastat + Anti-PD1

평가:
├── 종양 크기
├── 생존 기간
├── 조직학적 분석
├── IHC: DGAT1, BRD9, YAP
└── Ferroptosis 표지자
```

---

## 9. 임상 전환 전략

### 9.1 환자 선별

```
YAP-BRD9-DGAT1 축 환자 선별:

1차 선별:
├── YAP 핵 이동 (IHC 2+ 이상)
├── BRD9 높은 발현
├── DGAT1 높은 발현
└── KRAS-mutant (선택적)

2차 선별:
├── Lipid droplet 과다 (Oil Red O)
├── Ferroptosis 저항성 표지자
├── GPX4 낮은 발현
└── SLC7A11 높은 발현

최적 대상자:
┌─────────────────────────────────────────┐
│ YAP 핵 이동 (+)                          │
│ + BRD9 high                              │
│ + DGAT1 high                             │
│ + KRAS mutant                            │
│ + Ki67 low (<10%)                        │
│ = YAP-BRD9-DGAT1 축 활성화               │
│ = 최적 DGAT1 표적 치료 대상              │
└─────────────────────────────────────────┘
```

### 9.2 임상 시험 설계

```
Phase I/II 시험 설계:

대상:
├── 진행성 NSCLC
├── YAP-high (biomarker 선별)
├── 표준 치료 실패 후
└── ECOG 0-1

군:
├── Cohort 1: Pradigastat + Anti-PD1
├── Cohort 2: VT104 + Pradigastat
├── Cohort 3: Triple combination (optional)

1차 평가:
├── 안전성 (DLT)
├── PK/PD

2차 평가:
├── ORR
├── PFS
├── OS

탐색적 평가:
├── Biomarker 반응
├── Ferroptosis 표지자
└── YAP-BRD9-DGAT1 축 변화
```

---

## 10. 결론

### 10.1 핵심 요약

```
YAP/TEAD-BRD9-DGAT1 축 핵심:

1. 기전:
   YAP → TEAD → BRD9 → DGAT1 → LD → Ferroptosis 저항성
   
2. BRD9 역할:
   ├── 중간체 (Intermediate)
   ├── Epigenetic reader
   ├── DGAT1 전사 필수적
   └── 약물 표적으로서 유망

3. 치료 전략:
   ├── 단일: DGAT1 직접 저해 (Pradigastat)
   ├── 이중: VT104 + Pradigastat
   ├── 삼중: + Anti-PD1
   └── 사중: + SLC7A11 저해제

4. 환자 선별:
   ├── YAP 핵 이동
   ├── BRD9 high
   ├── DGAT1 high
   └── KRAS mutant
```

### 10.2 향후 연구 방향

```
필요한 연구:

1. NSCLC에서 검증:
   □ BRD9-DGAT1 결합 확인 (ChIP)
   □ YAP-BRD9-DGAT1 상관관계
   □ 저해제 효과 확인

2. 조합 최적화:
   □ VT104 + Pradigastat 시너지
   □ Pradigastat + Anti-PD1
   □ 순차적 투여 전략

3. Biomarker 개발:
   □ YAP-BRD9-DGAT1 signature
   □ 반응 예측 panel
   □ 내성 모니터링

4. 임상 진입:
   □ IND filing 준비
   □ Phase I 설계
   □ 파트너십 확보
```

---

## 참고 문헌

```
1. Cell Death & Disease 2026
   "Aberrant activation of epigenetic BRD9-DGAT1 axis 
    promotes lipid droplets deposition and ferroptosis resistance 
    in YAP-high prostate cancer"
   → YAP-BRD9-DGAT1 축 규명

2. Nature 2022
   "Targeting SWI/SNF ATPases in enhancer-addicted prostate cancer"
   → BRD9 dependency

3. Cancer Research 2026 (Pan et al.)
   "DGAT1 inhibition induces ferroptosis..."
   → DGAT1-Ferroptosis 기전

4. Nature Communications 2024
   "Cell cycle arrest induces lipid droplet formation..."
   → 세포주기-DGAT1-Ferroptosis

5. Nature Communications 2022
   "Targeting de novo lipogenesis and the Lands cycle 
    induces ferroptosis in KRAS-mutant lung cancer"
   → KRAS-Ferroptosis-DGAT1 연관
```

---

*Chapter 3: arp-v24/NSCLC_DGAT1_CHAPTER3_YAP_BRD9_2026.md*  
*작성일: 2026-05-01*