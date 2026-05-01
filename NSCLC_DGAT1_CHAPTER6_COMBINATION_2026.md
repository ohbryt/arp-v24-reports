# Chapter 6: 병용 요법 전략 - Ferroptosis 합성 치사

**작성일:** 2026-05-01  
**보고서:** NSCLC DGAT1 Advanced Report - Chapter 6

---

## 6. 병용 요법 전략

### 6.1 수정된 우선순위 매트릭스

```
⚠️ 전문가 권고 반영 (2026-05-01):

| 조합 | 기존 우선순위 | 수정 우선순위 | 이유 |
|------|-------------|---------------|------|
| DGAT1i + SLC7A11i | HIGH | ⭐⭐⭐⭐⭐ CRITICAL | 검증된 합성 치사 |
| DGAT1i + Anti-PD1 | MEDIUM | ⭐⭐⭐⭐ HIGH | March 2026 paper |
| DGAT1i + YAP/TEADi | HIGH | ⭐⭐⭐ MEDIUM | BRD9 매개 (간접적) |
| DGAT1i + Cisplatin | MEDIUM | ⭐ LOW | 증거 부족 |

최고 우선순위 조합:
1. Pradigastat + Anti-PD1 (NEW HIGHEST)
2. Pradigastat + Erastin (SLC7A11i)
3. Triple: VT104 + Pradigastat + Anti-PD1
```

---

## 7. DGAT1i + SLC7A11i 병용

### 7.1 합성 치사 기전

```
합성 치사 (Synthetic Lethality) 기전:

DGAT1 억제 시:
├── TG 합성 ↓
├── Lipid droplet ↓
├── Free fatty acid ↑
├── ROS/지질 과산화 ↑
└── Ferroptosis threshold 감소

SLC7A11 억제 시 (추가):
├── Cystine 흡수 ↓
├── GSH 합성 ↓
├── GPX4 기능 ↓
├── 지질 과산화 방어 붕괴
└── Ferroptosis 완전히 유도

결과:
├── Synergistic cell death
├── In vivo efficacy 확인
└── 저용량에서도 효과
```

### 7.2 SLC7A11 저해제 옵션

```
SLC7A11 저해제:

| 저해제 | 기전 | 상태 | 비고 |
|--------|------|------|------|
| **Erastin** | SLC7A11 직접 억제 | 도구 화합물 | 최초 발견 |
| **Sulfasalazine (SAS)** | SLC7A11 억제 | FDA 승인 (대장염) | repurposing |
| **Sorafenib** | SLC7A11 억제 + TK | FDA 승인 (간암) | 다중 표적 |
| **IKE** | SLC7A11 억제 | 개발 중 | 더 강력한 유도 |

임상적 활용:
├── Sulfasalazine: 안전성 데이터 존재
├── Sorafenib: FDA 승인 약물
├── Erastin: 연구용으로 제한
└── IKE: 임상 진입 준비
```

### 7.3 DGAT1i + SLC7A11i 조합 데이터

```
조합 연구 결과:

In vitro 데이터:
├── Erastin + DGAT1i: 시너지 효과
├── Sulfasalazine + DGAT1i: 종양 성장 억제
├── combination index < 1 (synergistic)
└── 다양한 종양 세포주에서 확인

In vivo 데이터:
├── 종양 이종이식 모델에서 효과 확인
├── 저용량 조합으로 종양 퇴행
├── 내성 감소
└── 생존 기간 연장

NSCLC 특이 데이터:
├── KRAS-mutant에서 특히 효과적
├── lipid metabolism 의존성 높아
├── ferroptosis 민감성 증가
└── YAP-high 종양에서 시너지
```

---

## 8. DGAT1i + Anti-PD1 병용

### 8.1 March 2026 핵심 논문

