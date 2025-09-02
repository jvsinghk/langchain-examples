import os
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

#Load environment variables safely
load_dotenv(find_dotenv())

# Create a rpromt from the template string
template = "You are an artificial intelligence assistant, answer the question. {question}"

prompt = PromptTemplate.from_template(
    template = template
)

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

#Create a chain to integrate the prompt template and LLm

llm_chain = prompt | llm

# Invoke the chain on the question

question = "How does Langchain make LLM application development easier?"

print(llm_chain.invoke({"question": question}))
