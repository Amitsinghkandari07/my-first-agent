# 🤖 Local AI Agent with Tool Calling (Agentic Loop)

## 🎯 Project Overview
This project demonstrates a foundational AI Agent architecture running 100% locally. Unlike standard chatbots, this agent utilizes an **Agentic Loop** to execute external tools (like checking system time) when it lacks the context to answer a user's prompt.

## 🧠 Architecture & Key Concepts
- **Local LLM Execution:** Uses Ollama and Llama 3.2 for zero-cost, private inference.
- **System Prompting (Personas):** Implements role-based prompting to control tone and output format.
- **Tool Use / Function Calling:** Implements a custom "Agentic Loop" where the LLM outputs a trigger token (`[TIME_CHECK]`) to invoke a Python function, mimicking the ReAct (Reasoning + Acting) pattern used in enterprise agents.

## 🛠️ Tech Stack
- **Language:** Python 3.12
- **AI Engine:** Ollama (Llama 3.2)
- **IDE:** Cursor (AI-Assisted Development)

## 🚀 How to Run
1. Install [Ollama](https://ollama.com) and pull the model: `ollama pull llama3.2`
2. Install dependencies: `pip install ollama`
3. Run the agent: `python ask_ollama.py`

## 💡 Why This Matters for Business
Running AI locally eliminates API costs and ensures data privacy. Understanding how to bridge LLMs with external tools is the foundational skill required to build autonomous enterprise agents.
