from langchain_core.prompts import PromptTemplate

class MockLLM:
    def __call__(self, inputs):
        return {
            "content": (
                "Artificial Intelligence accelerates startup growth in India "
                "by improving efficiency, innovation, and scalability."
            )
        }

def create_summarizer_agent():
    llm = MockLLM()
    memory = []

    prompt = PromptTemplate(
        input_variables=["research_output", "history"],
        template="""
You are a Summarizer Agent.

Research Notes:
{research_output}

Previous summaries:
{history}

Return a concise, structured paragraph.
"""
    )

    return prompt | llm, memory
