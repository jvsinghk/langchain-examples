import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_community.agent_toolkits.load_tools import load_tools

load_dotenv(find_dotenv())

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
tools = load_tools(["wikipedia"], llm=llm)
agent = create_react_agent(llm, tools)

response = agent.invoke({"messages": [("human", "How many people live in New York City?")]})

print(response['messages'][-1].content)
