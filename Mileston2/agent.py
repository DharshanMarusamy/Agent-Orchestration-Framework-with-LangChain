from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
import os

from tools import (
    mock_weather_api,
    dictionary_lookup,
    currency_converter
)

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-lite-latest",
    temperature=0.2,
    api_key=api_key
)

tools = [
    Tool("weather_api", mock_weather_api, "Get weather information"),
    Tool("dictionary", dictionary_lookup, "Get meaning of a word"),
    Tool("currency_converter", currency_converter, "Convert currency")
]

prompt = PromptTemplate(
    input_variables=["input", "tools", "tool_names", "agent_scratchpad"],
    template="""
You are a helpful AI agent.

TOOLS:
{tools}
Tool names: {tool_names}

RULES:
- Weather → weather_api
- Word meaning → dictionary
- Currency → currency_converter
- NEVER create your own questions
- NEVER loop
- If a tool cannot answer, say so clearly

Question: {input}

Thought: what do I need?
Action: <tool name if needed>
Action Input: <input>
Observation: <tool result>
Final Answer: <answer>

{agent_scratchpad}
"""
)

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

def get_agent():
    return agent_executor
