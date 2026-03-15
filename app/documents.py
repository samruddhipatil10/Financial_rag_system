from fastapi import APIRouter, UploadFile, File, Form
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models
import shutil
import os

router = APIRouter(prefix="/documents")

UPLOAD_FOLDER = "uploaded_docs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/upload")

def upload_document(
    title: str = Form(...),
    company_name: str = Form(...),
    document_type: str = Form(...),
    file: UploadFile = File(...)
):

    path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    db = SessionLocal()

    doc = models.Document(
        title=title,
        company_name=company_name,
        document_type=document_type,
        file_path=path
    )

    db.add(doc)
    db.commit()

    return {"message": "Document uploaded"}