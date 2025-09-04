import os
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv(find_dotenv())

destination_prompt = PromptTemplate (
    input_variables = ["destination"],
    template = "I am planning a trip to {destination}. Can you suggest some activities to do there?"
)

activities_prompt = PromptTemplate (
    input_variables = [{"activities"}],
    template = "I only have one day, so can you create an itinerary from your top three activities: {activities}"
)

llm = ChatOpenAI(model = "gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

seq_chain = ({"activities": destination_prompt | llm | StrOutputParser()}
             | activities_prompt
             | llm 
             | StrOutputParser())

print(seq_chain.invoke({"destination": "Rome"}))
