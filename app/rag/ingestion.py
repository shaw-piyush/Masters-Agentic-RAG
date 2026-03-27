import os
from langchain_community.document_loaders import PyMuPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from app.utils.config import CHROMA_PERSIST_DIR, CHUNK_OVERLAP, CHUNK_SIZE
from app.rag.embedder import get_embeddings
import pymupdf
import chromadb

import pymupdf4llm

# def load_pdf_properly(data_dir: str = "./data/cleaned"):
#     # Extracts text, tables, and handles headers properly
#     md_text = pymupdf4llm.to_markdown(data_dir)
     
#     page_content=md_text,
#     metadata={"source": data_dir}

#     return page_content, metadata
    

def clean_data(data_dir : str = "./data/raw", op_dir : str = "./data/cleaned"):

    for filename in os.listdir(data_dir):
        if filename.lower().endswith('.pdf'):
            input_path = os.path.join(data_dir, filename)
            output_path = os.path.join(op_dir, f"repaired_{filename}")

            try:
                # PyMuPDF automatically attempts to repair structure on open
                doc = pymupdf.open(input_path)
                
                doc.save(output_path, garbage=3, deflate=True, clean=True)
                doc.close()
                
                print(f"Successfully repaired: {filename}")
                
            except Exception as e:
                print(f"Failed to repair {filename}: {e}")

# clean_data()


def ingest_docs(data_dir : str = "./data/raw"):

    loader = DirectoryLoader(data_dir, glob="**/*.pdf", loader_cls= PyMuPDFLoader)

    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = CHUNK_SIZE,
    chunk_overlap = CHUNK_OVERLAP
    )

    chunks = text_splitter.split_documents(docs)

    avg = sum(len(c.page_content) for c in chunks) / len(chunks)
    print(f"Total chunks: {len(chunks)} | Avg chunk size: {avg:.0f} chars")

    stores = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=CHROMA_PERSIST_DIR
    )

    print(f"Ingested {len(chunks)} chunks into ChromaDB")
    return stores

def show_collection():
    client = chromadb.PersistentClient(path="./stores")
    collection = client.get_collection("langchain")
    print(collection)
    
    results = collection.get(include=["documents", "metadatas"])
    
    for i, doc in enumerate(results["documents"]):         ## Show all the chunks
        print(f"\n--- Chunk {i+1} ---")
        print(f"Source: {results['metadatas'][i]}")
        print(f"Content: {doc[:200]}...")

    