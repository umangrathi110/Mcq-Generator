import os 
import json 
import traceback 
import pandas as pd 
from dotenv import load_dotenv
import streamlit as st
from src.mcq_generator.utils import read_file, get_mcq_data
from langchain.callbacks import get_openai_callback
from src.mcq_generator.MCQ_Generator import evaluation_chain
from src.mcq_generator.logger import logging 


# loading the json file 
with open ('/home/umang.rathi/Documents/mcq_generator/response.json', 'r') as file:
    data = file.read()
    RESPONSE_JSON = json.loads(data)

# creating title for the app 
st.title("MCQ Generator")

# Creating form
with st.form ("user_inputs"):
    # upload file 
    uploaded_file= st.file_uploader("Upload a pdf or txt file")

    # Input fields 
    mcq_count = st.number_input("Number of MCQs ", min_value=3, max_value= 50)
    
    # Subject
    subject= st.text_input("Enter Subject", max_chars=20)

    # Quiz Tone
    tone= st.selectbox("Difficulty Level", ["Simple", "Medium", "Hard"])

    # Adding Button 
    button = st.form_submit_button("Generate MCQs")

    # Checking if button is clicked and all fields have input 
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("generating..."):
            try:
                text = read_file(uploaded_file)
                # Counting tokens and Cost of API call
                with get_openai_callback() as cb:
                    response = evaluation_chain(
                        {
                            'text' : text,
                            'number' : mcq_count,
                            "subject" : subject,
                            'tone' : tone,
                            'response_json' : json.dumps(RESPONSE_JSON)
                        }
                    )
                # st.write(response)
            
            except Exception as e:
                traceback.print_exception(type(e), e,e.__traceback__)
                st.write("Error")
            else:
                print(f"Total Tokens : {cb.total_tokens}")
                print(f"Prompt Tokens : {cb.prompt_tokens}")
                print(f"Completion Tokens : {cb.completion_tokens}")
                print(f"Total Cost : {cb.total_cost}")


                # checks whether response is a instance of dictionary or not
                if isinstance(response, dict):
                    # extracting mcq data from the response
                    mcq = response.get('mcq', None)
                    if mcq is not None:
                        mcq_data = get_mcq_data(mcq)
                        if mcq_data is not None:
                            df = pd.DataFrame(mcq_data)
                            df.index = df.index+1
                            st.table(df)
                            # display the review in a text box
                            st.text_area(label = "Review", value = response['review'])
                        else:
                            st.write("Error in the mcq_data")
                
                else:
                    st.write(response)


            