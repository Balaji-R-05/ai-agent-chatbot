from dotenv import load_dotenv, find_dotenv
import os

dotenv_path: str = find_dotenv()

load_dotenv(dotenv_path, override=True)

GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY")
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")

MAX_HISTORY: int = int(os.getenv("MAX_HISTORY", 10))
RECURSION_LIMIT: int = int(os.getenv("RECURSION_LIMIT", 20))

GROQ_MODELS: list[str] = [
    "openai/gpt-oss-120b"
]

GOOGLE_MODELS: list[str] = [
    "gemini-2.5-flash"
]

# OPENAI_MODELS: list[str] = [
#     "gpt-4o"
# ]

ALLOWED_MODEL_NAMES: list[str] = GROQ_MODELS + GOOGLE_MODELS
# + OPENAI_MODELS