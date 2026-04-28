"""
Molecular Deep Learning with Unfamiliarity Scoring
================================================
Based on: Nature Machine Intelligence (DOI: 10.1038/s42256-026-01216-w)

This module adds "unfamiliarity" metric for scoring novel molecules.
Poor reconstruction = High unfamiliarity = Structurally novel (OOD)

Integration with our existing molecular_dl.py
"""

import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import json

# ============================================================
# UNFAMILIARITY METRIC CLASS
# ============================================================

class UnfamiliarityScorer:
    """
    Scores molecules for "unfamiliarity" - how much they deviate 
    from the training distribution.
    
    Based on reconstruction loss from autoencoder:
    - Low reconstruction loss → Low unfamiliarity → In distribution
    - High reconstruction loss → High unfamiliarity → OOD (novel)
    
    In practice, we use molecular descriptors to estimate unfamiliarity
    since we don't have the actual JMM trained model.
    """
    
    def __init__(self, reference_molecules: List[str] = None):
        """
        Args:
            reference_molecules: List of SMILES for reference distribution
        """
        self.reference_mols = reference_molecules or []
        self._compute_reference_stats()
    
    def _compute_reference_stats(self):
        """Precompute statistics from reference molecules"""
        # These would be computed from actual training data
        # For now, use typical ranges for drug-like molecules
        self.stats = {
            'mw_mean': 350,
            'mw_std': 100,
            'logp_mean': 2.5,
            'logp_std': 1.2,
            'tpsa_mean': 80,
            'tpsa_std': 30,
            'hba_mean': 3,
            'hba_std': 1.5,
            'hbd_mean': 1,
            'hbd_std': 0.8,
            'rotatable_mean': 5,
            'rotatable_std': 2,
            'aromatic_ring_mean': 2,
            'aromatic_ring_std': 1,
            'heteroatom_mean': 3,
            'heteroatom_std': 1.5,
        }
        
        # Fragment diversity (Bemis-Murcko scaffolds)
        self.scaffold_set = set([
            'benzene', 'pyridine', 'piperidine', 'morpholine',
            'pyrrolidine', 'indole', 'quinoline', 'naphthalene'
        ])
    
    def compute_unfamiliarity(self, smiles: str, descriptors: Dict) -> float:
        """
        Compute unfamiliarity score for a molecule.
        
        Higher score = more out-of-distribution = more novel
        
        Args:
            smiles: SMILES string
            descriptors: Dict with molecular descriptors
            
        Returns:
            unfamiliarity score (higher = more novel)
        """
        score = 0.0
        factors = []
        
        # 1. Molecular weight deviation
        mw = descriptors.get('mw', 350)
        mw_z = abs(mw - self.stats['mw_mean']) / self.stats['mw_std']
        if mw_z > 2:
            score += mw_z * 0.15
            factors.append(('mw_outlier', mw_z))
        
        # 2. LogP deviation
        logp = descriptors.get('logp', 2.5)
        logp_z = abs(logp - self.stats['logp_mean']) / self.stats['logp_std']
        if logp_z > 2:
            score += logp_z * 0.15
            factors.append(('logp_outlier', logp_z))
        
        # 3. TPSA deviation
        tpsa = descriptors.get('tpsa', 80)
        tpsa_z = abs(tpsa - self.stats['tpsa_mean']) / self.stats['tpsa_std']
        if tpsa_z > 2:
            score += tpsa_z * 0.1
            factors.append(('tpsa_outlier', tpsa_z))
        
        # 4. Heteroatom count (scaffold diversity indicator)
        hetero = descriptors.get('heteroatom_count', 3)
        hetero_z = abs(hetero - self.stats['heteroatom_mean']) / self.stats['heteroatom_std']
        if hetero_z > 1.5:
            score += hetero_z * 0.1
            factors.append(('hetero_outlier', hetero_z))
        
        # 5. Aromatic ring count (novel scaffold indicator)
        aromatic = descriptors.get('aromatic_rings', 2)
        aromatic_z = abs(aromatic - self.stats['aromatic_ring_mean']) / self.stats['aromatic_ring_std']
        if aromatic_z > 1.5:
            score += aromatic_z * 0.15
            factors.append(('aromatic_outlier', aromatic_z))
        
        # 6. Ring count (complexity indicator)
        rings = descriptors.get('ring_count', 2)
        if rings < 1 or rings > 5:
            score += 0.2
            factors.append(('ring_unusual', rings))
        
        # 7. Sp3 carbon fraction (3D complexity)
        sp3 = descriptors.get('sp3_fraction', 0.4)
        if sp3 < 0.25 or sp3 > 0.7:
            score += 0.15
            factors.append(('sp3_unusual', sp3))
        
        # 8. Number of stereocenters (specificity indicator)
        stereo = descriptors.get('stereocenters', 0)
        if stereo > 3:
            score += stereo * 0.05
            factors.append(('stereo_complex', stereo))
        
        # 9. Molecular framework novelty
        framework = descriptors.get('framework', 'unknown')
        if framework not in self.scaffold_set:
            score += 0.1  # Non-common framework
            factors.append(('nonstandard_framework', 1))
        
        # Normalize to 0-10 scale (roughly)
        unfamiliarity = min(score * 2, 10.0)
        
        return {
            'unfamiliarity': unfamiliarity,
            'raw_score': score,
            'factors': factors,
            'novel': unfamiliarity > 3.0,  # Threshold for novelty
            'highly_novel': unfamiliarity > 5.0
        }
    
    def score_scaffolds(self, scaffolds: List[Dict]) -> List[Dict]:
        """
        Score multiple scaffolds with unfamiliarity.
        
        Args:
            scaffolds: List of dicts with 'smiles' and 'descriptors'
            
        Returns:
            List of scaffolds with unfamiliarity scores added
        """
        scored = []
        for scaffold in scaffolds:
            smiles = scaffold.get('smiles', '')
            descriptors = scaffold.get('descriptors', {})
            
            result = self.compute_unfamiliarity(smiles, descriptors)
            scored_scaffold = {**scaffold, **result}
            scored.append(scored_scaffold)
        
        # Sort by unfamiliarity (novel first)
        scored.sort(key=lambda x: x['unfamiliarity'], reverse=True)
        
        return scored


