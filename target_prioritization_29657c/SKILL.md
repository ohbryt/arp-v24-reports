# Skill: target_prioritization

## Problem
오류 발생: Disease extraction returned wrong disease

## Context
- Task Type: target_prioritization
- Parameters: {
  "disease": "masld",
  "query": "MASLD drug targets"
}

## Procedure

### Step 1: Verify Input
Check that all required parameters are present and valid.

### Step 2: Route to Optimal Tool
Based on task type:
- target_prioritization -> ARP_PIPELINE
- llm_analysis -> GROQ_LLAMA
- bioactivity_data -> CHEMBL_API

### Step 3: Execute with Fallback
If primary tool fails, use fallback chain.

### Step 4: Validate Output
Check that output matches expected schema.

## Verification
Run: `python -m pytest target_prioritization_test.py -v`
