from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.route import router
import uvicorn

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
        "status": "ok"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)