@echo off
echo ========================================================
echo Starting Ministry of Steel: Maritime Procurement Command Center
echo ========================================================

set PYTHONIOENCODING=utf-8

echo Starting FastAPI Backend (Port 8001)...
start "FastAPI Backend" cmd /k "call .venv\Scripts\activate.bat && python freight.py"

timeout /t 3 /nobreak >nul

echo Starting Streamlit Dashboard (Port 8501)...
start "Streamlit Dashboard" cmd /k "call .venv\Scripts\activate.bat && streamlit run dashboard.py"

echo ========================================================
echo Command Center Online!
echo Frontend UI: http://localhost:8501
echo Backend API: http://127.0.0.1:8001
echo Swagger Docs: http://127.0.0.1:8001/docs
echo ========================================================
