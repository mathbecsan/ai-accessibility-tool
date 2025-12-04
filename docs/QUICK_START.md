# Quick Reference Guide

## 🚀 Quick Start

### First Time Setup (2 minutes)

```bash
# 1. Clone repository
git clone https://github.com/Chaiya8/ai-accessibility-tool.git
cd ai-accessibility-tool

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run frontend/streamlitapp.py
```

Open browser → `http://localhost:8501` ✅

---

## 📖 Documentation Map

| Need                  | Link                                              |
| --------------------- | ------------------------------------------------- |
| **Project Overview**  | [README.md](../README.md)                         |
| **Installation Help** | [docs/SETUP.md](SETUP.md)                         |
| **API Reference**     | [docs/API_DOCUMENTATION.md](API_DOCUMENTATION.md) |
| **Project Structure** | [docs/PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) |
| **Contributing**      | [CONTRIBUTING.md](../CONTRIBUTING.md)             |

---

## 🎯 Common Tasks

### Run Frontend UI

```bash
source venv/bin/activate
streamlit run frontend/streamlitapp.py
# Visit: http://localhost:8501
```

### Run Backend API

```bash
source venv/bin/activate
pip install fastapi uvicorn
uvicorn backend.main:app --reload
# Visit: http://localhost:8000/docs (Swagger)
```

### Run Both (Recommended Development Setup)

```bash
# Terminal 1
source venv/bin/activate
uvicorn backend.main:app --reload

# Terminal 2
source venv/bin/activate
streamlit run frontend/streamlitapp.py
```

### Test Text Transformation

```bash
curl -X POST "http://localhost:8000/transform" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Photosynthesis is the process by which plants convert light energy into chemical energy.",
    "mode": "simplify",
    "level": "3rd grade"
  }'
```

### Download Pre-trained Model

```bash
python -c "from transformers import T5Tokenizer, T5ForConditionalGeneration; T5Tokenizer.from_pretrained('google/flan-t5-small'); T5ForConditionalGeneration.from_pretrained('google/flan-t5-small')"
```

---

## 🔧 Troubleshooting Quick Fixes

| Problem                    | Solution                                                                     |
| -------------------------- | ---------------------------------------------------------------------------- |
| Python not found           | Use `python3` instead of `python`                                            |
| Virtual env not activating | Use full path: `source /path/to/venv/bin/activate`                           |
| Port 8000/8501 in use      | Kill process: `lsof -i :8000 \| awk 'NR==2 {print $2}' \| xargs kill -9`     |
| Model download fails       | Check internet, set proxy, or use CPU mode: `export CUDA_VISIBLE_DEVICES=""` |
| Out of memory              | Reduce model: change to `flan-t5-small` (already default)                    |
| Permission denied          | Don't use `sudo`, use virtual environment instead                            |

---

## 🌐 API Endpoints

### Core Endpoints

| Method | Endpoint     | Purpose                         |
| ------ | ------------ | ------------------------------- |
| POST   | `/transform` | Simplify/summarize/explain text |
| POST   | `/tts`       | Convert text to speech          |
| POST   | `/diagram`   | Generate process diagrams       |
| GET    | `/`          | Health check                    |

### Transformation Modes

```
simplify   → Reduce reading level (with level param)
summarize  → Create concise summary
explain10  → Generate detailed explanation
example    → Create real-world examples
steps      → Break into step-by-step
```

---

## 📁 Key Files

```
README.md              ← Start here!
CONTRIBUTING.md       ← Want to contribute?
LICENSE              ← MIT License
requirements.txt     ← Dependencies

backend/
  ├── main.py        ← API routes
  ├── simplify.py    ← Text transformation
  ├── texttspeech.py ← Audio conversion
  └── diagram.py     ← Visualization

frontend/
  └── streamlitapp.py ← Web UI

docs/
  ├── SETUP.md              ← Installation guide
  ├── API_DOCUMENTATION.md  ← API reference
  └── PROJECT_STRUCTURE.md  ← Architecture
```

---

## 💻 Development Workflow

1. **Fork** the repository on GitHub
2. **Clone** your fork: `git clone https://github.com/YOUR_USERNAME/ai-accessibility-tool.git`
3. **Create branch**: `git checkout -b feature/my-feature`
4. **Make changes** and commit: `git commit -m "[FEATURE] Add my feature"`
5. **Push**: `git push origin feature/my-feature`
6. **Submit Pull Request** on GitHub

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines.

---

## 🔌 Code Examples

### Python - Simplify Text

```python
from backend.simplify import run_instruction

text = "The mitochondria is the powerhouse of the cell."
simplified = run_instruction(text, mode="simplify", level="5th grade")
print(simplified)
```

### Python - API Call

```python
import requests

response = requests.post("http://localhost:8000/transform", json={
    "text": "Complex text here",
    "mode": "simplify",
    "level": "6th grade"
})
result = response.json()
print(result["transformed"])
```

### JavaScript - API Call

```javascript
const response = await fetch("http://localhost:8000/transform", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    text: "Complex text here",
    mode: "simplify",
    level: "6th grade",
  }),
});
const data = await response.json();
console.log(data.transformed);
```

---

## 🧪 Testing

```bash
# (Once tests are set up)
pytest                          # Run all tests
pytest tests/test_simplify.py   # Run specific test
pytest --cov=backend tests/     # With coverage
```

---

## 🚢 Deployment

### Heroku

```bash
heroku login
heroku create learneasytool
git push heroku main
```

### Docker

```bash
docker build -t learneasy:latest .
docker run -p 8501:8501 -p 8000:8000 learneasy:latest
```

---

## 📊 Performance Notes

- **First run**: 2-3 seconds (model loading)
- **Subsequent runs**: <2 seconds (cached model)
- **Transformation**: 0.5-2 seconds depending on text
- **GPU**: Dramatically faster (2-5x speedup)

---

## ❓ FAQs

**Q: Which file should I edit to add a new transformation mode?**
A: Edit `backend/simplify.py` to add logic, then update `backend/main.py` for the API endpoint.

**Q: How do I run just the API without the UI?**
A: `uvicorn backend.main:app --reload` then visit `http://localhost:8000/docs`

**Q: Can I use a different NLP model?**
A: Yes, edit `backend/simplify.py` and change the `model_name` variable.

**Q: What's the difference between `cloudapp.py` and `streamlitapp.py`?**
A: `streamlitapp.py` is the main UI. `cloudapp.py` is an alternative implementation.

**Q: How do I contribute?**
A: Read [CONTRIBUTING.md](../CONTRIBUTING.md) then follow the workflow above.

---

## 📞 Getting Help

1. **Check docs**: [docs/](.)
2. **GitHub Issues**: https://github.com/Chaiya8/ai-accessibility-tool/issues
3. **Discussions**: https://github.com/Chaiya8/ai-accessibility-tool/discussions

---

## 🎯 Next Steps

- [ ] Run the app locally: `streamlit run frontend/streamlitapp.py`
- [ ] Test the API: Visit `http://localhost:8000/docs`
- [ ] Read full docs: Start with [README.md](../README.md)
- [ ] Contribute: See [CONTRIBUTING.md](../CONTRIBUTING.md)

---

**Last Updated:** December 2024
