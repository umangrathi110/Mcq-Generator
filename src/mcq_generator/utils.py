# utility file -> helper file contains the helper functions 

import os 
import json 
import PyPDF2
import traceback


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdffileReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        except Exception as e:
            raise Exception ("reading the pdf file")
    
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        raise Exception ("Unsuported file format only pdf and text file supported.")
    
def get_mcq_data(mcq_str):
    try:
        # converting the mcq from string to dictionary 
        mcq_dict = json.loads(mcq_str)
        mcq_data = []

        # iterating over the mcq dictionary and extracting the required information 

        for key, value in mcq_dict.items():
            mcq = value['mcq']
            option = " | ".join(
                [
                    f"{option} -> {option_value}" for option, option_value in value['options'].items()
                ]
            )
            correct = value['correct']
            mcq_data.append({"MCQ" : mcq, "Choices" : option, "Correct" : correct}) 
        return mcq_data
    
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
    