from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Deployment Successful!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }