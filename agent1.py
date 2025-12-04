from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate
from tools import tools
from memory import memory
import os
from dotenv import load_dotenv

load_dotenv()

def create_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0
    )

    # SIMPLE + PERFECT FOR GEMINI
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. Use tools when needed."),
        ("human", "{input}"),
        ("ai", "{agent_scratchpad}")
    ])

    agent = create_tool_calling_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True   # FIXES your second error
    )

    return agent_executor
