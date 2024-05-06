from langchain.prompts import PromptTemplate


# Few Shot Prompt
prompt_template = """
Text:{text}
You are an expert MCQ maker. Given the above text, it is you job to create a quiz of \
{number} multiple choice question for {subject} students in {tone} tone.
Make sure that the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to fromat your response like RESPONSE_JSON below and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}
"""

# prompt
mcq_generation_prompt=PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template= prompt_template
)


# second template for evaluating the quiz
prompt_template2="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.
You need to evaluate the complexity of the question and give a complete analysis of the quiz. only use at max 50 words for complexity. If the quiz is not as per the cognitive and analytical abilities of the students, \
update the quiz qestions which needs to be changed and change the tone such that it perfectly fits the student abilities.
Quiz_MCQs:
{mcq}

Check from an expert English Writer of the above quiz:
"""

# prompt
mcq_evaluation_prompt= PromptTemplate(
    input_variables=["subject", "mcq"],
    template = prompt_template2
)