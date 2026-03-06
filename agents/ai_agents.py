from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage, FunctionMessage, ToolMessage
from agents.llm_provider import get_llm
from agents.tools import get_tools
import traceback
import logging
from app.config import MAX_HISTORY, RECURSION_LIMIT

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_response_from_ai_agent(llm_id, query, allow_search: bool, system_prompt, provider):
    try:
        logger.info(f"--- Agent Invocation Start ---")
        logger.info(f"Model: {llm_id}, Search Enabled: {allow_search}")

        llm = get_llm(provider, llm_id)
        tools = get_tools(allow_search)

        agent = create_react_agent(
            model=llm,
            tools=tools
        )

        messages = [SystemMessage(content=system_prompt)]
        
        if len(query) > MAX_HISTORY:
            logger.info(f"Trimming history from {len(query)} to {MAX_HISTORY}")
            trimmed_query = query[-MAX_HISTORY:]
        else:
            trimmed_query = query

        for msg in trimmed_query:
            if msg['role'] == 'user':
                messages.append(HumanMessage(content=msg['content']))
            elif msg['role'] == 'ai':
                messages.append(AIMessage(content=msg['content']))

        logger.info(f"Final messages count (including system): {len(messages)}")
        config = {"recursion_limit": RECURSION_LIMIT}
        response = agent.invoke({"messages": messages}, config=config)
        res_messages = response.get("messages", [])
        ai_response = "No response from AI."

        for msg in reversed(res_messages):
            if isinstance(msg, AIMessage) and msg.content:
                ai_response = msg.content
                break
        tool_names = []

        for msg in res_messages:
            if isinstance(msg, ToolMessage):
                tool_names.append(msg.name if msg.name else "Unknown Tool")
            elif isinstance(msg, FunctionMessage):
                tool_names.append(msg.name if msg.name else "Unknown Function")
        
        tool_names = list(set(tool_names))
        
        logger.info(f"Agent finished. Tools used: {tool_names}")
        logger.info(f"--- Agent Invocation End ---")

        return {
            "response": ai_response, 
            "tool_used": len(tool_names) > 0,
            "tool_names": tool_names
        }
    
    except Exception as e:
        logger.error(f"FATAL ERROR in get_response_from_ai_agent: {str(e)}")
        logger.error(traceback.format_exc())
        error_msg = str(e)
        if "Recursion limit" in error_msg:
            error_msg = f"The agent reached its step limit ({RECURSION_LIMIT}). Try a simpler query or increase RECURSION_LIMIT in .env."
        elif "rate limit" in error_msg.lower():
            error_msg = "Rate limit exceeded. Please wait a moment."
        elif "authentication" in error_msg.lower():
            error_msg = "API Key authentication failed."
        return {"response": f"Server Error: {error_msg}", "tool_used": False, "tool_names": []}