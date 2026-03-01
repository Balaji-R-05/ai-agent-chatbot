import streamlit as st
import requests

st.set_page_config(page_title="AI Agent Chatbot", layout="centered")

st.title("AI Agent Chatbot")
st.markdown("Chat with powerful LLMs like Groq LLaMA3, Gemini with optional tools!")

with st.sidebar:
    st.header("Agent Configuration")
    model_provider = st.selectbox("Model Provider", ["Groq"])
    model_name = st.selectbox(
        "Model Name",
        ["openai/gpt-oss-120b", "llama-3.3-70b-versatile"]
    )
    system_prompt = st.text_area(
        "System Prompt", 
        value="Act as an AI chatbot who is smart and friendly", 
        height=100
    )
    allow_search = st.checkbox("Enable Tools", value=False)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for role, msg in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("user"):
            st.markdown(msg)
    else:
        with st.chat_message("ai"):
            st.markdown(msg)

user_query = st.chat_input("Type your message...")

if user_query:
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.chat_history.append(("user", user_query))

    with st.chat_message("ai"):
        with st.spinner("Thinking..."):
            try:
                formatted_history = [
                    {"role": role, "content": msg} 
                    for role, msg in st.session_state.chat_history
                ]
                
                payload = {
                    "model_name": model_name,
                    "model_provider": model_provider,
                    "system_prompt": system_prompt,
                    "messages": formatted_history,
                    "allow_search": allow_search
                }
                
                res = requests.post("http://127.0.0.1:8000/chat", json=payload)
                res.raise_for_status()
                
                response_data = res.json()
                ai_response = response_data.get("response", "No response received.")
                
                if response_data.get("tool_used"):
                    tool_names = response_data.get("tool_names", [])
                    tool_map = {
                        "tavily_search_results_json": "Web Search",
                        "wikipedia": "Wikipedia",
                        "python_repl": "Python REPL"
                    }
                    readable_names = [tool_map.get(t, t) for t in tool_names]
                    if readable_names:
                        st.caption(f"🛠️ **Tools used:** {', '.join(readable_names)}")
                
                st.markdown(ai_response)
                st.session_state.chat_history.append(("ai", ai_response))
            except Exception as e:
                st.error(f"Error: {e}")