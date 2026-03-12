from langchain_community.document_loaders import PyMuPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from app.utils.config import CHROMA_PERSIST_DIR, CHUNK_OVERLAP, CHUNK_SIZE
from app.rag.embedder import get_embeddings

def ingest_docs(data_dir : str = "./data/raw"):

    loader = DirectoryLoader(data_dir, glob="**/*.pdf", loader_cls= PyMuPDFLoader)

    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = CHUNK_SIZE,
    chunk_overlap = CHUNK_OVERLAP
    )

    chunks = text_splitter.split_documents(docs)

    stores = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=CHROMA_PERSIST_DIR
    )

    print(f"Ingested {len(chunks)} chunks into ChromaDB")
    return stores

    