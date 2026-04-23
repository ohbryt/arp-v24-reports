# MASLD Drug Discovery Report
## ARP v24 Director Agent + Groq Analysis

**Generated:** 2026-04-23  
**Pipeline:** ARP v24 Orchestration System  
**Disease:** MASLD (Metabolic dysfunction-associated steatotic liver disease)  
**Targets:** ARP v24 Engine 1-3 (5 targets)  
**Analysis:** Groq LLM (Llama 3.3 70B)

---

## 1. Executive Summary

### MASLD 개요
MASLD (Metabolic dysfunction-associated steatotic liver disease)는 대사이상과 관련된 간장 지방축적 질환으로, 기존 NAFLD/NASH 용어가 2023년부터 새로운 용어로 변경되었습니다.

### 핵심 타겟 (ARP v24 Pipeline)

| Rank | Gene | Protein | Score | Pathway |
|------|------|---------|-------|---------|
| 1 | **NR1H4** | FXR | 0.525 | 담즙산 항상성 |
| 2 | **PPARA** | PPARα | 0.525 | 지방산 산화 |
| 3 | **ACACA** | ACC | 0.525 | 지방생합성 |
| 4 | **SREBF1** | SREBP-1 | 0.525 | 지방합성 |
| 5 | **THRB** | TRβ | 0.485 | 대사조절 |

---

## 2. 타겟별 기전 및 약물 개발 현황

### 2.1 NR1H4 (FXR - Farnesoid X receptor)

**역할:**
- 담즙산 항상성 조절의 핵심 전사인자
- 간장 지방생성 억제
- 인슐린 민감성 개선

**약물 개발:**
- **Obeticholic acid (OCA)**: FXR Agonist
  - Company: Intercept Pharmaceuticals
  - Status: PBC 치료 approved, **MASLD Phase 3**
  - 효과: 간 fibrosis 개선

### 2.2 PPARA (PPARα - Peroxisome proliferator-activated receptor α)

**역할:**
- 지방산 산화 촉진
- 케톤체 생성 증가
- 항염증 효과

**약물 개발:**
- **Pemafibrate**: PPARα Agonist
  - Company: Kowa
  - Status: **MASLD Phase 3**
  - 효과: ALT/AST 개선

### 2.3 ACACA (ACC - Acetyl-CoA carboxylase)

**역할:**
- 지방생합성 속도결정효소
- Malonyl-CoA 생산 조절
- 지방산 산화 억제

**약물 개발:**
- **Firsocostat**: ACC Inhibitor
  - Company: NGM Bio
  - Status: **Phase 2**
  - 효과: 간지방 함량(HAF) 감소

### 2.4 SREBF1 (SREBP-1 - Sterol regulatory element-binding protein)

**역할:**
- 지방합성 유전자 전사인자
- ACC, FAS, SCD1 발현 조절
- 고농도에서 지방간 유발

**전략:**
- Inhibitor 개발 진행 중
- 전사 억제제 탐색

### 2.5 THRB (TRβ - Thyroid hormone receptor β)

**역할:**
- 간장에서 주요 갑상선호르몬 수용체
- 지방산 산화 촉진
- LDL-콜레스테롤 저하

**약물 개발:**
- **VK2809**: TRβ Agonist
  - Company: Viking Therapeutics
  - Status: **Phase 2**
  - 효과: 간지방 감소 + LDL 저하

---

## 3. 주요 임상 후보물질

| 약물 | 타겟 | Company | Phase | 상태 |
|------|------|---------|-------|------|
| **Obeticholic acid** | FXR | Intercept | Phase 3 | NDA 제출 예정 |
| **Semaglutide** | GLP-1R | Novo Nordisk | Phase 3 | 주 1회 주사로 효과 확인 |
| **Pemafibrate** | PPARα | Kowa | Phase 3 | 일본에서 승인 |
| **Lanifibranor** | PPARα/δ/γ | Inventiva | Phase 3 | 다중 PPAR 작용제 |
| **Firsocostat** | ACC | NGM Bio | Phase 2 | 단일요법 진행 |
| **VK2809** | TRβ | Viking | Phase 2 | 경구 투여 가능 |
| **Tirzepatide** | GLP-1R/GIPR | Eli Lilly | Phase 3 | MASH 치료 주목 |

