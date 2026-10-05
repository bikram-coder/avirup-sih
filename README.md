# Ministry of Steel | Maritime Procurement Command Center

Smart India Hackathon (SIH) Project by Team Web Pixel.

## 🚢 Overview
An intelligent maritime procurement and freight optimization platform designed for the Ministry of Steel. The platform provides real-time route analytics, predictive freight cost modeling, multi-carrier procurement matching, and dynamic risk monitoring.

## 🛠️ Tech Stack
- **Backend:** FastAPI, Python, SQLite, Uvicorn
- **Frontend / Dashboard:** Streamlit, Plotly, Pandas, NumPy
- **Automation / Testing:** Playwright

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- Virtual Environment recommended

### 2. Setup
```bash
# Clone the repository
git clone https://github.com/bikram-coder/avirup-sih.git
cd avirup-sih

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run Application
Run both backend and frontend using the provided Windows script:
```cmd
run.bat
```
Or run services individually:

**FastAPI Backend:**
```bash
python freight.py
# Backend API: http://127.0.0.1:8001
# Swagger Docs: http://127.0.0.1:8001/docs
```

**Streamlit Dashboard:**
```bash
streamlit run dashboard.py
# UI Dashboard: http://localhost:8501
```
