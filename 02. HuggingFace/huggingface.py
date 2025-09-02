# from transformers import pipeline

# generator = pipeline("text-generation", model="crumb/nano-mistral")
# print(generator("Hugging Face is", max_new_tokens=20))


#Import the class for defining Hugging Face Pipelines
from langchain_huggingface import HuggingFacePipeline

#Define the LLm from the Hugging Face model ID
llm= HuggingFacePipeline.from_model_id(
    model_id="crumb/nano-mistral",
    task = "text-generation",
    pipeline_kwargs={"max_new_tokens": 20} 
)

prompt = "Hugging Face is"

#Invoke the model
response = llm.invoke(prompt)

print(response)
