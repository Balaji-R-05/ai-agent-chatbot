import traceback

with open("out.log", "w", encoding="utf-8") as f:
    f.write("Testing TavilySearch\n")
    try:
        from langchain_tavily import TavilySearch
        f.write(str(TavilySearch(max_results=3)) + "\n")
    except Exception as e:
        f.write(traceback.format_exc() + "\n")

    f.write("Testing TavilySearchResults\n")
    try:
        from langchain_tavily import TavilySearchResults
        f.write(str(TavilySearchResults(max_results=3)) + "\n")
    except Exception as e:
        f.write(traceback.format_exc() + "\n")

    f.write("Testing WikipediaAPIWrapper\n")
    try:
        from langchain_community.tools import WikipediaQueryRun
        from langchain_community.utilities import WikipediaAPIWrapper
        api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=512)
        f.write(str(WikipediaQueryRun(api_wrapper=api_wrapper)) + "\n")
    except Exception as e:
        f.write(traceback.format_exc() + "\n")
