from typing import List
from pydantic import BaseModel,Field,validator

class MCQQuestion(BaseModel):

    question: str = Field(description="The question text")

    options: List[str] = Field(description="List of 4 options")

    correct_answer: str = Field(description="The correct answer from the options")

    @validator('question' , pre=True)
    def clean_question(cls,v):
        if isinstance(v,dict):
            return v.get('description' , str(v))
        return str(v)
    

class FillBlankQuestion(BaseModel):

    question: str = Field(description="The question text with '___' for the blank")

    answer : str = Field(description="The correct word or phrase for the blank")

    @validator('question' , pre=True)  
    def clean_question(cls,v):  # To convert the questions like dict format to normal format
        if isinstance(v,dict):
            return v.get('description' , str(v))  # it will extract only the value from the dictionary ignoring the key
        return str(v)
    
    """
    eg: dictionary
    
    "question": "What is captial of india?"
    "question": "What is captial of France?"


    cleaned to get only 
    "What is captial of india?"
    "What is captial of France?"
    """