# 폐암 대사(Cancer Metabolism) 기반 신규 치료제 개발 전략 및 비즈니스 타당성 분석

**작성자:** Manus AI  
**작성일:** 2026년 4월 25일  
**분류:** 전략 보고서 (내부 배포용)  

---

## Executive Summary

| Market | Value |
|--------|-------|
| 폐암 치료제 시장 (2025) | **316억 달러** |
| 폐암 치료제 시장 (2034) | **986억 달러** |
| 암 대사 치료제 시장 (2025) | **27억 달러** |
| 암 대사 치료제 시장 (2035) | **263억 달러** (CAGR 24.3%) |

---

## 타겟 평가 요약

| 타겟 | 평점 | 권고 |
|------|------|------|
| **SLC7A11** | ★★★★★ | **최우선** - KEAP1/NRF2 변이 NSCLC |
| **FASN** | ★★★★☆ | KRAS 억제제 병용 |
| **GLS1** | ★★★★☆ | KEAP1/NRF2 변이 + 뇌전이 |
| **GPX4** | ★★★★☆ | 페롭토시스 유도 |
| **Complex I** | ★★★★☆ | OXPHOS 의존성 |
| **SCD1** | ★★★☆☆ | 지질 불포화 |
| **SHMT2/MTHFD2** | ★★★☆☆ | 일탄소 대사 |
| **DGAT1** | ★★☆☆☆ | 단독 타겟 부적합, 보조 타겟으로 재포지셔닝 |
| **YARS2** | ★☆☆☆☆ | **삭제 권고** - 독성 위험 |

---

## 1. DGAT1 냉정 평가

### 과학적 근거
- DAG + acyl-CoA → TAG 합성
- 암세포는 지질독성(Lipotoxicity) 회피를 위해 DGAT1 활용
- 세포주기 정지 상태의 암세포는 PUFA를 TAG 형태로 격리하여 페롭토시스 억제
- DGAT1 억제 = PUFA를 세포막 인지질로 재배열 → 지질 과산화 → 페롭토시스 재감작

### 문제점
| Issue | Details |
|-------|---------|
| **임상 데이터 부재** | 폐암 대상 임상 시험 전무 |
| **글로벌 임상 실패** | AZ (AZD7687), Pfizer (PF-04620110) - 위장관 부작용으로 중단 |
| **DGAT2 보상** | 단일 타겟 효과 제한 |
| **선택성 문제** | 정상 소장 세포에도 영향 |

**종합:** ★★☆☆☆ - 단독 타겟 부적합. GPX4, SLC7A11 우선 고려

---

## 2. YARS2 냉정 평가

### 과학적 근거
- 미토콘드리아 티로실-tRNA 합성효소
- 미토콘드리아 단백질 번역에 필수
- YARS2 과발현 = 불량한 예후
- 대장암 모델에서 종양 성장 억제 보고

### 문제점
| Issue | Details |
|-------|---------|
| **극초기 단계** | Target Validation 단계 |
| **치명적 독성** | 심근병증, 근병증, 신경독성 위험 |
| **선택적 억제제 부재** | Hit Discovery부터 5-7년 소요 |
| **차별성 부족** | Tigecycline과 경쟁 |

**종합:** ★☆☆☆☆ - 스타트업이 감당하기엔 리스크 과대

---

## 3. 대안 타겟 분석

### 전략 A: SLC7A11 억제 (최우선 추천)

**기전:** System Xc-의 cystine/glutamate antiporter
- NSCLC에서 Nrf2 경로 활성화로 과발현
- GSH 합성에 필수 → 페롭토시스 저항

**비즈니스 강점:**
- ICD (Immunogenic Cell Death) 유발 → Cold Tumor → Hot Tumor 전환
- KEAP1 돌연변이 NSCLC (~20%) 대상
- PD-1/PD-L1 내성 환자 (~60-70%) 공략
- Keytruda/Opdivo 병용 파트너 포지셔닝 → License-out 가능성 높음

### 전략 B: FASN 억제

**기전:** De novo lipogenesis 차단
- NSCLC에서 고발현, 예후 불량
- Treg, MDSC의 지질 대사 교란 → 항종양 면역 회복

**참고:** Denifanstat (Sagimet) - 임상 2상 (NASH/암)
- 차세대 선택적 FASN 억제제 개발
- KRAS G12C + FASN 병용 시너지

### 전략 C: GLS1 억제

**기전:** 글루타민 → glutamate 전환 차단
- TCA 회로 보충, 항산화 방어, 핵산 합성에 필수
- KEAP1/NRF2 돌연변이 또는 MYC 증폭 NSCLC에서 강 의존성

**참고:** Telaglenastat/CB-839 (Calithera) - 임상 2상 병용
- 단독 요법 한계 확인 → 병용 필요
- 뇌전이 치료 틈새 시장 공략 가능

---

## 4. 병용 요법 전략

