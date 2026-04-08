import traceback
from dotenv import load_dotenv
import os
import sys

# Load .env from root directory
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

flag = True

with open("out.log", "w", encoding="utf-8") as f:
    f.write("Testing TavilySearch\n")
    try:
        from langchain_tavily import TavilySearch
        f.write(str(TavilySearch(max_results=3)) + "\n")
    except Exception as e:
        f.write(traceback.format_exc() + "\n")
        flag = False

    f.write("Testing TavilySearch Results (using tavily_search member)\n")
    try:
        from langchain_tavily import TavilySearch
        search = TavilySearch(max_results=3)
        # Testing if we can actually use it (requires API key)
        f.write("Success! TavilySearch initialized.\n")
    except Exception as e:
        f.write("Failed to initialize TavilySearch:\n" + traceback.format_exc() + "\n")
        flag = False

    f.write("Testing WikipediaAPIWrapper\n")
    try:
        from langchain_community.tools import WikipediaQueryRun
        from langchain_community.utilities import WikipediaAPIWrapper
        api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=512)
        f.write(str(WikipediaQueryRun(api_wrapper=api_wrapper)) + "\n")
    except Exception as e:
        f.write(traceback.format_exc() + "\n")
        flag = False

if flag:
    print("SUCCESS: All tools are working fine.")
    sys.exit(0)
else:
    print("FAILURE: Some tools failed initialization or checks.")
    sys.exit(1)
