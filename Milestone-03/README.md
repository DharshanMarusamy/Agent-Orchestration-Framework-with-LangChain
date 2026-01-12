# 🚀 Milestone 3 – Multi-Agent Orchestration & Memory Management
**LangChain + Gemini + Custom Shared Memory System**

## 📘 Overview
**Milestone 3** focuses on building a **Multi-Agent AI System** where two intelligent agents — a **Research Agent** and a **Summarizer Agent** — collaborate using an orchestrator and shared memory.

This project simulates real-world multi-agent workflows by enabling:
* Independent reasoning by each agent
* Shared knowledge storage
* Autonomous orchestration
* Memory-aware collaboration

---

## 🎯 Key Features

### ✅ Multi-Agent Architecture
* **Research Agent** → Generates detailed information.
* **Summarizer Agent** → Produces concise, structured summaries.

### ✅ Individual Memory
Each agent keeps its own interaction history using simple Python list buffers.

### ✅ Shared Memory
Implemented using **FAISS Vector Store + Fake Embeddings**:
* Stores cross-agent knowledge.
* Enables contextual handoff.
* Prevents information loss.

### ✅ Modular Design
Project structure organized for maintainability:

```text
/agents
    research_agent.py
    summarizer_agent.py
/memory
    sharedmemory.py
orchestrator.py
main.py
```

## 🔄 System Workflow

The following diagram illustrates the data flow between the agents and the shared memory system:

```text
      User Input Topic
             │
             ▼
  ┌────────────────────┐
  │   Research Agent   │
  │   (LLM + Memory)   │
  └──────────┬─────────┘
             │
             ▼
  ┌────────────────────┐
  │    Shared Memory   │
  │  (FAISS + Embeds)  │
  └──────────┬─────────┘
             │
             ▼
  ┌────────────────────┐
  │  Summarizer Agent  │
  │   (LLM + Memory)   │
  └──────────┬─────────┘
             │
             ▼
     Final Output JSON
```

## 📂 Project Structure

```text
.
├── agents/
│   ├── research_agent.py
│   └── summarizer_agent.py
├── memory/
│   └── sharedmemory.py
├── orchestrator.py
├── main.py
├── requirements.txt
└── README.md
```
## 🤖 Agent Details

### 🔍 Research Agent
* **File:** `agents/research_agent.py`
* **Responsibilities:**
    * Receives the user topic.
    * Checks its own local memory for past context.
    * Generates detailed research output.

In this milestone, it uses a custom `MockLLM` for simulation:

```python
class MockLLM:
    def __call__(self, inputs):
        return {"content": "AI is transforming..."}
```
### ✍️ Summarizer Agent
* **File:** `agents/summarizer_agent.py`
* **Responsibilities:**
    * Receives research output from the shared memory.
    * Uses local memory to maintain summary consistency across turns.
    * Returns a clean, structured summary string.
 
## 🔁 Multi-Agent Orchestrator
* **File:** `orchestrator.py`
* **Handles:**
  * Execution order of agents.
  * Memory passing between steps.
  * Coordination between the Research and Summarizer agents.

### Core Process
The orchestrator manages the flow by invoking chains sequentially:

```python
research_result = self.research_chain.invoke({...})
summary = self.summary_chain.invoke({...})
```

## 📦 Shared Memory System
* **File:** `memory/sharedmemory.py`

This module implements **FAISS + FakeEmbeddings** to simulate a shared memory vector store between agents.

```python
self.vector_store.add_texts([text])
```
### Why FakeEmbeddings?
* The **Gemini free tier** (and some lightweight models) does not provide direct embedding generation.
* However, **FAISS** (Facebook AI Similarity Search) requires vectors to function.
* Therefore, `FakeEmbeddings` are used to simulate the vectorization process for this milestone.

## ▶️ How to Run

### 1️⃣ Install dependencies
Run the following command to install the required Python packages:

```bash
pip install -r requirements.txt
```

### 2️⃣ Configure Environment
Create a `.env` file in the root directory and add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_gemini_api_key
```
### 3️⃣ Run the orchestrator
Execute the main script to start the multi-agent system:

```bash
python main.py
```

## 🧪 Example Output

```json
{
  "topic": "Impact of AI on Startup Ecosystem in India",
  "research": "AI is transforming the startup ecosystem...",
  "summary": "Artificial Intelligence accelerates startup growth..."
}
```
## 🚀 Future Enhancements
* **Replace MockLLM:** Switch to the real Gemini model for live inference.
* **Add More Agents:** Introduce Analyzer, Validator, and Planner agents.
* **Improve Shared Memory:** Upgrade to real embeddings (instead of FakeEmbeddings).
* **Async Orchestration:** Implement asynchronous processing for better performance.

---

## 📝 Conclusion
This milestone successfully demonstrates:

* [x] **Multi-Agent Collaboration**
* [x] **Custom Orchestration Logic**
* [x] **Shared + Individual Memory**
* [x] **Modular & Scalable Architecture**
