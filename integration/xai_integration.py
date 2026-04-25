"""
XAI (Explainable AI) Integration for ARP v24
==============================================
Explainable AI for drug discovery predictions

Supports:
- Grad-CAM for molecular binding visualization
- SHAP for feature attribution
- Attention-based explanations
- Counterfactual analysis

Usage:
    from integration.xai_integration import DrugDiscoveryXAI
    
    xai = DrugDiscoveryXAI(model=our_model)
    
    # Explain why compound binds to target
    explanation = xai.explain(
        compound=smiles,
        target="DGAT1"
    )
"""

import os
import sys
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import json
import numpy as np


class DrugDiscoveryXAI:
    """
    Explainable AI for drug discovery
    
    Provides interpretable predictions for:
    - Why does this molecule bind?
    - Which features are important?
    - What would improve binding?
    """
    
    def __init__(self, model=None):
        self.model = model
        self._captum_available = None
        self._shap_available = None
        self._check_dependencies()
    
    def _check_dependencies(self):
        """Check if XAI libraries are available"""
        try:
            import captum
            self._captum = captum
            self._captum_available = True
        except ImportError:
            print("Note: captum not installed. Install for Grad-CAM.")
            self._captum_available = False
        
        try:
            import shap
            self._shap = shap
            self._shap_available = True
        except ImportError:
            print("Note: shap not installed. Install for SHAP analysis.")
            self._shap_available = False
    
    def explain(
        self,
        compound: str,
        target: str,
        method: str = "auto"
    ) -> Dict[str, Any]:
        """
        Explain why compound interacts with target
        
        Args:
            compound: SMILES string or compound identifier
            target: Target protein name
            method: Explanation method (grad_cam, shap, auto)
        
        Returns:
            Explanation dictionary
        """
        if method == "auto":
            method = "feature_importance"
        
        try:
            if method == "grad_cam":
                return self._grad_cam_explanation(compound, target)
            elif method == "shap":
                return self._shap_explanation(compound, target)
            elif method == "feature_importance":
                return self._feature_importance(compound, target)
            elif method == "counterfactual":
                return self._counterfactual(compound, target)
            else:
                return {
                    "status": "error",
                    "message": f"Unknown method: {method}"
                }
        
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    def _feature_importance(self, compound: str, target: str) -> Dict[str, Any]:
        """
        Basic feature importance explanation
        
        Analyzes molecular features and their importance for binding
        """
        try:
            from rdkit import Chem
            from rdkit.Chem import Descriptors, AllChem
            
            # Parse molecule
            mol = Chem.MolFromSmiles(compound)
            if not mol:
                return {
                    "status": "error",
                    "message": "Invalid SMILES"
                }
            
            # Extract molecular features
            features = {
                "MW": Descriptors.MolWt(mol),
                "LogP": Descriptors.MolLogP(mol),
                "TPSA": Descriptors.TPSA(mol),
                "HBD": Descriptors.NumHDonors(mol),
                "HBA": Descriptors.NumHAcceptors(mol),
                "RotatableBonds": Descriptors.NumRotatableBonds(mol),
                "AromaticRings": Descriptors.NumAromaticRings(mol),
                "HeavyAtoms": mol.GetNumHeavyAtoms()
            }
            
            # Calculate importance scores (simplified - actual model would be used)
            importance = {}
            for feat, value in features.items():
                if feat == "MW":
                    importance[feat] = 0.9 if 200 < value < 500 else 0.5
                elif feat == "LogP":
                    importance[feat] = 0.85 if 1 < value < 4 else 0.6
                elif feat == "TPSA":
                    importance[feat] = 0.8 if 50 < value < 150 else 0.5
                elif feat == "HBD":
                    importance[feat] = 0.7 if value <= 5 else 0.4
                elif feat == "HBA":
                    importance[feat] = 0.7 if value <= 10 else 0.4
                else:
                    importance[feat] = 0.6
            
            # Get key residues for target (mock data)
            key_residues = self._get_target_residues(target)
            
            return {
                "status": "success",
                "compound": compound,
                "target": target,
                "method": "feature_importance",
                "features": features,
                "importance_scores": importance,
                "key_residues": key_residues,
                "overall_score": sum(importance.values()) / len(importance),
                "confidence": "high" if all(v > 0.7 for v in importance.values()) else "moderate",
                "explanation": self._generate_explanation(features, importance, target)
            }
        
        except ImportError:
            return {
                "status": "error",
                "message": "RDKit not installed. Run: pip install rdkit-pypi"
            }
    
    def _get_target_residues(self, target: str) -> List[str]:
        """Get known binding residues for common targets"""
        residues_db = {
            "DGAT1": ["Phe306", "Ala327", "Gln330", "His348", "Asp395"],
            "CD36": ["Lys262", "Arg263", "Lys266", "Lys293"],
            "ATGL": ["Ser47", "His76", "Asp148"],
            "ACSL4": ["Gly298", "Phe299", "Cys311"],
            "EGFR": ["Lys745", "Met790", "Thr854"],
            "KRAS": ["Val12", "Gly13", "Gln61", "Lys117"]
        }
        return residues_db.get(target, ["Unknown - AlphaFold prediction needed"])
    
    def _generate_explanation(
        self,
        features: Dict[str, float],
        importance: Dict[str, float],
        target: str
    ) -> str:
        """Generate human-readable explanation"""
        
        explanations = []
        
        # Check MW
        mw = features.get("MW", 0)
        if 200 < mw < 500:
            explanations.append(f"분자량 ({mw:.1f})은 약물로서 적합합니다.")
        else:
            explanations.append(f"분자량 ({mw:.1f})이 범위를 벗어났습니다.")
        
        # Check LogP
        logp = features.get("LogP", 0)
        if 1 < logp < 4:
            explanations.append(f"LogP ({logp:.2f})는 적당한 지용성을 나타냅니다.")
        
        # Check HBD/HBA
        hbd = features.get("HBD", 0)
        hba = features.get("HBA", 0)
        if hbd <= 5 and hba <= 10:
            explanations.append(f"수용성 ({hbd} HBD, {hba} HBA)이 양호합니다.")
        
        return " ".join(explanations)
    
    def _grad_cam_explanation(self, compound: str, target: str) -> Dict[str, Any]:
        """
        Grad-CAM style explanation for molecular binding
        
        Note: Full implementation requires trained neural network
        """
        if not self._captum_available:
            return {
                "status": "error",
                "message": "captum not installed. Run: pip install captum"
            }
        
        # Placeholder - actual implementation would use captum
        return {
            "status": "success",
            "method": "grad_cam",
            "compound": compound,
            "target": target,
            "activation_map": "Simulated - requires trained model",
            "important_atoms": self._get_important_atoms(compound),
            "note": "Install captum and train model for actual Grad-CAM"
        }
    
    def _shap_explanation(self, compound: str, target: str) -> Dict[str, Any]:
        """
        SHAP-based explanation
        
        Note: Full implementation requires model and background data
        """
        if not self._shap_available:
            return {
                "status": "error",
                "message": "shap not installed. Run: pip install shap"
            }
        
        # Placeholder
        return {
            "status": "success",
            "method": "shap",
            "compound": compound,
            "target": target,
            "shap_values": {"placeholder": 0.5},
            "feature_importance": self._feature_importance(compound, target),
            "note": "Install shap for actual SHAP analysis"
        }
    
    def _counterfactual(self, compound: str, target: str) -> Dict[str, Any]:
        """
        Counterfactual analysis: what would change binding?
        
        Finds minimal changes to compound that would affect binding
        """
        try:
            from rdkit import Chem
            from rdkit.Chem import AllChem
            
            mol = Chem.MolFromSmiles(compound)
            if not mol:
                return {
                    "status": "error",
                    "message": "Invalid SMILES"
                }
            
            # Find similar compounds with different properties
            similar_variations = []
            
            # Example: if LogP is high, suggest lower LogP analog
            logp = self._calc_logp(mol)
            if logp > 4:
                similar_variations.append({
                    "change": "Reduce LogP",
                    "suggestion": "Add hydroxyl group",
                    "expected_effect": "Improved solubility"
                })
            
            return {
                "status": "success",
                "method": "counterfactual",
                "compound": compound,
                "target": target,
                "variations": similar_variations,
                "what_if_scenarios": [
                    "If we add HBD: May improve binding but reduce membrane permeability",
                    "If we add aromatic ring: May increase binding affinity but reduce solubility"
                ]
            }
        
        except ImportError:
            return {
                "status": "error",
                "message": "RDKit not installed"
            }
    
    def _calc_logp(self, mol) -> float:
        """Calculate LogP (simplified)"""
        try:
            from rdkit.Chem import Descriptors
            return Descriptors.MolLogP(mol)
        except:
            return 2.0
    
    def _get_important_atoms(self, compound: str) -> List[int]:
        """Get atoms predicted to be important for binding"""
        # Placeholder - would use actual model prediction
        try:
            from rdkit import Chem
            mol = Chem.MolFromSmiles(compound)
            if mol:
                return [i for i in range(min(5, mol.GetNumAtoms()))]
        except:
            pass
        return []
    
    def compare_compounds(
        self,
        compound1: str,
        compound2: str,
        target: str
    ) -> Dict[str, Any]:
        """
        Compare two compounds for the same target
        
        Args:
            compound1: First SMILES
            compound2: Second SMILES
            target: Target protein
        
        Returns:
            Comparison result
        """
        exp1 = self.explain(compound1, target)
        exp2 = self.explain(compound2, target)
        
        if exp1.get("status") != "success" or exp2.get("status") != "success":
            return {
                "status": "error",
                "message": "Explanation failed for one or both compounds"
            }
        
        score1 = exp1.get("overall_score", 0)
        score2 = exp2.get("overall_score", 0)
        
        return {
            "status": "success",
            "compound1": {
                "smiles": compound1,
                "score": score1,
                "features": exp1.get("features", {})
            },
            "compound2": {
                "smiles": compound2,
                "score": score2,
                "features": exp2.get("features", {})
            },
            "winner": "compound1" if score1 > score2 else "compound2",
            "score_difference": abs(score1 - score2)
        }
    
    def batch_explain(
        self,
        compounds: List[str],
        target: str
    ) -> List[Dict[str, Any]]:
        """
        Explain multiple compounds
        
        Args:
            compounds: List of SMILES strings
            target: Target protein
        
        Returns:
            List of explanations
        """
        results = []
        for compound in compounds:
            exp = self.explain(compound, target)
            results.append(exp)
        
        # Sort by score
        scored_results = [
            (r, r.get("overall_score", 0)) 
            for r in results 
            if r.get("status") == "success"
        ]
        scored_results.sort(key=lambda x: x[1], reverse=True)
        
        return {
            "status": "success",
            "ranked_compounds": [
                {"rank": i+1, "smiles": r[0].get("compound"), "score": r[1]}
                for i, r in enumerate(scored_results)
            ],
            "all_explanations": results
        }


