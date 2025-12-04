import requests
from langchain.tools import Tool

def greet(name: str):
    return f"Hello {name}, I am your Langchain Agent!"

def weather(city: str):
    url = f"https://wttr.in/{city}?format=j1"
    res = requests.get(url, timeout=10).json()
    temp = res["current_condition"][0]["temp_C"]
    return f"Current temperature in {city} is {temp}°C"

greet_tool = Tool(
    name="greeting_tool",
    func=greet,
    description="Use this tool to greet a person."
)

weather_tool = Tool(
    name="weather",
    func=weather,
    description="Get current temperature of a city."
)

tools = [greet_tool, weather_tool]
