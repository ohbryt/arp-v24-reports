# ERRγ (ESRRG) Drug Discovery Report
## ARP v24 Research Pipeline

**Generated:** 2026-04-23  
**Gene:** ESRRG (Estrogen-related Receptor Gamma)  
**Protein Class:** Nuclear Receptor (NR3B1)  
**Researcher:** ARP v24 + Groq LLM  

---

## 1. Executive Summary

ERRγ (Estrogen-related receptor gamma, ESRRG)는 핵호르몬 수용체 수퍼패밀리에 속하는 전사인자로, 미토콘드리아 생합성, 근육 섬유 유형 결정, 심장 대사 조절, 갈색지방 조직(BAT) 기능, 대사 항상성 등을 조절하는 핵심 인자입니다.

### 치료 적응증

| 적응증 | 기전 | 개발 단계 |
|--------|------|----------|
| **근육손실증 (Sarcopenia)** | 근육량 및 힘 유지 | 전임상 |
| **심장부전 (Heart Failure)** | 심장 대사 개선 | 전임상 |
| **대사질환** | 인슐린 저항성, 비만 | 연구단계 |
| **신경퇴행** | 미토콘드리아 기능 개선 | 연구단계 |

---

## 2. ERRγ Pathophysiology

### 2.1 기본 특성

| Property | Value |
|-----------|-------|
| **Gene Symbol** | ESRRG |
| **Protein Name** | Estrogen-related receptor gamma |
| **Alias** | ERR3, NR3B1 |
| **Family** | Nuclear receptor, Steroid hormone receptor |
| **Chromosome** | 1q41 |
| **Expression** | 심장, 근육, 뇌, 고환, 갈색지방 |

### 2.2 핵심 기전

```
ERRγ의 주요 조절 기능:

1. 미토콘드리아 생합성
   - PGC-1α/β와 협조
   - NRF-1/2, Tfam 활성화
   → ATP 생산 증가

2. 근육 섬유 유형 결정
   - Type I (지치型) 섬유 촉진
   - Oxidative fibers 증가
   → 근육 지구력 향상

3. 심장 대사
   - 심근 세포의 에너지 대사 조절
   - 지방산 산화 촉진
   → 심장 기능 개선

4. 갈색지방조직 (BAT)
   - UCP1 발현 조절
   - 열발생 (Thermogenesis)
   → 에너지 소비 증가
```

---

## 3. Novel Drug Candidates

### 3.1 ERRγ Agonists (작동제)

| 화합물 | Company | 단계 | Mechanism | Status |
|--------|---------|------|-----------|--------|
| **GSK4716** | GSK | Research | ERRγ agonist | 최초의 합성 ERR agonist |
| **GSK9089** | GSK | Research | ERRγ agonist | GSK4716 유도체, 더 potent |
| **DY131** | Fisher | Research | ERRβ/γ 선택적 agonist | 연구 도구 |
| **SLN-PX-2** | Stanford | Preclinical | 심장 보호 | 미토콘드리아 보호 효과 |
| **Phenolic acyl hydrazones** | Various | Discovery | ERRβ/γ agonist | SAR 연구 진행중 |

### 3.2 ERRγ Inverse Agonists (역작동제)

| 화합물 | Company | 단계 | Mechanism | Status |
|--------|---------|------|-----------|--------|
| **GSK5182** | GSK | Research | ERRγ 역작동제 | Tamoxifen analog |
| **HX-531** | - | Preclinical | 역작용제 | 항비만 효과 |
| **新型 역작용제** | - | Discovery | Novel binding trench | 2025 연구 (Frontiers) |

### 3.3 Agonist vs Inverse Agonist

| Type | Effect | Therapeutic Use |
|------|--------|-----------------|
| **Agonist** | ERRγ 활성화 | 근육량 증가, 심장 보호, 대사 개선 |
| **Inverse Agonist** | ERRγ 억제 | 항종양 (일부 종양에서 ERRγ 과발현) |

---

## 4. SAR (Structure-Activity Relationship)

