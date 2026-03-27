from app.tools.retriever_tool import get_retriever_tool

tool = get_retriever_tool()
result = tool.func("What are the admission requirements for MS CS?")
print(result)