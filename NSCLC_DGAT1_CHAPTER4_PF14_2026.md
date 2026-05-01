# Chapter 4: PF14-siDGAT1 폐 특이적 전달 시스템

**작성일:** 2026-05-01  
**보고서:** NSCLC DGAT1 Advanced Report - Chapter 4

---

## 4. PF14-siDGAT1 폐 특이적 전달 시스템

### 4.1 PF14 (PepFect 14) 특성

```
PF14 (PepFect 14) - 세포투과 펩타이드 전달체:

기본 특성:
├── 양이온성 세포투과 펩타이드 (CPP)
├── 14개 아미노산 (amphipathic 구조)
├── Stearic acid N-terminus 변형
├── 분자량: ~2,000 Da
├── 전하: +7 (pH 7.4)
└── 비공유결합으로 siRNA와 복합체 형성

 Science Reports 2019 (PMID: 31126904):
├── In vitro: >90% gene knockdown
├── In vivo: 폐 특이적 축적 확인
├── 기관지내/정맥 투여 모두 가능
└── 낮은 세포 독성 (IC50 > 100μM)
```

### 4.2 최적화된 프로토콜

```
⚠️ 수정된 PF14-siDGAT1 프로토콜 (전문가 검토 반영):

투여 경로:
├── 기존: 기관지내 (intratracheal)
├── 수정: 정맥내 (IV) - PF14는全身투여後肺에 자연 집중
└── 이유: PF14는全身IV後폐에 자연적으로 축적

용량:
├── N/P 비율: 2 (안전성優先)
├── siRNA dose: 50μg (N/P 4와 유사 효력, 더 안전)
└── 기존: 20μg → 수정: 50μg

관리 스케줄:
├── 주 2-3회 IV 투여
├── 4-6주疗程
└──毒性 모니터링 포함
```

### 4.3 복합체 형성 조건

```
PF14-siDGAT1 복합체 형성:

재료:
├── PF14: 10mM HEPES buffer (pH 7.4)
├── siDGAT1: RNase-free water (50 μM)
└── 버퍼: 10mM HEPES (pH 7.4)

계산 (N/P 2, siRNA 50μg):
├── siRNA (21bp) 전하: -42
├── N/P 2 = PF14 12nmol per 1nmol siRNA
├── siRNA 50μg ≈ 1nmol (21bp ≈ 13,300 Da)
├── PF14 필요량: 12nmol
└── PF14 용액: 1.2μL (10mM stock)

복합체 형성 과정:
1. siDGAT1 1nmol (20μL) + HEPES 5μL 준비
2. PF14 12nmol (1.2μL) + HEPES 23.8μL 준비
3. PF14 용액을 siRNA에 천천히 첨가
4. Pipette up/down 10×
5. 실온 30분 incubation

품질 관리:
├── DLS: 50-200nm 확인
├── Zeta potential: +15-25mV
├── Gel shift assay: 완전한 shift 확인
└── 저장:新鲜 사용 권장 (24시간 이내)
```

---

## 5. 에어로졸 전달 최적화

### 5.1吸入 전달 고려사항

```
吸入 전달 (Nebulization) 고려사항:

에어로졸 특성:
├── MMAD (Mass Median Aerodynamic Diameter): 1-5 μm
│   └── 폐포 침착 최적화
├── GSD (Geometric Standard Deviation): < 1.5
│   └── 균일한 입자 분포
├── Deposition: alveolar > bronchial
└── 입자 크기 1-5μm이 폐포 깊숙이 도달

PF14 복합체 최적화:
├── 입자 크기: 100-200nm (DLS)
├── 표면 전하: +15-25mV (zeta potential)
├── mucoadhesive 추가 고려 (mucin)
├── 계면활성제 내성
└── 반복 투여 가능성

吸入装置 옵션:
├── Jet nebulizer
├── Ultrasonic nebulizer
├── Mesh nebulizer (더 미세한 입자)
└── Soft mist inhaler
```

### 5.2吸入-vs-IV 비교

```
吸入 vs 정맥내 (IV) 투여 비교:

吸入 (Inhalation):
├── 장점:
│   ├── 폐에 직접 작용 (국소 효과)
│   ├── 전신 독성 최소화
│   ├── 낮은 용량으로 효과 가능
│   └── 환자의顺应성 향상
├── 단점:
│   ├── 흡입 효율 변동성
│   ├── 폐 침착 불확실성
│   ├── 흡입기 필요
│   └── 점막 장벽
└── 적합 상황: 초기 연구, 동물 모델

정맥내 (IV):
├── 장점:
│   ├── 투여 정확성
│   ├── PF14 자연 폐 축적 활용
│   ├── 시스템적으로 예측 가능
│   └── 임상 전환 용이
├── 단점:
│   ├── 전신 노출
│   ├── 정맥 주사 필요
│   └── 비용
└── 적합 상황: 임상 단계, 정확한 dosing

권장:
├── 동물 실험: IV 투여 (표준화)
├── 임상 1상: IV 또는 inhalation 비교
└── 장기 치료: inhalation 고려
```

