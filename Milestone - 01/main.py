from agent import create_agent
from prompts import basic_prompt

def main():
    llm = create_agent()
    print("Gemini Agent Ready!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            
            formatted = basic_prompt.format(topic=user_input)
            response = llm.invoke(formatted)

            print("Agent:", response, "\n")
            print()
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
