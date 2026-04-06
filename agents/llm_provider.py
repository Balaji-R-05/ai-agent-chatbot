from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import GROQ_API_KEY
# from app.config import GEMINI_API_KEY

def get_llm(provider: str, model: str):
    if provider == "Groq":
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found in environment or config.py")
        return ChatGroq(model=model, api_key=GROQ_API_KEY)

    # if provider == "Google":
    #     if not GEMINI_API_KEY:
    #         raise ValueError("GEMINI_API_KEY not found in environment or config.py")
    #     return ChatGoogleGenerativeAI(model=model, api_key=GEMINI_API_KEY)

    # if provider == "OpenAI":
    #     if not OPENAI_API_KEY:
    #         raise ValueError("OPENAI_API_KEY not found in environment or config.py")
    #     return ChatOpenAI(model=model, api_key=OPENAI_API_KEY)
    
    else:
        raise ValueError(f"Unknown provider: {provider}")