# PF14-siDGAT1 Manufacturing Protocol
## How to Produce Lung-Targeting siRNA Complex

**Date:** 2026-04-28  
**Components:** PF14 peptide + siRNA targeting DGAT1

---

## Overview

```
PF14-siDGAT1 = PF14 peptide (carrier) + siRNA (active agent)
               ↓ non-covalent complex
               ↓
         Cellular uptake via endocytosis
               ↓
         Endosomal escape
               ↓
         Cytosolic siRNA → RISC → DGAT1 knockdown
```

---

## Step 1: Materials Required

### 1.1 PF14 Peptide

```
Source: Commercial suppliers (e.g., PolyPeptide Group, Bachem)
Sequence: Proprietary (but similar to Transportan 10)
Alternative: Use custom synthesis

Recommended:
- Purity: >85% (HPLC purified)
- Quantity: 10-50mg (for validation studies)
- Form: Lyophilized powder
- Storage: -20°C, protected from moisture

Cost estimate: $500-1000 for 10mg
```

### 1.2 siRNA

```
Target: DGAT1 (Exon 2)
Sequence: 5'-GCAUCCUUCAGCGAGAGCAUU-3' (sense)

Purchase from: Thermo Fisher, Dharmacon, or TriLink
Modification: 2'-O-Me + phosphorothioate (for stability)

Standard siRNA format:
Sense: 19-21nt + 2nt overhang (dTdT)
Antisense: Complementary + 2nt overhang (dTdT)

Cost estimate: $300-500 for 1nmole (research scale)
```

### 1.3 Buffer Components

```
Required:
- RNase-free water (DEPC-treated)
- 10mM HEPES buffer, pH 7.4
- 150mM NaCl
- 5% glucose (optional, for osmolarity)

Equipment:
- RNase-free tubes (1.5mL Eppendorf)
- Vortex mixer
- Centrifuge
- Nanodrop or微量 spectrophotometer
```

---

## Step 2: siRNA Resuspension

```
PROTOCOL:

1. Spin down siRNA tube (brief centrifugation, 10,000g, 10 sec)

2. Add RNase-free water to final concentration:
   - For 5nmole tube: Add 100μL → 50μM stock
   - For 1nmole tube: Add 20μL → 50μM stock

3. Vortex vigorously (30 sec, max speed)

4. Incubate room temperature (15 min)

5. Vortex again (30 sec)

6. Store at -20°C (or -80°C for long-term)
   - Aliquot to avoid freeze-thaw cycles
   - Max 5 cycles
```

### siRNA Sequence

```
siDGAT1-1 (19-21nt):
├── Sense (5'→3'): GCAUCCUUCAGCGAGAGCAUU
├── Antisense (5'→3'): UGCUCUCGCUGAAGGAUGCUU
├── Modification: 2'-O-Me on position 2, 5 (sense)
├── Phosphorothioate: 3' end of both strands
└── dTdT overhang: Yes

QC check:
- MW: ~14,000 Da (double-stranded)
- Purity: >85% by HPLC
```

---

## Step 3: PF14 Resuspension

```
PROTOCOL:

1. Centrifuge peptide tube (brief, 10,000g, 10 sec)

2. Add RNase-free water or 10mM HEPES:
   - For 10mg tube: Add 1mL → 10mg/mL (10mM)
   - For 5mg tube: Add 0.5mL → 10mg/mL (10mM)

3. Vortex vigorously (30 sec)

4. Sonicate (if not dissolving):
   - 3 cycles × 10 sec ON, 30 sec OFF
   - Keep on ice

5. Centrifuge (12,000g, 5 min) to remove aggregates

6. Collect supernatant (clear solution)

7. Store at -20°C
   - Aliquot to avoid freeze-thaw
   - Max 10 cycles
```

### PF14 Characterization

```
Expected properties:
- Length: ~14 amino acids
- MW: ~2,000 Da
- Charge: +6 to +8 (net positive at pH 7)
- Solubility: Water soluble
- Purity: >85%

Note: PF14 is amphipathic → forms nanoparticles with siRNA
```

---

## Step 4: Complex Formation (PF14-siRNA)

### Charge Ratio Calculation

```
PF14 charge: +7 (at pH 7.4)
siRNA charge: -2 per base pair (21bp = -42 per molecule)

Charge ratio (N/P) = PF14(+)/siRNA(-)

For CR 2:1:
- siRNA 1nmole (50μM stock, 20μL) = 1nmole
- PF14 needed: 1nmole × (42/7) × 2 = 12nmole
- PF14 stock (10mM) → add 1.2μL

For CR 3:1:
- PF14 needed: 1nmole × (42/7) × 3 = 18nmole
- PF14 stock (10mM) → add 1.8μL

RECOMMENDED: Start with CR 2:1 (lower toxicity)
```

### Protocol (CR 2:1 example)

```
PROTOCOL:

1. Prepare siRNA solution:
   - Take 1nmole siRNA (e.g., 20μL of 50μM stock)
   - Add 80μL HEPES buffer
   - Final volume: 100μL (10μM siRNA)

2. Prepare PF14 solution:
   - Take 12nmole PF14 (from 10mM stock)
   - Add to siRNA solution
   - Mix by pipetting (10x)

3. Incubate:
   - Room temperature, 30 min
   - Protect from light

4. Check:
   - Solution should be clear (no precipitation)
   - If cloudy → too much PF14, reduce CR

5. Use fresh or store at 4°C (24hr max)
```

---

## Step 5: Quality Control

### 5.1 Size Verification (optional)

