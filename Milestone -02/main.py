from agent import get_agent

agent = get_agent()

print("\nLangChain Agent Ready")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    try:
        response = agent.invoke({"input": user_input})
        print("Agent:", response["output"], "\n")
    except Exception as e:
        print("Agent Error:", e, "\n")
