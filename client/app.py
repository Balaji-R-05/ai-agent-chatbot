import streamlit as st
import requests

st.set_page_config(page_title="AI Agent Chatbot", layout="centered")

st.title("AI Agent Chatbot")
st.markdown("Chat with powerful LLMs like Groq LLaMA3, Gemini with optional tools!")

with st.sidebar:
    st.header("Agent Configuration")
    model_provider = st.selectbox("Model Provider", ["Groq"], key="model_provider_select") # Add "Google" if needed
    
    if model_provider == "Groq":
        model_options =  [
            "openai/gpt-oss-120b"
        ]
    # else:
    #     model_options = [
    #         "gemini-2.5-flash",
    #         "gemini-1.5-pro",
    #         "gemini-2.5-pro"
    #     ]
         
    model_name = st.selectbox("Model Name", model_options, key="model_name_select")
    system_prompt = st.text_area(
        "System Prompt", 
        value="Act as an AI chatbot who is smart and friendly", 
        height=100,
        key="system_prompt_input"
    )
    
    allow_tools = st.checkbox("Enable Tools", value=False, key="enable_tools_check")

    st.divider()

    if st.button("Clear Chat 🗑️", key="clear_chat_button"):
        st.session_state.chat_history = []
        st.rerun()

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
                    "allow_tools": allow_tools
                }
                
                import os
                backend_url = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
                res = requests.post(
                    url = f"{backend_url}/chat", 
                    json = payload
                )
                res.raise_for_status()
                
                response_data = res.json()
                ai_response = response_data.get("response", "No response received.")
                
                if response_data.get("tool_used"):
                    tool_names = response_data.get("tool_names", [])
                    tool_map = {
                        "tavily_search": "Web Search",
                        "wikipedia_search": "Wikipedia",
                        "python_repl": "Python REPL",
                        "clear_chat_history": "Clear History"
                    }
                    readable_names = [tool_map.get(t, t) for t in tool_names]
                    if readable_names:
                        st.caption(f"🛠️ **Tools used:** {', '.join(readable_names)}")
                
                st.markdown(ai_response)
                st.session_state.chat_history.append(("ai", ai_response))

                if response_data.get("clear_chat"):
                    st.session_state.chat_history = []
                    st.rerun()
            except requests.exceptions.RequestException as e:
                error_msg = f"Error: {e}"
                if hasattr(e, 'response') and e.response is not None:
                    error_msg += f" | Details: {e.response.text}"
                st.error(error_msg)
            except Exception as e:
                st.error(f"Unexpected Error: {e}")