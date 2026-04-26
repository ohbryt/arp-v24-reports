# XAIPath-Style Knowledge Graph Drug Repurposing Extension

**Date:** 2026-04-26  
**Based on:** XAIPath (Perdomo-Quinteiro et al., Sci Rep 2026)  
**Goal:** Integrate GNN + Knowledge Graph + Explainable AI into ARP v24

---

## 1. Current State

| Component | Status |
|-----------|--------|
| **XAI Integration** | ✅ Grad-CAM, SHAP, Feature Importance |
| **Knowledge Graph** | ✅ Drug-Target network (STRING, DrugBank, ChEMBL) |
| **DTI Prediction** | ✅ GNN-based (TFBindFormer) |
| **MRL Pipeline** | ✅ Multi-objective reward |

**Gap:** No systematic drug repurposing pipeline with explainable paths

---

## 2. XAIPath Pipeline Design

### 2.1 Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  Knowledge Graph Layer                        │
│  DrugBank + STRING + ChEMBL + Hetionet + NeDRex            │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    GNN Prediction Layer                       │
│  GraphSAGE / GAT / GCN for drug-target links               │
│  Predict: Indication, Interaction, Adverse Event            │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                 Explainability Layer (XAIPath)                │
│  • Path Extraction (BFS/DFS in graph)                      │
│  • MinHash Similarity for path comparison                   │
│  • K-means clustering of mechanisms                        │
│  • Rule extraction (Decision tree on GNN embeddings)        │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  Hypothesis Generation                       │
│  Drug-Disease pairs with mechanistic explanations           │
│  Evidence ranking by path confidence                        │
│  Literature validation (PubMed integration)                 │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Target Applications

| Use Case | Description |
|----------|-------------|
| **SLC7A11 Repurposing** | Find new indications for SLC7A11 inhibitors beyond NSCLC |
| **Drug-Disease Matching** | Match existing drugs to lung cancer subtypes |
| **Mechanism Clustering** | Group similar mechanisms for combination therapy |
| **Adverse Event Prediction** | Predict drug-drug interactions |

---

## 3. Implementation Plan

### Phase 1: Knowledge Graph Construction (Month 1-2)

#### 3.1 Data Sources

```python
# Knowledge Graph Integration
SOURCES = {
    "drugbank": "https://www.drugbank.ca/releases/latest",  # Drugs
    "string": "https://string-db.org/cgi/download",          # PPI
    "chembl": "https://www.ebi.ac.uk/chembl/g/",           # Bioactivity
    "hetionet": "https://github.com/hetio/hetionet",       # Disease links
    "therapeutic": "https://dfed杯.github.io/therapeutic/",  # Drug-disease
}
```

#### 3.2 Graph Schema

```python
# Node Types
NODES = {
    "Drug": ["id", "name", "structure", "MOA", "indication"],
    "Protein": ["id", "name", "gene", "family", "function"],
    "Disease": ["id", "name", "DOID", "category", "phenotype"],
    "Pathway": ["id", "name", "kegg_id", "genes"],
    "SideEffect": ["id", "name", "UMLS_id"],
}

# Edge Types
EDGES = {
    "drug_interacts_protein": ["binding_affinity", "action"],
    "protein_interacts_protein": ["score", "channel_type"],
    "drug_treats_disease": ["evidence", "status"],
    "protein_associated_disease": ["evidence", "pmid"],
    "drug_has_side_effect": ["frequency", "severity"],
}
```

### Phase 2: GNN Model Development (Month 2-4)

#### 3.3 Model Architecture

```python
# GNN for Drug Repurposing
class DrugRepurposeGNN(nn.Module):
    def __init__(self, hidden_dim=256):
        self.drug_encoder = GraphEncoder(node_dim=512, hidden_dim=hidden_dim)
        self.disease_encoder = GraphEncoder(node_dim=512, hidden_dim=hidden_dim)
        self.gnn = GATConv(hidden_dim, hidden_dim, n_heads=4)
        self.predictor = MLP(hidden_dim * 2, 1)
        
    def forward(self, drug_graph, disease_graph):
        drug_emb = self.drug_encoder(drug_graph)
        disease_emb = self.disease_encoder(disease_graph)
        combined = torch.cat([drug_emb, disease_emb], dim=-1)
        return self.predictor(combined)
```

#### 3.4 Training Strategy

```python
TRAINING = {
    "task": "Link Prediction (Drug → Disease)",
    "positive_pairs": "Known drug-disease associations",
    "negative_pairs": "Random drug-disease (non-interacting)",
    "loss": "BCEWithLogitsLoss",
    "optimizer": "AdamW",
    "learning_rate": 1e-4,
    "epochs": 100,
    "validation": "AUROC, AUPRC, Precision@10",
}
```

### Phase 3: Explainability Layer (Month 3-5)

#### 3.5 Path Extraction

