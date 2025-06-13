from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage, FunctionMessage
from agents.llm_provider import get_llm
from agents.tools import get_tools

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    # Load the LLM and tools
    llm = get_llm(provider, llm_id)
    tools = get_tools(allow_search)

    # Create the ReAct agent with the specified model and tools
    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    # Prepare the initial conversation state
    state = {
        "messages": [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query[-1])
        ]
    }

    # Invoke the agent
    response = agent.invoke(state)

    # Extract messages from the response
    messages = response.get("messages", [])

    # Extract the last AI message content
    ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]
    ai_response = ai_messages[-1] if ai_messages else "No response from AI."

    # Check if a tool was used (i.e., if a FunctionMessage appears in the message list)
    tool_used = any(isinstance(msg, FunctionMessage) for msg in messages)

    # Return both the response and whether a tool was used
    return ai_response
