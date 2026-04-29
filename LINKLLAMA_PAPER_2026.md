# LinkLlama: Large Language Model for Chemically Reasonable Linker Design
## bioRxiv | DOI: 10.64898/2026.04.15.718690v1

**Posted:** April 16, 2026  
**Authors:** THGLab  
**URL:** https://www.biorxiv.org/content/10.64898/2026.04.15.718690v1

---

## Overview

```
LinkLlama: LLM for chemically reasonable linker design
Purpose: Design protein/chemical linkers for drug discovery
Model: Llama-3.2-1B fine-tuned on ChEMBL
```

---

## Key Features

| Feature | Description |
|---------|-------------|
| **Model** | Llama-3.2-1B (THGLab/Llama-3.2-1B-Instruct-LinkLlama-Cap50) |
| **Training Data** | ChEMBL |
| **Application** | Protein linker design |
| **Focus** | Chemically reasonable linkers |

---

## Connection to Our Research (ARP v24)

### TOOLS.md Reference

```
LinkLlama (단백질 Linker 설계) - NEW! 🔗
- Location: arp-v24/LinkLlama/
- Model: Llama-3.2-1B fine-tuned on ChEMBL
- Purpose: 화학적으로 합리적인 linker 서열 설계
- biolab: https://www.biorxiv.org/content/10.64898/2026.04.15.718690v1
- 설치: conda env create -f environment.yml && conda activate linkllama
```

### Use Cases

```
1. PROTAC Linker Design
   ├── Our target: DGAT1 + SLC7A11 PROTACs
   └── LinkLlama: Generate chemically feasible linkers

2. Bifunctional Molecule Design
   ├── Linker between two warheads
   └── Critical for molecular stability + activity

3. Peptide-Peptide Conjugates
   ├── Our PF14-siDGAT1 project
   └── Linkers for peptide-RNA conjugates
```

---

## Workflow Integration

```
Our pipeline: LinkLlama → RosettaSearch → 최적 linker

1. LinkLlama: Generate candidate linker sequences
2. RosettaSearch: Optimize structure (arxiv:2604.17175v1)
3. Experimental validation: Synthesize + test
```

---

## Next Steps

```
1. [ ] Read full paper when accessible
2. [ ] Set up LinkLlama environment
3. [ ] Test linker generation for DGAT1 PROTAC
4. [ ] Integrate with RosettaSearch
```

---

## Reference

```
LinkLlama: Enabling Large Language Model for Chemically Reasonable Linker Design
bioRxiv. 2026. doi:10.64898/2026.04.15.718690v1
Posted April 16, 2026
```

---

*Document: arp-v24/LINKLLAMA_PAPER_2026.md*  
*Created: 2026-04-29*