from langchain.tools import tool
from app.utils.config import TAVILY_API_KEY
# from langchain_tavily import TavilySearchResults
from langchain_tavily import TavilySearch

import getpass
import os

if not os.environ.get("TAVILY_API_KEY"):
    os.environ["TAVILY_API_KEY"] = getpass.getpass("Tavily API key:\n")

def get_web_search_tool():
    return TavilySearch(
        max_results=3,
        search_depth="basic",
        name="web_search",
        description=(
            "Use this for current information like recent admission changes, "
            "GRE waiver updates, visa rule changes, or any info that may have "
            "changed recently. Input should be a search query."
        )
    )


