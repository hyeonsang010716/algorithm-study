from pydantic import BaseModel
from typing import List

class InRequest(BaseModel):
    input: List


class OutResponse(BaseModel):
    answer: List
    
class OutProblemNumber(BaseModel):
    answer: str