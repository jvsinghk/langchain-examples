# LangGraph ReAct Agents Examples

This folder contains examples of using **LangGraph's prebuilt ReAct agents** with LangChain.  
The **ReAct (Reason + Act)** framework allows an LLM to **reason through problems** and **use external tools** before responding.  

These examples show how to create lightweight agents for math computations and Wikipedia lookups.

### ⚙️ Setup Instructions

Install dependencies:
```bash
pip install -r requirements.txt
```

Create a .env file in this folder with your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

Run the examples:
```bash
python math_react_agent.py
python wikipedia_react_agent.py
```

## 📂 Agents

### 1. `math_react_agent.py`
A ReAct agent that uses the `llm-math` tool for solving mathematical queries.

Run:
```bash
python math_react_agent.py
```

Example output:
```bash
The square root of 101 is approximately 10.05.
```

### 2. wikipedia_react_agent.py

A ReAct agent that uses the wikipedia tool to search and summarize information from Wikipedia.

Run:
```bash
python wikipedia_react_agent.py
```

Example output:
```bash
As of the latest data from 2020, New York City has a population of over 8.3 million people. The city is noted for its high density, with about 26,403 people per square mile.
```

### 🛠 How It Works

ChatOpenAI → LLM backend (gpt-4o-mini in these examples)

load_tools → Loads external tools (llm-math, wikipedia)

create_react_agent → Wraps the LLM and tools into a ReAct agent

agent.invoke(...) → Sends messages to the agent and retrieves the reasoning & response

### ✅ Requirements

Python 3.9+

LangChain

LangGraph

OpenAI API key