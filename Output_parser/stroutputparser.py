from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate


load_dotenv()

model=ChatOpenAI()

#1st prompt--> detailed report

template1=PromptTemplate(template='write down a detailed report on the {topic}',
                         input_variables=['topic'])

#2nd prompt--> summary

template2=PromptTemplate(template='write a five line summary  on the following text. /n {text}',
input_variables=['text'])

parser=StrOutputParser()

chain=template1 | model | parser | template2 | model | parser

result=chain.invoke({'topic':'blackhole'})

print(result)