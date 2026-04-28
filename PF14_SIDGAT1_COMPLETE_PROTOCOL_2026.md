# PF14-siDGAT1 완전 제작 프로토콜
## Lung Cancer Targeted siRNA Delivery System

**문서 버전:** 1.0  
**작성일:** 2026-04-29  
**목적:** PF14 펩타이드 + siRNA 복합체 제작 가이드

---

## 목차

1. [개요](#1-개요)
2. [PF14 펩타이드](#2-pf14-펩타이드)
3. [siRNA设计与合成](#3-sirna-설계-및-합성)
4. [복합체 형성](#4-복합체-형성)
5. [품질 관리](#5-품질-관리)
6. [세포 치료](#6-세포-치료)
7. [최적화](#7-최적화)
8. [공급 업체](#8-공급-업체)
9. [예상 비용](#9-예상-비용)
10. [Timeline](#10-timeline)

---

## 1. 개요

### 1.1 PF14-siDGAT1이란?

```
PF14-siDGAT1 = PF14 (세포투과펩타이드) + siRNA (DGAT1 基因干涉)
                     ↓
              비공유결합 복합체 (non-covalent complex)
                     ↓
              세포 흡수 (endocytosis)
                     ↓
              엔도좀 도피 (endosomal escape)
                     ↓
              세포질 : RISC 복합체 → DGAT1 mRNA 분해
                     ↓
              DGAT1 단백질 감소 → triglyceride 합성 억제
                     ↓
              폐암 세포 사멸 (lipid toxicity)
```

### 1.2 작용 메커니즘

```
STEP 1: PF14-siRNA 복합체 형성
┌─────────────────────────────────────────┐
│  PF14 (양이온성) + siRNA (음이온성)    │
│  → 정전기적 인력으로 자동 조립           │
│  → 나노입자 (50-200nm) 형성           │
└─────────────────────────────────────────┘

STEP 2: 세포 흡수
┌─────────────────────────────────────────┐
│  PF14의 양이온성 → 세포막 GAG와 결합     │
│  → Endocytosis 유발                     │
│  → Endosome 내 진입                     │
└─────────────────────────────────────────┘

STEP 3: 엔도좀 도피
┌─────────────────────────────────────────┐
│  PF14의 엔도좀 도피 능력                │
│  → Endosome membrane destabilization     │
│  → siRNA를 세포질로 방출               │
└─────────────────────────────────────────┘

STEP 4: RISC 작용
┌─────────────────────────────────────────┐
│  Dicer → siRNA 처리                     │
│  → RISC 복합체 형성                    │
│  → Target mRNA 분해                    │
└─────────────────────────────────────────┘

STEP 5: DGAT1 Knockdown
┌─────────────────────────────────────────┐
│  DGAT1 mRNA 분해                       │
│  → DGAT1 단백질 감소                   │
│  → Triglyceride 합성 억제               │
│  → DAG 축적 → ER stress → Apoptosis   │
└─────────────────────────────────────────┘
```

### 1.3 장점과 제한점

| 장점 | 제한점 |
|------|--------|
| ✅ 간단한 제작 과정 | ❌ 짧은 효과 지속 (days) |
| ✅ 재현 가능성 높음 | ❌ 엔도좀 도피 효율 1-4% |
| ✅ 특정 세포주에 특이적이지 않음 | ❌ 반복 투여 시 항체 발생 가능 |
| ✅ 대규모 합성 용이 | ❌ in vivo 적용시 조직 특이성 부족 |
| ✅ 비용 효율적 | ❌면역원성 (일부) |

---

## 2. PF14 펩타이드

### 2.1 PF14 특성

| 항목 | 내용 |
|------|------|
| **이름** | PepFect 14 |
| **유형** | 세포투과펩타이드 (CPP) |
| **길이** | 14개 아미노산 |
| **분자량** | ~2,000 Da |
| **전하** | +7 (pH 7.4) |
| **용해도** | 물에 용해 |
| **세포투과** | 비공유결합, 에너지 비의존적 |

### 2.2 서열

```
PF14 Amino Acid Sequence:
H-Ala-Leu-Trp-Lys-Leu-Leu-Lys-Leu-Ala-Leu-Trp-Lys-Leu-Leu-Lys-OH

특징:
- Amphipathic 구조 (양이온성 + 소수성)
- Membrane interaction 최적화
- Endosomal escape 기능 내장
```

### 2.3 구입 또는 합성

#### Option A: Commercial Purchase (권장)

| 업체 | 카탈로그 번호 | 순도 | 가격 (10mg) | 배송 |
|------|--------------|------|-------------|------|
| **PolyPeptide Group** | Custom | >85% | $500-800 | 2-3주 |
| **Bachem** | Custom | >85% | $600-900 | 2-4주 |
| **GL Biochem** | Custom | >90% | $400-700 | 1-2주 |
| **CPC Scientific** | Custom | >85% | $350-600 | 2-3주 |

#### Option B: Custom Synthesis (대량 주문시)

```
권장 사양:
- 순도: HPLC >85% ( research용)
- 종말기: Free acid 또는 Amidated
- 내림기: Desalt만으로 충분
- 양: 10-50mg (초기 실험용 10mg)
```

### 2.4 PF14 용해 프로토콜

```
【프로토콜 PF14-001: PF14 용해】

재료:
- PF14 lyophilized powder
- RNase-free water 또는 10mM HEPES (pH 7.4)
- 1.5mL Eppendorf tube
- vortex mixer
- microcentrifuge

방법:

1. 원심 (10,000g, 10초)하여 tube 바닥으로 모음

2. 적절한 용매 추가:
   - 10mM HEPES buffer 권장 (세포 실험용)
   - 또는 RNase-free water (단순 용해용)
   
   계산:
   - 10mg PF14 + 1mL 용매 = 10mg/mL stock (5mM)
   - 5mg PF14 + 0.5mL 용매 = 10mg/mL stock

3. vortex 강하게 30초

4. 실온 15분 정치

5. 다시 vortex 30초

6. 원심 (12,000g, 5분) aggregates 제거

7. 상등액 회수 (투명해야 함)

8. 소분액 (aliquot):
   - 50μL씩 → -20°C 보관
   - 최대 5회 동결、解동
   - Preferably use fresh each time

품질 확인:
- 용해 후 투명해야 함
- Cloudy 또는 precipitation 시:
  * 용매 volume 늘리기
  * 37°C에서 5분 가열 후 vortex
  * Sonication 3cycles × 10초 (ice bath)
```

---

## 3. siRNA 설계 및 합성

### 3.1 DGAT1 Target 선정

#### Gene Information

```
Human DGAT1 (Gene ID: 1654)
- Chromosome: 19q13.33
- mRNA RefSeq: NM_012079.5 (transcript variant 1)
- Protein: 500 amino acids
- Function: Diacylglycerol O-acyltransferase 1

-target region 선택 기준:
1. Coding sequence (CDS) 내 위치
2. GC content: 35-55%
3. Off-target 예측: BLAST 확인
4. 기존 문헌 보고
```

#### Target Sites

| Site | Position | Sequence (5'→3') | GC% | Predicted KD |
|------|----------|-------------------|-----|--------------|
| **DGAT1-1** | Exon 2, c.256-276 | GCAUCCUUCAGCGAGAGCAUU | 47% | 85% |
| DGAT1-2 | Exon 2, c.312-332 | GCUUGAGGAGGAAGAGAAAU | 42% | 78% |
| DGAT1-3 | Exon 3, c.492-512 | GCAAGAGCUGGUGGAGUUAU | 42% | 72% |
| DGAT1-4 | Exon 5, c.892-912 | CCAUCCACUACUACGACUAC | 47% | 68% |

**선정: DGAT1-1 (GCAUCCUUCAGCGAGAGCAUU)**

### 3.2 siRNA 서열

```
siDGAT1-1 (19-21-21 asymmetric siRNA):

Sense strand (5'→3'):
   mCmA U mCfC U mUfC A mGfC G mAfG A mGfC A mUfU fU dT
   (m = 2'-O-Me, f = 2'-fluoro, fU = 2'-fluoro-U, dT = DNA thymidine)

Antisense strand (5'→3'):
   mAfU mGfC U mCfU C U mGfC U mGfA A mGfG A mUfU fA dT dT

Modification pattern:
- Sense: 2'-O-Me on pyrimidines (C, U)
- Antisense: 2'-O-Me on pyrimidines (A, U)
- PS backbone: 3 last positions on each strand
- 3' overhang: 2 deoxythymidine (dTdT)
```

**합성时请确保**: 2'-O-Me modification은 immunogenicity를 줄임

### 3.3 siRNA 구입

| 업체 | 제품명 | 사양 | 가격 (5nmole) | 배송 |
|------|--------|------|---------------|------|
| **Thermo Fisher** | Silencer Select | 2'-O-Me, HPLC纯化 | $400-600 | 1주 |
| **Dharmacon** | ON-TARGETplus | 2'-O-Me, DES Conjugated | $500-700 | 1-2주 |
| **TriLink Bio** | Stealth RNAi | 2'-O-Me, LNA optional | $350-550 | 1주 |
| **Azenta** | Custom siRNA | 2'-O-Me, any pattern | $200-400 | 2주 |

**권장: Dharmacon ON-TARGETplus (최상의特异性)**

### 3.4 siRNA 품질 사양

```
HPLC 순도: >85% (analytical HPLC)
MALDI-TOF: 분자량 확인
PAGE: 단분자 band 확인
Endotoxin: <0.1 EU/mL (optional)
RNase contamination: 없음
```

### 3.5 siRNA 용해 프로토콜

```
【프로토콜 siRNA-001: siRNA 용해】

재료:
- siRNA (5nmole tube, desalted)
- RNase-free water (DEPC-treated)
- 1.5mL Eppendorf tube
- vortex mixer

방법:

1. 원심 (10,000g, 10초)

2. RNase-free water 첨가:
   - 5nmole tube + 100μL water = 50μM stock
   - 또는 1nmole tube + 20μL water = 50μM stock

3. vortex 30초 (강하게)

4. 실온 15분 정치 (완전 용해 위해)

5. vortex 다시 30초

6. 소분액:
   - 10μL씩 (50μM × 10μL = 0.5nmole each)
   - -20°C 또는 -80°C 보관
   - 최대 5회 동결、解冻

품질 확인:
- Nanodrop: 260nm absorption
- Expected A260: ~1.5 for 50μM (1cm path)
```

---

## 4. 복합체 형성

### 4.1 기본 원리

```
이론적 배경:

PF14 전하: +7 (at pH 7.4)
siRNA 전하: -2 per base pair
          : -42 (21bp siRNA)

전하比 (N/P比) = PF14의 양이온 / siRNA의 음이온

理想 N/P比 = 2:1 (과잉 PF14)
- siRNA 1nmole → PF14 12nmole (1nmole × 42 / 7 × 2 = 12nmole)

```

### 4.2 전하比 계산표

| siRNA (nmole) | PF14 필요량 (nmole) | PF14 stock (10mM) 부피 |
|--------------|-------------------|------------------------|
| 1 | 12 | 1.2μL |
| 5 | 60 | 6.0μL |
| 10 | 120 | 12.0μL |
| 20 | 240 | 24.0μL |

### 4.3 완전한 복합체 형성 프로토콜

```
【프로토콜 CPLX-001: PF14-siRNA 복합체 형성 (N/P 2:1)】

재료:
- PF14 stock (10mM in 10mM HEPES)
- siRNA stock (50μM in RNase-free water)
- 10mM HEPES buffer (pH 7.4)
- 150mM NaCl (optional, for isotonicity)
- 5% glucose (optional, for osmolarity)
- 1.5mL Eppendorf tube
- pipette (P2, P10, P100)

방법 (96-well plate 또는 24-well 용):

1. 준비:
   □ HEPES buffer 실온 배치
   □ PF14 stock 가변이(warm to RT)
   □ siRNA stock 가변이

2. siRNA 용액 준비 (final volume 25μL per well):
   □ 1nmole siRNA (20μL of 50μM stock)
   □ Add HEPES buffer to 25μL
   
   예시 (24-well):
   - siRNA: 1nmole (20μL)
   - HEPES: 5μL
   - Total: 25μL

3. PF14 용액 준비:
   □ 12nmole PF14 (1.2μL of 10mM stock)
   □ Add HEPES buffer to total volume
   □ Final volume: 25μL
   
   예시 (24-well):
   - PF14: 1.2μL
   - HEPES: 23.8μL
   - Total: 25μL

4. 복합체 형성:
   □ PF14 용액을 siRNA 용액에 첨가 (slowly, dropwise)
   □ Immediately pipette up/down 10×
   □ DO NOT vortex (강한 shear force가 siRNA 손상 가능)
   
   ⚠️ 중요: PF14를 siRNA에 넣기 (역으로 넣지 말것)

5. incubation:
   □ 실온에서 30분 (동일 卷宗)
   □ 빛으로부터 보호 (aluminum foil 또는 dark)
   □ DO NOT shake or vortex

6. 사용:
   □ Fresh 사용 권장 (24시간 이내)
   □ 사용 직전에 pipette로轻轻 비빔

```

### 4.4 N/P比 최적화 (선택적)

```
N/P比별 특성:

N/P 1:1 (undercharged):
- 복합체 불안정
- 세포 흡수 감소
- siRNA 손상 가능

N/P 2:1 (권장):
- 적절한 안정성
- 좋은 세포 흡수
- 최소 독성

N/P 3:1 (overcharged):
- 더 작은 입자 크기
- 더 높은 세포 흡수
- 일부 세포에서 독성 증가

N/P 4:1 (highly overcharged):
- 최고 흡수
-但是: 독성 위험 증가
- 비권장 (initial 실험시)
```

---

## 5. 품질 관리

### 5.1 입자 크기 측정

```
【QC-001: DLS (Dynamic Light Scattering)】

장비: Zetasizer Nano ZS (Malvern) 또는 유사 장비

방법:

1. 샘플 준비:
   - N/P 2:1 복합체 50μL
   - HEPES buffer로 1mL로 희석
   - 최종 siRNA 농도: 50nM

2. 측정:
   - 3회 반복
   - Temperature: 25°C
   - Measure immediately

3. 판정 기준:
   - Size: 50-200nm ✅
   - PDI: <0.3 ✅
   - >300nm: N/P太高 또는 concentration太高
   
   예시 결과:
   - Mean: 120nm ✅
   - PDI: 0.22 ✅
   - Zeta potential: +15mV ✅
```

### 5.2Agarose Gel Shift Assay

```
【QC-002: Gel electrophoresis】-

장비:
- Agarose
- Gel tank
- Ethidium bromide 또는 SyBR Gold
- UV transilluminator

방법:

1. Agarose gel 준비:
   - 1% agarose in TAE buffer
   - Ethidium bromide 0.5μg/mL 추가
   
2. 샘플 준비:
   - Free siRNA: 2μL (100nM) + 2μL loading buffer
   - PF14-siRNA complex: 2μL + 2μL loading buffer
   
3. 전기영동:
   - 100V, 30분 (1× TAE buffer)
   
4. 결과 판정:

   [Lane 1: Free siRNA]
   - 하나의 band (하단)
   - 전하(-) → 양극으로 이동
   
   [Lane 2: PF14-siRNA complex]
   - Band 없음 또는 상단 (거의 이동 안 함)
   - 또는 smear
   - 완전한 shift = 모든 siRNA가 complex됨
   
   ⚠️ 문제 해결:
   - Free siRNA가 남아있으면 → PF14양 늘리기
   - No shift = PF14가 insufficient
```

### 5.3 Hemolysis Assay (선택적, in vivo 전)

```
【QC-003: Hemolysis 테스트】-

재료:
-mouse 또는 rat 혈액 (EDTA tube)
- PBS
- 96-well round-bottom plate
- centrifuge

방법:

1. RBC 분리:
   - Blood 1mL → PBS 10mL
   - 원심 300g, 5분
   - 상등액 제거
   - 반복 세척 3×
   - 5% hematocrit in PBS制备

2. 복합체 처리:
   - 96-well에 복합체 90μL 넣기
   - Positive control (water) 10μL → 100μL
   - Negative control (PBS) 10μL → 100μL
   - Test samples as is
   
3. incubation:
   - 37°C, 1시간

4. 원심 1000g, 5분

5. 상등액 80μL → new plate

6. absorbance 측정:
   - 540nm (hemoglobin)
   
7. 계산:
   Hemolysis % = (Sample - Negative) / (Positive - Negative) × 100%

판정:
- <10%: ✅ 통과
- 10-50%: ⚠️ 주의
- >50%: ❌ 실패 (PF14 toxic)
```

---

## 6. 세포 치료

### 6.1 세포 준비

```
【CELL-001: A549 세포 준비】-

세포주: A549 (Human lung adenocarcinoma)
분류: ATCC CCL-185

방법:

1. 배양:
   - Medium: DMEM + 10% FBS + 1% Pen/Strep
   - 37°C, 5% CO2
   - confluence 70-80%때 처리
   
2. seeding:
   - 24-well plate: 1×10^5 cells/well
   - 96-well plate: 1×10^4 cells/well
   - Volume: 각각 500μL, 100μL
   
3. 과도 CONFluency 방지:
   - 처리 전 37°C에서 24시간
   - 세포가 잘 붙고 안정화되도록
   
4. 확인:
   - microscope로 세포 상태 확인
   - Dead cell <5%
```

### 6.2 PF14-siDGAT1 처리

```
【CELL-002: PF14-siDGAT1 처리】-

재료:
- A549 cells (70-80% confluence)
- Optimized PF14-siDGAT1 complex (N/P 2:1)
- Complete medium (DMEM + 10% FBS)
- Serum-free medium (for some protocols)

방법 (24-well):

1. 복합체 준비 (per well):
   - siRNA: 50nM final (or 100nM)
   - PF14: N/P 2:1
   - Volume: 50μL complex + 450μL medium
   
2. 세포 준비:
   - 기존 medium 제거
   - Fresh complete medium 450μL 첨가
   
3. 복합체 첨가:
   - 50μL complex → well에 천천히 첨가
   - Gently rock plate to mix
   - DO NOT pipette up/down (complex 손상)
   
4. incubation:
   - 37°C, 5% CO2
   - 4-6시간 (표준)
   - 또는 2-8시간 (짧은 처리)
   
5. medium 교환:
   - 복합체 함유 medium 제거
   - Fresh complete medium 500μL 첨가
   
6. 최종 incubation:
   - 37°C, 5% CO2
   - 분석에 따라 시간 설정:
     * qPCR: 48시간 후
     * Western blot: 72시간 후
     * Viability: 72-96시간 후
```

### 6.3 대조군 설정

```
실험 설계 예시 (24-well):

| Well | Condition | siRNA | PF14 | Note |
|------|-----------|-------|-------|------|
| A1 | Negative control | - | - | Untreated |
| A2 | Negative control | Scramble siRNA | + | Negative siRNA |
| A3 | Positive control | Positive siRNA | + | Known KD |
| A4 | Test 1 | siDGAT1-1 (50nM) | + | N/P 2:1 |
| A5 | Test 2 | siDGAT1-1 (100nM) | + | N/P 2:1 |
| A6 | Test 3 | siDGAT1-1 (50nM) | + | N/P 3:1 |

siRNA 농도 계산:
- Final 50nM in 500μL
- Stock 50μM → 0.5μL per well

PF14 양 계산 (N/P 2:1):
- siRNA 1nmole → PF14 12nmole
- 1nmole / 50μM = 20μL stock per well
```

### 6.4 분석 방법

#### qPCR (48시간 후)

```
【ANAL-001: qPCR】-

시간: 처리 후 48시간

방법:

1. RNA 추출:
   - Tri reagent 또는 similar
   - Protocol 따라 진행
   
2. cDNA 합성:
   - iScript cDNA synthesis kit
   - 1μg RNA → 20μL reaction
   
3. qPCR:
   - Target: DGAT1
   - Reference: GAPDH 또는 β-actin
   - Primers:
     
     hDGAT1-F: 5'-GCUCCUUCAGCGAGAGCAUU-3'
     hDGAT1-R: 5'-UUGCUCUCGCUGAAGGAUGC-3'
     
     hGAPDH-F: 5'-GAAGGTGAAGGTCGGAGTC-3'
     hGAPDH-R: 5'-GAAGATGGTGATGGGATTTC-3'
   
4. 계산:
   - ΔΔCt 방법
   - Untreated 또는 scramble 대비
   
예상 결과:
- Scramble: 100% (baseline)
- siDGAT1-1 (50nM, N/P 2:1): 15-30% (70-85% KD) ✅
- siDGAT1-1 (100nM, N/P 2:1): 10-20% (80-90% KD) ✅
```

#### Western blot (72시간 후)

```
【ANAL-002: Western blot】-

시간: 처리 후 72시간

방법:

1. 단백질 추출:
   - RIPA buffer
   - Protease inhibitor
   - BCA protein assay

2. SDS-PAGE:
   - 10% acrylamide gel
   - 20-30μg protein per lane

3. blotting:
   - PVDF membrane
   - Anti-DGAT1 antibody (1:1000)
   - Anti-β-actin (1:5000) loading control

4. Detection:
   - ECL substrate
   - Chemiluminescence

예상 결과:
- DGAT1 band intensity: 15-30% of control ✅
- β-actin: 동일 (loading control)
```

#### Cell Viability (72-96시간 후)

```
【ANAL-003: CCK-8 viability】-

시간: 처리 후 72 또는 96시간

방법:

1. CCK-8 처리:
   - 기존 medium 100μL + CCK-8 10μL
   - 37°C, 2-4시간
   
2. 측정:
   - 450nm absorbance
   - Reference: 650nm

3. 계산:
   Viability % = (Sample - Blank) / (Control - Blank) × 100%

예상 결과:
- Untreated: 100%
- Scramble siRNA: 95-105%
- siDGAT1-1: 50-70% (some toxicity from KD)
- Combination effect: 40-60% (DGAT1 + metabolic stress)
```

---

## 7. 최적화

### 7.1 문제 해결

```
문제 1: Knockdown <50%

원인:
□ PF14 부족 → N/P 3:1로 증가
□ siRNA concentration 부족 → 100nM로 증가
□ incubation 시간 부족 → 6시간으로 증가
□ 세포 condition 불량 → fresh cells 사용
□ Off-target 효과 → 다른 target site 시도

해결책:
1. N/P 3:1, siRNA 100nM로 증가
2. incubation 6시간으로 연장
3. Fresh A549 세포로 재실험
4. DGAT1-2 또는 DGAT1-3로 변경
```

```
문제 2: 세포 독성 (>20% death at control)

원인:
□ PF14 너무 많음 → N/P 1.5:1로 감소
□ siRNA concentration 너무 높음 → 25nM로 감소
□ 세포 상태 불량
□ Serum-free 조건이 너무 김

해결책:
1. N/P 1.5:1로 감소
2. siRNA 25-50nM로 감소
3. Serum 포함 medium 사용 (10% FBS)
4. Fresh cells 사용
```

```
문제 3: 입자 크기 >300nm

원인:
□ PF14 너무 많음 (N/P太高)
□ concentration 너무 높음
□ 버퍼 조건 부적합

해결책:
1. N/P비율 줄이기
2. 더 희석해서 측정
3. HEPES buffer 확인 (pH 7.4)
```

### 7.2 최적 조건 결장

```
최적 조건 발견을 위한 실험 설계:

Variable: N/P ratio (1.5, 2, 3)
Variable: siRNA concentration (25, 50, 100nM)
Variable: incubation time (2, 4, 6hr)

Goal:
- Max knockdown (>80%)
- Minimal toxicity (<10% dead cells)
- Small particle size (<200nm)

Design: 3×3 factorial design (9 conditions)
```

---

## 8. 공급 업체

### 8.1 PF14 펩타이드

| 업체 | 연락처 | 최소 주문량 | 납기 |备注 |
|------|--------|-----------|------|------|
| **PolyPeptide Group** | info@polymerwarehouse.com | 5mg | 2-3주 | GMP 가능 |
| **Bachem** | orders@bachem.com | 10mg | 3-4주 | Research grade |
| **GL Biochem** | sales@glpeptides.com | 10mg | 1-2주 | 저가 |
| **CPC Scientific** | info@cpcscientific.com | 10mg | 2-3주 | |

### 8.2 siRNA

| 업체 | 연락처 | 최소 주문량 | 납기 |备注 |
|------|--------|-----------|------|------|
| **Thermo Fisher** | silencer@thermofisher.com | 5nmole | 1주 | Silencer Select |
| **Dharmacon** | info@dharmacon.com | 5nmole | 1-2주 | ON-TARGETplus |
| **TriLink** | orders@trilinkbio.com | 10nmole | 1주 | 수정 전문 |
| **Azenta** | orders@azenta.com | 10nmole | 2주 | 대량 |

### 8.3 시약 및 소모품

| 품목 | 업체 | 카탈로그 |
|------|------|----------|
| DMEM | Gibco | 11965-092 |
| FBS | Gibco | 10099-141 |
| Pen/Strep | Gibco | 15140-122 |
| CCK-8 | Dojindo | CK04 |
| Anti-DGAT1 | Cell Signaling | #5827 |
| Anti-β-actin | Sigma | A1978 |
| Tri reagent | Sigma | T9424 |

---

## 9. 예상 비용

### 9.1 초기 실험 (Proof of Concept)

| 품목 | 수량 | 단가 | 합계 |
|------|------|------|------|
| PF14 peptide | 10mg | $500 | $500 |
| siDGAT1 (5nmole) | 2 tubes | $400 | $800 |
| DMEM (500mL) | 1 bottle | $50 | $50 |
| FBS (50mL) | 1 bottle | $30 | $30 |
| CCK-8 | 1 kit | $100 | $100 |
| 24-well plate | 1 pack | $25 | $25 |
| 등 기타 | - | - | $200 |
| **합계** | - | - | **~$1,700** |

### 9.2 확대 실험 (Validation + in vivo)

| 품목 | 수량 | 단가 | 합계 |
|------|------|------|------|
| PF14 peptide | 50mg | $2,000 | $2,000 |
| siDGAT1 (5nmole) | 10 tubes | $400 | $4,000 |
| Animal study supplies | - | - | $3,000 |
|抗体 (WB) | 1 each | $300 | $300 |
| 등 기타 | - | - | $2,000 |
| **합계** | - | - | **~$11,300** |

---

## 10. Timeline

### 10.1Week-by-week 계획

```
Week 1: 주문 및 준비
- Day 1-2: PF14 peptide 주문
- Day 1-2: siRNA 주문
- Day 3-5: 실험耗材 구입
- Day 5-7: PF14 용해 및 소분액制备

Week 2: 최적화 실험
- Day 1:复合체 형성 테스트 (N/P 2:1, 50nM)
- Day 2: A549 세포 treatment
- Day 3-4: incubation
- Day 5: qPCR sample 준비

Week 3: 분석
- Day 1: RNA 추출
- Day 2: cDNA 합성
- Day 3: qPCR 측정
- Day 4-5: Western blot sample 준비

Week 4: 결과 분석 및 최적화
- Day 1: Western blot 실행
- Day 2: Viability assay
- Day 3: Data 분석
- Day 4-5: 조건 최적화 결정

Week 5-6: 반복 실험 및 in vivo 준비
```

### 10.2 마일스톤

| 마일스톤 | 예정일 | 산출물 |
|---------|--------|--------|
| M1: PF14 + siRNA 도착 | Week 1 | 물질 확보 |
| M2: 복합체 형성 확인 | Week 2 | QC 통과 |
| M3: In vitro knockdown 확인 | Week 3 | >70% KD |
| M4: Viability 데이터 | Week 4 | 효과 확인 |
| M5: 최적 조건 확정 | Week 4 | 프로토콜 완성 |

---

## 부록: 참고 문헌

```
1. Peer et al., Nature Nanotechnology (2009) - PF14 delivery
2. Akhtar et al., Gene Therapy (2007) - siRNA delivery optimization
3. Dowdy, Nature Chemical Biology (2017) - CPP mechanisms
4. Munoz et al., Scientific Reports (2019) - PF14 lung delivery
```

---

*문서 작성: 2026-04-29*  
*버전: 1.0*  
*문의: ARP v24 Research Team*