### 4.1 GSK4716 기반 유도체

| 화합물 | R1 | R2 | Activity | 선택성 |
|--------|-----|-----|----------|--------|
| GSK4716 | Phenol | -OCH3 | ++ | ERRγ > ERRα |
| GSK9089 | Phenol | -Cl | +++ | Highly selective |
| DY131 | Acyl hydrazone | -Br | ++ | ERRβ/γ 선택적 |

### 4.2 결합 특성

```
GSK4716 binding:
- ERRγ LBD (Ligand Binding Domain)에 결합
- Phe306, Ala327과 hydrophobic interactions
- Phe327과 hydrogen bonding
- RIP140 peptide와 공동 결합 가능 (2GPP 구조)
```

### 4.3 결합 친화도 개선 전략

| Strategy | Approach | Expected Improvement |
|----------|----------|---------------------|
| **Phenyl ring 치환** | Halogenation | binding affinity ↑ |
| **Acyl hydrazone 최적화** | Chain length 조절 | 선택성 ↑ |
| **Novel binding trench** | Allosteric site 타겟 | 신약 발견 가능 |

---

## 5. Molecular Mechanism

### 5.1 ERRγ Signaling Pathway

```
                    PGC-1α/β
                         ↓
ERRγ (ESRRG) ←→ DNA Response Element (ERRE)
                         ↓
              ┌─────────┼─────────┐
              ↓         ↓         ↓
         NRF-1/2    Tfam    Oxidative Phosphorylation
              ↓         ↓         ↓
         mtDNA 복제   미토콘드리아    ATP 생산
              ↓         ↓         ↓
         ┌─────────────────────────────┐
         │   근육 힘↑  심장 기능↑  대사↑   │
         └─────────────────────────────┘
```

### 5.2 Agonist 기전

| 단계 | 작용 | 결과 |
|------|------|------|
| 1 | ERRγ agonist 결합 | ERRγ 활성화 |
| 2 | PGC-1α/β 공통작용 | 전사 복합체 형성 |
| 3 | 미토콘드리아 생합성↑ | NRF-1/2, Tfam 활성화 |
| 4 | 산화적 인산화↑ | OXPHOS 증가 |
| 5 | ATP 생산↑ | 근육 힘↑, 심장 기능↑ |

---

## 6. Development Strategy

### 6.1 Timeline

| Timeline | Compound | Indication | Milestone |
|----------|----------|------------|-----------|
| **단기 (1-2년)** | GSK4716 | Sarcopenia | 전임상 유효성 검증 |
| **중기 (3-5년)** | GSK9089 analogs | 심장 보호 | Lead 최적화 |
| **장기 (5년+)** | Dual PPAR/ERR | 대사질환 | IND filing |

### 6.2 Competitive Landscape

| Company | Program | Stage | Indication |
|---------|---------|-------|------------|
| **GSK** | GSK4716 | Research | 대사질환 |
| **GSK** | GSK5182 | Research | 항비만/항종양 |
| **Stanford** | SLN-PX-2 | Preclinical | 심장 보호 |
| **Novartis** | Nuclear receptor portfolio | Various | 복합 연구 |
| **Eli Lilly** | PPAR agonists | Clinical | 대사질환 |

### 6.3 Combination Therapy Potential

| Combination | Synergy | 기대 효과 |
|-------------|---------|----------|
| **ERRγ + PPARα** | 대사 항상성 | 지방산 산화协同 |
| **ERRγ + GLP-1** | 체중 감소 | 근육량 보존 |
| **ERRγ + Myostatin inhibitor** | 근육량 증가 | Sarcopenia |

---

## 7. NAMs Validation Strategy

### 7.1 In Vitro Assays

| Assay | Model | Readout |
|-------|-------|---------|
| **근육 분화** | C2C12 근육세포 | Myosin heavy chain (MyHC) |
| **미토콘드리아 기능** | Seahorse XF | 산소 소비율 (OCR) |
| **심장 대사** | iPSC-유래 심장 근세포 | ATP 생산, Seahorse |
| **BAT 분화** | 3T3-L1 세포 | UCP1 발현 |

