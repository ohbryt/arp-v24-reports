# DGAT1 NSCLC 보고서 - 전문가 검토 및 수정
## 피드백 일자: 2026-05-01
## 출처: 전문가 분석

---

## 1. 핵심 강점 (확인됨)

### 1.1 페로프토시스 기전 확인

```
2026년 3월 Cancer Research (Pan et al.):
DGAT1 억제 → ferroptosis 유도
├── Lipid droplet 감소
├── GPX4 감소
├── 지질 과산화 증가
└── 면역관문억제제 효과 개선

→ 사용자 보고서의 핵심仮설 검증됨!
```

### 1.2 사용 가능한 임상 단계 저해제

| 저해제 | 상태 | 장점 |
|--------|------|------|
| **Pradigastat (LCQ908)** | Phase II/III | 안전성 데이터 있음, 최신 ferroptosis 논문에서 사용 |
| **AZD7687** | Phase I/II | AstraZeneca开发 |
| **A922500** | 전임상 | Potency 높지만 인간 안전성 데이터 없음 |

### 1.3 PF14 전달 검증

```
 PF14 전달 검증:
- In vitro: >90% knockdown 확인
- In vivo: 폐 특이적 축적 확인
└──全身 투여 후 폐에 자연적으로 집중
```

---

## 2. ⚠️ 수정 필요 사항

### 2.1 YAP/TEAD-DGAT1 축 - 증거가 간접적

```
현재 기술:
"YAP/TEAD가 DGAT1 전사를 직접 활성화"

실제 증거:
├── BRD9-DGAT1 축: YAP-high 전립선암에서 확인
├── 직접적 YAP/TEAD-DGAT1 연결: 증거 부족
└── VT104 (YAP/TEAD 저해제):间接作用

수정 필요:
├── BRD9를 공동 타겟 또는 중간체로 추가
├── 기전을 "BRD9-DGAT1 축"으로 재정리
└── 조합 전략에 BRD9 저해제 포함 고려
```

### 2.2 저해제 우선순위 오류

```
현재 기술:
A922500 (IC50 7nM) 우선

수정:
Pradigastat를 In vivo 연구의 우선 저해제로 사용

| 저해제 | 상태 | 우선순위 |
|--------|------|----------|
| **Pradigastat** | Phase II/III | ⭐⭐⭐⭐⭐ 우선 |
| A922500 | 전임상 | 백업으로 |
| T863 | Natural product | 도구 화합물 |

이유:
- 임상 안전성 데이터 보유
- 2026년 3월 ferroptosis 논문에서 사용
- 규제 경로 축소
```

### 2.3 PF14 N/P 비율 - 중요한 오류

```
현재 기술:
- N/P 비율: 2:1
- siRNA dose: 20μg
- 투여 경로: 기관지내 (intratracheal)

수정 (2026 문헌):
├── N/P 4: 폐 축적最高但는 독성 occasional
├── N/P 2: 안전 (zero lethality), 하지만 higher dose 필요
└── siRNA dose: 50μg (20μg 아님)

修正 PROTOCOL:
├── N/P 비율: 2 (安全のため)
├── siRNA dose: 50μg
├── 투여 경로: 정맥내 (IV) - PF14는 IV 후自然に폐에 집중
└── 기관지내 아니님 (PF14는全身투여后肺에 자연 축적)
```

### 2.4 누락: 세포주기 정지 저항성 기전

```
2025년 중요 논문 발견:
세포주기 정지 → Lipid droplet 형성 → ferroptosis 저항성
                          ↓
                   DGAT1 상향돌연변이

임상적 함의:
1. 환자 선택:
   └── 느린 주기 세포 (post-chemotherapy 잔류 병변)에서 DGAT1 발현 highest
   
2. 조합 타이밍:
   └──DGAT1i는 항분열제治疗后아니고 전보다 투여
   
3. biomarker:
   └── Ki67 low + DGAT1 high = 최적 반응자
```

---

## 3. 📊 수정된 우선순위 매트릭스

### 3.1 환자 선택 biomarker (수정됨)

```
수정된 biomarker 조합:

1차 biomarker (필수):
├── DGAT1 높은 발현 (IHC 또는 RNA-seq)
├── Ki67 낮은 발현 (느린 세포주기)
└── YAP 핵 이동 (BRD9 연관)

2차 biomarker (권장):
├── SLC7A11 높은 발현 (ferroptosis 민감성)
├── LD 수 (Oil Red O)
└── GPX4 낮은 발현

3차 biomarker (탐색적):
├── KRAS mutant
├── EGFR mutant
└── BRD9 발현
```

### 3.2 조합 전략 (수정됨)

```
수정된 조합 전략:

우선순위 1: DGAT1i + SLC7A11i
├── 기전: 合성 치사 (확인됨)
├── 의존성: 직접적
└── 임상 데이터: 2026년 3월 paper

우선순위 2: DGAT1i + 항분열제
├── 타이밍: 항분열제 → DGAT1i (순서 중요!)
├── 기전: 세포주기 정지 후 ferroptosis 감수성 증가
└── biomarker: Ki67 변화 추적

우선순위 3: DGAT1i + BRD9i
├── 기전: BRD9-DGAT1 축 차단
├── 주의: 간접적 효과
└── 더 높은 환자 선택 필요

우선순위 4: DGAT1i + 면역관문억제제
├── 기전: Ferroptosis → ICD → 면역 활성화
└── 2026년 3월 paper 확인
```

