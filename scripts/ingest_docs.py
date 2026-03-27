import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.rag.ingestion import ingest_docs, clean_data, show_collection

if __name__ == "__main__":
    print("Starting document ingestion...")
    # clean_data("./data/raw", "./data/cleaned")
    # ingest_docs("./data/cleaned")
    show_collection()
    print("Done!")