```python
def extract_paths(graph, drug_node, disease_node, max_length=4):
    """
    Extract mechanistic paths between drug and disease
    Returns: List of paths with node/edge annotations
    """
    paths = []
    for path in bfs_paths(graph, drug_node, disease_node, max_length):
        annotated = annotate_path(path, graph)
        paths.append(annotated)
    return paths

def bfs_paths(graph, start, end, max_length):
    """BFS with depth limit"""
    queue = [(start, [start])]
    while queue:
        node, path = queue.pop(0)
        if len(path) > max_length:
            continue
        for neighbor in graph.neighbors(node):
            if neighbor == end:
                yield path + [neighbor]
            elif neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
```

#### 3.6 Path Similarity (MinHash)

```python
from datasketch import MinHash, MinHashLSH

def path_to_minhash(path):
    """Convert path to MinHash signature"""
    m = MinHash(num_perm=128)
    # Create features from path
    for i, node in enumerate(path):
        m.update(f"node_{i}_{node.type}_{node.id}".encode('utf-8'))
        if i > 0:
            edge = path[i-1].edges[i]
            m.update(f"edge_{edge.type}_{edge.weight}".encode('utf-8'))
    return m

def cluster_paths(paths, n_clusters=10):
    """Cluster similar paths"""
    lsh = MinHashLSH(threshold=0.5)
    for i, path in enumerate(paths):
        lsh.insert(f"path_{i}", path_to_minhash(path))
    
    # K-means on MinHash signatures
    signatures = [path_to_minhash(p) for p in paths]
    clusters = kmeans(signatures, n_clusters)
    return clusters
```

### Phase 4: Drug Repurposing Applications (Month 4-6)

#### 3.7 SLC7A11 Repurposing Pipeline

```python
# Example: Find new indications for SLC7A11 inhibitors
SLC7A11_INHIBITORS = [
    "sulfasalazine",    # Approved (IBD)
    "erastin",          # Research
    "sorafenib",        # Approved (Raf inhibitor, also xCT)
    "sulfasalazine",    # Generic
]

def find_slc7a11_repurposing():
    """
    XAIPath pipeline for SLC7A11 inhibitors
    """
    results = []
    
    for drug in SLC7A11_INHIBITORS:
        # 1. GNN prediction
        predictions = gnn_predict(drug, all_diseases)
        
        # 2. Extract top disease candidates
        top_diseases = predictions.sort_values('score', ascending=False)[:20]
        
        # 3. Path extraction for each prediction
        for _, row in top_diseases.iterrows():
            paths = extract_paths(kg, drug, row['disease'])
            clusters = cluster_paths(paths)
            
            # 4. Generate explainable hypothesis
            hypothesis = {
                'drug': drug,
                'disease': row['disease'],
                'score': row['score'],
                'mechanisms': clusters,
                'literature_support': check_pubmed(drug, row['disease']),
            }
            results.append(hypothesis)
    
    return pd.DataFrame(results)
```

#### 3.8 Expected Outputs

```python
# Example Output
{
    'drug': 'sulfasalazine',
    'disease': 'KRAS-mutant lung adenocarcinoma',
    'score': 0.89,
    'mechanisms': [
        {
            'cluster_id': 0,
            'n_paths': 15,
            'summary': 'xCT inhibition → GSH depletion → ferroptosis',
            'path_example': 'SAS → SLC7A11 → GSH → GPX4 → lipid peroxidation',
            'evidence': ['PMID:12345', 'PMID:67890'],
        },
        {
            'cluster_id': 1,
            'n_paths': 8,
            'summary': 'Immunomodulation via NRF2 pathway',
            'path_example': 'SAS → NRF2 → SLC7A11 → T cell activation',
            'evidence': ['PMID:11111'],
        }
    ]
}
```

---

## 4. Integration with Existing ARP v24

### 4.1 Architecture Diagram

```
                    ┌─────────────────────────────────────────┐
                    │           ARP v24 Unified Platform       │
                    ├─────────────────────────────────────────┤
                    │                                          │
                    │  ┌─────────────┐  ┌─────────────────┐  │
                    │  │ Literature  │  │ Knowledge Graph │  │
                    │  │  Integrator │  │   (XAIPath)    │  │
                    │  └──────┬──────┘  └────────┬────────┘  │
                    │         │                  │             │
                    │         ↓                  ↓             │
                    │  ┌─────────────────────────────────┐   │
                    │  │       GNN Prediction Layer       │   │
                    │  │  Drug Repurpose + DTI + MRL    │   │
                    │  └──────────────┬──────────────────┘   │
                    │                 │                        │
                    │                 ↓                        │
                    │  ┌─────────────────────────────────┐   │
                    │  │     Explainability Layer       │   │
                    │  │  Path Extraction + Clustering   │   │
                    │  └──────────────┬──────────────────┘   │
                    │                 │                        │
                    │                 ↓                        │
                    │  ┌─────────────────────────────────┐   │
                    │  │    Hypothesis Generation       │   │
                    │  │  Repurposing Candidates        │   │
                    │  └─────────────────────────────────┘   │
                    │                                          │
                    └─────────────────────────────────────────┘
```

