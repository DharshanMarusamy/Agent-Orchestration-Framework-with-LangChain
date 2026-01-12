import json
from agent import get_agent

print("Milestone 2 – Tool Agent Ready!\n")

chain, tools = get_agent()
tool_map = {tool.name: tool for tool in tools}

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = chain.invoke({"input": user_input})

    if response.strip().startswith("{") and "tool" in response:
        try:
            tool_call = json.loads(response)
            tool_name = tool_call["tool"]
            tool_input = tool_call["input"]

            if tool_name in tool_map:
                tool_function = tool_map[tool_name]
                result = tool_function.invoke(tool_input)
                print(f"Agent: {result}")
            else:
                print(f"System Error: Tool '{tool_name}' not found.")
        
        except json.JSONDecodeError:
            print("System Error: Failed to parse agent tool call.")
    
    else:
        print(f"Agent: {response}")
    
    print("-" * 30)
