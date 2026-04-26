# PROTAC + Quantum Chemistry Integration Design

**Date:** 2026-04-26  
**Based on:** Sargolzaei & Nikoofard (2026), J Comput Aided Mol Des  
**Goal:** Integrate DFT calculations into SLC7A11 PROTAC design

---

## 1. Current State

| Component | Status |
|-----------|--------|
| **SLC7A11 PROTAC Design** | ✅ Initial SAR defined |
| **MRL Pipeline** | ✅ Synthesizability scoring |
| **XAI Integration** | ✅ Mechanistic explanation |

**Gap:** No quantum chemical calculations for binding energy prediction

---

## 2. Quantum Chemistry Integration

### 2.1 Why DFT for PROTAC Design?

```
PROTAC Structure:
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  SLC7A11 Warhead │────│    Linker      │────│  E3 Ligase Warhead │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        ↓                        ↓                       ↓
   Binding to          Distance/Conformation     Binding to CRBN/VHL
   SLC7A11 protein     Optimization            protein
```

**DFT can predict:**
- Binding energy of warhead to target protein
- Linker conformational stability
- Reactivity of electrophilic warheads
- Solvation effects

### 2.2 DFT Levels of Theory

| Level | Accuracy | Speed | Use Case |
|-------|----------|-------|----------|
| **PM6** | Low | Fast | Initial screening (100s of compounds) |
| **B3LYP-D3BJ** | Medium | Medium | Lead optimization (10s of compounds) |
| **ωB97X-D** | High | Slow | Final validation (1-5 compounds) |
| **DLPNO-CCSD(T)** | Very High | Very Slow | Benchmark only |

---

## 3. Implementation Design

### 3.1 Pipeline Architecture

```
                    ┌─────────────────────────────────────────┐
                    │       PROTAC Design Pipeline              │
                    └─────────────────────────────────────────┘
                                      ↓
                    ┌─────────────────────────────────────────┐
                    │  Step 1: Warhead Binding (DFT)          │
                    │  • SLC7A11 active site docking          │
                    │  • Binding energy calculation             │
                    │  • Reactivity assessment                 │
                    └─────────────────────────────────────────┘
                                      ↓
                    ┌─────────────────────────────────────────┐
                    │  Step 2: Linker Optimization (DFT)      │
                    │  • Conformational analysis               │
                    │  • Distance between warheads             │
                    │  • Synthetic accessibility score         │
                    └─────────────────────────────────────────┘
                                      ↓
                    ┌─────────────────────────────────────────┐
                    │  Step 3: E3 Ligase Recruiting (DFT)     │
                    │  • CRBN/VHL binding affinity             │
                    │  • Ternary complex stability             │
                    └─────────────────────────────────────────┘
                                      ↓
                    ┌─────────────────────────────────────────┐
                    │  Step 4: Multi-Objective Ranking         │
                    │  • DFT binding energies                  │
                    │  • MRL synthesizability                 │
                    │  • ADMET predictions                    │
                    │  • Final priority score                  │
                    └─────────────────────────────────────────┘
```

### 3.2 Code Structure

