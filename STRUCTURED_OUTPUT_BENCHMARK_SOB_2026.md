# Structured Output Benchmark (SOB) - interfaze.ai
## LLM Performance on Structured Data Extraction

**Source:** https://interfaze.ai/blog/introducing-structured-output-benchmark  
**Date:** April 2026  

---

## Key Insight

```
JSON Pass Rate ≠ Correct JSON
           ↓
Most models pass JSON parsing 97%+
But Value Accuracy sits 15-30 points LOWER

This gap is where structured output benchmarks have been lying to us.
```

---

## SOB Benchmark Overview

| Aspect | Details |
|--------|---------|
| **Purpose** | Evaluate structured output quality beyond schema compliance |
| **Sources** | Text (HotpotQA), Image (olmOCR-bench), Audio (AMI) |
| **Records** | 5,000 text, 209 image, 115 audio |
| **Metrics** | 7 per record (not just 1) |
| **Difficulty** | Easy/Medium/Hard schemas weighted (1.0/2.0/3.0) |

---

## The 7 Metrics

| Metric | What it Measures |
|--------|------------------|
| **Value Accuracy** | Exact leaf-value match (PRIMARY) |
| JSON Pass Rate | Parseable JSON |
| Type Safety | Leaf values match schema types |
| Structure Coverage | Required object/array structure |
| Path Recall | All required keys present |
| Faithfulness | Values grounded in context |
| Perfect Response | Every leaf value exactly correct |

---

## Leaderboard (Top 10)

| Rank | Model | Overall | Value Acc | Gap* |
|------|-------|---------|-----------|------|
| 1 | **GPT-5.4** | 0.870 | 79.8% | 19.5pp |
| 2 | **GLM-4.7** | 0.861 | 80.4% | 18.4pp |
| 3 | **Qwen3.5-35B** | 0.861 | 80.1% | 16.8pp |
| 4 | **Gemini-2.5-Flash** | 0.860 | 79.6% | 17.6pp |
| 5 | Qwen3-235B | 0.857 | 78.6% | 19.2pp |
| 6 | Interfaze-Beta | 0.855 | 79.5% | 16.0pp |
| 7 | Claude-Sonnet-4.6 | 0.854 | 77.9% | 20.0pp |
| 8 | GPT-4.1 | 0.850 | 78.3% | 17.0pp |
| 9 | GPT-5-Mini | 0.849 | 76.9% | 21.2pp |
| 10 | Gemma-3-27B | 0.847 | 77.7% | 19.2pp |

*Gap = JSON Pass Rate - Value Accuracy (the "lying gap")

---

## Critical Findings

### 1. The JSON Pass vs Value Accuracy Gap

```
Model         JSON Pass  Value Acc  Gap
GPT-5.4       99.3%      79.8%      19.5pp
Qwen3.5-35B   96.9%      80.1%      16.8pp ← tightest
Gemini-2.5-F  97.2%      79.6%      17.6pp
Schematron-8B 98.7%      73.1%      25.6pp ← widest
```

**Insight**: Every model passes JSON parsing 97%+, but actual leaf-value extraction is 15-30 points lower.

### 2. Modality Performance

| Modality | Best Score | Leader |
|----------|-----------|--------|
| **Text** | 83.0% | GLM-4.7 |
| **Image** | 67.2% | Gemma-4-31B |
| **Audio** | 23.7% | Gemini-2.5-Flash |

Audio is hardest (long transcripts ~7,300 tokens, overlapping speakers).

### 3. Perfect Response Rate

```
Even best models: ~50% perfect response rate
Worst models: ~36%
```

---

## 7 Patterns Worth Internalizing

1. **Valid JSON ≠ Correct JSON** - Gap is 15-30 points everywhere
2. **Structural metrics mask value errors** - Path Recall ~99% while 20-30% values wrong
3. **Modality matters** - Text >> Image >> Audio difficulty
4. **No model wins all three** - GPT-5.4 ranks 3rd on text, 9th on images
5. **Hard schemas separate leaders** - Easy schemas mask real performance
6. **Faithfulness varies** - Hallucination is still a problem
7. **Perfect response is rare** - Best models achieve ~50%

---

## Implications for Our Research

### Where We Use Structured Output

| Use Case | Modality | Importance |
|----------|----------|------------|
| Literature extraction | Text | High (Value Accuracy) |
| Drug candidate classification | Text | High |
| Clinical trial parsing | PDF/Text | Medium |
| Meeting notes analysis | Audio | Low (we don't use) |

### Model Selection for ARP Pipeline

```
For structured extraction tasks:
✅ GLM-4.7 or Qwen3.5-35B (best Value Accuracy)
✅ Gemini-2.5-Flash (good overall, fast)
❌ Avoid models with wide gaps (Schematron-8B)

For our pipeline:
- Use GLM-4.7 for high-accuracy extraction
- Use Gemini-2.5-Flash for balanced speed/accuracy
```

---

## Reference

- Paper: https://arxiv.org/abs/XXXX
- Leaderboard: https://interfaze.ai/leaderboards/structured-output-benchmark
- Dataset: https://huggingface.co/datasets/interfaze-ai/sob

---

*Document: arp-v24/STRUCTURED_OUTPUT_BENCHMARK_SOB_2026.md*  
*Created: 2026-04-29*