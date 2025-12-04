# Project Structure Overview

## 📂 LearnEasy - AI Accessibility Tool

```
ai-accessibility-tool/
│
├── 📄 README.md                          # Main project documentation
├── 📄 CONTRIBUTING.md                    # Contribution guidelines
├── 📄 LICENSE                            # MIT License
├── 📄 requirements.txt                   # Python dependencies
├── 📄 .gitignore                         # Git ignore rules
│
├── 📁 backend/                           # Backend API (FastAPI)
│   ├── main.py                          # FastAPI app and routes
│   ├── simplify.py                      # Text transformation logic
│   ├── texttspeech.py                   # Text-to-Speech conversion
│   └── diagram.py                       # Diagram generation
│
├── 📁 frontend/                          # Frontend (Streamlit)
│   ├── streamlitapp.py                  # Main Streamlit interface
│   └── cloudapp.py                      # Alternative UI implementation
│
└── 📁 docs/                              # Documentation
    ├── SETUP.md                         # Detailed setup guide
    └── API_DOCUMENTATION.md             # API reference
```

## 📋 File Descriptions

### Root Level Files

| File               | Purpose                                                   |
| ------------------ | --------------------------------------------------------- |
| `README.md`        | Comprehensive project overview, features, and quick start |
| `CONTRIBUTING.md`  | Guidelines for contributing to the project                |
| `LICENSE`          | MIT License for the project                               |
| `requirements.txt` | List of Python dependencies with versions                 |
| `.gitignore`       | Files and directories to exclude from git                 |

### Backend Directory (`backend/`)

| File             | Purpose                                      |
| ---------------- | -------------------------------------------- |
| `main.py`        | FastAPI application with all API endpoints   |
| `simplify.py`    | Core NLP logic for text transformation       |
| `texttspeech.py` | Text-to-Speech conversion functionality      |
| `diagram.py`     | Process diagram generation and visualization |

### Frontend Directory (`frontend/`)

| File              | Purpose                                        |
| ----------------- | ---------------------------------------------- |
| `streamlitapp.py` | Main web UI built with Streamlit               |
| `cloudapp.py`     | Alternative or legacy Streamlit implementation |

### Documentation Directory (`docs/`)

| File                   | Purpose                                           |
| ---------------------- | ------------------------------------------------- |
| `SETUP.md`             | Step-by-step installation and configuration guide |
| `API_DOCUMENTATION.md` | Complete API reference with examples              |

---

## 🚀 Quick Navigation

### For Users

- Start with: `README.md`
- Setup help: `docs/SETUP.md`
- Run: `streamlit run frontend/streamlitapp.py`

### For Developers

- Setup: `docs/SETUP.md`
- API Reference: `docs/API_DOCUMENTATION.md`
- Contributing: `CONTRIBUTING.md`
- Backend code: `backend/`

### For Contributors

- Guidelines: `CONTRIBUTING.md`
- Code structure: See sections below
- Commit standards: See `CONTRIBUTING.md`

---

## 🔧 Key Dependencies

### Frontend

- **streamlit** - Web UI framework
- **requests** - HTTP client for API calls

### Backend

- **fastapi** - Web framework for APIs
- **uvicorn** - ASGI server
- **transformers** - NLP models (Hugging Face)
- **torch** - Deep learning framework
- **pydantic** - Data validation

### Common

- **gtts** - Text-to-Speech conversion
- **graphviz** - Diagram visualization

---

## 📡 Architecture

```
┌─────────────────────────────────────────┐
│       User Browser (Port 8501)          │
│   Streamlit Web Interface (Frontend)    │
└────────────────┬────────────────────────┘
                 │
                 │ HTTP/REST Requests
                 ▼
┌─────────────────────────────────────────┐
│   FastAPI Backend Server (Port 8000)    │
│  ┌─────────────────────────────────────┐│
│  │    /transform   (Text Processing)   ││
│  │    /tts         (Audio Conversion)  ││
│  │    /diagram     (Visualization)     ││
│  └─────────────────────────────────────┘│
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│     NLP Models (FLAN-T5)                │
│     Libraries (Transformers, PyTorch)   │
└─────────────────────────────────────────┘
```

---

## 🔄 Data Flow

### 1. Text Simplification Flow

```
User Input (Frontend)
    ↓
Streamlit UI
    ↓
HTTP POST /transform
    ↓
Backend API (main.py)
    ↓
Simplification Logic (simplify.py)
    ↓
NLP Model Processing
    ↓
Simplified Text
    ↓
Response to Frontend
    ↓
Display Result
```

### 2. Text-to-Speech Flow

```
User Input (Text)
    ↓
HTTP POST /tts
    ↓
Backend API (main.py)
    ↓
TTS Processing (texttspeech.py)
    ↓
Google TTS API
    ↓
MP3 Audio (Base64)
    ↓
Response to Frontend
    ↓
Play Audio
```

---

## 📚 Development Workflow

### Setting Up Development Environment

1. Clone repository
2. Create virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Start backend: `uvicorn backend.main:app --reload`
5. Start frontend: `streamlit run frontend/streamlitapp.py`

### Adding New Features

1. Implement logic in `backend/`
2. Add API endpoint in `main.py`
3. Create UI component in `frontend/streamlitapp.py`
4. Test thoroughly
5. Document changes
6. Submit pull request

### Code Organization Principles

- **Separation of Concerns**: UI, API, and logic are separate
- **Modularity**: Each transformation mode has its own logic
- **Reusability**: Core functions used by both API and UI
- **Testability**: Functions designed to be easily testable
- **Documentation**: All functions have docstrings

---

## 🧪 Testing

```bash
# Run tests (once implemented)
pytest tests/

# With coverage
pytest --cov=backend tests/

# Specific test file
pytest tests/test_simplify.py
```

---

## 📈 Performance Considerations

| Component      | Performance | Notes                     |
| -------------- | ----------- | ------------------------- |
| Model Loading  | 2-3 sec     | Happens once, then cached |
| Text Transform | 0.5-2 sec   | Depends on text length    |
| TTS Generation | 1-3 sec     | Depends on text length    |
| API Response   | <100ms      | Without model loading     |

---

## 🔒 Security Notes

- No authentication currently required
- Use environment variables for config
- Input validation on API endpoints
- Sanitize text before processing
- Rate limiting recommended for production

---

## 📝 Version History

### v1.0 (Current)

- ✅ Text simplification
- ✅ Summarization
- ✅ Explanation generation
- ✅ Example generation
- ✅ Process decomposition
- ✅ Text-to-Speech
- ✅ Diagram generation

### Planned Improvements

- [ ] Multi-language support
- [ ] Offline mode
- [ ] Mobile app
- [ ] Advanced analytics
- [ ] Custom model fine-tuning

---

## 🤝 Contributing

See `CONTRIBUTING.md` for detailed guidelines.

Quick summary:

1. Fork repository
2. Create feature branch
3. Make changes with clear commits
4. Submit pull request
5. Respond to feedback

---

## 📞 Support & Resources

- 📖 Documentation: See `docs/`
- 🐛 Bug Reports: GitHub Issues
- 💬 Discussions: GitHub Discussions
- 📧 Contact: [Project maintainers]

---

**Last Updated:** December 2024
