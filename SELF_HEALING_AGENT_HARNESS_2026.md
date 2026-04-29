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

### Categorical Rubric

```
Each judge sees same transcript but evaluates against category-specific constraints
→ "Good" is domain-dependent
```

---

## Reference

- Author: Peter Pang (@intuitiveml)
- Original: Twitter/X thread, April 28, 2026
- Topic: AI agent evaluation, production QA, self-healing systems

---

*Document: arp-v24/SELF_HEALING_AGENT_HARNESS_2026.md*  
*Updated: 2026-04-29*