```
Cancer Research 2026 (Pan et al.):

핵심 발견:
├── DGAT1 KO → ferroptosis 유도
├── ferroptosis → 면역원성 세포사멸 (ICD)
├── ICD → 항원 제시 증가
├── T세포 침윤 증가
└── Anti-PD1 효능 향상

분자 기전:
┌─────────────────────────────────────────┐
│ DGAT1 억제                               │
│     ↓                                   │
│ Lipid droplet ↓                         │
│     ↓                                   │
│ Ferroptosis ↑ (ROS, 4-HNE)              │
│     ↓                                   │
│ Calreticulin (ecto-CRT) ↑              │
│ ATP 방출 ↑                               │
│ HMGB1 방출 ↑                             │
│     ↓                                   │
│ Antigen presenting ↑                   │
│     ↓                                   │
│ T세포 침윤 ↑                             │
│     ↓                                   │
│ Anti-PD1 efficacy ↑                     │
└─────────────────────────────────────────┘
```

### 8.2 면역 활성화 메커니즘

```
DGAT1 억제 → 면역 활성화:

Immunogenic Cell Death (ICD):
├── DAMPs (Damage-Associated Molecular Patterns) 방출
├── Calreticulin (ecto-CRT): "eat me" 시그널
├── ATP: chemokine 방출
├── HMGB1: Toll-like receptor 활성화
└── Type I interferon response

T세포 활성화:
├── 종양 유래 T세포 증가
├── CD8+ T세포 침윤 증가
├── T세포 세포독성 증가
└── 면역 반응 강화

종양 미세환경 변화:
├── 냉양종양 (cold) → 온종양 (hot)
├── 면역 억제 환경 개선
├── Treg 감소
└── NK cell 활성화
```

### 8.3 임상적 함의

```
DGAT1i + Anti-PD1 조합의 임상적 함의:

권장 조합:
├── Pradigastat (DGAT1i) + Nivolumab
├── Pradigastat (DGAT1i) + Pembrolizumab
├── PF14-siDGAT1 + Pembrolizumab
└── 임상 시험에서 검증 필요

적응증:
├── NSCLC (전liner)
├── 치료 실패 후 진행성
├── DGAT1 높은 발현
├── MSI-H/dMMR 종양
└── Triple combination 고려

연구 필요:
├── biomarker로서 ICD 표지자
├── 면역 반응 모니터링
├── 최적 용량/스케줄
└── 내성 메커니즘
```

---

## 9. DGAT1i + YAP/TEADi 병용

### 9.1 BRD9-YAP 축 병용 논리

```
BRD9-YAP-DGAT1 축 병용:

기전:
├── YAP/TEAD 억제 → BRD9 ↓ → DGAT1 ↓
├── 직접적 DGAT1 억제 추가
├── 다중 경로 차단
└── 시너지 가능성

문제점:
├── 기전이 간접적 (BRD9 매개)
├── YAP/TEAD 저해제만으로 DGAT1 감소 불충분
└── 직접적 병용이 더 효과적

권장:
├── VT104 + Pradigastat (이중 표적)
├── 직접적 병용 우선
├── BRD9 저해제는 추가 옵션
└── 순차적 투여 고려
```

### 9.2 Triple Combination 전략

```
Triple Combination: DGAT1i + YAP/TEADi + ICI

권장 조합:
├── VT104 (YAP/TEADi) + Pradigastat (DGAT1i) + Anti-PD1
├── BI-7273 (BRD9i) + Pradigastat + Anti-PD1
└── Triple 조합으로 추가 효과 기대

기전:
├── YAP/TEAD → BRD9 → DGAT1 (다중 차단)
├── Ferroptosis 유도
├── ICD 활성화
└── 면역 반응 극대화

주의:
├── 독성 증가 가능성
├── 순차적 투여로 최적화
├── 용량 최적화 필요
└── 환자 선별 필수
```

---

## 10. 저항성 관리 전략

### 10.1 세포주기 정지와 DGAT1

```
⚠️ 2025 Nature Communications에서 중요한 발견:

"Cell cycle arrest induces lipid droplet formation 
 and confers ferroptosis resistance via DGAT1 upregulation"

핵심 기전:
├── 세포주기 정지 → LD 형성 → Ferroptosis 저항성
├── DGAT1 상향이 필수적
├── 정지된 세포에서는 DGAT1가 ferroptosis 방어에 필수
└── 세포주기 정지 유도 시 DGAT1的重要性 증가

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
│   → 저항성 역전                         │
└─────────────────────────────────────────┘

저항성 biomarker:
├── Ki67 높은 종양 (활발한 증식)
├── DGAT1 높은 발현
├── LD 과다
└── 세포주기 정지 상태
```

