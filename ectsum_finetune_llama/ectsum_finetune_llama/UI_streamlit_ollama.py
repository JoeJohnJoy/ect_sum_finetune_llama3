# create a streamlit app to host an ollama model

import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

llm = Ollama(model = 'ft-llama3-quant')

st.title('Earning Calls Text Summarization Tool using Fine tuned Llama 3 Model')

st.write('This is a simple extractive summarization tool that uses the Ollama model to summarize text. '
            'Simply paste your text in the box below and click the button to generate a summary.')

text = st.text_area('Enter text here:', height=200)

alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:
{input_text}

### Response:
"""
prompt = ChatPromptTemplate.from_messages([
    ("user", alpaca_prompt)
])

# create a new chain
chain = prompt | llm

if st.button('Summarize'):
    summary = chain.invoke({'instruction': "Please summarize the key points from the recent earnings call transcript. Focus on financial performance, strategic initiatives, and management's outlook.", 'input_text': text})
    st.write(summary)