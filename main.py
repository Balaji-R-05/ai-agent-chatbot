from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.route import router
import uvicorn
from datetime import datetime

app = FastAPI(
    title = "AI Agent Chatbot", 
    docs_url="/doc"
)

app.include_router(router)

@app.get("/")
def read_root():
    return RedirectResponse(url="/doc")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "AI Agent Chatbot is running",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)