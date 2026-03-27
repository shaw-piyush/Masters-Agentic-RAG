import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.tools.retriever_tool import get_retriever_tool

tool = get_retriever_tool()
result = tool.func("Give some tips to write an engaging SOP")
print(result)