# 🤖 AI Agents – Multi-Agent System (Google ADK | Gemini API)

This repository contains my complete 5-day journey of building AI Agents using  
**Google ADK (Agent Development Kit)** + **Gemini 2.5 Flash Lite API**, including:

- Single LLM agents  
- Tool-using agents  
- Search-enabled agents  
- Multi-agent orchestration  
- Agent-to-Agent (A2A) communication  
- Remote agent servers  
- CLI Chatbot using A2A  
- Hands-on code from every day

---

## 📁 Project Structure

ai_agents/
│
├── day5/
│ ├── product_catalog_agent.py
│ └── customer_support_agent.py
│
├── research_agent/
│ ├── agent.py
│ └── run_day4_agent.py
│
├── simple_agent.py
├── adk_demo.py
└── run_day4_agent.py


---

## 🚀 Tech Stack

- **Google ADK (Agent Development Kit)**
- **Gemini 2.5 Flash Lite**
- **Python 3.13**
- **uvicorn + FastAPI (A2A server)**
- **GitHub (version control)**

---

# 🧩 Day-wise Breakdown

## **Day 1 – Basic Agent**
✔ Introduction to ADK  
✔ Create a simple LLM agent  
✔ Run agent in CLI

Run:
```bash
python simple_agent.py

Day 2 – Tool Calling

✔ Add Python functions as agent tools
✔ Agents that run logic + LLM reasoning

Day 3 – Sessions & Memory

✔ Create persistent sessions
✔ Enable conversational memory
✔ Create a runner

Day 4 – Sub-Agents & Advanced Tools

✔ Build Research Agent
✔ Integrate Google Search Tool
✔ Count papers using custom tool
✔ Multi-step toolchain execution

Run:

python run_day4_agent.py

Day 5 – A2A Communication (Major Project)

✔ Build remote Product Catalog Agent
✔ Expose via A2A protocol
✔ Start A2A uvicorn server
✔ Build Customer Support Agent using RemoteA2aAgent
✔ Fully working multi-agent system

Start A2A server:

uvicorn product_catalog_agent:app --host localhost --port 8001


Run customer support agent:

python customer_support_agent.py

🖥️ CLI Chatbot

Ask:

User: Tell me about the iPhone 15 Pro


Agent responds using:

Gemini LLM

A2A Remote Product Catalog Agent

Tool functions
