from langchain_tavily import TavilySearch
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_experimental.tools import PythonREPLTool
from langchain_core.tools import tool

@tool
def clear_chat_history() -> str:
    """Clear the entire chat history and start a fresh conversation."""
    return "Chat history cleared successfully. The next response will be from a clean state."

@tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia for technical terms, famous people, or general knowledge."""
    api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=1000)
    wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
    return wiki.run(query)

@tool
def tavily_search(query: str) -> str:
    """Search the web for current events, news, or real-time information."""
    search = TavilySearch(max_results=3)
    return search.run(query)




def get_tools(enable: bool):
    tools = []
    if enable:
        tools.append(tavily_search)
        tools.append(wikipedia_search)
        tools.append(PythonREPLTool())
        tools.append(clear_chat_history)
        
    return tools
