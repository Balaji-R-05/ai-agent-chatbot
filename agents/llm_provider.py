from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY

def get_llm(provider, model):
    if provider == "Groq":
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found in environment or config.py")
        return ChatGroq(model=model, api_key=GROQ_API_KEY)
    
    else:
        raise ValueError(f"Unknown provider: {provider}")