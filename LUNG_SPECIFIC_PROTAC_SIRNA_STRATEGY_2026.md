# Lung-Specific PROTAC + siRNA Combination Strategy
## SLC7A11 Dual Targeting for NSCLC

**Date:** 2026-04-27  
**Partner:** WuXi TIDES  
**Strategy:** Lung-targeted PROTAC-IM + siRNA Combination  
**Indication:** Non-Small Cell Lung Cancer (NSCLC)

---

## Executive Summary

| Item | Value |
|------|-------|
| **Target** | SLC7A11 (system Xc⁻) |
| **Modality** | PROTAC-IM + siRNA (dual mechanism) |
| **Delivery** | Lung-specific peptide conjugate |
| **Mechanism** | Ferroptosis + Gene knockdown |
| **Partner** | WuXi TIDES |
| **Estimated Cost** | $2-3M (18 months) |
| **Status** | Ready for quotation request |

---

## 1. Scientific Rationale

### 1.1 Dual Targeting Strategy

```
┌─────────────────────────────────────────────────────────────┐
│                  SLC7A11 Dual Targeting                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────┐    ┌──────────────────┐               │
│  │  PROTAC-IM        │    │  siRNA            │               │
│  │  (Small Molecule) │ +  │  (Large Molecule) │               │
│  │                   │    │                   │               │
│  │  • SLC7A11 binding│    │  • SLC7A11 mRNA   │               │
│  │  • CRBN recruitment│   │    degradation   │               │
│  │  • Immune mod.    │    │  • Durable KD    │               │
│  │  • Ferrotosis ↑  │    │  • Ferrotosis ↑  │               │
│  └────────┬─────────┘    └────────┬─────────┘               │
│           │                      │                         │
│           └──────────┬───────────┘                         │
│                      ▼                                     │
│              ┌──────────────┐                              │
│              │   Synergy    │                              │
│              │              │                              │
│              │ • Enhanced   │                              │
│              │   ferroptosis│                              │
│              │ • Reduced   │                              │
│              │   resistance │                              │
│              │ • Durable   │                              │
│              │   response   │                              │
│              └──────────────┘                              │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Mechanism of Synergy

| Mechanism | PROTAC-IM | siRNA | Combined |
|-----------|-----------|-------|-----------|
| SLC7A11 protein degradation | Rapid (4-6h) | Gradual (24-48h) | ✅ Rapid + Durable |
| Ferrotosis induction | +++ | +++ | ✅ +++++ |
| Immune checkpoint modulation | PD-1/PD-L1 | Indirect | ✅ Enhanced |
| Resistance development | Low | Medium | ✅ Very Low |
| Duration of effect | Short (24-48h) | Long (7-14 days) | ✅ Both |

---

## 2. Molecular Design

### 2.1 PROTAC-IM Component

| Parameter | Design |
|-----------|--------|
| **Warhead** | Erastin derivative (IC50 ~80nM) |
| **E3 Ligase** | Pomalidomide (CRBN) |
| **Linker** | PEG4 (4 units) |
| **Immune Modulation** | PD-1/PD-L1 binding motif |
| **Lung Targeting** | Peptide conjugate (RGD/iRGD) |
| **Total MW** | ~1,200 Da |

### 2.2 siRNA Component

| Parameter | Design |
|-----------|--------|
| **Target** | SLC7A11 mRNA (exon 2-3) |
| **Sequence** | 21-mer double-stranded |
| **Modification** | 2'-OMe, PS backbone |
| **Conjugation** | Lung-targeting peptide |
| **Length** | ~14 kDa |
| **Stability** | Enhanced (modified nucleotides) |

### 2.3 Conjugate Structure

```
                    ┌──────────────────────────────────────┐
                    │     Lung Targeting Peptide          │
                    │         (iRGD, cRGD)                │
                    │         MW ~ 2,000                  │
                    └──────────────┬───────────────────────┘
                                   │
                    ┌──────────────┴───────────────────────┐
                    │          LINKER                      │
                    │    (cleavable disulfide)              │
                    └──────────────┬───────────────────────┘
                                   │
           ┌───────────────────────┼───────────────────────┐
           │                       │                       │
           ▼                       ▼                       ▼
    ┌────────────┐      ┌──────────────┐      ┌────────────┐
    │  PROTAC-IM │      │    siRNA     │      │  Targeting │
    │  (~1,200)  │      │   (~14,000)  │      │   Ligand   │
    └────────────┘      └──────────────┘      └────────────┘
