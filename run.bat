@echo off
REM Start FastAPI backend
start "FastAPI" cmd /k uvicorn main:app --reload --port 8000

REM Wait a moment to ensure backend starts
timeout /t 3

REM Start Streamlit client
start "Streamlit" cmd /k streamlit run client\app.py

REM Optional: Keep the batch window open
pause