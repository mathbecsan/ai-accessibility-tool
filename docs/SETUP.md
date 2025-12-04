# Setup & Installation Guide

## 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Pre-Installation](#pre-installation)
3. [Installation Steps](#installation-steps)
4. [Running the Application](#running-the-application)
5. [Troubleshooting](#troubleshooting)
6. [Configuration](#configuration)
7. [Docker Setup (Optional)](#docker-setup-optional)

---

## 🖥️ System Requirements

### Minimum Requirements

- **OS:** macOS 10.13+, Ubuntu 18.04+, Windows 10+
- **RAM:** 4 GB (8 GB recommended)
- **Storage:** 5 GB (for model files)
- **Python:** 3.8 or higher
- **Internet:** Required for first-run model download

### Recommended Setup

- **RAM:** 8+ GB
- **GPU:** NVIDIA GPU with CUDA support (optional but recommended)
- **SSD:** For faster model loading

---

## 📦 Pre-Installation

### 1. Verify Python Installation

```bash
python --version
python3 --version
```

Should show Python 3.8 or higher.

### 2. Install/Update pip

```bash
python -m pip install --upgrade pip
```

### 3. Verify Git Installation

```bash
git --version
```

If not installed, download from [git-scm.com](https://git-scm.com/)

---

## 🚀 Installation Steps

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/Chaiya8/ai-accessibility-tool.git

# Navigate to project directory
cd ai-accessibility-tool
```

### Step 2: Create Virtual Environment

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (Command Prompt):**

```bash
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**

```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

### Step 3: Upgrade pip and setuptools

```bash
pip install --upgrade pip setuptools wheel
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:

- **streamlit** - Frontend UI framework
- **transformers** - NLP model library
- **torch** - Deep learning framework
- **sentencepiece** - Tokenization
- **gtts** - Text-to-Speech
- **graphviz** - Diagram generation

### Step 5: Verify Installation

```bash
python -c "import streamlit; import transformers; import torch; print('✓ All dependencies installed successfully!')"
```

### Step 6: Download Pre-trained Model

The model will auto-download on first run, but you can pre-download:

```bash
python -c "from transformers import T5Tokenizer, T5ForConditionalGeneration; print('Downloading model...'); T5Tokenizer.from_pretrained('google/flan-t5-small'); T5ForConditionalGeneration.from_pretrained('google/flan-t5-small'); print('✓ Model downloaded successfully!')"
```

---

## 💻 Running the Application

### Option 1: Streamlit Frontend (Recommended for Users)

```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Run the frontend
streamlit run frontend/streamlitapp.py
```

**Output:**

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.100:8501
```

Visit `http://localhost:8501` in your browser.

### Option 2: Backend API (For Development)

In a new terminal:

```bash
# Activate virtual environment
source venv/bin/activate

# Install FastAPI and uvicorn (if not already installed)
pip install fastapi uvicorn

# Run the backend
uvicorn backend.main:app --reload
```

**Output:**

```
Uvicorn running on http://127.0.0.1:8000
```

Access:

- **API:** http://localhost:8000
- **Swagger Docs:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### Option 3: Both Frontend and Backend

**Terminal 1 - Backend:**

```bash
source venv/bin/activate
uvicorn backend.main:app --reload
```

**Terminal 2 - Frontend:**

```bash
source venv/bin/activate
streamlit run frontend/streamlitapp.py
```

---

## 🔧 Troubleshooting

### Issue 1: Python Version Error

**Error:** `Python 3.8+ required`

**Solution:**

```bash
python3 --version  # Check version
python3 -m venv venv  # Use python3 explicitly
source venv/bin/activate
```

### Issue 2: Virtual Environment Not Activating

**Error:** `command not found: python` or wrong Python version

**Solution:**

```bash
# Verify venv location
which python
which python3

# Manually set Python path
export PATH="$PWD/venv/bin:$PATH"
```

### Issue 3: pip Permission Denied

**Error:** `Permission denied: /Library/...`

**Solution:**

```bash
# Don't use sudo, use virtual environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # No sudo needed
```

### Issue 4: Model Download Fails

**Error:** `Connection error` or `Model download failed`

**Solution:**

```bash
# Try with manual cache directory
export HF_HOME="./models"
python -c "from transformers import T5Tokenizer; T5Tokenizer.from_pretrained('google/flan-t5-small')"

# Or set proxy if behind corporate firewall
pip install -r requirements.txt --proxy [user:passwd@]proxy.server:port
```

### Issue 5: Port Already in Use

**Error:** `Address already in use: ('127.0.0.1', 8000)`

**Solution:**

```bash
# Find process using port
lsof -i :8000

# Kill the process (macOS/Linux)
kill -9 <PID>

# Or use different port
streamlit run frontend/streamlitapp.py --server.port 8502
```

### Issue 6: Out of Memory

**Error:** `CUDA out of memory` or `MemoryError`

**Solution:**

```bash
# Use CPU instead of GPU
export CUDA_VISIBLE_DEVICES=""

# Or reduce batch size in code
# Modify run_instruction in backend/simplify.py
```

### Issue 7: Missing Dependencies

**Error:** `ModuleNotFoundError: No module named 'transformers'`

**Solution:**

```bash
# Reinstall requirements
pip install --upgrade -r requirements.txt

# Or install specific package
pip install transformers torch
```

### Issue 8: NVIDIA CUDA Issues

**Error:** `CUDA driver not compatible`

**Solution:**

```bash
# Check CUDA installation
nvcc --version

# Use CPU mode
export CUDA_VISIBLE_DEVICES=""

# Or install CPU version of torch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# Model Configuration
HF_HOME=./models
HF_DATASETS_CACHE=./data

# API Configuration
API_PORT=8000
API_HOST=0.0.0.0

# Frontend Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_HEADLESS=false

# Logging
LOG_LEVEL=INFO
```

### Memory Optimization

For systems with limited RAM:

```python
# In backend/simplify.py
import torch

# Set to use CPU only
torch.cuda.is_available = lambda: False

# Or use quantized model
from transformers import T5ForConditionalGeneration
model = T5ForConditionalGeneration.from_pretrained(
    'google/flan-t5-small',
    load_in_8bit=True
)
```

### Model Configuration

Change model size in `backend/simplify.py`:

```python
# Smaller model (faster, lower accuracy)
model_name = "google/flan-t5-small"

# Larger model (slower, higher accuracy)
model_name = "google/flan-t5-base"
```

---

## 🐳 Docker Setup (Optional)

### Build Docker Image

```dockerfile
# Dockerfile (in project root)
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 8501

CMD ["streamlit", "run", "frontend/streamlitapp.py"]
```

### Build and Run

```bash
# Build image
docker build -t learneasy:latest .

# Run container
docker run -p 8501:8501 -p 8000:8000 learneasy:latest

# With GPU support
docker run --gpus all -p 8501:8501 -p 8000:8000 learneasy:latest
```

---

## ✅ Verification Checklist

After setup, verify everything works:

```bash
# 1. Check Python
python --version

# 2. Check virtual environment
which python  # Should show venv path

# 3. Check imports
python -c "import streamlit, transformers, torch; print('✓')"

# 4. Test model loading (takes ~2 minutes on first run)
python -c "from backend.simplify import load_model; print('✓ Model loaded')"

# 5. Test Streamlit
streamlit run frontend/streamlitapp.py

# 6. Test FastAPI
uvicorn backend.main:app --reload
```

---

## 📊 Performance Tips

- **First Run:** Will take 2-3 minutes to download and load the model (normal)
- **Subsequent Runs:** Much faster as model is cached
- **GPU:** Dramatically speeds up text transformation (recommended)
- **CPU:** Works fine for small texts, slower for large documents
- **RAM:** Monitor usage, allocate 4GB+ for optimal performance

---

## 🔐 Security Notes

For production deployment:

1. **Update requirements.txt** to pin specific versions
2. **Use environment variables** for sensitive config
3. **Enable authentication** for API endpoints
4. **Use HTTPS** instead of HTTP
5. **Set up rate limiting**
6. **Run behind a reverse proxy** (nginx)

---

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Transformers Documentation](https://huggingface.co/docs)
- [PyTorch Installation Guide](https://pytorch.org/get-started/locally/)

---

## 🤝 Need Help?

1. Check the [Troubleshooting](#troubleshooting) section
2. Review [GitHub Issues](https://github.com/Chaiya8/ai-accessibility-tool/issues)
3. Ask in [GitHub Discussions](https://github.com/Chaiya8/ai-accessibility-tool/discussions)
4. Review [CONTRIBUTING.md](../CONTRIBUTING.md)

---

**Last Updated:** December 2024
