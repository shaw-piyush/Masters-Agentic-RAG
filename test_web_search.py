import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.tools.web_search_tool import get_web_search_tool

# query = "What is the capital of India?"
tool = get_web_search_tool()
# result = tool.invoke(query)
result = tool.invoke("How many Ballon Dors does messi have?")
print(result)