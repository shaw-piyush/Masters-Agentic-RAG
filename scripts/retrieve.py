import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.rag.retriever import result

if __name__ == "__main__":
    print(result)

