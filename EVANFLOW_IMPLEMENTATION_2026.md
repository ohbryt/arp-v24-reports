# EvanFlow Implementation for ARP v24
## TDD-Driven Development Applied to Research Code

**Date:** 2026-04-29  
**Framework:** EvanFlow (evanklem/evanflow)  
**Purpose:** Quality code development for research pipeline

---

## Overview

```
EvanFlow: Development phase quality
Agent Harness: Production phase quality

Together: Full lifecycle quality for ARP v24
```

---

## Core Principles Applied

### 1. Never Invent Values
```
Research code often invents:
- File paths without checking
- API endpoints without verifying
- Parameter values without citing

EvanFlow Rule: If unsure, STOP and ASK

Applied to ARP v24:
□ Verify all file paths exist before using
□ Confirm API endpoints with actual URLs
□ Cite parameter sources (literature, not guesswork)
□ Check database schema before queries
```

### 2. TDD Inside Every Code Task
```
Traditional: Write code → Write tests → Ship
EvanFlow: One test → Minimal impl → Refactor → Repeat

Applied to ARP v24:
For each function/module:
1. Write failing test (what should it do?)
2. Write minimal code to pass
3. Refactor immediately
4. Next test
```

### 3. Vertical Slice Only
```
Not: Write all code → Write all tests → Done
Yes: One feature slice → Test → Refactor → Next slice

Applied to ARP v24:
Instead of building entire pipeline at once:
- Slice 1: Literature search only → test → working
- Slice 2: Target ID only → test → working
- Slice 3: ADMET prediction → test → working
- Integrate gradually
```

### 4. Checkpoints
```
EvanFlow: Real checkpoints at design, plan, iteration
- Agent stops and waits for YOUR approval

Applied to ARP v24:
□ Before starting major feature: Present design
□ Before merging major change: Present plan
□ After iteration: Report + await direction
□ Never auto-commit
```

### 5. Five Failure Modes Checklist
```
In iterate phase, check:
□ Hallucinated actions (did it really call that API?)
□ Scope creep (did requirements grow?)
□ Cascading errors (did one failure cause others?)
□ Context loss (does it remember earlier decisions?)
□ Tool misuse (right tool for right job?)

Applied to ARP v24:
Before declaring "done", run through checklist
```

---

## Implementation Steps

### Step 1: Create EvanFlow-Inspired Workflow

```markdown
# ARP v24 Development Workflow (EvanFlow-Inspired)

## For Each Task

### 1. Brainstorm
```
What's the goal?
What are 2-3 approaches?
What could go wrong?
```
↓ (you approve design)

### 2. Plan
```
File structure
Dependencies
Test strategy
```
↓ (you approve plan)

### 3. Execute
```
One test → minimal code → refactor → repeat
Quality checks inline (lint, typecheck, test)
```
↓ (complete task)

### 4. Iterate
```
Self-review the diff
Run Five Failure Modes checklist
Verify against original requirements
```
↓ (max 5 iterations)

### 5. STOP
```
Report: What was done, what was verified
Await your direction on next steps
```
```

### Step 2: Quality Gates

```yaml
# Before "done" - must pass all:
quality_gates:
  - lint_check: true
  - type_check: true
  - unit_tests: true
  - integration_tests: false  # Optional for research
  - documentation: true
  - no_hardcoded_values: true
  - citations_verified: true
```

### Step 3: Create Project-Specific Checks

```python
# arp_v24_quality_checks.py

def check_no_invented_values():
    """Check for hardcoded values that should be verified"""
    issues = []
    
    # Check file paths
    for path in find_file_references():
        if not Path(path).exists():
            issues.append(f"File path does not exist: {path}")
    
    # Check API endpoints
    for url in find_url_references():
        if not verify_url_accessible(url):
            issues.append(f"URL may not be accessible: {url}")
    
    # Check parameter values
    for param in find_literature_params():
        if not has_citation(param):
            issues.append(f"Parameter lacks citation: {param}")
    
    return issues

def five_failure_modes_check(code_diff):
    """Run through five failure modes"""
    modes = {
        "hallucinated_actions": check_actual_tool_calls(code_diff),
        "scope_creep": check_requirement_drift(),
        "cascading_errors": check_error_propagation(),
        "context_loss": check_memory_consistency(),
        "tool_misuse": check_tool_selection()
    }
    
    return modes
```

