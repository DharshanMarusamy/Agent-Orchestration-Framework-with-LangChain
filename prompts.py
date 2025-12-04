from langchain_core.prompts import PromptTemplate

basic_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain the topic: {topic} in a simple way."
)