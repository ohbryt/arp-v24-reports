# ARP v24 Self-Healing Agent Harness Implementation
## Applying Peter Pang's Framework to Our Research Pipeline

**Date:** 2026-04-29  
**Framework Source:** Peter Pang (@intuitiveml) - Self-Healing Agent Harness

---

## Overview

```
Original: AI agent platform evaluation + QA
Ours: ARP v24 research pipeline evaluation + QA

The loop is the same: grade → triage → fix → verify → release
```

---

## Component 1: The Grader (ARP v24)

### Our Judge Panel

```
We run 3 judges from different model families:
├── MiniMax-M2.7 (default, dominant)
├── GLM-4.7-flash (fast secondary)
└── Qwen3-14B (reasoning)

Purpose: Reduce self-preference bias
```

### Sampling Strategy

```
Per model, not flat:
├── Dominant (MiniMax): 10% sampling
├── Secondary (GLM, Qwen): 50% sampling
└── New models: 100% until statistical significance
```

### Our 12 Core Domains (ARP v24)

```
1. Literature analysis
2. Target identification
3. Drug candidate screening
4. ADMET prediction
5. Experimental design
6. Data analysis
7. Report generation
8. Code generation
9. Research synthesis
10. Protocol generation
11. Literature review
12. Error recovery
```

### Structured Output (Our Schema)

```json
{
  "task_id": "unique_task_identifier",
  "category": "literature_analysis | target_id | screening | ...",
  "quality": "excellent | good | acceptable | poor",
  "issues": [
    "incomplete_analysis",
    "hallucination",
    "missed_citations",
    "wrong_target",
    "methodology_error",
    "logic_error",
    "data_mismatch",
    "inconsistent",
    "other"
  ],
  "confidence": 0.0-1.0,
  "reasoning": "2-3 sentences",
  "model": "model_name"
}
```

### Quality Scale

```
1 = Poor (critical errors, unusable)
2 = Acceptable (major issues, usable with caution)
3 = Good (minor issues, mostly usable)
4 = Excellent (no significant issues)

Mathematical Consensus: Average across judges
```

---

## Component 2: Engineering Pipeline (6 Jobs)

### Job 1: Detect and Triage

```python
# Pseudocode
def detect_and_triage(verdicts):
    # Pull poor quality verdicts
    poor_quality = [v for v in verdicts if v.quality in ['poor', 'acceptable']]
    
    # Cluster by:
    # - Category (which research domain)
    # - Issue type (hallucination, missed_context, etc.)
    # - Time (similar timeframe = likely same cause)
    
    clusters = cluster(poor_quality)
    
    # Score each cluster on 9-dim severity:
    # 1. User impact (how important was this task?)
    # 2. Velocity (how often does this happen?)
    # 3. Duration (how long has this been occurring?)
    # 4. Error type (hallucination worse than incomplete)
    # 5. Downstream effect (did it affect other outputs?)
    # 6. Fixability (easy fix vs fundamental change needed)
    # 7. Pattern persistence (repeating issue?)
    # 8. Blast radius (how many outputs affected?)
    # 9. Research impact (would this change conclusions?)
    
    for cluster in clusters:
        severity = calculate_severity(cluster)
        if severity > URGENCY_CUTOFF:
            submit_to_job2(cluster)
        else:
            log_for_trend(cluster)
```

### Job 2: Investigate

```python
# For top 3 clusters:
def investigate(cluster):
    # Walk the evidence
    evidence = {
        'task_ids': cluster.task_ids,
        'category': cluster.category,
        'issue_types': cluster.issue_types,
        'models_involved': cluster.models,
        'timestamps': cluster.times,
        'input_prompts': cluster.inputs,
        'outputs': cluster.outputs,
        'expected_vs_actual': cluster.comparison
    }
    
    # Root cause analysis
    root_cause = analyze(evidence)
    
    # Route to appropriate handler
    if root_cause.type == 'model_hallucination':
        route_to('model_tuning_team')
    elif root_cause.type == 'prompt_mismatch':
        route_to('prompt_engineering_team')
    elif root_cause.type == 'data_quality':
        route_to('data_curation_team')
    elif root_cause.type == 'integration_error':
        route_to('infrastructure_team')
    
    return EvidenceBundle(evidence, root_cause)
```

### Job 3: Auto-Fix

```python
# Guardrails for our pipeline
GUARDRAILS = {
    'max_prs_per_run': 3,  # Prevent reviewer exhaustion
    'auto_close_patterns': [
        '.env',
        '.github/',
        'credentials',
        'api_keys',
        'IAM'
    ],
    'blocking_checks': [
        'type_errors',
        'failing_tests',
        'syntax_errors',
        'import_errors'
    ],
    'max_file_changes': 10,  # Don't touch too many files
    'safety_categories': ['safety_critical', 'clinical', 'patient']  # Extra review
}

def auto_fix(cluster):
    if not is_high_confidence(cluster):
        return None  # Skip, let humans handle
    
    if cluster.severity < URGENT_THRESHOLD:
        return None  # Not worth auto-fixing
    
    # Generate fix
    fix = generate_fix(cluster)
    
    # Validate
    if not validate_fix(fix):
        return None
    
    # Create PR
    pr = create_draft_pr(fix)
    
    return pr
```