---

## Skill Mapping: EvanFlow → ARP v24

| EvanFlow Skill | ARP v24 Equivalent |
|----------------|-------------------|
| evanflow-go | arp-run |
| evanflow-brainstorming | research-question-formulation |
| evanflow-writing-plans | experiment-design |
| evanflow-tdd | test-driven-development |
| evanflow-iterate | quality-review |
| evanflow-debug | bug-investigation |
| evanflow-review | code-peer-review |
| evanflow-compact | session-summarization |

---

## Installation & Setup

```bash
# Not available as OpenClaw plugin yet, but we can apply principles manually

# Create workflow directory
mkdir -p ~/.openclaw/workspace/arp-v24/evanflow_workflow

# Create workflow template
cat > ~/.openclaw/workspace/arp-v24/evanflow_workflow/TEMPLATE.md << 'EOF'
# Task: [TASK_NAME]

## 1. Brainstorm
Goal:
Approaches (2-3):
Risks:
[ ] Approved

## 2. Plan  
File structure:
Dependencies:
Test strategy:
[ ] Approved

## 3. Execute
- [ ] Test 1:
- [ ] Code:
- [ ] Refactor:
[Continue until feature complete]

## 4. Iterate
Five Failure Modes:
- [ ] Hallucinated actions
- [ ] Scope creep
- [ ] Cascading errors
- [ ] Context loss
- [ ] Tool misuse

Quality checks:
- [ ] Lint passed
- [ ] Type check passed
- [ ] Tests passed
- [ ] Documentation updated

## 5. STOP
Summary:
Next steps:
EOF

echo "EvanFlow workflow template created"
```

---

## Example: Adding DGAT1 Analysis Feature

### Before (Without EvanFlow)
```
1. Write code
2. Test manually
3. "Looks good, done"
4. Problems found later in production
```

### After (With EvanFlow)
```
## Task: Add DGAT1 expression analysis

### 1. Brainstorm
Goal: Add DGAT1 to expression analysis pipeline
Approaches:
1. Add to existing cancer metabolism module
2. Create separate DGAT1-specific module
3. Integrate via new target interface

Risks:
- May duplicate existing SLC7A11 code
- Citation needed for DGAT1 pathway
- Test data availability

### 2. Plan
Files to create/modify:
- core/targets/dgat1.py (new)
- tests/test_dgat1.py (new)
- docs/dgat1_analysis.md (new)

Dependencies:
- Existing cancer_metabolism.py
- Literature citation: [NEED TO ADD]

Test strategy:
- Unit test for expression lookup
- Integration test with SLC7A11

### 3. Execute
[One test at a time, following TDD discipline]

### 4. Iterate
Five Failure Modes check...
Quality gates passed...

### 5. STOP
Implemented DGAT1 analysis
All tests passing
Awaiting review
```

---

## Integration with Agent Harness

```
Development (EvanFlow)           Production (Agent Harness)
       ↓                                  ↓
  Write code                        Deploy to production
  TDD discipline                    Grader scores outputs
  Checkpoints                      Score + ticket = action
  Five failure modes                6 jobs pipeline
  Quality gates                    Continuous monitoring
       ↓                                  ↓
  Better code ────────────────────→ Better outputs
```

---

## Next Steps

```
□ [ ] Create EvanFlow workflow template in workspace
□ [ ] Set up project-specific quality checks
□ [ ] Apply to next ARP v24 feature
□ [ ] Integrate with Agent Harness for full lifecycle
```

---

*Document: arp-v24/EVANFLOW_IMPLEMENTATION_2026.md*  
*Created: 2026-04-29*  
*Framework: evanklem/evanflow*