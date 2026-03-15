from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from qdrant_client.http.models import PointStruct
from .vector_db import client, COLLECTION

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def index_document(file_path: str):

    # Load PDF
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    points = []

    for i, chunk in enumerate(chunks):

        text = chunk.page_content.strip()

        if not text:
            continue

        # Convert text → embedding
        vector = model.encode(text).tolist()

        points.append(
            PointStruct(
                id=i,
                vector=vector,
                payload={"text": text}
            )
        )

    # Store vectors in Qdrant
    client.upsert(
        collection_name=COLLECTION,
        points=points
    )

    return "Document indexed successfully"