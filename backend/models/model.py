from pydantic import BaseModel
from typing import List 


class QuestionAnswer(BaseModel):
    questionID :str
    answer : str

class Metadata(BaseModel):
    type: str
    value: str

class Feedback(BaseModel):
    modelName : str
    imageKey : str
    qa : List[QuestionAnswer]

class Query(BaseModel):
    query : str
