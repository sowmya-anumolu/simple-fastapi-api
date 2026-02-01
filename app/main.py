from fastapi import FastAPI

app = FastAPI(
    title="Simple FastAPI API",
    description="A minimal FastAPI service",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
