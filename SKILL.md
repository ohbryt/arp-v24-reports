# Skillify - Agent Failure to Permanent Fix

**Purpose:** Convert agent failures into reproducible skills with tests

**Based on:** Garry Tan's Skillify methodology (Y Combinator)

---

## Core Concept

When an agent fails:
1. Capture the failure context
2. Convert to a "Skill" (markdown + script + test)
3. Register in resolver for discoverability
4. Verify with automated tests

---

## Skill Structure

```
skill_name/
├── SKILL.md           # Markdown procedure
├── script.py          # Deterministic script
├── test_skill.py      # Unit test
├── test_integration.py # Integration test
└── resolver.yaml       # Trigger conditions
```

---

## Our Implementation

### For MASLD/Sarcopenia Pipeline:

| Skill | Trigger | Script | Test |
|-------|---------|--------|------|
| `masld_target_id` | MASLD query | target_prioritization | Verify targets NR1H4, PPARA, etc. |
| `sarcopenia_target_id` | Sarcopenia query | target_prioritization | Verify targets FOXO1, MSTN, etc. |
| `disease_extraction` | Any query | extract_disease | Verify correct disease mapping |
| `llm_analysis` | Analysis request | groq_analyze | Verify Korean output |
| `bioactivity_fetch` | Drug query | chembl_search | Verify Bimagrumab→ACVR2B |

---

## 10-Step Checklist (from Skillify)

- [x] 1. SKILL.md 작성
- [x] 2. 결정론적 스크립트 작성
- [ ] 3. 유닛 테스트 (vitest)
- [ ] 4. 통합 테스트
- [ ] 5. LLM 평가 (LLM-as-judge)
- [ ] 6. 리졸버 트리거 등록
- [ ] 7. 리졸버 평가
- [ ] 8. 도달 가능성/중복 감사
- [ ] 9. E2E 스모크 테스트
- [ ] 10. 브레인 파일링 규칙

---

## Integration with Director Agent

```python
# When task fails:
skillify.failed(task, error, context)
# → Creates skill file
# → Registers resolver
# → Triggers tests
```

---

## Key Insight

> "Deterministic work should ALWAYS use scripts, not LLM inference"

**Our current bug:** LLM sometimes ignores target context from dependencies

**Fix:** Enforce deterministic extraction with scripts

---

## Status

- [x] Conceptual framework
- [ ] Skill files for each task type
- [ ] Automated test runner
- [ ] Resolver integration
- [ ] E2E smoke tests