```python
# integration/dft_protac_design.py

class DFTPROTACDesigner:
    """
    Quantum chemistry-guided PROTAC design
    """
    
    def __init__(self):
        self.dft_engine = DFTEngine()  # ORCA or PySCF
        self.docking_engine = DockingEngine()  # AutoDock Vina
        self.mrl_scorer = MRLScorer()
        
    def evaluate_warhead(self, warhead_smiles, target_pdb):
        """
        Step 1: Evaluate warhead binding to SLC7A11
        """
        # 1.1 Dock warhead to SLC7A11 active site
        docking_pose = self.docking_engine.dock(
            warhead_smiles, 
            target_pdb,
            exhaustiveness=32
        )
        
        # 1.2 Calculate binding energy with DFT
        # Use QM region = warhead + key residues
        binding_energy = self.dft_engine.calculate_binding_energy(
            pose=docking_pose,
            method='B3LYP-D3BJ',
            basis_set='6-31G*',
            qm_region_size=50  # atoms
        )
        
        # 1.3 Calculate reactivity (electrophilicity)
        reactivity = self.dft_engine.calculate_reactivity(
            warhead_smiles,
            descriptor='electrophilicity'
        )
        
        return {
            'docking_score': docking_pose.score,
            'dft_binding_energy': binding_energy,  # kcal/mol
            'electrophilicity': reactivity,
        }
    
    def evaluate_linker(self, linker_smiles, warhead_pose, e3_pose):
        """
        Step 2: Evaluate linker conformation
        """
        # 2.1 Generate conformers
        conformers = self.docking_engine.generate_conformers(linker_smiles)
        
        # 2.2 Calculate distances between attachment points
        results = []
        for conf in conformers:
            # Distance from warhead attachment to e3 attachment
            distance = self.dft_engine.calculate_distance(
                conf,
                point_a=warhead_pose.attachment,
                point_b=e3_pose.attachment
            )
            
            # Conformational energy
            conf_energy = self.dft_engine.calculate_energy(
                conf,
                method='PM6'  # Fast for screening
            )
            
            results.append({
                'conformer': conf,
                'distance': distance,
                'energy': conf_energy,
            })
        
        # Return best linker conformer
        return min(results, key=lambda x: x['energy'])
    
    def evaluate_ternary_complex(self, protac_pdb, e3_pdb, target_pdb):
        """
        Step 3: Evaluate PROTAC + E3 + Target ternary complex
        """
        # 3.1 Build ternary complex model
        complex_structure = self.docking_engine.build_ternary(
            protac_pdb,
            e3_pdb,
            target_pdb
        )
        
        # 3.2 Calculate cooperative binding
        # ΔG_bind = ΔG_binary + ΔG_cooperativity
        binary_target = self.dft_engine.calculate_binding_energy(
            protac_pdb + target_pdb
        )
        binary_e3 = self.dft_engine.calculate_binding_energy(
            protac_pdb + e3_pdb
        )
        ternary = self.dft_engine.calculate_binding_energy(
            protac_pdb + e3_pdb + target_pdb
        )
        
        cooperativity = ternary - (binary_target + binary_e3)
        
        return {
            'binary_target': binary_target,
            'binary_e3': binary_e3,
            'ternary': ternary,
            'cooperativity': cooperativity,  # Negative = favorable
        }
    
    def multi_objective_rank(self, candidates):
        """
        Step 4: Rank PROTAC candidates
        """
        ranked = []
        
        for cand in candidates:
            # DFT scores (higher = better)
            binding_score = -cand['dft_binding_energy'] / 10  # Normalize
            reactivity_score = cand['electrophilicity'] / 5
            cooperativity_score = -cand['cooperativity'] / 5
            
            # MRL score
            mrl_score = self.mrl_scorer.score(cand['smiles'])
            
            # ADMET score (from prior calculation)
            admet_score = cand['admet']['overall']
            
            # Combined score (weighted)
            final_score = (
                0.25 * binding_score +
                0.20 * mrl_score +
                0.25 * admet_score +
                0.15 * reactivity_score +
                0.15 * cooperativity_score
            )
            
            ranked.append({
                'smiles': cand['smiles'],
                'final_score': final_score,
                'binding_energy': cand['dft_binding_energy'],
                'mrl_score': mrl_score,
                'admet_score': admet_score,
                'cooperativity': cand['cooperativity'],
            })
        
        # Sort by final score
        return sorted(ranked, key=lambda x: x['final_score'], reverse=True)
```

### 3.3 DFT Software Options

```python
# Option 1: ORCA (Free for academic)
ORCA_CONFIG = {
    'executable': '/path/to/orca',
    'methods': ['B3LYP', 'ωB97X-D', 'DLPNO-CCSD(T)'],
    'basis_sets': ['6-31G*', 'def2-TZVP'],
    'parallel': True,
    'n_cores': 16,
}

# Option 2: PySCF (Python-based, free)
PYSCF_CONFIG = {
    'methods': ['B3LYP', 'PBE0'],
    'basis_sets': ['cc-pVDZ', 'cc-pVTZ'],
    'integral_engine': 'mcfun',
}

# Option 3: Q-Chem (Commercial)
QCHEM_CONFIG = {
    'methods': ['ωB97X-V', 'VV10'],
    'basis_sets': ['def2-TZVP'],
}
```

