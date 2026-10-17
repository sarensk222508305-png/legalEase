from fastapi import FastAPI
from legalEaseAPI.routes import router

app = FastAPI(
    title="LegalEase - AI Legal Document Generator",
    version="1.0.0",
    description="FastAPI backend for the LegalEase academic project.",
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to LegalEase AI Legal Document Generator API",
        "status": "running",
        "docs": "/docs",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("legalEaseAPI.main:app", host="127.0.0.1", port=8000, reload=True)