```
Method: Dynamic Light Scattering (DLS)

Expected:
- Complex size: 50-200nm (nanoparticles)
- PDI: <0.3 (uniform)

If >300nm:
- Reduce PF14 amount
- Increase buffer volume
- Sonicate briefly

Note: Size >200nm may reduce cellular uptake
```

### 5.2 Complex Verification

```
Agarose gel electrophoresis (shift assay):

1. Prepare 1% agarose gel (with ethidium bromide or SyBR)

2. Load samples:
   - Lane 1: siRNA alone (free, fast migration)
   - Lane 2: PF14-siRNA complex (shifted, slow)

3. Run: 100V, 30 min

4. Visualize under UV

Expected:
- Free siRNA: Lower band
- Complex: Upper shift (or no migration)
```

### 5.3 Hemolysis Assay (if IV delivery)

```
Check for red blood cell lysis:

1. Collect mouse/human blood (EDTA tube)
2. Isolate RBCs (centrifuge 300g, 5min)
3. Wash 3x with PBS
4. Resuspend in PBS (5% hematocrit)

5. Add PF14-siRNA complexes (various concentrations)
6. Incubate 37°C, 1hr

7. Centrifuge, collect supernatant

8. Measure absorbance at 540nm (hemoglobin)

Controls:
- Water: 100% lysis (positive)
- PBS: 0% lysis (negative)
- PF14-siRNA: Should be <10% lysis
```

---

## Step 6: Cellular Validation

### 6.1 A549 Treatment

```
Protocol:

1. Seed A549 cells in 24-well plate:
   - Density: 1×10⁵ cells/well
   - Culture: DMEM + 10% FBS
   - Incubate: 37°C, 5% CO₂, overnight

2. Prepare PF14-siDGAT1:
   - Use CR 2:1
   - Final siRNA concentration: 50-100nM
   - Volume: 100μL per well

3. Add complexes to cells:
   - Replace media with fresh (no antibiotics)
   - Add PF14-siRNA complexes
   - Mix gently

4. Incubate: 4-6 hours

5. Replace with fresh media (remove complexes)

6. Incubate: 48-72 hours (for knockdown)

7. Harvest for analysis:
   - qPCR: DGAT1 mRNA (48hr)
   - Western: DGAT1 protein (72hr)
   - Viability: CCK8 (72hr)
```

### 6.2 Transfection Efficiency Control

```
Positive control: Lipofectamine 2000-siRNA
Negative control: PF14 alone (no siRNA)
Mock control: siRNA alone (no PF14)

Expected efficiency:
- Lipofectamine: ~80-90%
- PF14: ~60-80% (similar or slightly lower)

If PF14 < 50% efficiency:
- Increase CR to 3:1
- Or increase siRNA concentration to 200nM
```

---

## Step 7: Optimization Checklist

```
If knockdown < 50%:

□ Increase PF14 (CR 3:1 or 4:1)
□ Increase siRNA concentration (100→200nM)
□ Extend incubation time (4→6hr)
□ Use fresh PF14 (check aggregation)
□ Check siRNA sequence (BLAST)
□ Confirm cell line (A549 vs H1299)
□ Add serum-free incubation step

If cytotoxicity high:

□ Reduce PF14 (CR 1.5:1)
□ Reduce concentration (50nM)
□ Reduce incubation time (2hr)
□ Use healthier cell passage number
```

---

## Step 8: Scale-Up (for animal study)

```
For mouse xenograft study (10 mice):

Required:
- siRNA: 100nmole (per treatment)
- PF14: ~1.2μmole (at CR 2:1)
- Total volume: 1mL (100μL per mouse)

Protocol:
1. Scale up complex formation (10x batch)
2. Sterile filter (0.22μm)
3. Aliquot for injection
4. IV or intratumoral injection (100μL per mouse)
5. Repeat dosing (every 3-4 days)
```

---

## Supplier Information

| Item | Supplier | Catalog | Cost |
|------|----------|---------|------|
| **PF14 peptide** | PolyPeptide Group | Custom | $500-1000/10mg |
| **PF14 peptide** | Bachem | Custom | $600-1200/10mg |
| **siRNA (DGAT1)** | Thermo Fisher | Silencer Select | ~$500/5nmole |
| **siRNA (DGAT1)** | Dharmacon | ON-TARGETplus | ~$400/5nmole |
| **siRNA (SLC7A11)** | Same suppliers | Custom | Same |

---

## Summary: Quick Protocol

```
DAY 1: Order materials (1 week delivery)

DAY 8: siRNA resuspension
       - 50μM stock in RNase-free water
       - Store at -20°C

DAY 8: PF14 resuspension
       - 10mM stock in HEPES
       - Store at -20°C

DAY 9: Complex formation (CR 2:1)
       - 1nmole siRNA + 12nmole PF14
       - 30 min incubation RT

DAY 9: A549 treatment
       - 50-100nM final concentration
       - 4-6 hr incubation
       - 48hr for qPCR, 72hr for Western

DAY 11-12: qPCR analysis
DAY 14-15: Western + viability
```

---

## Alternative: Direct Purchase

```
If you don't want to make it yourself:

Option 1: Ready-made siRNA (commercial)
- Dharmacon ON-TARGETplus
- Already validated, guaranteed knock

Option 2: PF14-siRNA combo kits
- Some suppliers offer pre-formed complexes
- Check with PolyPeptide Group

Option 3: Use Lipofectamine for validation first
- Save PF14 for later
- Validate siRNA sequence
```

---

*Document: arp-v24/PF14_SIDGAT1_MANUFACTURING_2026.md*  
*Protocol: 2026-04-28*