from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.utils.config import GEMINI_API_KEY

def get_embeddings():
    return GoogleGenerativeAIEmbeddings(
        model = 'gemini-embedding-001',
        api_key = GEMINI_API_KEY
    )