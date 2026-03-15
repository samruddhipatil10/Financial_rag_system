from fastapi import APIRouter
from sentence_transformers import SentenceTransformer
from .rag import index_document
from .vector_db import client, COLLECTION

router = APIRouter(prefix="/rag", tags=["RAG"])

model = SentenceTransformer("all-MiniLM-L6-v2")


@router.post("/index-document")
def index_doc(file_path: str):

    result = index_document(file_path)

    return {
        "status": "success",
        "message": result
    }


@router.post("/search")
def search(query: str):

    # Convert query to embedding
    query_vector = model.encode(query).tolist()

    # Correct method for new Qdrant versions
    results = client.query_points(
        collection_name=COLLECTION,
        query=query_vector,
        limit=5
    )

    output = []

    for r in results.points:
        output.append(r.payload["text"])

    return {
        "query": query,
        "results": output
    }