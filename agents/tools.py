from langchain_tavily import TavilySearch
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_experimental.tools import PythonREPLTool

def get_tools(enable: bool):
    tools = []
    if enable:
        # Tavily Search Tool
        tools.append(TavilySearch(max_results=3))
        
        # Wikipedia Tool
        api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=512)
        tools.append(WikipediaQueryRun(api_wrapper=api_wrapper))
        
        # Python REPL Tool
        tools.append(PythonREPLTool())
        
    return tools
