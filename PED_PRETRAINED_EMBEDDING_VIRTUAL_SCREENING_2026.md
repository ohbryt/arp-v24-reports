# PED: Pretrained Embedding Distance for Virtual Screening
## arXiv | 2604.24474v1

**Date:** 2026-04-29  
**Authors:** Shiyun Wang, Yifei Wang, Simone Sciabola, Ye Wang (Biogen)  
**URL:** https://arxiv.org/html/2604.24474v1

---

## Overview

```
Traditional molecular similarity measures (fingerprints, 3D alignment):
├── Computationally expensive at scale
├── Rely on hand-crafted descriptors
└── Speed vs accuracy trade-off

Proposed: Pretrained Embedding Distance (PED)
├── Computed directly from pretrained molecular models
├── No task-specific training required
└── Fast and scalable
```

---

## Key Innovation

### Pretrained Embedding Distance (PED)

```
Without any task-specific fine-tuning or explicit similarity supervision:

PED captures:
├── Rich structural information
├── Advanced chemical semantics
└── Without explicit alignment

Two pretrained models used:
├── GeoDiff (diffusion-based, conformation generation)
└── MoLFormer (Transformer-based, SMILES)
```

---

## Tasks Evaluated

| Task | Method | Result |
|------|--------|--------|
| **Correlation analysis** | PED vs traditional 3D alignment | Distinct correlations shown |
| **Virtual screening** | LIT-PCBA benchmark | Effective ranking |
| **Molecular generation** | REINVENT, SynFormer | Successful reward design |

---

## Framework

```
Modern ligand-based drug discovery requires:
├── Similarity/distance signals for scoring
├── Virtual screening prioritization
└── RL-based molecular generation rewards

Traditional approaches:
├── 2D fingerprints (fast but limited)
├── 3D alignment (accurate but slow)

PED solution:
├── Highly scalable
├── Computationally efficient
└──捕获 advanced chemical semantics
```

---

## Comparison

| Aspect | Traditional 2D/3D | PED |
|--------|-------------------|-----|
| Speed | Slow at scale | Fast |
| Accuracy | 3D gold standard | Competitive |
| Supervision | None | None required |
| Scalability | Limited | High |

---

## Molecular Generation Applications

### REINVENT-style (SMILES-based)
```
PED as reward signal
→ Guide exploration toward bioactive regions
```

### SynFormer-style (Synthesizable)
```
PED-guided generation
→ Prioritize synthesizable molecules
```

---

## Relevance to Our Research (ARP v24)

### DGAT1/SLC7A11 Drug Discovery

```
1. Virtual Screening:
   ├── Candidate ranking for DGAT1 inhibitors
   ├── Analog searching with PED
   └── High-throughput screening at scale

2. Molecular Generation:
   ├── REINVENT-style generation for PROTACs
   ├── SynFormer-style for synthesizable linkers
   └── PED-guided reward for RL

3. Integration with existing tools:
   ├── UBio-MolFM (geometry optimization)
   ├── LinkLlama (linker design)
   └── PED (similarity scoring)
```

### Potential Pipeline

```
Traditional VIRTUAL SCREENING:
Compound library → Fingerprints/3D → Ranking → Experimental validation

PED-DRIVEN:
Compound library → PED embeddings → Similarity ranking → Experimental validation

ADVANTAGE: Faster, scalable, captures chemical semantics
```

---

## Key Findings

1. **PED exhibits distinct correlations** with traditional similarity metrics
2. **Effective in ranking molecules** for virtual screening
3. **Guides molecular generation** via reward design
4. **Pretrained embeddings** capture rich structural information
5. **Promising and scalable** for modern AI-aided drug discovery

---

## Reference

```
@article{ped2026,
  title={Advancing Ligand-based Virtual Screening and Molecular Generation 
         with Pretrained Molecular Embedding Distance},
  author={Wang, Shiyun and Wang, Yifei and Sciabola, Simone and Wang, Ye},
  journal={arXiv},
  year={2026},
  doi={2604.24474v1}
}
```

---

*Document: arp-v24/PED_PRETRAINED_EMBEDDING_VIRTUAL_SCREENING_2026.md*  
*Created: 2026-04-29*