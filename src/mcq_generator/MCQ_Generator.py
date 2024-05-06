import os 
import json
import traceback
import pandas as pd 
from dotenv import load_dotenv
from src.mcq_generator.logger import logging
from src.mcq_generator.utils import read_file, get_mcq_data
from src.mcq_generator.prompt import *

# importing necessary langchain packages 
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


load_dotenv()

# extracting openai api key from the environment key 
key = os.getenv('OPENAI_API_KEY')
print(key)

llm = ChatOpenAI(openai_api_key = key, model_name= 'gpt-3.5-turbo', temperature=0.7)


mcq_chain = LLMChain(llm = llm, prompt = mcq_generation_prompt, output_key = "mcq", verbose= True)

review_chain = LLMChain(llm = llm , prompt= mcq_evaluation_prompt, output_key= 'review', verbose= True)

# by using the sequential chain we are connecting both the chains 
evaluation_chain= SequentialChain(chains=[mcq_chain, review_chain], input_variables=["text", "number", "subject", "tone","response_json"], output_variables=["mcq", "review"], verbose=True)





