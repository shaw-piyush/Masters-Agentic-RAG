import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("MODEL")

CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./stores")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH", "./data/db/masters_knowledge.db")
