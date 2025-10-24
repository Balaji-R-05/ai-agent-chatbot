from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path, override=True)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

print(f"GROQ_API_KEY loaded: {GROQ_API_KEY}")
print(f"TAVILY_API_KEY loaded: {TAVILY_API_KEY}")