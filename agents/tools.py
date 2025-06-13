from langchain_community.tools.tavily_search import TavilySearchResults

def get_tools(enable: bool):
    return [TavilySearchResults(max_results=3)] if enable else []