---

## 4. 수정된 개발 전략

### 4.1 수정된 약물 우선순위

```
수정된 약물 개발 순서:

1단계 (즉시):
├── Pradigastat (Novartis) 확보
│   └── Phase II/III 데이터 활용
├── A922500 (백업)
└── Erastin 또는 Sulfasalazine (SLC7A11i)

2단계 (3-6개월):
├── Pradigastat + erastin 조합 in vitro
├── PF14-siDGAT1 (N/P 2, 50μg, IV)
└── BRD9 저해제 평가 (선택적)

3단계 (6-12개월):
├── In vivo efficacy (Pradigastat + erastin)
├── 환자 유래 이종이식 (PDX)
└── biomarker 검증
```

### 4.2 수정된 PF14 프로토콜

```
修正 PF14-siDGAT1:

투여 경로 변경:
├── 기존: 기관지내 (intratracheal)
├── 수정: 정맥내 (IV) - PF14는自然に폐에 집중
└── 이유: 기관지내는 불필요, IV로 충분

용량 변경:
├── N/P 비율: 2 (기존 유지)
├── siRNA dose: 50μg (20μg → 50μg)
└── 효과: N/P 4와 유사한 효력, 더 안전

관리 스케줄:
├── 주 2-3회 IV 투여
├── 4-6주疗程
└──毒性 모니터링 포함
```

---

## 5. 수정된 임상 개발 로드맵

### 5.1 수정된 환자 선택 기준

```
수정된 환자 선택:

선정 기준:
├── 조직학적으로 확인된 NSCLC
├── DGAT1 높은 발현 (IHC 2+ 이상)
├── Ki67 낮은 발현 (<10% 또는 중앙값 미만)
├── 1차 이상 치료 후 진행
└── 선택적: YAP 핵 이동 (BRD9 연관)

제외 기준:
├── 급성 감염 또는 염증
├── 중대한 심혈관 질환
├── 임신 또는 수유
└── 활동성 자가면역 질환
```

### 5.2 수정된 평가 판정

```
수정된 평가 사항:

1차 평가 (필수):
├── 안전성 (용량 제한 독성, 부작용)
├── 약동학 (AUC, Cmax, 반감기)
├── 병증 진행 자유 생존 (PFS)
└── 객관적 반응률 (ORR)

2차 평가 (중요):
├── Overall survival (OS)
├── 반응 기간 (DoR)
├── biomarker 반응 (DGAT1, Ki67, LD)
└── ferroptosis 표지자 변화

探索적 평가:
├── 질 жизни (QoL)
├── immune 관련 표지자
└── 내성 메커니즘
```

---

## 6. 📋 실행 계획 (수정됨)

### 6.1 0-3개월 (즉시)

```
□ Pradigastat 확보 (Novartis에 문의)
□ 수정된 PF14 프로토콜 적용 (N/P 2, 50μg, IV)
□ Ki67-DGAT1 correlation 검증 (세포주)
□ 세포주기 정지 후 ferroptosis 민감성 증가 확인
□ BRD9 발현 검증 (TCGA/CCLE)
```

### 6.2 3-6개월

```
□ Pradigastat + erastin 조합 in vitro
□ 환자 유래 세포주 (PDC) 테스트
□ Ki67 low + DGAT1 high 환자-derived 모델 평가
□ In vivo 용량 결정 (老鼠)
□ IND 준비 시작
```

### 6.3 6-12개월

```
□ GLP toxicology 연구
□ In vivo疗效 확인 (PDX 모델)
□ biomarker 패널 최종화
□ 파트너십 논의
□ IND filing
```

---

## 7. 📊 수정 사항 요약

| 구분 | 기존 | 수정 | 이유 |
|------|------|------|------|
| **BRD9** | 언급 없음 | 공동 타겟으로 추가 | YAP-DGAT1 축의 중간체 |
| **우선 저해제** | A922500 | Pradigastat | 임상 단계, 안전성 데이터 |
| **PF14 투여** | 기관지내 | 정맥내 (IV) | PF14는 자연 폐 집중 |
| **siRNA dose** | 20μg | 50μg | N/P 2에서 동일한 효력 |
| **조합 타이밍** | 동시 | 순차적 | 세포주기 정지 후が最適 |
| **환자 biomarker** | DGAT1 단일 | Ki67 low + DGAT1 high | 최적 반응자 |

---

## 8. 결론

```
핵심 수정 사항:

1. BRD9 추가
   └── YAP/TEAD-DGAT1 축의缺失된 연결고리

2. Pradigastat 우선
   └── 임상 단계 저해제로 전환

3. PF14 프로토콜 수정
   └── IV 투여, 50μg dose

4. Ki67 biomarker 추가
   └── 최적 환자 선택 기준

5. 조합 타이밍 최적화
   └── 항분열제 → DGAT1i 순서
```

---

*피드백 문서: arp-v24/DGAT1_NSCLC_EXPERT_REVIEW_2026.md*  
*저장일: 2026-05-01*