### 4.1 대사 억제제 + 면역관문억제제 (가장 유망)

| 조합 | 메커니즘 |
|------|---------|
| **SLC7A11 + PD-1** | 페롭토시스 → ICD → T세포 활성화 |
| **GLS1 + PD-1** | 글루타민 차단 → 면역 억제 세포 약화 |
| **FASN + PD-1** | 지질 감소 → T세포 기능 회복 |

### 4.2 대사 억제제 + 표적 치료제

| 조합 | 적응증 |
|------|-------|
| **FASN + KRAS G12C 억제제** | KRAS 내성 극복 |
| **GLS1 + EGFR TKI** | Osimertinib 내성 극복 |

---

## 5. 개발 로드맵

### Phase 1: Hit Discovery (0-2년, $5-15M)
- SLC7A11 또는 FASN 선택적 억제제 선정
- SBDD + AI 기반 약물 발굴
- KEAP1/NRF2 변이 NSCLC 세포주/PDX 모델 검증
- Seed/Series A 투자 유치

### Phase 2: 전임상 + IND (2-4년, $15-30M)
- ADMET 최적화 + GLP 독성
- 면역적격 마우스 모델 병용 효능
- 바이오마커 기반 환자 선별 전략
- FDA IND 신청 → Series B 유치

### Phase 3: 임상 1/2a + 파트너십 (4-7년)
- 바이오마커 기반 임상 1상
- 면역관문억제제 병용 임상 2a상
- 목표: License-out 계약금 $50-200M + 마일스톤 $500M-1B

---

## 6. 자금 조달 전략

| 단계 | 투자 규모 | 핵심 마일스톤 |
|------|-----------|-------------|
| Seed | $2-5M | 타겟 선정, Hit 도출 |
| Series A | $10-20M | 전임상 PoC |
| Series B | $30-50M | IND 신청, 임상 1상 진입 |
| Series C/L/O | $50M+ 또는_exit | 임상 2a PoC → 기술 수출 |

---

## 7. 경쟁사 현황

| Company | Pipeline | Stage | Strategy |
|---------|---------|-------|----------|
| **Sagimet/Nuvation Bio** | Denifanstat (FASN) | 임상 2상 | FASN 선도, 폐암 적응증 확대 |
| **Calithera** | Telaglenastat (GLS1) | 임상 2상 병용 | 단독 한계 → 병용 필요 |
| **Forma Therapeutics** | FT-113 (FASN) | 전임상 | 차세대 FASN 경쟁 |
| **Agios** | IDH1/2 억제제 | 상업화 | 혈액암 → 고형암 확대 |

---

## 8. 최종 권고사항

### 우선순위

| 순위 | 행동 | 기대 효과 |
|------|------|-----------|
| **1순위** | SLC7A11 선택적 억제제 개발 착수 | KEAP1/NRF2 변이 NSCLC, 빅파마 파트너십 |
| **2순위** | FASN 억제제 + KRAS 억제제 병용 전임상 | KRAS 내성 극복 |
| **3순위** | DGAT1 재포지셔닝 | 보조 타겟으로 활용, 독성 최소화 |
| **4순위** | YARS2 연구 축소 | 불필요한 자원 낭비 방지 |
| **5순위** | 바이오마커 플랫폼 구축 | 임상 성공률 향상 |

### 핵심 메시지

> "좋은 과학"과 "현명한 비즈니스 판단"의 균형이 성공의 핵심이다.  
> 타겟의 학술적 흥미보다는 임상 성공 가능성, 독성 프로파일, 환자 선별 전략, 그리고 빅파마가 원하는 것을 우선적으로 고려하라.

---

## 참고문헌

1. Fortune Business Insights. (2026). Lung Cancer Therapeutics Market Size.
2. Roots Analysis. (2026). Cancer Metabolism Based Therapeutics Market, 2025-2035.
3. Lee, H., et al. (2024). Cell cycle arrest induces lipid droplet formation and confers ferroptosis resistance. Nature Communications.
4. Pan, D., et al. (2026). DGAT1 Inhibition Induces Ferroptosis and Enhances Cancer Immunotherapy Efficacy. Cancer Research.
5. Fang, Q., et al. (2022). Targeting YARS2 suppresses colorectal cancer progression. Cancer Biology & Therapy.
6. Sung, Y., et al. (2022). Functional association of aminoacyl-tRNA synthetases with cancer. Exp Mol Med.
7. Zhou, Q. (2024). Ferroptosis in cancer: from molecular mechanisms to therapeutic applications. Nat Rev Drug Discov.
8. Researchandmarkets.com. (2026). FASN Inhibitors Market Global Forecast to 2032.
9. ClinicalTrials.gov. (2020). Telaglenastat + Pembrolizumab in KEAP1/NRF2 NSCLC (NCT04265534).

---

*Report by Manus AI · 2026-04-25*  
*For: Brown Biotech Lung Cancer Metabolism Strategy*