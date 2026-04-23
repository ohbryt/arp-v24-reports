# Skillify - Agent Failure to Permanent Fix

**Based on:** Garry Tan's Skillify methodology (Y Combinator)  
**Source:** https://news.hada.io/topic?id=28777  
**Date:** 2026-04-23

---

## Core Concept

When an agent fails:
1. Capture the failure context
2. Convert to a "Skill" (markdown + script + test)
3. Register in resolver for discoverability
4. Verify with automated tests

```
실패 발생 → "skillify it" → 10단계 프로세스 자동 수행
                          ↓
              마크다운 절차서 + 결정론적 스크립트 + 테스트
                          ↓
              영구적 구조물로 전환
```

---

## Skill Structure

```
skill_name/
├── SKILL.md           # Markdown procedure
├── script.py          # Deterministic script
├── test_skill.py      # Unit test
├── resolver.json      # Trigger conditions
└── skill.json        # Metadata
```

---

## 10-Step Checklist (from Skillify)

| Step | Description | Status |
|------|-------------|--------|
| 1 | SKILL.md 작성 | ✅ |
| 2 | 결정론적 스크립트 작성 | ✅ |
| 3 | 유닛 테스트 (vitest) | ✅ |
| 4 | 통합 테스트 | 📋 |
| 5 | LLM 평가 (LLM-as-judge) | 📋 |
| 6 | 리졸버 트리거 등록 | ✅ |
| 7 | 리졸버 평가 | 📋 |
| 8 | 도달 가능성/중복 감사 | 📋 |
| 9 | E2E 스모크 테스트 | 📋 |
| 10 | 브레인 파일링 규칙 | 📋 |

---

## Our Implementation

### ARP v24 Orchestration System

| Skill | Trigger | Script | Test |
|-------|---------|--------|------|
| `masld_target_id` | MASLD query | target_prioritization | Verify targets NR1H4, PPARA, etc. |
| `sarcopenia_target_id` | Sarcopenia query | target_prioritization | Verify targets FOXO1, MSTN, etc. |
| `disease_extraction` | Any query | extract_disease | Verify correct disease mapping |

### Generated Skill Files

```
target_prioritization_29657c/
├── SKILL.md           # Procedure
├── script.py          # Deterministic script
├── test_skill.py      # Unit test
├── resolver.json      # Trigger
└── skill.json         # Metadata
```

---

## Integration with Director Agent

```python
from skills.orchestration_skills.skillify import get_skillify

class DirectorAgent:
    def __init__(self):
        self.skillify = get_skillify()
    
    def _execute_task(self, task, plan):
        try:
            result = self.router.execute_with_fallback(task.type, task_params)
            return result
        except Exception as e:
            # Skillify the failure
            skill = self.skillify.failed(
                task_type=task.type.value,
                task_params=task_params,
                error=e,
                context={"plan_id": plan.id}
            )
            return {"status": "error", "skill_created": skill.name}
```

---

## Key Insight

> **"Deterministic work should ALWAYS use scripts, not LLM inference"**

### Our Bug (Fixed)
- LLM sometimes ignores target context from dependencies
- e.g., Query for MASLD returned Sarcopenia targets

### Fix
- Enforce deterministic extraction with scripts
- All disease extraction now uses `_extract_disease()` function

---

## Usage

```python
from skills.orchestration_skills.skillify import get_skillify

skillify = get_skillify()

# When task fails:
skill = skillify.failed(
    task_type="target_prioritization",
    task_params={"disease": "masld"},
    error=Exception("Wrong disease returned"),
    context={"plan_id": "abc123"}
)

# List all skills:
skills = skillify.list_skills()

# Get skill for task type:
skill = skillify.get_skill("target_prioritization")
```

---

## Status

- [x] Conceptual framework
- [x] Skill files generated automatically
- [x] Resolver integration
- [ ] Automated test runner
- [ ] LLM-as-judge evaluation
- [ ] E2E smoke tests