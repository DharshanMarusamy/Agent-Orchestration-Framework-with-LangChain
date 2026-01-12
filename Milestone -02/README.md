# 📘 Milestone-02: Tool-Based Reasoning Agent

## 🚀 Overview
**Milestone-02** focuses on expanding the basic conversational agent created in Milestone-01. In this phase, we enhance the system by adding tool-based reasoning, integrating multiple utility tools, and implementing a **ReAct-based agent**.

The goal is to build a smart agent that can decide **when** to use a tool, execute it, observe the result, and provide a final answer to the user.

---

## 🧠 Objectives Completed
- [x] Integrated tool-driven reasoning using **LangChain ReAct Agent**.
- [x] Created 3 custom tools (**Weather API, Dictionary Lookup, Currency Converter**).
- [x] Connected tools to the **Gemini LLM**.
- [x] Implemented agent decision-flow using a **ReAct prompt template**.
- [x] Added `Tool Call` → `Observation` → `Final Answer` logic.
- [x] Added command-line interaction for tool execution.
- [x] Handled invalid input, tool errors, and edge cases.
- [x] Verified agent produces accurate tool-based responses.

---

## 🛠 Features Implemented

### 🔹 ReAct Agent Architecture
Uses the **ReAct** (Reasoning + Acting) framework. The agent autonomously decides when to:
1. **Think** about the user request.
2. **Choose** the correct tool.
3. **Provide** the final answer based on observations.

### 🔹 Custom Tools
| Tool Name | Functionality |
| :--- | :--- |
| **Weather Tool** | Returns simulated conditions and temperature. |
| **Dictionary Tool** | Returns the meaning of common technical words. |
| **Currency Converter** | Converts values between USD and INR. |

### 🔹 Gemini LLM Integration
- **Library:** `ChatGoogleGenerativeAI`
- **Model:** `gemini-flash-lite-latest`
- **Temperature:** `0.2` (Set low for balanced, factual reasoning).

### 🔹 Improved PromptTemplate
- Defines strict rules for tool usage.
- Forces the agent to follow the ReAct format.
- Prevents infinite loops and unnecessary tool calls.

### 🔹 Console Chat System
- Accepts user input via CLI.
- Runs the agent with the defined tools.
- Displays the final AI answer cleanly.

---
## ⚙️ Installation & Setup

### 1️⃣ Install Dependencies
Ensure you have Python installed, then run the following commands:

```bash
pip install langchain==0.1.12
pip install langchain-core==0.1.30
pip install langchain-community==0.0.24
pip install python-dotenv
pip install langchain-google-genai
```

### 2️⃣ Configure Environment
Create a `.env` file in the root directory and add your Google API key:

```env
GOOGLE_API_KEY=your_actual_api_key_here
```

## ▶️ Usage
To start the agent, run the `main.py` file:

```bash
python main.py
```
### 🤖 Example Commands
Try typing requests such as:

* "What is the weather in Chennai?"
* "What is the meaning of computer?"
* "Convert 100 USD to INR"
  
## 🤖 Example Output (Terminal)
Here is how the agent processes a request using the ReAct pattern:

```text
User Input: weather in chennai

Agent Output:
Thought: I need weather details → use weather_api
Action: weather_api
Action Input: chennai
Observation: Weather in Chennai: Sunny, 32°C
Final Answer: The weather in Chennai is Sunny with 32°C.
```
## 🧩 Learning Outcomes
By completing **Milestone-02**, the system now supports:

* **Multi-step reasoning:** Breaking down complex queries.
* **Intelligent decision-making:** Choosing the right tool for the job.
* **Tool usage chaining:** Passing data between reasoning steps.
* **Real-time information retrieval:** Simulating API calls.
* **Structured ReAct pattern:** Standardizing LLM thought processes.

This creates a foundation for building more powerful AI agents with more tools, memory, and planning abilities.
