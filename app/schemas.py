from pydantic import BaseModel

class PredictionRequest(BaseModel):
    feature_1: float
    feature_2: float

class PredictionResponse(BaseModel):
    prediction: float
