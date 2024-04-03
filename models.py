from pydantic import BaseModel

class InputData(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str