---

## 4. SLC7A11 PROTAC Application

### 4.1 Warhead Options

```python
SLC7A11_WARHEADS = [
    {
        'name': 'Sulfasalazine (SAS)',
        'smiles': 'O=C(Nc1cccc(C2=CC(=NN=C2C(=O)O)C(=O)O)c1)CC(=O)O',
        'type': 'xCT inhibitor',
        'note': 'Approved drug, weak potency',
    },
    {
        'name': 'Erastin',
        'smiles': 'CC1=CC(=NN1C2=CC=C(C=C2)OCCCN3CCNCC3)C(=O)N',
        'type': 'xCT inhibitor',
        'note': 'Research tool, potent but insoluble',
    },
    {
        'name': 'Novel sulfamate',
        'smiles': 'CNS(=O)(=O)C1=CC=C(C=C1)N2C=NC3=C2N=C(N=C3N)N',
        'type': 'xCT inhibitor',
        'note': 'Our design - predicted potent',
    },
]
```

### 4.2 E3 Ligase Options

```python
E3_LIGASES = [
    {
        'name': 'CRBN (Pomalidomide)',
        'smiles': 'O=C1C(C2=CC=CC=C2NC1=O)N1CCC(C(=O)N)=CC1',
        ' recruiting_moiety': 'Pomalidomide',
        'note': 'Most used, good PK',
    },
    {
        'name': 'VHL',
        'smiles': 'CC(C)(C)NC(=O)C1CCCN1C(=O)C2CCCCC2',
        'recruiting_moiety': 'VHL ligand',
        'note': 'High affinity, less explored',
    },
]
```

### 4.3 Linker Options

```python
LINKERS = [
    {
        'name': 'PEG3',
        'smiles': 'OCCOCCOCCO',
        'length': 'medium',
        'hydrophilicity': 'high',
    },
    {
        'name': 'Alkyl-C3',
        'smiles': 'CCCCC',
        'length': 'short',
        'hydrophilicity': 'low',
    },
    {
        'name': 'Mixed (alkyl-PEG)',
        'smiles': 'CCCOCCOCCO',
        'length': 'medium',
        'hydrophilicity': 'medium',
    },
]
```

---

## 5. Expected Outcomes

### 5.1 Metrics

| Metric | Target | Method |
|--------|--------|--------|
| **DFT binding energy** | < -10 kcal/mol | B3LYP-D3BJ/6-31G* |
| **Coopertivity** | < -2 kcal/mol | Ternary calculation |
| **Synthesizability** | > 0.7 | MRL score |
| **ADMET pass rate** | > 80% | Predicted |

### 5.2 Validation Plan

```
1. Validate DFT against experimental Ki values for known ligands
2. Benchmark against X-ray structures (if available)
3. Test top 10 candidates in cellular assays
4. Validate in xenograft model
```

---

## 6. Timeline

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| **Setup** | Week 1-2 | ORCA/PySCF installation, test calculations |
| **Warhead screen** | Week 3-4 | DFT binding energies for 20 warheads |
| **Linker optimization** | Week 5-6 | 10 linker variants evaluated |
| **Ternary complex** | Week 7-8 | Top 5 PROTACs validated |
| **Synthesis plan** | Week 9-10 | CDMO-ready molecules |

---

## 7. Dependencies

```bash
# DFT Software (choose one)
# ORCA (free for academic)
conda install -c psi4 orca

# PySCF (Python, free)
pip install pyscf

# For docking
pip install vina  # AutoDock Vina

# For visualization
pip install rdkit pymol  # or nglview for Jupyter
```

---

## 8. Summary

**This integration adds:**

| Component | Description |
|-----------|-------------|
| **Quantum binding** | DFT-accurate binding energies |
| **Reactivity** | Electrophilicity calculations |
| **Coopertivity** | Ternary complex modeling |
| **Multi-objective** | Combined DFT + MRL + ADMET ranking |

**Value:** More accurate PROTAC design, reduced experimental failure rate, mechanistic insight into binding.

---

*Design by ARP v24*  
*2026-04-26*