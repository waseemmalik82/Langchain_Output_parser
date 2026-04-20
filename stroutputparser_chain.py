from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

template1 = PromptTemplate(
    template= 'write a detail report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template= 'Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model

result = chain.invoke({'topic': 'blackhole'})
print(result)