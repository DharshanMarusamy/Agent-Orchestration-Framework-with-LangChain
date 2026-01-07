# Milestone 3: Multi-Agent Orchestration & Memory Management  
### (Gemini + LangChain)

---

## 📌 Project Overview

This milestone implements a **multi-agent orchestration system** using **LangChain** and **Google Gemini**.

The project demonstrates how **multiple intelligent agents** can collaborate, maintain memory, and complete a task together through a centralized orchestration mechanism.

---

## 🎯 Objective

The system showcases:

- Collecting detailed information on a topic  
- Summarizing the collected information  
- Coordinating agent behavior using **individual memory** and **shared memory**

---

## 🤖 Agents Implemented

### 1️⃣ Research Agent
- Powered by **Google Gemini**
- Responsible for gathering detailed information, facts, and insights about a given topic
- Maintains its own short-term memory using `ConversationBufferMemory`

### 2️⃣ Summarizer Agent
- Powered by **Google Gemini**
- Converts research output into a concise and well-structured summary
- Maintains its own individual memory for contextual understanding

---

## 🧠 Memory Architecture

### 🔹 Individual Memory
- Each agent uses `ConversationBufferMemory`
- Allows agents to remember their own interaction history independently

### 🔹 Shared Memory
- Implemented using **FAISS Vector Store**
- Uses **FakeEmbeddings** (local embeddings) to simulate vector-based shared memory
- Enables agents to share context and information during execution

> **Note:**  
> `FakeEmbeddings` are used because the Gemini free tier does not provide embedding quotas.  
> This approach is suitable for **prototyping and academic evaluation**.

---

## 🔁 Orchestration Flow

User Topic
↓
Research Agent (Gemini)
↓
Shared Memory (FAISS + FakeEmbeddings)
↓
Summarizer Agent (Gemini)
↓
Final Summary



A **central orchestrator** controls the execution order and manages communication between agents.

---

## 🛠️ Tools & Technologies Used

- Python  
- LangChain  
- Google Gemini (`ChatGoogleGenerativeAI`)  
- FAISS Vector Store  
- FakeEmbeddings (for shared memory simulation)  
- python-dotenv (for API key management)

---

## ▶️ How to Run

1. Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
