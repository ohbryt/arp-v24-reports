# EvanFlow: TDD-Driven Iterative Feedback Loop for Software Development
## GitHub: evanklem/evanflow

**URL:** https://github.com/evanklem/evanflow  
**Type:** Claude Code Plugin / Skill Set  
**Purpose:** TDD-driven iterative development with AI

---

## Overview

```
A TDD-driven iterative feedback loop for software development.

16 cohesive skills walk an idea from:
brainstorm → plan → execute → iterate → STOP

With checkpoints where YOU stay in control.
```

---

## The Core Loop

```
brainstorm → plan → execute → iterate → STOP
     ↓          ↓        ↓          ↓
  Design    Plan    Vertical    Quality
  approval  approval slice TDD   checks
```

### Key Principles

| Principle | Description |
|-----------|-------------|
| **TDD is NOT a phase** | It's the discipline INSIDE each code-writing task |
| **Conductor, not autopilot** | Real checkpoints at design, plan, iteration |
| **No auto-commits** | Agent stops short of every git operation |
| **No forced ceremony** | No "must invoke a skill" tax |
| **Vertical-slice TDD** | One failing test → minimal impl → refactor → repeat |

---

## 16 Skills (Organized by Purpose)

### Entry Point
| Skill | Purpose |
|-------|---------|
| **evanflow-go** | Single entry point. "Let's evanflow this" |

### Core Loop
| Skill | Purpose |
|-------|---------|
| **evanflow-brainstorming** | Clarify intent, propose 2-3 approaches with stress-test |
| **evanflow-writing-plans** | File structure first, bite-sized tasks |
| **evanflow-executing-plans** | Task-by-task with inline verification |
| **evanflow-tdd** | Vertical-slice TDD. RED → GREEN → REFACTOR |
| **evanflow-iterate** | Self-review loop. 5 iteration cap |

### Support
| Skill | Purpose |
|-------|---------|
| **evanflow-glossary** | Extract domain terms to CONTEXT.md |
| **evanflow-improve-architecture** | Refactor opportunities via deletion test |
| **evanflow-design-interface** | "Design it twice" - parallel subagents |
| **evanflow-debug** | Root-cause discipline. Failing test first |
| **evanflow-review** | Code review (giving + receiving) |
| **evanflow-prd** | Synthesize PRD from context |
| **evanflow-qa** | Conversational bug discovery |

### Session Management
| Skill | Purpose |
|-------|---------|
| **evanflow-compact** | Long-session context management |

### Index
| Skill | Purpose |
|-------|---------|
| **evanflow** | The index. Shared vocabulary + when to invoke |

---

## Subagents (in agents/)

| Subagent | Tools | Purpose |
|----------|-------|---------|
| **evanflow-coder** | Read, Edit, Write, Glob, Grep, Bash, TodoWrite | Implementation subagent |
| **evanflow-overseer** | Read, Grep, Glob (NO Edit/Write/Bash) | Read-only review |

### Parallel Mode (3+ independent units)
```
One coder per unit (vertical-slice TDD)
One overseer per coder (read-only review)
Plus integration overseer (integration tests)
```

---

## Key Rules (with citations)

### 1. Never Invent Values
```
File paths, env vars, IDs, function names, library APIs
→ If unsure, agent stops and asks

Source: Action-hallucination is TOP failure mode
(DAPLab/Columbia "9 Critical Failure Patterns of Coding Agents")
```

### 2. Assertion-Correctness Warning
```
Over 62% of LLM-generated test assertions were incorrect
across HumanEval evaluation of four LLMs

Source: "Test-Driven Development for Code Generation" (arXiv 2402.13521)
```

### 3. Five Failure Modes (iterate phase)
```
1. Hallucinated actions
2. Scope creep
3. Cascading errors
4. Context loss
5. Tool misuse

Source: Synthesized from DAPLab failure patterns paper
```

### 4. Context Drift Watch
```
Nearly 65% of enterprise AI failures in 2025 attributed to:
- Context drift
- Memory loss during multi-step reasoning
NOT raw context exhaustion

Source: "Context Management Strategies for OpenCode" (March 2026)
```

### 5. Never Auto-Commit
```
Opinion from running loop on real projects:
Every time agent decided to integrate, it integrated wrong.
```

---

## Installation

### Method 1: Plugin (Recommended)
```bash
/plugin marketplace add evanklem/evanflow
/plugin install evanflow@evanflow
Restart Claude Code
```

### Method 2/3: See GitHub for alternatives

### Requirements
- Claude Code (any recent version)
- Bash
- jq (for hook script)
- Optional: Chromium (for UI screenshots)

---

## Hook: Dangerous Git Protection

```
hooks/block-dangerous-git.sh
Blocks: git push, git reset --hard, git clean -f,
        git branch -D, git checkout ., git restore .
```

---

## Comparison: EvanFlow vs Self-Healing Agent Harness

| Aspect | EvanFlow | Agent Harness (Peter Pang) |
|--------|----------|---------------------------|
| **Focus** | Code development | AI agent evaluation |
| **Loop** | brainstorm→plan→execute→iterate→STOP | grade→triage→fix→verify→gate |
| **Human control** | Checkpoints at each phase | Release gates via Grader |
| **Quality** | TDD + 5 failure modes | Grader scores + bug pipeline |
| **Auto-commit** | NEVER | NEVER |
| **Iteration cap** | 5 iterations max | Continuous monitoring |

---

## Integration with Our Research

### For ARP v24 Development

```
EvanFlow could help us:
1. Write better code with TDD discipline
2. Have checkpoints before major changes
3. Prevent context drift in long sessions
4. Quality checks before "done"

Integration with Agent Harness:
- EvanFlow: Development phase quality
- Agent Harness: Production phase quality
```

---

## Reference

- GitHub: https://github.com/evanklem/evanflow
- Author: evanklem
- Related: DAPLab "9 Critical Failure Patterns of Coding Agents"

---

*Document: arp-v24/EVANFLOW_TDD_LOOP_2026.md*  
*Created: 2026-04-29*