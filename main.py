from fastapi import FastAPI
from app.route import router

app = FastAPI(title = "AI Agent Chatbot")
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)