import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.rag.ingestion import ingest_docs

if __name__ == "__main__":
    print("Starting document ingestion...")
    ingest_docs("./data/raw")
    print("Done!")