def estimate_descriptors(smiles: str) -> Dict:
    """
    Estimate molecular descriptors from SMILES.
    In production, use RDKit for accurate calculation.
    
    This is a simplified placeholder.
    """
    # Placeholder - real implementation uses RDKit
    return {
        'mw': 350 + np.random.uniform(-100, 200),
        'logp': 2.5 + np.random.uniform(-2, 3),
        'tpsa': 80 + np.random.uniform(-40, 80),
        'hba': 3 + np.random.randint(-2, 4),
        'hbd': 1 + np.random.randint(-1, 3),
        'heteroatom_count': 3 + np.random.randint(-2, 5),
        'aromatic_rings': 2 + np.random.randint(-1, 3),
        'ring_count': 2 + np.random.randint(-1, 3),
        'sp3_fraction': 0.4 + np.random.uniform(-0.2, 0.4),
        'stereocenters': np.random.randint(0, 4),
        'rotatable_bonds': 5 + np.random.randint(-3, 8),
        'framework': 'benzene'  # placeholder
    }


# ============================================================
# INTEGRATION WITH MOLECULAR DEEP LEARNING
# ============================================================

class NoveltyAwareMolecularGenerator:
    """
    Enhanced molecular generator with unfamiliarity scoring.
    Combines generation with novelty assessment.
    """
    
    def __init__(self):
        self.unfamiliarity_scorer = UnfamiliarityScorer()
        self.generation_count = 0
    
    def generate_and_score(self, target_gene: str = 'SLC7A11') -> Dict:
        """
        Generate molecules and score novelty.
        
        In production, this would:
        1. Generate candidates (use existing molecular_dl.py logic)
        2. Compute descriptors (RDKit)
        3. Score with unfamiliarity
        4. Return ranked by novelty + activity
        """
        # Placeholder for generation
        generated = self._generate_candidates(target_gene)
        
        # Score each with unfamiliarity
        scored = []
        for mol in generated:
            descriptors = estimate_descriptors(mol['smiles'])
            mol['descriptors'] = descriptors
            result = self.unfamiliarity_scorer.compute_unfamiliarity(
                mol['smiles'], descriptors
            )
            mol.update(result)
            scored.append(mol)
        
        # Sort by novelty (highest unfamiliarity first)
        scored.sort(key=lambda x: x['unfamiliarity'], reverse=True)
        
        return {
            'generated': scored,
            'summary': {
                'total': len(scored),
                'novel': sum(1 for m in scored if m['novel']),
                'highly_novel': sum(1 for m in scored if m['highly_novel']),
                'avg_unfamiliarity': np.mean([m['unfamiliarity'] for m in scored])
            }
        }
    
    def _generate_candidates(self, target: str) -> List[Dict]:
        """Generate placeholder candidates"""
        # This would call the actual molecular generation
        candidates = [
            {
                'smiles': 'C1=CC=C(C=C1)C(=O)NC2=CC=C(C=C2)C(=O)NC3=CC=C(C=C3)C(=O)O',
                'name': 'Novel_scaffold_A',
                'type': 'warhead',
                'target': target
            },
            {
                'smiles': 'CC1=CC(=CC(=C1C2=CC=C(C=C2)F)C3=CC(=CS3)C(=O)NC4=CC=C(C=C4)C#N',
                'name': 'Erastin_analog',
                'type': 'warhead',
                'target': 'SLC7A11'
            },
            {
                'smiles': 'CC(C)CCN(C1=CC=C(C=C1)C(=O)NC2=CC=C(C=C2)C(=O)NN3C(=O)CN(C3=O)C4=CC=CC=C4',
                'name': 'Triazolopyridine_derivative',
                'type': 'linker_warhead',
                'target': target
            }
        ]
        return candidates
    
    def filter_by_novelty(self, molecules: List[Dict], 
                         threshold: float = 3.0) -> List[Dict]:
        """Filter molecules by unfamiliarity threshold"""
        return [m for m in molecules if m.get('unfamiliarity', 0) >= threshold]


