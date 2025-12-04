from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor
from langchain.agents import create_react_agent

from tools import tools
from memory import memory

import os
from dotenv import load_dotenv

load_dotenv()

def create_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        api_key=os.getenv("GOOGLE_API_KEY")
    )

    # Load the default ReAct prompt template
    from langchain.agents.react import react_agent_prompt

    # Build the agent using LCEL
    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=react_agent_prompt
    )

    # Build the executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True
    )

    return agent_executor
