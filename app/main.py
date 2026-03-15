from fastapi import FastAPI
from .database import Base, engine
from . import auth, documents, rag_api

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Financial Document Management System with RAG"
)

app.include_router(auth.router)
app.include_router(documents.router)
app.include_router(rag_api.router)


@app.get("/")

def home():
    return {"message": "Financial Document Management API Running"}