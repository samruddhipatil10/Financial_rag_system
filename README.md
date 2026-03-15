# 📄 Financial Document Management System with RAG

A **Retrieval-Augmented Generation (RAG) based document management system** built using **Python, FastAPI, LangChain, Sentence Transformers, and Qdrant**.

This project allows users to **upload financial documents, store metadata, index document content into a vector database, and perform semantic search** on the uploaded documents.

---

# 🚀 Features

✔ User Authentication (Register & Login)  
✔ Upload Financial Documents (PDF)  
✔ Document Metadata Storage using SQLite  
✔ Document Chunking using LangChain  
✔ Vector Embeddings using Sentence Transformers  
✔ Vector Storage using Qdrant  
✔ Semantic Search using Vector Similarity  

---

# 🧠 System Architecture

```
User Query
     │
     ▼
FastAPI API
     │
     ▼
Sentence Transformer (Embedding Model)
     │
     ▼
Qdrant Vector Database
     │
     ▼
Top Relevant Document Chunks
     │
     ▼
Returned as Semantic Search Results
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|-----------|--------|
| Python | Backend programming |
| FastAPI | API development |
| LangChain | Document processing |
| Sentence Transformers | Embedding generation |
| Qdrant | Vector database |
| SQLite | Metadata storage |
| Pydantic | Data validation |

---

# 📁 Project Structure

```
app
│
├── auth.py            # User authentication APIs
├── database.py        # Database connection
├── documents.py       # Document upload API
├── main.py            # FastAPI application entry
├── models.py          # SQLAlchemy models
├── rag.py             # Document indexing logic
├── rag_api.py         # RAG APIs (index + search)
├── roles.py           # Role-based access
├── schemas.py         # Pydantic schemas
└── vector_db.py       # Qdrant vector database setup
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/financial-rag-system.git
cd financial-rag-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶ Run the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open Swagger API documentation:

```
http://127.0.0.1:8000/docs
```

---

# 📂 Upload Document API

```
POST /documents/upload
```

Example Input:

| Field | Value |
|------|------|
title | Financial Report |
company_name | ABC Ltd |
document_type | report |
file | sample.pdf |

Example Response:

```json
{
  "message": "Document uploaded"
}
```

---

# 📊 Index Document into Vector Database

```
POST /rag/index-document
```

Query Parameter:

```
file_path=uploaded_docs/sample.pdf
```

Response:

```json
{
  "status": "success",
  "message": "Document indexed successfully"
}
```

---

# 🔎 Semantic Search

```
POST /rag/search
```

Example Query:

```
financial risk in company
```

Example Output:

```json
{
  "query": "financial risk in company",
  "results": [
    "The company experienced increased financial risk due to rising debt.",
    "Liquidity issues were observed in FY2023.",
    "Debt ratio increased significantly."
  ]
}
```

---

# 🧩 How RAG Works

1. User uploads financial documents  
2. Documents are converted into text  
3. Text is split into smaller chunks  
4. Embeddings are generated using Sentence Transformers  
5. Embeddings are stored in Qdrant vector database  
6. User query is converted into embeddings  
7. Vector similarity search retrieves relevant document chunks  

---

# 📌 Example Queries

You can test semantic search with the following queries:

```
financial risk in company
```

```
revenue growth of company
```

```
debt ratio analysis
```

```
liquidity issues in financial report
```

---

# 🧪 API Endpoints

| Method | Endpoint | Description |
|------|------|------|
POST | /auth/register | Register user |
POST | /auth/login | Login user |
POST | /documents/upload | Upload document |
POST | /rag/index-document | Index document |
POST | /rag/search | Semantic search |

---

# 📈 Future Improvements

✔ Add LLM response generation (complete RAG system)  
✔ Add document summarization  
✔ Add role-based access control  
✔ Store vectors permanently in Qdrant server  
✔ Add web UI for document search  

---

# 👩‍💻 Author

**Samruddhi Patil**

Data Science | AI/ML | Python | NLP

---

# ⭐ Support

If you like this project, please give it a ⭐ on GitHub.