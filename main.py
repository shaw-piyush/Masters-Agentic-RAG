from langchain_google_genai import ChatGoogleGenerativeAI
from app.utils.config import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
print(llm.invoke("Can you write me a ballad about Shakespeare? Don't make it long").content)