---

## 4. FXR/PPAR/GLP-1 Pathway Analysis

### 4.1 FXR Pathway
```
담즙산 → FXR 활성화
    ↓
SHP 발현 ↑ → SREBP-1C 억제 → 지방합성 감소
    ↓
FGF19 분비 ↑ → 간으로 돌아가 지방산 산화 ↑
    ↓
결과: 간지방 감소 + 인슐린 민감성 개선
```

### 4.2 PPAR Pathway
```
PPARα Agonist → PPARα 활성화
    ↓
CPT1A 발현 ↑ → 지방산 미토콘드리아로 이동
    ↓
β-산화 ↑ → 에너지 생산 ↑
    ↓
결과: 지방산 산화 촉진 + 염증 감소
```

### 4.3 GLP-1 Pathway
```
GLP-1R Agonist → GLP-1R 활성화
    ↓
食欲 억제 + 위 배출 지연
    ↓
체중 감소 → 간지방 감소
    ↓
항염증 효과 + 혈당 개선
```

---

## 5. NAMs Validation Strategy

### 5.1 iPSC-유래 간세포

**방법:**
1. 환자 유래 iPSC 분화 → 간세포 (hepatocyte-like cells)
2. 지방유도 배지 처리 → MASLD 모델
3. 약물 처리 → 기능 평가

**평가지표:**
- 간지방 함량 (Oil Red O staining)
- 알부민 분비
- 요소 생산
- CYP450 활성

### 5.2 간장 Organoid

**방법:**
1. 간 전구세포 유래 3D organoid
2. 지방 축적 유발 → 병태 모델
3. 약물 처리 → 조직수준 반응

**평가지표:**
- 조직 구조 유지
- 지방 축적 정량
- 세포사멸 측정

### 5.3 MPS (Microphysiological System)

**방법:**
1. 간장 칩 (Liver-on-chip)
2. 혈류 조건 시뮬레이션
3. 약물 동태 + 대사 평가

**평가지표:**
- 약물 대사율
- 담즙산 항상성
- 염증 바이오마커

---

## 6. 결론 및 권고

### 가장 유망한 타겟: **FXR (NR1H4)**

| Strategy | 타겟 | 약물 | Timeline |
|----------|------|------|----------|
| **단기** | FXR | Obeticholic acid | Phase 3 완료, NDA 예정 |
| **중기** | GLP-1R/GIPR | Tirzepatide | Phase 3 진행 |
| **장기** | 다중 타겟 | Lanifibranor | Phase 3 진행 |

### 개발 전략

1. **단기 (1-2년):**
   - Obeticholic acid MASLD 적응증 획득
   - Semaglutide Phase 3 완료

2. **중기 (3-5년):**
   - GLP-1/PPAR 다중작용제 개발
   - ACC + FXR 조합 요법 탐색

3. **장기 (5년+):**
   - 표적 조합 요법 (Triple therapy)
   - 개인별 맞춤 치료 (Precision medicine)

### 핵심 인사이트

> **MASLD는 다중 경로 질환으로, 단일 타겟보다 다중 작용제나 조합 요법이 더 효과적일 가능성이 높음**

---

## 7. System Information

### Pipeline Architecture
```
┌─────────────────────────────────────────────────────┐
│           DIRECTOR AGENT (MiniMax-M2.7)              │
│                                                       │
│   Query → Plan → Route → Execute → Synthesize       │
└─────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ↓                   ↓                   ↓
   ┌─────────┐        ┌─────────┐        ┌─────────┐
   │ARP Pipe │        │  Groq   │        │ ChemBL  │
   │NR1H4 등 │        │LLM 분석 │        │ 약물정보│
   └─────────┘        └─────────┘        └─────────┘
```

### Tools Used
- **ARP Pipeline**: Target prioritization (NR1H4, PPARA, ACACA, SREBF1, THRB)
- **Groq (Llama 3.3 70B)**: LLM analysis
- **ChemBL API**: Bioactivity data

### Performance
- Tasks: 4/4 successful
- Duration: ~6 seconds
- Cache: Enabled (TTL 24h)

---

*Report generated by ARP v24 Director Agent + Groq LLM · 2026-04-23*
