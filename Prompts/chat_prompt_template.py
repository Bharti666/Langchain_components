# What is a Prompt or PromptTemplate?
#A prompt is the input text you send to the LLM (like ChatGPT or GPT-4) to get a response.

#A PromptTemplate is like a template or format where you leave some parts blank and fill them later dynamically.

#Advantages of using prompt templates:
# Resuable: You can use the same template for different inputs.
# Dynamic: You can change the input values without changing the template.
# Consistent: It helps maintain a consistent format for your prompts.
# Helpful while chaining different components together. 


from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI()

chat_template=ChatPromptTemplate([('system','you are a helpful {domain} expert'),
                                 ('human','explain  in simple terms,what is {topic}')])

prompt=chat_template.invoke({'domain':'medical','topic':'dialysis'})

print(prompt)

print(model.invoke(prompt).content)
