#OpenAI models in LanChain

import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI

#Load environment variables safely
load_dotenv(find_dotenv())

# Define the LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))


# Predict the words flowing the text in the question
prompt = "THree resons for using Langchain for LLM applicatin development"
respnse = llm.invoke(prompt)

print(respnse.content)