### Job 4: Verify

```python
def verify(cluster, hours=6):
    # Check if issue still occurring
    recent_issues = check_recent_outputs(
        category=cluster.category,
        issue_types=cluster.issue_types,
        timeframe=f'last_{hours}h'
    )
    
    if len(recent_issues) == 0:
        # Issue resolved
        close_ticket(cluster, evidence=f"No occurrences in last {hours} hours")
        return True
    else:
        # Still happening
        update_ticket(cluster, new_count=len(recent_issues))
        return False
```

### Job 5: Re-grade

```python
def re_grade(closed_clusters):
    # 100% sampling for 24 hours
    for cluster in closed_clusters:
        set_sampling_rate(cluster.category, 1.0)  # 100%
    
    # If regression detected
    if regression_detected(closed_clusters):
        # Reopen tickets
        for cluster in regressed_clusters:
            reopen_ticket(cluster)
            revert_fix(cluster)  # Rollback the PR
```

### Job 6: Report

```python
def nightly_report():
    report = {
        'date': today(),
        'clusters_detected': count_new_clusters(),
        'clusters_resolved': count_resolved_clusters(),
        'prs_shipped': count_shipped_prs(),
        'prs_reverted': count_reverted_prs(),
        'score_by_category': get_scores_by_domain(),
        'score_by_model': get_scores_by_model(),
        'trend_analysis': get_trends(),
        'top_issues': get_top_issue_types()
    }
    
    # Send to:
    # - Discord/Slack channel
    # - brain memory (for long-term tracking)
    # - GitHub project board
    
    return report
```

---

## Component 3: The Bridge (Release Gates)

### Our Promotion Ladder

```
For any major change to ARP v24:
- New model integration
- New pipeline stage
- Significant prompt changes
- New database or API

Ladder: 5% → 20% → 50% → 100%
```

### Gates

```python
def evaluate_change(change, current_traffic_pct=5):
    baseline_score = get_baseline_score()
    
    # Route small traffic to new variant
    variant_score = evaluate_variant(change, traffic_pct=current_traffic_pct)
    
    # Statistical test
    if variant_score < baseline_score - 0.15:
        if p_value < 0.05 and min_interactions >= 200:
            # FAIL - abort
            abort_release()
            open_ticket(f"Regression detected: {change}")
            flip_traffic_to_stable()
            return False
    
    # HOLD or IMPROVE
    if variant_score > baseline_score:
        # IMPROVE - accelerate ladder
        if current_traffic_pct < 100:
            scale_up_traffic(change, next_tier())
    
    # Continue monitoring
    return True
```

---

## Implementation for ARP v24

### Phase 1: Basic Grader (Week 1)

```yaml
# Setup basic grading
models:
  judge_1: minimax/MiniMax-M2.7
  judge_2: opencode-go/glm-4.7-flash
  judge_3: opencode-go/qwen3-14b

sampling:
  default: 0.1  # 10%
  new_model: 1.0  # 100%

categories:
  - literature_analysis
  - target_identification
  - drug_screening
  - admet_prediction
  - experimental_design
  - data_analysis
  - report_generation
  - code_generation
  - synthesis
```

### Phase 2: Engineering Pipeline (Week 2-3)

```python
# Implement 6 jobs
JOBS = {
    'detect_triage': run_job_1,
    'investigate': run_job_2,
    'auto_fix': run_job_3,
    'verify': run_job_4,
    're_grade': run_job_5,
    'report': run_job_6
}

# Cron schedule
CRON = {
    'job_1': '*/15 * * * *',  # Every 15 minutes
    'job_2': '0 * * * *',       # Every hour
    'job_3': '0 9,17 * * *',   # Twice daily
    'job_4': '*/30 * * * *',   # Every 30 minutes
    'job_5': '0 */4 * * *',    # Every 4 hours
    'job_6': '0 9 * * *'       # Daily morning
}
```

### Phase 3: Bridge Integration (Week 4)

```python
# Integration with OpenClaw cron
# For release gates on major changes
RELEASE_GATES = {
    'min_interactions': 200,
    'score_threshold': 0.15,
    'p_value': 0.05,
    'cohort_sizes': [5, 20, 50, 100]
}
```

---

## Metrics to Track

| Metric | Target |
|--------|--------|
| Response Quality Score | >3.0 (1-4 scale) |
| Hallucination Rate | <5% |
| Missed Context Rate | <10% |
| Time to Detection | <1 hour |
| Time to Fix | <24 hours |
| Regression Rate | <2% |
| Auto-fix Success | >70% |

---

## Key Differences from Original

| Aspect | Original (Peter Pang) | Ours (ARP v24) |
|--------|----------------------|-----------------|
| Domain | Code/Agent platform | Scientific research |
| Users | End users | Researchers |
| Failure cost | Bug/internship | Wrong conclusions |
| Evaluation | Code quality | Scientific accuracy |
| Stakes | Medium | High (drug discovery) |

---

*Document: arp-v24/ARP_SELF_HEALING_HARNESS_IMPLEMENTATION.md*  
*Created: 2026-04-29*  
*Framework: Peter Pang (@intuitiveml)*