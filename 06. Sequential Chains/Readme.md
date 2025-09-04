# 06 Sequential Chains

This folder demonstrates how to use **sequential chains in LangChain** with the **LangChain Expression Language (LCEL)**.  
Sequential chains allow you to connect multiple prompts and LLM calls together, where the output of one step becomes the input to the next.  

We build two practical examples:  
- **Learning Plan Generator** (`learn.py`)  
- **Travel Itinerary Planner** (`travel.py`)  


## 📦 Installation

Before running the scripts, make sure you have the required dependencies installed:

```bash
pip install langchain-core langchain-openai python-dotenv
```

You will also need an OpenAI API key. Create a .env file in the root of your project with:

```bash
OPENAI_API_KEY=your_api_key_here
```

## 📘 Example 1: Learning Plan Generator (learn.py)

This script creates a step-by-step learning plan for any activity and adapts it into a 1-week schedule.

Workflow:

Prompt 1 → Ask how to learn an activity step by step.

LLM → Generate a general learning approach.

Prompt 2 → Reframe the plan into a 1-week schedule.

LLM → Generate a detailed week-long plan.

Run:
```bash
python learn.py
```

Example Output:
```sql
Day 1: Learn the basics of AI Agent Development
Day 2: Study LangChain fundamentals
Day 3: Build your first simple AI agent
...

```

## 📘 Example 2: Travel Itinerary Planner (travel.py)

This script generates top activities for a destination and then builds a 1-day itinerary.

Workflow:

Prompt 1 → Ask for activities to do in a given destination.

LLM → Generate a list of activities.

Prompt 2 → Convert those activities into a 1-day itinerary.

LLM → Generate a final itinerary.

Run:
```bash
python travel.py
```

Example Output:
```bash
Morning: Visit the Colosseum
Afternoon: Explore the Roman Forum
Evening: Enjoy dinner in Trastevere
```


## 🔑 Key Concepts

PromptTemplate → Define structured prompts with input variables.

ChatOpenAI → Interface to OpenAI models.

StrOutputParser → Parse outputs into clean strings.

Sequential Chains with LCEL → Pipe outputs between multiple prompts and LLMs using |.

Example LCEL chain:

```python
seq_chain = ({"learning_plan": learning_prompt | llm | StrOutputParser()}
             | time_prompt
             | llm
             | StrOutputParser())
```

## 🚀 Next Steps

Extend these chains with conditionals or parallel chains.

Add memory to make the assistant recall past inputs.

Try different models (gpt-4, gpt-4o-mini, gpt-3.5-turbo).