# The Self-Healing Agent Harness
## Peter Pang (@intuitiveml) | April 28, 2026

**Context:** Startup shipping to production 3-8x/day with 99% AI-written code

---

## Key Insight

```
Traditional: Evaluation (ML team) + QA (Engineering) = SEPARATE
AI Agent: Same question - bad response is both metric AND bug
```

---

## Two Critical Lessons

### 1. Grade Outcome, Not Trajectory

```
Agents often take paths that look inefficient or strange to humans,
but still produce the right answer.

→ Penalizing the path is NOT efficient evaluation
→ Focus on final outcome, not process
```

### 2. Score + Ticket = Real Impact

```
A bad score without engineering action = just a dashboard
A bug pipeline without grader signals = blind

→ Build BOTH or build NEITHER
```

### 3. Don't Chase "Scientific Correctness"

```
❌ "Is this methodologically rigorous?"
✅ "Does this trigger a fix today?"

Fast signal that triggers fix TODAY
> Perfect benchmark that ships next quarter
```

---

## Failure Sources in AI Agents

| Source | Example |
|--------|---------|
| **Model** | Hallucination, poor reasoning |
| **Integration** | 500 errors, stale tokens, malformed payload |
| **Infra** | Cloudflare timeout, Postgres lag, OOM |
| **Tool contract** | Schema drift, argument mismatch |
| **Prompt/context** | System prompt truncation, RAG failure, memory miss |
| **Deploy** | Regression in small components |

```
All look the same to user: bad answer
All look the same to grader: low score on messageId X
```

---

## The Three Components

### 1. The Grader
```
- Tri-judge panel (multiple evaluators)
- Scores every live agent response
- Replaces: human QA review + offline benchmark eval
```

### 2. The Engineering Pipeline
```
- 6 daily jobs
- Turn low scores → Linear tickets + draft PRs + verified fixes
- Replaces: manual bug triage + sprint planning + regression testing
```

### 3. The Feedback Loop
```
Grade → Triage → Fix → Verify → Gate Release
         ↑                    ↓
         ← ← ← ← ← ← ← ← ← ←
```

---

## For Our Research (ARP v24)

### Apply This Framework

| Their System | Our Equivalent |
|--------------|----------------|
| Grader | Unfamiliarity scorer + Validation metrics |
| Bug pipeline | brain memory + ticket system |
| Daily jobs | Cron-triggered health checks |
| Release gate | Manual review before publishing |

### Key Takeaways

1. **Grade outcomes** - Don't penalize strange agent reasoning paths
2. **Connect scores to action** - bad score → draft PR or fix ticket
3. **Fast > perfect** - good enough signal today > perfect benchmark next quarter
4. **Eval = QA** - same loop for AI agent platforms

---

## Component 1: The Grader (Details)

### The Trigger and Sampling

```
Every response triggers POST to grading endpoint
- Per model sampling (not flat)
- 10% for dominant model (handles 24x more traffic)
- 100% for minority/experimental models

Why? Minority models need statistical significance in HOURS, not weeks
```

### Job 0: The Categorical Router

```
Before judges see transcript, classifier maps to 12 core domains:
1. Coding
2. Research
3. Data analysis
4. Task automation
5. Agent building
6. Artifact building
7. Traditional app building
8. Planning
9. Writing
10. Creative work
11. Conversation
12. Error recovery

Category-conditioned rubric: good coding ≠ good research criteria
```

### Three Judges, Three Personas

```
We run 3 judges from different model families:
├── Anthropic
├── OpenAI
└── Google

Purpose: Reduce self-preference bias

How: Concurrent via AI Gateway → single slow judge doesn't block
     → Just lowers quorum size for that row

Quality control: Sample verdicts back to humans for calibration
               → Gap between judge consensus + human review = rubric bug
```

### Structured Output Schema

```json
{
  "reasoning": "2-3 sentences step-by-step rationale",
  "category": "domain being graded",
  "quality": "excellent | good | acceptable | poor",
  "issues": [
    "incomplete",
    "hallucination",
    "tool_misuse",
    "missed_context",
    ... (9-item taxonomy)
  ],
  "confidence": 0.0 to 1.0
}
```

### Mathematical Consensus

```
Quality → 1-4 scale → average across surviving judges
        ↓
Continuous metric (3.33 vs 2.66) vs blunt vote

Benefit: Per-model trends visible at SMALLER sample sizes

Self-preference bias handling:
├── Sonnet grades Sonnet → score can inflate ~0.3
├── But OpenAI + Google judges flag same issue → bias washed out by quorum
└── Each verdict persisted: sonnet_quality, gpt_quality, gemini_quality, judge_count

Audit: Engineers can re-weight if any judge drifts
```

### The Stream

```
Output: Stream of category-tagged, judge-averaged scores
        tied to exact messageId
        ↓
Feeds everything downstream
```

---

## Component 2: The Engineering Pipeline

### Six Jobs from Score to Fix

```
low score = bug report → 6 sequential jobs

Replaces: manual QA (triage, investigation, fix, regression test, sign-off)
```

#### Job 1: Detect and Triage

```
Agent pulls poor-quality verdicts + clusters them
Scoring: 9-dimensional severity engine
├── User impact
├── Velocity
├── Duration
├── Alarm correlation
├── Resource pressure
├── Latency
├── 4xx rate
├── Blast radius
└── Business criticality

Above urgency cutoff → moves forward
Below → logged for trend tracking
```

#### Job 2: Investigate

```
For top 3 clusters:
├── Walk stack traces through monorepo
├── Pull CloudWatch logs
├── Check recent deployments
├── Query database replica
└── Assign root cause + evidence bundle

Routes ticket to human with full evidence
```

#### Job 3: Auto-Fix (Draft PR)

```
For high-confidence, urgent issues:
├── Branch code
├── Write fix
├── Validate
└── Submit draft PR

Guardrails:
├── Max 3 PRs per run (prevent reviewer exhaustion)
├── .env, .github/, IAM policies → auto-close
├── Type errors → block submission
└── Failing tests → block submission

Goal: Fix obvious bugs quickly → humans focus on deep work
NOT: Fix deep architectural debt
```

#### Job 4: Verify

```
For tickets in In Review:
├── Query CloudWatch last 6 hours
├── Zero occurrences → close ticket + paste telemetry evidence
└── Still failing → update with new error count + loop again

Objective proof that fixes work
Zero manual regression testing
```

#### Job 5: Re-grade

```
Closed clusters: 100% sampling for next 24 hours
Regression detected → reopens ticket + reverts fix
```

#### Job 6: Report

```
Nightly digest to Linear + team channel:
├── Clusters detected
├── PRs shipped
├── PRs reverted
├── Score changes per category
└── Per-model leaderboard

Dashboard isn't the goal - it's a RECORD of what happened
```

---

## Component 3: The Bridge

### AI-Gated Grey Rollouts

```
First two components: Close loop on bugs that ALREADY shipped
Third component: Close loop on bugs about to SHIP

When you swap foundational model, rewrite core prompt, or give new tool access:
→ Behavioral risk goes VERTICAL
→ Cannot push to 100% and hope
```

---

## Reference

- Author: Peter Pang (@intuitiveml)
- Original: Twitter/X thread, April 28, 2026
- Topic: AI agent evaluation, production QA, self-healing systems

---

*Document: arp-v24/SELF_HEALING_AGENT_HARNESS_2026.md*  
*Updated: 2026-04-29*