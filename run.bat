@echo off

echo Cleaning up ports...

for /f "tokens=5" %%a in ('netstat -aon ^| find ":8000" ^| find "LISTENING"') do taskkill /f /pid %%a > nul 2>&1
for /f "tokens=5" %%a in ('netstat -aon ^| find ":8501" ^| find "LISTENING"') do taskkill /f /pid %%a > nul 2>&1

echo Starting FastAPI backend...
start "FastAPI Backend" cmd /k uvicorn main:app --reload --host 0.0.0.0 --port 8000

echo Waiting for backend to initialize...
timeout /t 5 > nul

echo Starting Streamlit frontend...
start "Streamlit Frontend" cmd /k streamlit run client\app.py --server.port 8501 --server.address 0.0.0.0

echo Opening app in browser...
start http://localhost:8501

echo All services started!
pause