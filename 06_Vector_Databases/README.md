# 🗄️ Vector Databases

## Overview

Vector databases are specialized systems designed to store and query high-dimensional vectors efficiently. They're essential for AI applications that need semantic search, similarity matching, and retrieval-augmented generation (RAG).

### Topics Covered

1. **Vector Database Basics** - How they work
2. **ChromaDB** - Local, lightweight option
3. **Pinecone** - Cloud-native, scalable solution

## 📊 Concept Diagram

```mermaid
graph LR
    A[Text: "AI is amazing"] --> B[Embedding Model]
    B --> C[Vector: [0.2, 0.8, ...]]
    C --> D[Vector Database]
    
    E[Query: "artificial intelligence"] --> F[Embedding Model]
    F --> G[Query Vector]
    G --> H[Similarity Search]
    D --> H
    H --> I[Top-K Results]
    
    style A fill:#e1f5ff
    style D fill:#ffe1e1
    style I fill:#e1ffe1
```

## What are Vector Databases?

**Traditional Database**:
```sql
SELECT * FROM documents WHERE title = 'AI Guide'
```
→ Exact match only

**Vector Database**:
```python
db.similarity_search("artificial intelligence guide", k=5)
```
→ Semantic similarity matching

### Why Vectors?

Text is converted to vectors (embeddings) that capture meaning:
```
"dog" → [0.2, 0.8, 0.1, -0.3, ...]
"puppy" → [0.25, 0.75, 0.15, -0.25, ...]  # Similar!
"car" → [-0.5, 0.1, 0.9, 0.4, ...]        # Different
```

Vector distance = semantic similarity

## 💻 Running the Examples

### ChromaDB Example
```bash
python 06_Vector_Databases/chromadb_example.py
```

Features:
- Local, persistent storage
- Collection management
- Metadata filtering
- Similarity search

### Pinecone Example
```bash
python 06_Vector_Databases/pinecone_example.py
```

Features:
- Cloud-hosted
- Scalable to billions of vectors
- Namespace isolation
- Production-ready

## 🎯 Use Cases

### Semantic Search
```python
# Traditional: Find documents with exact keywords
# Vector DB: Find documents with similar meaning

db.search("machine learning algorithms")
# Returns: "ML techniques", "AI models", "neural networks"
```

### Recommendation Systems
```python
# Find similar products, content, or users
similar_items = db.similarity_search(
    query_vector=user_preferences,
    k=10
)
```

### RAG Systems
```python
# Retrieve relevant context for LLM
context = db.similarity_search(user_question, k=3)
answer = llm.generate(question=user_question, context=context)
```

### Duplicate Detection
```python
# Find near-duplicate content
potential_duplicates = db.similarity_search(
    query_vector=document_embedding,
    threshold=0.95
)
```

### Anomaly Detection
```python
# Find outliers by distance from cluster
anomalies = db.search_dissimilar(normal_pattern, threshold=0.3)
```

## 🔑 Key Concepts

### 1. Embeddings
Convert data to vectors:
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
embedding = model.encode("Hello world")
# → [0.123, -0.456, 0.789, ...]  (384 dimensions)
```

### 2. Similarity Metrics

**Cosine Similarity** (most common):
```
similarity = dot(A, B) / (||A|| * ||B||)
Range: [-1, 1], higher = more similar
```

**Euclidean Distance**:
```
distance = sqrt(sum((A - B)²))
Range: [0, ∞], lower = more similar
```

**Dot Product**:
```
similarity = dot(A, B)
Range: [-∞, ∞], higher = more similar
```

### 3. Indexing Algorithms

**HNSW** (Hierarchical Navigable Small World):
- Fast approximate search
- Good balance of speed/accuracy
- Used by ChromaDB, Weaviate

**IVF** (Inverted File Index):
- Clusters vectors
- Fast for large datasets
- Used by FAISS

**LSH** (Locality Sensitive Hashing):
- Hash similar items to same buckets
- Very fast approximate search

### 4. Metadata Filtering

Combine vector search with filters:
```python
results = db.search(
    query_vector=embedding,
    filter={
        "category": "technology",
        "date": {"$gte": "2024-01-01"}
    },
    k=10
)
```

## 🚀 Choosing a Vector Database

| Database | Best For | Hosting | Scale | Cost |
|----------|----------|---------|-------|------|
| **ChromaDB** | Prototyping, local | Self-hosted | Small-Medium | Free |
| **Pinecone** | Production, scale | Cloud | Large | Paid |
| **Weaviate** | Open source | Self/Cloud | Medium-Large | Free/Paid |
| **Milvus** | Enterprises | Self-hosted | Large | Free |
| **Qdrant** | Performance | Self/Cloud | Medium-Large | Free/Paid |
| **FAISS** | Research | Library | Medium | Free |

### Decision Matrix

**Use ChromaDB if**:
- Prototyping or small projects
- Want local deployment
- Budget constrained
- < 1M vectors

**Use Pinecone if**:
- Production application
- Need high availability
- Want managed service
- > 1M vectors

**Use Weaviate if**:
- Want open source
- Need self-hosting control
- Complex metadata filtering

## 📈 Best Practices

### Chunking Strategy
```python
# ✅ Good: Semantic chunks
chunk_size = 500-1000 tokens
chunk_overlap = 100-200 tokens

