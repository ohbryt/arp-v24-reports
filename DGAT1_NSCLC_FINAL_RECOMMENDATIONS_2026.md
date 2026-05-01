# DGAT1 NSCLC 보고서 - 최종 전문가 권고 (2026-05-01)
## 추가 피드백: 2026-05-01

---

## 1. 수정된 우선순위 매트릭스

| 전략 | 기존 우선순위 | 근거 기반 우선순위 | 근거 |
|------|-------------|-------------------|------|
| **DGAT1i + SLC7A11i** | 높음 | ⭐⭐⭐⭐⭐ **CRITICAL** | 합성 치사 검증됨; Pan et al. 2026 확인 |
| **DGAT1i + Anti-PD1** | 중간 | ⭐⭐⭐⭐ **HIGH** | 같은 논문에서 DGAT1 KO가 ICB 효능 향상 확인 |
| **DGAT1i + YAP/TEADi** | 높음 | ⭐⭐⭐ **MEDIUM** | 기전이 BRD9 매개, 직접적 아님 |
| **DGAT1i + Cisplatin** | 중간 | ⭐ **LOW** | 대사 스트레스 + DNA 손상에 시너지 증거 부족 |

---

## 2. 수정된 실험 계획

### 2.1 Phase 1 (1-4주): 필수 대조군 추가

```
새로 추가해야 할 실험:

□ Pradigastat dose-response (0.01-10μM)
   └── 임상 후보물질 사용

□ Ferrostatin-1 구조 확인 실험 (ferroptosis 기전 확인)

□ 세포주기 분석 (propidium iodide)
   └── 정지된 세포군 식별

□ BRD9 발현 상관관계 (NSCLC 세포주에서)
```

### 2.2 Phase 2 (5-12주): 치료군 수정

```
수정된 치료군:

| 군 | 근거 |
|----|------|
| Vehicle | 대조군 |
| Pradigastat (경구, 매일) | 임상 후보물질 |
| PF14-siDGAT1 (IV, 주 2회) | N/P 2, 50μg |
| Pradigastat + Anti-PD1 | 검증된 조합 |
| Pradigastat + Erastin | 합성 치사 |
| Pradigastat + VT104 | BRD9-YAP 축 |

제거: Cisplatin 조합 (단일 약제 효능 입증 전까지 우선순위 낮음)
```

---

## 3. 📊 수정된 개발 타임라인

### 3.1 즉시 (1주)

```
□ Pradigastat 주문 (A922500만 아니고)
□ NSCLC 세포주에서 BRD9 발현 확인
□ N/P 2, 50μg siRNA로 PF14 조제 최적화
```

### 3.2 1개월

```
□ Ferroptosis 기전 검증 (Fer-1 구조 확인)
□ Pradigastat + Anti-PD1 in vitro 테스트
□ 느린 주기 저항성 세포군 식별
```

### 3.3 2-3개월

```
□ Pradigastat in vivo (경구 생체이용률 알려짐)
□ BRD9 공동 타겟팅 평가
□ 환자 계층화 biomarker 패널 확립
```

### 3.4 4-6개월

```
□ PROTAC 설계 (A922500를 warhead로, CRBN/VHL)
□ Pradigastat 데이터 패키지로 IND 가능화
```

---

## 4. 🆕 신규 기회

### 4.1 저항성 biomaker로서의 DGAT1

```
DGAT1를 저항성 biomarker로 포지셔닝:

기전:
항분열제 치료 후 (docetaxel, lorlatinib):
├── 잔류 세포가 DGAT1 상향
├── Lipid droplet 형성 증가
└── Ferroptosis 저항성 획득

임상적 함의:
├── DGAT1i를 저항성 역전 약제로 포지셔닝
├── 2차 치료로 사용
└── 선별적 환자에서 효과 극대화
```

### 4.2 경구 생체이용률 이점

```
Pradigastat의 경구 이용 가능성:

장점:
├── PF14 (흡입)보다 실제적 임상 경로
├── 경구 DGAT1i + 정맥 면역관문억제제
├── 더 간단한 임상 프로토콜
└── 환자 준수성 향상

현재 계획 문제:
├── PF14에 과도하게 집중
├── 경구 옵션을轻视
└── 임상 가능성이 낮음

수정:
├── Pradigastat를 주력으로
├── PF14는 보조적으로
└── 경구 + IV 조합 임상 경로
```

### 4.3 PROTAC 실용성 고려

```
DGAT1는 ER 막 단백질:

문제:
├── PROTAC는 세포질 단백질에 효과적
├── ER 막 단백질은 도달 어려움
└── 분해 효율 제한

대안으로 고려:
├── AUTAC (Autophagy-targeting chimera)
├── LYTAC (Lysosome-targeting)
└── 분해 경로 다른 접근
```

---

## 5. 🚨 위험 대응 업데이트

| 위험 | 기존 대응 | 강화된 대응 |
|------|----------|-------------|
| **위장 독성 (계통성 DGAT1i)** | 흡입 전달 | Pradigastat는 위장 AE 프로파일 알려짐; 용량 최적화Known |
| **제한된 단일 약제 효능** | 조합 설계 | 단일 효능 입증 전에도 Anti-PD1 조기 추가 |
| **저항성** | siRNA + 소분자 | 동시에 BRD9-DGAT1 축 타겟 |

---

## 6. 최종 권고

```
핵심 권고:

1. Pradigastat로 전환
   └── A922500가 아닌 임상 후보

2. PF14 용량 프로토콜 수정
   └── N/P 2, 50μg

3. BRD9-YAP 축 통합
   └── 직접적 YAP/TEAD-DGAT1 전사로 가정하지 말고

4. 면역치료 조합을 최고 우선순위로 격상
   └── 2026년 3월 최신 증거 기반

5. 경구 임상 경로 고려
   └── PF14만 강조하지 말고
```

---

## 7. 📋 실행 체크리스트

### 즉시 (이번 주)

```
□ Pradigastat 견적 요청
□ BRD9 primer 설계/주문
□ 세포주기 프로토콜 준비

□ PF14 조제:
   ├── N/P 2로 재계산
   ├── 50μg siRNA 준비
   └── IV 투여 프로토콜 준비
```

### 1개월

```
□ Pradigastat +/- Anti-PD1 효능 테스트
□ Fer-1 구조 확인 실험
□ BRD9/DGAT1 상관관계 분석
□ 느린 주기 세포에서 DGAT1 발현
```

### 3개월

```
□ In vivo疗效 연구 (Pradigastat)
□ biomarker 패널 확정
□ IND 자료 포장 시작
```

---

*최종 권고 문서: arp-v24/DGAT1_NSCLC_FINAL_RECOMMENDATIONS_2026.md*  
*일자: 2026-05-01*