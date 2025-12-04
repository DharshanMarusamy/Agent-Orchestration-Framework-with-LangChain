from agent1 import create_agent

agent = create_agent()

print("Gemini Agent Ready!")
print("Type 'exit' to quit.\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    response = agent.invoke({"input": query})
    print("Agent:", response["output"])
