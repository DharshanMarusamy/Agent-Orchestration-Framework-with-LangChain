from agents.research_agent import create_research_agent
from agents.summarizer_agent import create_summarizer_agent
from memory.sharedmemory import SharedMemory

class MultiAgentOrchestrator:
    def __init__(self):
        self.research_chain, self.research_memory = create_research_agent()
        self.summary_chain, self.summary_memory = create_summarizer_agent()
        self.shared_memory = SharedMemory()

    def run(self, topic: str):
        # ---- Research Agent ----
        history = "\n".join(self.research_memory)

        research_result = self.research_chain.invoke({
            "topic": topic,
            "history": history
        })["content"]

        self.research_memory.append(research_result)
        self.shared_memory.add(research_result)

        # ---- Summarizer Agent ----
        summary = self.summary_chain.invoke({
            "research_output": research_result,
            "history": "\n".join(self.summary_memory)
        })["content"]

        self.summary_memory.append(summary)
        self.shared_memory.add(summary)

        return {
            "topic": topic,
            "research": research_result,
            "summary": summary
        }
