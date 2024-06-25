from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


import streamlit as st

import os

from dotenv import load_dotenv


os.environ["OPENAI_API_KEY"]="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"
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]="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"

prompt =ChatPromptTemplate.from_messages(

    [
        ("system","You are a helpful assistant. Please response to the queries")
        ,("user","Question:{question}")
    ]
)


st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