def demo():
    """Demonstrate unfamiliarity scoring"""
    print("="*60)
    print("UNFAMILIARITY SCORING DEMO")
    print("="*60)
    
    scorer = UnfamiliarityScorer()
    
    test_molecules = [
        {
            'name': 'Typical drug-like (benzene)',
            'smiles': 'c1ccccc1',
            'descriptors': {
                'mw': 350, 'logp': 2.5, 'tpsa': 80,
                'heteroatom_count': 0, 'aromatic_rings': 1
            }
        },
        {
            'name': 'Novel scaffold (complex)',
            'smiles': 'C1CC2C(C1)C3C(C2)C4C(C3)C5C(C4)C6C(C5)C7C(C6)C8C(C7)C9C(C8)C%10C(C9)C%11C(C%10)C%12C(C%11)C%13C(C%12)C%14C(C%13)C%15C(C%14)C%16C(C%15)C%17C(C%16)C%18C(C%17)C%19C(C%18)C%20C(C%19)C%21C(C%20)C%22C(C%21)C%23C(C%22)C%24C(C%23)C%25C(C%24)C%26C(C%25)C%27C(C%26)C%28C(C%27)C%29C(C%28)C%30C(C%29)C%31C(C%30)C%32C(C%31)C(C)CC%33C(C%32)C%34C(C%33)C%35C(C%34)C%36C(C%35)C(C)CC%37',
            'descriptors': {
                'mw': 1200, 'logp': 8.5, 'tpsa': 150,
                'heteroatom_count': 8, 'aromatic_rings': 0, 'sp3_fraction': 0.95
            }
        },
        {
            'name': 'Out-of-distribution (large)',
            'smiles': 'CC' * 50,
            'descriptors': {
                'mw': 800, 'logp': 6.0, 'tpsa': 200,
                'heteroatom_count': 0, 'aromatic_rings': 0
            }
        }
    ]
    
    print("\nScoring molecules:")
    print("-"*60)
    
    for mol in test_molecules:
        result = scorer.compute_unfamiliarity(
            mol['smiles'], 
            mol['descriptors']
        )
        print(f"\n{mol['name']}:")
        print(f"  Unfamiliarity: {result['unfamiliarity']:.2f}")
        print(f"  Novel: {result['novel']}, Highly novel: {result['highly_novel']}")
        if result['factors']:
            print(f"  Factors: {result['factors']}")
    
    # Demo novel generator
    print("\n" + "="*60)
    print("NOVELTY-AWARE GENERATION DEMO")
    print("="*60)
    
    generator = NoveltyAwareMolecularGenerator()
    results = generator.generate_and_score('SLC7A11')
    
    print(f"\nGenerated {results['summary']['total']} molecules:")
    print(f"  Novel (>3.0): {results['summary']['novel']}")
    print(f"  Highly novel (>5.0): {results['summary']['highly_novel']}")
    print(f"  Average unfamiliarity: {results['summary']['avg_unfamiliarity']:.2f}")
    
    print("\nRanked by novelty:")
    for i, mol in enumerate(results['generated'], 1):
        print(f"  {i}. {mol['name']}: U={mol['unfamiliarity']:.2f}")


if __name__ == '__main__':
    demo()