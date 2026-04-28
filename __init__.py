#!/usr/bin/env python3
"""
ARP v24 AI Integration Package
================================
Multi-omics Framework + Molecular Deep Learning + SHAP Analysis

Based on:
- Cell Metabolism: Multi-omics Generative AI (PMID: 42019500)
- Nature Machine Intelligence: Molecular Deep Learning (PMID: 42037759)  
- Frontiers in Pharmacology: SHAP Interpretability (PMID: 42038295)

Usage:
    python3 -m ai_integration.main --mode all --target SLC7A11
"""

import os
import sys
import json
import warnings
warnings.filterwarnings('ignore')

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
import hashlib

# Configuration
CONFIG = {
    'target_gene': 'SLC7A11',
    'pathway_genes': ['SLC7A11', 'SLC3A2', 'GPX4', 'FSP1', 'NRF2', 'KEAP1', 
                     'ATF4', 'CHAC1', 'SLC7A5', 'SLC38A1', 'GCLC', 'GCLM', 
                     'GSS', 'TXNRD1', 'HMOX1', 'GSR', 'PRDX1', 'NAD', 'TXN'],
    'cancer_types': ['LUAD', 'LUSC', 'NSCLC'],
    'models_dir': os.path.dirname(os.path.abspath(__file__)) + '/models',
    'data_dir': os.path.dirname(os.path.abspath(__file__)) + '/data'
}

print("="*70)
print("ARP v24 AI INTEGRATION PACKAGE")
print("Multi-omics + Molecular Deep Learning + SHAP")
print("="*70)

# Import submodules
from .multiomics import MultiOmicsFramework
from .molecular_dl import MolecularDeepLearning
from .shap_analysis import SHAPAnalyzer

__all__ = ['MultiOmicsFramework', 'MolecularDeepLearning', 'SHAPAnalyzer', 'run_complete_pipeline']

def run_complete_pipeline(target: str = 'SLC7A11', output_dir: str = None):
    """
    Run the complete AI integration pipeline for a drug discovery target.
    
    Pipeline:
    1. Multi-omics Analysis (transcriptomics + proteomics + metabolomics)
    2. Molecular Deep Learning (scaffold generation + ADMET prediction)
    3. SHAP Analysis (interpretable predictions + feature importance)
    
    Args:
        target: Gene/protein target name
        output_dir: Output directory for results
    
    Returns:
        Dict with complete pipeline results
    """
    print(f"\n[1/3] Starting Multi-omics Analysis for {target}...")
    
    # 1. Multi-omics Framework
    multiomics = MultiOmicsFramework(CONFIG)
    omics_results = multiomics.analyze(target_gene=target)
    
    print(f"\n[2/3] Running Molecular Deep Learning for {target}...")
    
    # 2. Molecular Deep Learning
    mol_dl = MolecularDeepLearning(CONFIG)
    dl_results = mol_dl.run_pipeline(target_gene=target)
    
    print(f"\n[3/3] SHAP Analysis for {target}...")
    
    # 3. SHAP Analysis
    shap_analyzer = SHAPAnalyzer(CONFIG)
    shap_results = shap_analyzer.analyze(target_gene=target)
    
    # Combine all results
    results = {
        'target': target,
        'timestamp': datetime.now().isoformat(),
        'multiomics': omics_results,
        'molecular_dl': dl_results,
        'shap': shap_results,
        'pipeline_version': '1.0.0'
    }
    
    print("\n" + "="*70)
    print("PIPELINE COMPLETE!")
    print("="*70)
    print(f"\nResults summary:")
    print(f"  - Multi-omics biomarkers: {len(omics_results.get('biomarkers', []))}")
    print(f"  - Novel scaffolds: {len(dl_results.get('novel_scaffolds', []))}")
    print(f"  - SHAP features: {len(shap_results.get('important_features', []))}")
    
    return results

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='ARP v24 AI Integration')
    parser.add_argument('--mode', choices=['all', 'multiomics', 'dl', 'shap'], default='all')
    parser.add_argument('--target', default='SLC7A11')
    parser.add_argument('--output', default=None)
    
    args = parser.parse_args()
    
    if args.mode == 'all':
        results = run_complete_pipeline(args.target, args.output)
    elif args.mode == 'multiomics':
        mo = MultiOmicsFramework(CONFIG)
        results = mo.analyze(args.target)
    elif args.mode == 'dl':
        mdl = MolecularDeepLearning(CONFIG)
        results = mdl.run_pipeline(args.target)
    elif args.mode == 'shap':
        sa = SHAPAnalyzer(CONFIG)
        results = sa.analyze(args.target)
    
    print("\nResults:", json.dumps(results, indent=2, default=str))