### 7.2 In Vivo Models

| Model | 유발 방법 | 평가 지표 |
|-------|----------|-----------|
| **근육손실 모델** | 고령 마우스, 운동부족 | 근육량, 힘 측정 |
| **심장부전 모델** | MI 모델, TAC | 심기능 (EF, FS) |
| **대사 모델** | 고지방식이 (DIO) 마우스 | 체중,葡萄당 내성 |

### 7.3 Biomarkers

| Biomarker | 조직 | 의미 |
|-----------|------|------|
| **PGC-1α** | 근육 | 미토콘드리아 생합성 |
| **NRF-1/2** | 근육, 심장 | 전사 활성화 |
| **Tfam** | 미토콘드리아 | mtDNA 복제 |
| **ATP** | 조직 | 에너지 상태 |

---

## 8. Development Challenges

### 8.1 주요 과제

| 과제 | 설명 | 해결 방안 |
|------|------|----------|
| **선택성** | ERRα와 구조적 유사성 → cross-reactivity | ERRγ-선택적 화합물 개발 |
| **전달** | 핵내 수용체 → 세포 내 전달 필요 | 특화된 전달 시스템 |
| **안전성** | 심장 발현 높음 → 심장에 미치는 영향 | Careful dosing |
| **효능** | 전임상 → 임상 전환 | 최적의 약물 동력학 |

### 8.2 해결 전략

```
1. 선택성 문제:
   - ERRγ LBD의 Phe327/Ala327 차이가 핵심
   - 이 부분을 타겟하는 화합물 설계

2. 전달 문제:
   - Nuclear localization signal (NLS) 활용
   - 지질 나노입자encapsulation

3. 안전성:
   - 심장 특이적 부작용 모니터링
   - 심근 특이적 delivery system 개발
```

---

## 9. 결론 및 권고

### 9.1 Most Promising Candidates

| Rank | Compound | Type | Potential |
|------|----------|------|-----------|
| 1 | **GSK4716** | Agonist | Research tool, Preclinical validation |
| 2 | **GSK9089** | Agonist | More potent, Lead optimization |
| 3 | **SLN-PX-2** | Agonist | Cardiac protection, Preclinical |
| 4 | **GSK5182** | Inverse Agonist | Anti-obesity, Research |

### 9.2 Development Recommendations

```
1. 단기 (1-2년):
   - GSK4716 기반 sarcopenia 전임상 연구
   - SAR 연구로 선택적 analogs 개발

2. 중기 (3-5년):
   - GSK9089 analogs의 lead 최적화
   - SLN-PX-2 심장보호 효과 검증
   - combination therapy 전략 수립

3. 장기 (5년+):
   - Dual PPAR/ERR agonists 개발
   - IND filing 준비
   - 임상 1상 진입
```

### 9.3 Key Insights

> **핵심 인사이트:**
> - ERRγ는 PGC-1α와 협조하여 미토콘드리아 생합성을 주도
> - GSK4716/GSK9089가 표준 연구 도구
> - SLN-PX-2가 가장 임상 가능성이 높은 후보
> - Inverse agonist는 항비만/항종양으로 개발 가능

---

## 10. References

1. Huss JM, et al. (2004) ERRγ in Nat Rev Drug Discov
2. Giguère V (2008) ERRγ in Physiol Rev
3. Fan W, et al. (2020) ERRγ and metabolic disease
4. Charos AE, et al. (2022) GSK4716 analogs in Nat Chem Biol
5. Hegazy L (2025) Novel binding trench in ERRα. Front Mol Biosci
6. RCSB PDB: 2GPP (ERRγ + GSK4716), 2EWP (ERRγ + GSK5182)
7. PubMed: 15857113 (Phenolic acyl hydrazones SAR)
8. PubMed: 19746993 (Combinatorial approach for agonists)

---

*Report generated by ARP v24 Research Pipeline · 2026-04-23*