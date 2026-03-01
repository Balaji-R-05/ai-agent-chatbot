# AI Agent Chatbot

A multi-model conversational AI chatbot built with **Streamlit, LangChain, LangGraph, and FastAPI**. This project allows users to chat with various LLMs (Groq, Gemini, etc.) and enable advanced tools like Web Search, Wikipedia, and a Python REPL.

<div align="center">
  <img src="./imgs/chatbot_ui.png" alt="Chat UI">
  <img src="./imgs/tool_tavily_demo.png" alt="Tavily Search">
  <img src="./imgs/tool_wikipedia_demo.png" alt="Wikipedia">
  <img src="./imgs/tool_python_demo.png" alt="Python REPL">
  <img src="./imgs/tool_list.png" alt="Sidebar Config">
</div>

## ✨ Features

| Feature | Description |
| :--- | :--- |
| **Multi-Model Support** | Native support for Groq LLaMA3, Google Gemini, and more. |
| **Advanced Tools** | Integrated Web Search (Tavily), Wikipedia, and Python REPL. |
| **Smart Orchestration** | Powered by **LangGraph** for robust tool-use decision logic. |
| **Optimized Performance** | History sliding window & recursion limits for cost/speed efficiency. |
| **Customization** | Easily tailor system prompts and add custom tools in `tools.py`. |


## 🛠️ Tech Stack

| Tool/Library | Purpose |
| :--- | :--- |
| **Python** | Core logic and agent framework. |
| **Streamlit** | Sleek, interactive frontend for the chat interface. |
| **FastAPI** | High-performance backend API for model orchestration. |
| **LangChain** | The backbone for LLM integration and chaining. |
| **LangGraph** | State-of-the-graph logic for complex agentic workflows. |


## >_  Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/Balaji-R-05/ai-agent-chatbot.git
cd ai-agent-chatbot
```

### 2. Environment Setup
```sh
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure API Keys
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key         # For Web Search
```

### 4. Run the Application
Start both services using the batch script:
```sh
.\run.bat
```

Alternatively, start the backend and frontend separately:
```sh
# Terminal 1: Backend
uvicorn main:app --port 8000

# Terminal 2: Frontend
streamlit run client/app.py
```

---
**API Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