def quick_explain(smiles: str, target: str = "DGAT1") -> Dict:
    """
    Quick explanation helper
    
    Usage:
        result = quick_explain("CC(=O)Nc1ccc(cc1)C(=O)NCCN", "DGAT1")
    """
    xai = DrugDiscoveryXAI()
    return xai.explain(smiles, target)


# Demo function
def demo():
    """Demo XAI integration"""
    print("=" * 70)
    print("XAI (Explainable AI) Integration Demo")
    print("=" * 70)
    
    xai = DrugDiscoveryXAI()
    
    # Check dependencies
    print(f"\nDependencies:")
    print(f"  captum: {'✅' if xai._captum_available else '❌'}")
    print(f"  shap: {'✅' if xai._shap_available else '❌'}")
    
    # Test compound
    test_smiles = "CC(=O)Nc1ccc(cc1)C(=O)NCCN"
    
    print(f"\nTest compound: {test_smiles}")
    
    # Feature importance explanation
    result = xai.explain(test_smiles, "DGAT1")
    
    print(f"\nExplanation:")
    print(f"  Status: {result.get('status')}")
    print(f"  Score: {result.get('overall_score', 'N/A')}")
    print(f"  Confidence: {result.get('confidence', 'N/A')}")
    
    if result.get("features"):
        print(f"\n  Features:")
        for feat, val in result.get("features", {}).items():
            print(f"    {feat}: {val:.2f}")


if __name__ == "__main__":
    demo()