### 4.2 Module Integration

```python
# integration/xai_path_integration.py
class XAIPathPipeline:
    """
    XAIPath-style drug repurposing pipeline
    Integrates with existing ARP v24 modules
    """
    
    def __init__(self):
        self.kg = KnowledgeGraph()
        self.gnn = DrugRepurposeGNN()
        self.xai = XAIExplainer()
        
    def predict_repurposing(self, drug_name, top_k=10):
        # 1. Get drug node
        drug_node = self.kg.get_drug(drug_name)
        
        # 2. GNN prediction for all diseases
        scores = self.gnn.predict(drug_node, self.kg.diseases)
        
        # 3. Top-k candidates
        top_diseases = scores.nlargest(top_k)
        
        # 4. Path extraction for each
        results = []
        for disease, score in top_diseases.items():
            paths = self.kg.extract_paths(drug_node, disease)
            clusters = self.xai.cluster_paths(paths)
            
            results.append({
                'disease': disease,
                'score': score,
                'mechanisms': clusters,
            })
        
        return results
```

---

## 5. Knowledge Graph Sources

### 5.1 Primary Sources

| Source | Type | Nodes | Edges | URL |
|--------|------|-------|-------|-----|
| DrugBank | Drug | 13,000+ drugs | 200,000+ | drugbank.ca |
| STRING | PPI | 5,000+ proteins | 24,000,000+ | string-db.org |
| ChEMBL | Bioactivity | 2,000,000+ compounds | 20,000,000+ | ebi.ac.uk/chembl |
| Hetionet | Drug-Disease | 47,000 nodes | 2,250,000 | github.com/hetio/hetionet |
| DGIdb | Drug-Gene | 10,000+ drugs | 40,000+ genes | dgidb.org |

### 5.2 Integration Code

```python
# integration/knowledge_graph_loader.py
from langgraph_community.graphs import NetworkxEntityGraph

class KnowledgeGraphBuilder:
    """
    Build multi-source knowledge graph
    """
    
    def __init__(self):
        self.graph = None
        
    def load_drugbank(self, filepath):
        """Load DrugBank XML"""
        pass
    
    def load_string(self, filepath):
        """Load STRING PPI"""
        pass
    
    def load_chembl(self, filepath):
        """Load ChEMBL bioactivity"""
        pass
    
    def build_heterogeneous_graph(self):
        """
        Build heterogeneous graph with:
        - Drug nodes
        - Protein/Gene nodes
        - Disease nodes
        - Pathway nodes
        - Multi-typed edges
        """
        pass
    
    def to_networkx(self):
        """Convert to NetworkX for GNN"""
        pass
    
    def to_langgraph(self):
        """Convert to LangGraph for agentic workflows"""
        pass
```

---

## 6. Expected Outcomes

### 6.1 Metrics

| Metric | Target |
|--------|--------|
| **AUROC** | > 0.90 |
| **AUPRC** | > 0.85 |
| **Path coherence** | > 80% literature support |
| **Novel predictions** | 10+ new drug-disease pairs |

### 6.2 Deliverables

| Deliverable | Timeline |
|-------------|----------|
| Knowledge Graph DB | Month 2 |
| GNN Model | Month 4 |
| XAIPath Pipeline | Month 5 |
| Integration with MRL | Month 6 |
| **Publication** | Month 12 |

---

## 7. Publication Plan

| Journal | Target | Content |
|---------|--------|---------|
| **Nature Methods** | Month 12 | XAIPath methodology |
| **Bioinformatics** | Month 15 | Benchmarking results |
| **NPJ Precision Oncology** | Month 18 | Lung cancer application |

---

## 8. Dependencies

```bash
# Python packages needed
pip install torch_geometric>=2.5.0
pip install datasketch>=1.6.0
pip install networkx>=3.0
pip install langchain-community>=0.0.20
pip install hg_majority_vote>=1.0.0  # For graph ensemble
```

---

## 9. Summary

**This extension adds:**

| Component | Description |
|-----------|-------------|
| **Knowledge Graph** | Multi-source (DrugBank, STRING, ChEMBL, Hetionet) |
| **GNN Prediction** | Drug-disease link prediction |
| **Path Extraction** | Mechanistic paths via BFS |
| **MinHash Clustering** | Similar mechanism grouping |
| **Explainability** | Human-interpretable hypotheses |

**Value:** Systematic drug repurposing with mechanistic explanations, directly supporting SLC7A11/FASN/WEE1 programs.

---

*Design by ARP v24*  
*2026-04-26*