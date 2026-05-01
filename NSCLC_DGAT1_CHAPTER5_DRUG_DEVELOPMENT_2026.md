# Chapter 5: 차세대 DGAT1 저해제 및 PROTAC 개발

**작성일:** 2026-05-01  
**보고서:** NSCLC DGAT1 Advanced Report - Chapter 5

---

## 5. 약물 개발 전략

### 5.1 임상 단계 저해제

```
临床阶段 저해제 (수정됨 - 전문가 검토 반영):

⚠️ 중요 수정: Pradigastat를 Lead로 변경

| 저해제 | 상태 | IC50 | 장점 | 단점 |
|--------|------|------|------|------|
| **Pradigastat (LCQ908)** | Phase II/III | ~100 nM | 임상 안전성 데이터, March 2026 paper 사용, 경구 이용 가능 | potency 중간 |
| **A922500** | 전임상 | 7 nM | Potency 높음 | 인간 안전성 데이터 없음 |
| **AZD7687** | Phase I/II | ~50 nM | AstraZeneca开发 | 임상 데이터 제한적 |
| **T863** | 도구 화합물 | ~10 μM | 첫 번째 DGAT1 저해제 | drug-like properties 낮음 |

권장:
├── Lead: Pradigastat (IND 데이터 활용)
├── 백업: A922500
└── inhaled formulation: 별도 개발
```

### 5.2 Pradigastat 특성

```
Pradigastat (LCQ908, Novartis):

개발 이력:
├── Novartis 개발
├── Fatty acid oxidation disorder 치료 위해 Phase II/III 완료
├──罕见疾病 치료제 (Orphan drug)
└── oncology repurposing 가능

약물학적 특성:
├── 선택적 DGAT1 억제
├── IC50: ~100 nM (cellular)
├── 경구 생체이용률: 확인됨
├── 반감기: 4-6시간
└── 안전성 프로파일: 알려짐

2026년 3월 Cancer Research (Pan et al.):
└── Pradigastat + Ferroptosis induction → 종양 억제 확인
```

### 5.3 PROTAC 개발 전략

```
DGAT1 PROTAC 설계 (수정됨):

⚠️ Membrane Protein 문제:
DGAT1은 ER 막 단백질 → PROTAC 접근 어려움

대안 접근법:
├── AUTAC (Autophagy-targeting chimera)
├── LYTAC (Lysosome-targeting chimera)
└── 분해 경로 alternative

DGAT1 PROTAC 설계 원칙:
├── Warhead: A922500 유도체 (높은 potency)
├── Linker: PEG3-6, Alkyl chain 2-4
├── E3 리가아제: CRBN (pomalidomide) 또는 VHL
├── 길이: 12-15 Å (효율적 ubiquitination)
└── 분해 효율 최적화 필요

PROTAC 구조:
┌─────────────────────────────────────┐
│ DGAT1 binder ← Linker → E3 ligand   │
│ (A922500)      PEG      Pomalidomide │
└─────────────────────────────────────┘
```

### 5.4 소분자 SAR 최적화

```
DGAT1 저해제 SAR (Structure-Activity Relationship):

핵심 pharmacophore:
├── Carboxylic acid: DAG 결합 부위 (필수)
├── Heterocyclic core: 선택성 결정
├── 치환기: 세포 투과성 조절
└── 양전하 도입: 종양 집적 (EPR 효과)

종양 선택적 설계:
├── 낮은 pH 활성화: 종양 미세환경 (pH 6.5)
├── 효소 절단 linker: matrix metalloproteinase (MMP)
├── 프로-drug 형태: 종양에서 활성화
└── 표적 조직 선택성

ADMET 최적화:
├── Caco-2 투과성: >10⁻⁶ cm/s
├── Microsomal stability: CLint <15 μL/min/mg
├── CYP 억제: IC50 >10 μM
├── Solubility (FaSSIF): >100 μM
└── PPB: <99%
```

---

## 6. ADMET 프로파일링

### 6.1 Pradigastat ADMET

```
Pradigastat ADMET (문헌 기반):

흡수:
├── 경구 생체이용률: ~40-60% (고용량)
├── Cmax: 2-4 μg/mL (100mg 경구)
├── Tmax: 2-4 시간
└── 음식 효과: 미미

분포:
├── Vd: ~10 L/kg
├── 단백질 결합: ~95%
├── 반감기: 4-6 시간
└── 조직 분포: 간 > 폐

대사:
├── CYP3A4 의해 대사
├── 주요 대사물: 비활성
└── 반감기: 4-6 시간

배설:
├── 소변: ~60%
├──粪便: ~30%
└──unchanged drug: <10%

Drug-drug相互作用:
├── CYP3A4 기질
├── 강력한 CYP3A4 억제제 피해야 함
└── 경구 혈당강하제와 상호작용 최소화
```

### 6.2 PF14-siDGAT1 ADMET

```
PF14-siDGAT1 (핵산 약물):

흡수:
├── IV 투여 후迅速 흡수
├── 목표 조직: 폐
└── 생체이용률: 직접적인静脉주사

분포:
├── 폐 집중: 16-350배 (비폐 조직 대비)
├── 종양 vs 정상 폐: 추가 평가 필요
└── 뇌: 제한적 (BBB)

대사/消除:
├── 핵산 분해: 일반적인 nucleotides
├── 반감기: 24-48 시간 (조직)
└── 최종 분해물: nucleotides + peptides

안전성:
├── 면역원성: 최소화 ( chemical modification)
├── off-target: minimal
└── mitochondrial toxicity: low
```

