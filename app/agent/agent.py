from langchain.agents import create_agent
from langchain_classic.agents import AgentExecutor
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.memory import ConversationBufferMemory
from langchain import hub

from app.utils.config import GEMINI_API_KEY
from app.agent.prompt import build_system_prompt
from app.tools.retriever_tool import get_retriever_tool
from app.tools.web_search_tool import get_web_search_tool

def build_agent(profile: dict):
    
    llm = ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash",
        google_api_key = GEMINI_API_KEY,
        verbose = True,
        temperature = 0.5
    )

    memory = ConversationBufferMemory(
        chat_memory = "BaseChatMessageHistory",
        return_messages = True,
        k = 10
    )

    tools = [
        get_retriever_tool(),
        get_web_search_tool()
    ]

    # base_prompt = hub.pull('')
    system_context = build_system_prompt(profile)

    agent = create_agent(llm, tools, system_context)

    return AgentExecutor(
        agent = agent,
        memory = memory,
        tools = tools,
        verbose = True,
        handle_parsing_errors = True
    )



