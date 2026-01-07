# 🤖 Agent-Orchestration Framework with LangChain

<div align="center">

![LangChain](https://img.shields.io/badge/LangChain-🦜-blue)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-teal)
![Gemini](https://img.shields.io/badge/Google-Gemini-red)
![Status](https://img.shields.io/badge/Status-Active-success)

**An intelligent multi-agent orchestration system using LangChain + Google Gemini to automate research-based workflows.**

</div>

---

## 📌 Overview

The **Agent-Orchestration Framework** enables multiple AI agents to collaborate and automate complex workflows.

This project demonstrates:

- A full workflow: **Research → Summarize → Compose Email**
- AI agents communicating using shared + local memory
- LangChain-powered orchestration with modular architecture
- A backend-powered API and frontend UI (optional expansion)

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🧠 Multi-Agent System | Research, Summarization, and Email Composer agents |
| 🔧 Tool Support | Agents use LLM chains and prompt templates |
| 🔄 End-to-End Workflow | Automated processing pipeline |
| 💾 Memory System | Shared + per-agent memory management |
| 🌐 API Backend | FastAPI-based REST endpoints |
| 🖥️ Future Frontend Support | Ready for React/Next.js integration |
| 📝 Structured Output | Clean JSON outputs |

---

## 🏗️ Architecture

```
┌────────────────────────┐
│        Frontend        │
│     (React/Next.js)    │
└───────────┬────────────┘
            │  REST API
┌───────────▼────────────┐
│       FastAPI App       │
└───────────┬────────────┘
      ┌─────▼─────┬──────────────────────────────┐
      │           │                              │
┌─────▼────┐ ┌────▼─────┐ ┌───────────────────┐ ┌▼─────┐
│Researcher│ │Summarizer│ │ Email Composer    │ │Memory│
│  Agent   │ │  Agent    │ │    Agent          │ │Store │
└─────┬────┘ └────┬──────┘ └───────────────────┘ └──────┘
      │           │               │
      └───────────┴───────────────┘
               LangChain
```

---

## 🛠️ Tech Stack

### Backend
- Python 3.10+
- LangChain
- Google Gemini API
- FastAPI
- Uvicorn

### Frontend (Planned)
- React 18+
- Tailwind CSS
- Axios

---

## 📍 Milestones

### ✅ Milestone 1 — Environment Setup & Basic Agent
- Setup Python venv
- LangChain + Gemini integration
- Basic LLM chain
- Console-based agent chat
- Markdown → CLI formatter

---

### ✅ Milestone 2 — Tools & API Integration
- Added custom tools
- Implemented Tool abstraction
- Error-handling for tool execution
- Multi-step prompt chaining

---

### ✅ Milestone 3 — Multi-Agent System & Memory
- Research Agent
- Summarizer Agent
- Email Agent
- Shared memory class
- Inter-agent communication

---

### ✅ Milestone 4 — Orchestration + FastAPI
- Workflow orchestrator implemented
- Clean endpoint: `/run-workflow?topic=XYZ`
- JSON responses ready for UI integration

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DharshanMarusamy/Agent-Orchestration-Framework-with-LangChain
cd Agent-Orchestration-Framework-with-LangChain
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv/Scripts/activate  # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Your API Key

Create `.env` file:

```
GOOGLE_API_KEY=your_key_here
```

### 5️⃣ Run FastAPI Server

```bash
uvicorn AGENT_ORCHESTRATION.api:app --reload
```

---

## 📡 API Documentation

### ▶️ Run Workflow

**POST** `/run-workflow?topic=YOUR_TOPIC`

#### Response Example

```json
{
  "research": "Detailed research output...",
  "summary": "Condensed summary...",
  "email": "Formatted email composed using summary."
}
```

---

## 📁 Project Structure

```
AGENT_ORCHESTRATION/
├── agents/
│   ├── research_agent.py
│   ├── summarizer_agent.py
│   └── email_agent.py
├── memory/
│   └── sharedmemory.py
├── api.py
├── orchestrator.py
├── requirements.txt
└── README.md
```

---

## 💡 Usage Example

```python
from AGENT_ORCHESTRATION.orchestrator import WorkflowOrchestrator

bot = WorkflowOrchestrator()
result = bot.run("Future of AI in India")

print(result["email"])
```

---

## 🧪 Testing

```bash
pytest
```

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Dharshan Marusamy**

GitHub: https://github.com/DharshanMarusamy

---

<div align="center">

⭐ If this project helped you, please **star the repository**!

</div>
