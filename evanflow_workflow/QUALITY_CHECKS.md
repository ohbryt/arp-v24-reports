# ARP v24 Quality Checks

## Before "Done" - Run These

### 1. No Invented Values Check
```bash
# Verify all file paths exist
find . -name "*.py" | xargs grep -E "Path\(|open\(" | grep -v ".pyc"

# Check for hardcoded URLs
grep -rE "https?://" --include="*.py" | grep -v "# note:"

# Verify API keys are env vars
grep -rE "api_key|token|password" --include="*.py" | grep -v "os.environ"
```

### 2. Citation Check
- [ ] All biological data has literature citation
- [ ] All algorithm parameters cited
- [ ] All dataset sources documented

### 3. Test Coverage
```bash
# Run tests
pytest --cov=. --cov-report=term-missing

# Minimum coverage: 70%
```

### 4. Lint & Type Check
```bash
# Lint
ruff check .

# Type check
mypy . --ignore-missing-imports
```

### 5. Five Failure Modes
1. Hallucinated actions: Did APIs actually respond?
2. Scope creep: Did requirements stay stable?
3. Cascading errors: Did errors propagate?
4. Context loss: Does code remember earlier decisions?
5. Tool misuse: Right tool for each job?

---

## Common Issues to Avoid

### Invented Values (Never Do This)
```python
# BAD - invented path
data = pd.read_csv("/users/ocm/data/file.csv")  # Might not exist

# GOOD - verified path
DATA_PATH = Path(os.environ.get("DATA_PATH", "data/"))
data = pd.read_csv(DATA_PATH / "file.csv")  # Checked
```

### Missing Citations
```python
# BAD - magic number
threshold = 0.7  # Why this value?

# GOOD - cited
threshold = 0.7  # From: Smith et al. 2025, DOI: xxx
```

### No Tests
```python
# BAD
def process_dgat1(data):
    return data.transform(lambda x: x * 0.7)

# GOOD
def test_process_dgat1():
    result = process_dgat1(pd.DataFrame({"a": [1, 2, 3]}))
    assert result["a"].tolist() == [0.7, 1.4, 2.1]
```