---

## 7. 독성 프로파일

### 7.1 Systemic DGAT1 Inhibition 독성

```
DGAT1 전신 억제의 잠재적毒性:

위장 독성 (GI Toxicity):
├── 설사, 지방변, 소화不良
├── 창자 DGAT1이 지질 흡수에 필수
├── 임상 데이터:輕도～中等도
└── 관리: 점진적 용량 증가

간 독성:
├── 간에서 TG 합성 담당
├── 간 기능 변화 가능성
├── 모니터링: ALT, AST, bilirubin
└── 중증 사례: 거의 없음

대사 이상:
├── 혈중 TG 변화
├── 인슐린 저항성 가능성
├── 고콜레스테롤혈증
└── 대사 증후군 관리

발생毒性:
├── 태아毒性: 확인 안 됨
├── 임신 카테고리: C
└── 임산부 제외 필요

관리 전략:
├── 폐 선택적 전달 (PF14)
├── inhaled formulation
├── 저용량 병용 요법
└── biomarker 기반 환자 선별
```

### 7.2 위장 관리 전략

```
위장 부작용 관리:

예방:
├── 낮은 용량부터 시작
├── 식사와 함께 투여
├── 점진적 용량 증가
└── 위장약 병용 (선택적)

대상 환자 선별:
├── 위장病史 주의
├── 이전 위장 수술력 확인
├── baseline 위장 기능 평가
└── 위험/이득 평가

대안적 접근:
├── PF14-siDGAT1 (흡입)
├── inhaled 소분자
├── 주 2-3회 투여 (매일 아니orum)
└── 프로-drug 형태

임상 모니터링:
├── 위장 증상 일지
├── 체중 변화
├── 영양 상태 평가
└── 필요시 영양사 상담
```

---

## 8. 약물相互作用

### 8.1 Pradigastat drug-drug相互作用

```
DDI 프로파일:

CYP3A4 기질:
├── 강한 CYP3A4 억제제: ketoconazole, itraconazole
│   └── Pradigastat 농도 증가 가능
├── 중간/약한 CYP3A4 억제제: 주의
└── CYP3A4 유도제: 효능 감소 가능

병용 시 주의:
├── 항응고제 (warfarin): INR 모니터링
├── 스타틴: CK 모니터링
├── 당뇨병 약물: 저혈당 위험
└── Immunosuppressants: 감염 위험

병용 권장:
├── ✓ 항PD-1/PD-L1: synergistic
├── ✓ SLC7A11 저해제: synergistic
├── ✓ 항응고제: 주의하며 모니터링
└── ✗ 강하게 CYP3A4 억제하는 약물: 피하거나 용량 조절
```

### 8.2 PF14-siDGAT1 drug-drugInteractions

```
핵산 약물의 DDI:

일반적으로 핵산 약물은:
├── CYP450 효소와 상호작용 드묾
├── 약물 수송체와 상호작용 드묾
└── 약동학적으로 독립적

그러나:
├──免疫调节제와 병용 시 면역 활성화
├── 스테로이드와 동시 투여 시 효과 변화
└── 항응고제와 출혈 위험 (주사部位)

관리:
├── 병용 약물 목록 확인
├── 면역 반응 모니터링
├── 주사部位 출혈 확인
└── 필요시 용량 조절
```

---

## 9. 결론 및 권고

### 9.1 약물 개발 로드맵

```
약물 개발 경로:

1단계 (즉시):
├── Pradigastat 확보 (Novartis 문의)
├── A922500 백업 확보
├── In vitro 효능 테스트
└── PF14-siDGAT1 제조

2단계 (3-6개월):
├── Pradigastat dose-response (NSCLC 세포)
├── PF14-siDGAT1 효능 검증
├── 조합 시너지 확인 (Pradigastat + Anti-PD1)
└── In vivo PoC (老鼠)

3단계 (6-12개월):
├── PROTAC/AUTAC design (선택적)
├── ADMET profiling
├── GLP toxicology 준비
└── IND filing

4단계 (12개월+):
├── IND approval
├── Phase I trial
└── Phase II 준비
```

### 9.2 핵심 권고사항

```
약물 개발 핵심 권고:

1. Lead 화합물: Pradigastat
   └── 임상 데이터 활용, repurposing 경로

2. 전달 시스템: PF14-siDGAT1
   └── 폐 특이적, 낮은 전신 독성

3. 조합 전략: Pradigastat + Anti-PD1
   └── highest priority based on March 2026 data

4. PROTAC: Membrane protein으로 도전적
   └── AUTAC/LYTAC alternative 고려

5. 환자 선별: 필수
   └── biomarker 기반 선별

6. 위장 독성 관리:
   └── inhaled formulation 고려
```

---

*Chapter 5: arp-v24/NSCLC_DGAT1_CHAPTER5_DRUG_DEVELOPMENT_2026.md*
*작성일: 2026-05-01*