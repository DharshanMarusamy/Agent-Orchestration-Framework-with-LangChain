import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain_core.output_parsers import StrOutputParser
import os

# Assuming tools.py exists with your definitions
from tools import (
    mock_weather_api,
    dictionary_lookup,
    currency_converter
)

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=api_key,
    temperature=0.2
)

# --- TOOL DEFINITIONS ---
@tool
def weather_api(city: str) -> str:
    """Fetch weather for a city"""
    return mock_weather_api(city)

@tool
def dictionary(word: str) -> str:
    """Get meaning of a word"""
    return dictionary_lookup(word)

@tool
def currency(value: str) -> str:
    """Convert currency"""
    return currency_converter(value)

tools = [weather_api, dictionary, currency]


prompt = PromptTemplate(
    input_variables=["input"],
    template="""
You are an intelligent AI agent.

TOOLS AVAILABLE:
- weather_api: for weather conditions
- dictionary: for word definitions
- currency: for currency conversion (format: '100 USD to INR')

RULES:
1. If you can answer the user directly, do so.
2. If you need a tool, output ONLY a JSON object in this format:
   {{"tool": "tool_name", "input": "input_value"}}

User Input:
{input}
"""
)

def get_agent():
    chain = prompt | llm | StrOutputParser()
    return chain, tools
