from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path, override=True)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

MAX_HISTORY = int(os.getenv("MAX_HISTORY", 10))
RECURSION_LIMIT = int(os.getenv("RECURSION_LIMIT", 20))

ALLOWED_MODEL_NAMES = [
    "llama-3.3-70b-versatile",
    "openai/gpt-oss-120b"
]