### 10.2 저항성对策

```
저항성 관리 전략:

내성 발생 시 대안:
├── 순차적 치료: 항분열제 → DGAT1i
├── combination으로 진행
├── 다른 기전의 약물 추가
└── immunotherapy 고려

예방 전략:
├── biomarker 모니터링
├── 조기 intervention
├── 조합 치료로 단독 사용 회피
└── 치료 순서 최적화

다음 단계 치료:
├── FSP1 저해제 (ferroptosis alternative pathway)
├── GPX4 저해제
├── System x_c^- independent ferroptosis induction
└── immunotherapy + 다른 기전
```

---

## 11. 임상 개발 로드맵

### 11.1 조합 임상 시험 설계

```
临床试验 设计:

Phase Ib/II: Pradigastat + Pembrolizumab

대상:
├── 진행성 NSCLC
├── PD-1/PD-L1 치료 실패 후
├── DGAT1 높은 발현
└── 20-30명

디자인:
├── Phase Ib: 안전성 확인
├── Phase II: efficacy 확인
├── 병용 용량: Pradigastat 100mg BID + Pembrolizumab 200mg Q3W
└── 1차 평가: ORR, DLT

 biomarker 연구:
├──治疗 전 tumor biopsy
├── 치료 후 biopsy (선택적)
├── 혈액 biomarker
└── 영상学研究
```

### 11.2 치료 순서 최적화

```
치료 순서 및 용량 최적화:

선택 1: 동시 병용
├── Pradigastat + Pembrolizumab 동시 투여
├── 단순한 프로토콜
└── 약물 상호작용 모니터링

선택 2: 순차 치료
├── 1차: Pembrolizumab 단독 (2-3 cycles)
├── 2차: Pradigastat 추가 (ferroptosis 감수성 증가 후)
└── 면역 활성화 후 DGAT1 억제로 synergy

선택 3:交替 치료
├── Cycle 1: Pembrolizumab
├── Cycle 2: Pradigastat
├── Cycle 3: Pembrolizumab
└──毒性 관리 용이

권장:
├── Phase I에서 순차/동시 비교
├── biomarker 기반个体화
└── 환자 반응에 따른 조정
```

---

## 12. 결론

### 12.1 핵심 조합 전략

```
DGAT1 병용 요법 핵심 권고:

1차 우선순위:
┌─────────────────────────────────────────┐
│ Pradigastat + Anti-PD1                  │
│ (March 2026 Cancer Research 기반)       │
└─────────────────────────────────────────┘

2차 우선순위:
┌─────────────────────────────────────────┐
│ Pradigastat + Erastin/Sulfasalazine     │
│ (SLC7A11 억제로 합성 치사 극대화)        │
└─────────────────────────────────────────┘

3차 우선순위:
┌─────────────────────────────────────────┐
│ Triple: VT104 + Pradigastat + Anti-PD1  │
│ (YAP-BRD9-DGAT1 다중 차단)              │
└─────────────────────────────────────────┘

저항성 관리:
├── 치료 순서 최적화 (항분열제 → DGAT1i)
├── biomarker 모니터링
└── 순차적 치료 전략
```

### 12.2 향후研究方向

```
필요한 연구:

1. 조합 최적화:
   □ Pradigastat + Anti-PD1 용량/용법
   □ 순차 vs 동시 비교
   □ triple combination 평가

2. biomarker 개발:
   □ ICD 표지자 확인
   □ 반응 예측 panel
   □ 저항성 조기 발견

3. 임상 진입:
   □ IND filing
   □ Phase I trial 설계
   □ 파트너십 확보

4. 저항성 연구:
   □ 내성 기전 규명
   □ 순차 치료 최적화
   □ 대안적 접근 개발
```

---

*Chapter 6: arp-v24/NSCLC_DGAT1_CHAPTER6_COMBINATION_2026.md*
*작성일: 2026-05-01*