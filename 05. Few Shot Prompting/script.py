import os
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv(find_dotenv())

#Create the examples list of dicts
examples = [
    {
        "question": "How many books has Alice read this year?",
        "answer": "12"
    },
    {
        "question": "What is Bob's favorite programming language?",
        "answer": "JavaScript"
    },
    {
        "question": "How many kilometers did Charlie run last week?",
        "answer": "42 km"
    },
    {
        "question": "Which movie did Dana watch most recently?",
        "answer": "Inception"
    },
    {
        "question": "What is Eve's current chess rating?",
        "answer": "1850"
    }
]


# Complete the prompt for formatting answers
example_prompt = PromptTemplate.from_template("Question: {question}\n{answer}")

# Create the few-shot Prompt
prompt_template = FewShotPromptTemplate(
    examples= examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"]
)

# prompt = prompt_template.invoke({"input": "How many books has Alice finished reading so far this year?"})
# print(prompt.text)

# Create an OpenAI chat LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

# Create and invoke the chain
llm_chain = prompt_template | llm
response = llm_chain.invoke({"input": "How many books has Alice finished reading so far this year?"})
print(response.content)