---

## 6. 동물 모델 검증

### 6.1小鼠 모델 실험

```
동물 실험 계획 (老鼠):

모델:
├── C57BL/6 마우스 (정상)
├── NSG 마우스 (종양 이식)
├── KRASLSL-G12D/+; p53fl/fl 모델 (자가 종양)
└── A549 xenograft (인간 종양)

군 배치:
├── Naive + PF14-siDGAT1 ( pharmacokinetics)
├── A549 종양 + Vehicle
├── A549 종양 + PF14-siNC (대조군)
├── A549 종양 + PF14-siDGAT1 (저용량)
├── A549 종양 + PF14-siDGAT1 (고용량)
└── A549 종양 + Pradigastat (경구)

투여:
├── PF14-siDGAT1: IV, 주 2회, 3주
├── Pradigastat: 경구, 매일, 3주
└── 종양 크기: 주 2회 측정

평가:
├── 종양 크기/체중
├──DGAT1 knockdown (qPCR, Western)
├── Lipid droplet (Oil Red O)
├── Ferroptosis 표지자
├── 장기 독성 (H&E)
└── 혈중 biomarker
```

### 6.2 종양 특이성 확인

```
종양 vs 정상 폐 조직 분포:

목표:
├── 종양 조직에 선택적 축적
├── 정상 폐 상피에 최소 침착
└── 전신 장기에는 제한적 분포

평가 방법:
├── In vivo imaging (fluorophore-labeled)
├── 조직학적 분석 (종양 vs 정상)
├── qPCR로 siRNA 분포
└── immunohistochemistry

기대 결과:
├── 종양: 높은 siRNA 축적
├── 정상 폐: 낮은 수준
├── 간/신장: 최소화
└── 혈액: 빠르게 제거
```

---

## 7. 환자 계층화 biomarker

### 7.1 환자 선별 기준

```
DGAT1 표적 치료 대상 환자:

1차 선별 (필수):
├── 조직학적으로 확인된 NSCLC
├── 종양 조직 DGAT1 발현 확인 (IHC 2+)
├── 표준 치료 실패 후
├── ECOG performance status 0-1
└── 적절한 장기 기능

2차 선별 (권장):
├── YAP 핵 이동 확인
├── KRAS 돌연변이 (특히 lung adenocarcinoma)
├── Ki67 낮은 발현 (<10%)
├── SLC7A11 높은 발현
└── 이전 치료 병력

제외 기준:
├── 중대한 감염 또는 염증
├── 임신 또는 수유
├── 활동성 자가면역 질환
├── 심혈관 질환 (DGAT1i 장기 투여 시)
└── 알려진 PF14 과민증
```

### 7.2 반응 예측 biomarker

```
치료 반응 예측 biomarker:

치료 전:
┌─────────────────────────────────────────┐
│ Biomarker          │ 방법      │ 기준   │
├────────────────────┼───────────┼────────┤
│ DGAT1              │ IHC       │ 2+ 이상│
│ YAP (핵 이동)     │ IHC       │ +      │
│ KRAS               │ NGS/PCR   │ Mutant │
│ Ki67               │ IHC       │ <10%   │
│ SLC7A11            │ IHC       │ High   │
└─────────────────────────────────────────┘

치료 중 (약력학):
┌─────────────────────────────────────────┐
│ Biomarker          │ 방법      │ 변화   │
├────────────────────┼───────────┼────────┤
│ DGAT1 (종양)      │ qPCR/IHC  │ ↓ 감소 │
│ Lipid droplet      │ Oil Red O │ ↓ 감소 │
│ 4-HNE              │ IHC       │ ↑ 증가 │
│ PTGS2 (mRNA)      │ qPCR      │ ↑ 증가 │
│ GSH/GSSG ratio    │ HPLC      │ ↓ 감소 │
└─────────────────────────────────────────┘

저항성 예측:
├── SLC7A11 돌연변이/증폭
├── FSP1, NQO1 증가
├── GPX4 증가
└── ACSL4 감소
```

---

## 8. 임상 전환 계획

### 8.1 Phase I/II 설계

```
임상 시험 설계:

Phase I (안전성):
├── 대상: 진행성 NSCLC (DGAT1 높은 발현)
├── 시작 용량: PF14-siDGAT1 50μg (N/P 2, IV)
├── 용량 증가: 25μg → 50μg → 100μg
├── 투여 일정: 주 2회, 3주 주기
├── 평가: DLT, 부작용, PK/PD
└── 인원: 12-18명

Phase II (효능):
├── 대상: 1차 이상 치료 실패 후 NSCLC
├── 디자인: 단일-arm 또는 무작위 배정
├── 치료: PF14-siDGAT1 + Anti-PD1
├── 1차 평가: ORR, PFS
├── 2차 평가: OS, biomarker
└── 인원: 40-60명
```

---

*Chapter 4: arp-v24/NSCLC_DGAT1_CHAPTER4_PF14_DELIVERY_2026.md*
*작성일: 2026-05-01*