from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

client = QdrantClient(":memory:")

COLLECTION = "financial_docs"

client.recreate_collection(
    collection_name=COLLECTION,
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)