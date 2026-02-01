from fastapi import FastAPI
from app.schemas import PredictionRequest, PredictionResponse

app = FastAPI(
    title="Simple FastAPI API",
    description="A minimal FastAPI service with a prediction endpoint",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    """
    Mock prediction endpoint.
    In real scenarios, this is where an ML model would be loaded and used.
    """
    prediction = request.feature_1 + request.feature_2
    return {"prediction": prediction}
