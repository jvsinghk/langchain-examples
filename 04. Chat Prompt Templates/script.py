import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv(find_dotenv())

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

#Create a chat prompt template
prompt_template = ChatPromptTemplate.from_messages(
    {
        ("system", "You are a geography expert that returns the colors present in a country's flag"),
        ("human", "Japan"),
        ("ai", "red, white"),
        ("human", "{country}")
    }
)

#Chain the prompt template and model, and invoke the chain
llm_chain = prompt_template | llm

country = "Canada"
response = llm_chain.invoke({"country": country})
print(response.content)