```

---

## 3. Lung Targeting Strategy

### 3.1 Targeting Ligands

| Ligand | Target | Affinity | WuXi Support |
|--------|--------|----------|--------------|
| **iRGD** | αvβ3/αvβ5 integrin | nM range | ✅ Available |
| **cRGD** | αvβ3 integrin | nM range | ✅ Available |
| **GE11** | EGFR | nM range | ✅ Available |
| **NGR** | CD13 (angiogenesis) | nM range | ✅ Available |

### 3.2 Delivery Routes

| Route | Method | Pros | Cons |
|-------|--------|------|------|
| **Inhalation** | pMDI, DPI, nebulizer | Direct delivery | Formulation complexity |
| **Intratracheal** | Instillation | Precise dosing | Invasive |
| **Intranasal** | Nose drops | Non-invasive | Upper airway mainly |
| **IV** | Systemic | Easy administration | Off-target effects |

### 3.3 Selected Delivery: Inhalation (Primary)

**Rationale:**
- Direct targeting to lung tumor
- Reduced systemic toxicity
- Higher local concentration
- Patient compliance

---

## 4. WuXi TIDES Collaboration Scope

### 4.1 Work Packages

| Package | Deliverables | Timeline |
|---------|--------------|----------|
| **WP1: PROTAC-IM Synthesis** | 50mg PROTAC-01 | M1-3 |
| **WP2: siRNA Synthesis** | 100mg SLC7A11 siRNA | M1-3 |
| **WP3: Conjugate Development** | PROTAC-siRNA conjugate | M3-6 |
| **WP4: Lung Targeting** | iRGD conjugate optimization | M4-6 |
| **WP5: Inhalation Formulation** | Aerosol formulation | M6-9 |
| **WP6: Analytical Methods** | QC methods, specifications | M3-6 |
| **WP7: Scale-up** | GMP batch (1g) | M9-12 |
| **WP8: Stability** | 12-month stability data | M12-24 |

### 4.2 Cost Estimate

| Package | Estimated Cost | Notes |
|---------|----------------|-------|
| WP1 (PROTAC synthesis) | $80,000 | 50mg, 95% purity |
| WP2 (siRNA synthesis) | $120,000 | 100mg, 90% purity |
| WP3 (conjugate) | $150,000 | Conjugation chemistry |
| WP4 (lung targeting) | $100,000 | Peptide conjugate |
| WP5 (inhalation) | $200,000 | Formulation development |
| WP6 (analytical) | $80,000 | Methods validation |
| WP7 (scale-up) | $300,000 | GMP batch, 1g |
| WP8 (stability) | $150,000 | 12-month accelerated |
| **Contingency (20%)** | $236,000 | |
| **Total** | **$1,416,000** | |

*Note: Actual costs may vary; requires quotation from WuXi TIDES*

---

## 5. Timeline (18 months)

```
Month:  1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18
        │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │
WP1:    [═════════════]
WP2:    [═════════════]
WP3:              [═════════════════]
WP4:                    [═════════════]
WP5:                              [═════════════════]
WP6:              [═════════════════════════════]
WP7:                                            [═════════════]
WP8:                                                  [═════════════════]
```

---

## 6. IND-Enabling Studies (Separate)

| Study | Timeline | Estimated Cost | Performed by |
|-------|----------|----------------|--------------|
| **In vitro PK/PD** | M3-6 | $100,000 | WuXi TIDES |
| **In vitro tox** | M6-9 | $150,000 | Contract lab |
| **In vivo efficacy (PDX)** | M6-12 | $200,000 | Contract lab |
| **In vivo PK** | M9-12 | $150,000 | Contract lab |
| **GLP tox (14-day)** | M12-18 | $400,000 | Contract lab |
| **IND filing** | M18 | $50,000 | Sponsor |

**Total IND-enabling:** ~$1,050,000

**Grand Total:** ~$2.5M (18 months to IND)

---

## 7. Competitive Advantages

| Advantage | Description |
|-----------|-------------|
| **First-in-class** | No lung-targeted SLC7A11 PROTAC-siRNA |
| **Dual mechanism** | Ferroptosis + durable gene knockdown |
| **Synergy** | Enhanced efficacy, reduced resistance |
| **Lung targeting** | Reduced systemic toxicity |
| **Proprietary sequence** | Novel SLC7A11 targeting |

---

## 8. Next Steps

### Immediate (This Week)

1. [x] Strategy finalized ✅
2. [ ] Draft CDA/NDA for WuXi TIDES
3. [ ] Prepare quotation request package
4. [ ] Compile scientific rationale document

### Short-term (2-4 weeks)

- [ ] Send CDA/NDA to WuXi TIDES
- [ ] Submit quotation request
- [ ] Schedule technical call
- [ ] Gather preliminary quotes (3 vendors)

### Medium-term (1-2 months)

- [ ] Evaluate quotes (WuXi + 2 competitors)
- [ ] Finalize scope and budget
- [ ] Sign contract
- [ ] Kick-off meeting

---

## 9. Contact Information for WuXi TIDES

| Item | Details |
|------|---------|
| **Website** | https://tides.wuxiapptec.com |
| **Inquiry Form** | https://tides.wuxiapptec.com/contact |
| **Key Services** | Oligo conjugate, siRNA synthesis |
| **Reference** | Request case studies for lung delivery |

---

## 10. Attachments Needed for Quotation

When submitting quotation request, include:

1. **Scientific Rationale** (this document)
2. **Target Sequence** - SLC7A11 siRNA target region
3. **PROTAC Structure** - preliminary design
4. **Specifications** - purity, scale, timeline
5. **Regulatory Plan** - intended indication, markets
6. **IP Position** - freedom-to-operate analysis

---

*Document generated: 2026-04-27*  
*Strategy: Lung-specific PROTAC-IM + siRNA combination for NSCLC*  
*Partner: WuXi TIDES*
