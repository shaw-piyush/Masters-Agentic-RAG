from langchain_community.vectorstores import Chroma
from app.rag.embedder import get_embeddings
from app.utils.config import CHROMA_PERSIST_DIR
from langchain_core.tools import create_retriever_tool

# @tool
def get_retriever_tool() -> str:
    vectorstore = Chroma(
        persist_directory=CHROMA_PERSIST_DIR,
        embedding_function=get_embeddings()
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 1}
    )

    # def retrieve(query: str) -> str:
    #     docs = retriever.invoke(query)

    #     if not docs:
    #         return "No relevant documents found."

    #     results = []
    #     for i, doc in enumerate(docs):
    #         source = doc.metadata.get("source", "Unknown")
    #         results.append(f"[Source {i+1}: {source}]\n{doc.page_content}")

    #     return "\n\n".join(results)

    return create_retriever_tool(
        retriever,
        name="retrieve_docs",
        description=(
            "Use this to search through university guides, visa documents, "
            "SOP writing tips, and scholarship information. "
            "Input should be a natural language question."
        )
    )