# ❌ Bad: Too large or too small
chunk_size = 10  # Too granular
chunk_size = 10000  # Loses context
```

### Embedding Model Selection
```python
# General purpose
model = "text-embedding-ada-002"  # OpenAI
model = "all-MiniLM-L6-v2"  # Open source

# Domain-specific
model = "allenai/specter"  # Scientific papers
model = "sentence-transformers/all-mpnet-base-v2"  # High quality
```

### Metadata Design
```python
# ✅ Good: Structured metadata
metadata = {
    "source": "doc_123",
    "category": "technology",
    "date": "2024-01-15",
    "author": "john_doe"
}

# ❌ Bad: Unstructured
metadata = {
    "info": "Some document from 2024 about tech"
}
```

### Query Optimization
```python
# ✅ Use appropriate k value
results = db.search(query, k=5)  # Usually 3-10

# ✅ Add metadata filters
results = db.search(
    query,
    k=5,
    filter={"category": "AI"}  # Narrows search space
)

# ✅ Tune threshold
results = db.search(
    query,
    k=10,
    threshold=0.7  # Only return if similarity > 0.7
)
```

## 🔒 Security & Privacy

### Data Isolation
```python
# Use namespaces or separate collections
user1_collection = db.get_collection("user_123")
user2_collection = db.get_collection("user_456")
```

### Access Control
```python
# Implement authentication
if not user.has_permission(collection_id):
    raise PermissionError("Access denied")
```

### Encryption
- Encrypt vectors at rest
- Use TLS for transmission
- Consider private embeddings

## 📊 Performance Tuning

### Indexing
```python
# Build index for faster searches
collection.create_index(
    index_type="HNSW",
    parameters={
        "M": 16,  # Connections per node
        "efConstruction": 200  # Build quality
    }
)
```

### Query Settings
```python
# Trade-off: Speed vs Accuracy
results = collection.search(
    query,
    k=10,
    ef=50  # Higher = slower but more accurate
)
```

### Batch Operations
```python
# ✅ Batch inserts
collection.add_batch(
    documents=docs,
    embeddings=embeddings,
    batch_size=100
)

# ❌ One at a time
for doc, emb in zip(docs, embeddings):
    collection.add(doc, emb)  # Slow!
```

## 🔗 Integration Examples

### With LangChain
```python
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=OpenAIEmbeddings(),
    persist_directory="./db"
)

retriever = vectorstore.as_retriever(k=3)
```

### With LlamaIndex
```python
from llama_index import VectorStoreIndex
from llama_index.vector_stores import ChromaVectorStore

vector_store = ChromaVectorStore(chroma_collection=collection)
index = VectorStoreIndex.from_vector_store(vector_store)
```

## 🔗 Next Steps

After mastering vector databases:
1. Build [RAG systems](../03_RAG/README.md) with semantic retrieval
2. Create [AI Agents](../05_Agents/README.md) with knowledge access
3. Optimize with [Prompt Engineering](../07_Prompt_Engineering/README.md)

## 📚 See Also

- [ai_in_5_minutes.md](./ai_in_5_minutes.md) - Quick vector DB overview
- [ChromaDB Docs](https://docs.trychroma.com/)
- [Pinecone Docs](https://docs.pinecone.io/)
- [Vector DB Comparison](https://github.com/erikbern/ann-benchmarks)
