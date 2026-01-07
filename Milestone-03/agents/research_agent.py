from langchain_core.prompts import PromptTemplate

class MockLLM:
    def __call__(self, inputs):
        return {
            "content": (
                "AI is transforming the startup ecosystem in India by enabling "
                "automation, data-driven decision making, cost reduction, "
                "and faster innovation."
            )
        }

def create_research_agent():
    llm = MockLLM()
    memory = []

    prompt = PromptTemplate(
        input_variables=["topic", "history"],
        template="""
You are a Research Agent.

Previous discussion:
{history}

Topic:
{topic}

Provide a detailed explanation.
"""
    )

    return prompt | llm, memory
