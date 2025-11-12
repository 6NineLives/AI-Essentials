"""
Vector Store Setup Example
Demonstrates setting up and configuring ChromaDB for document storage and retrieval.
"""

import os
import chromadb
from chromadb.config import Settings
from datetime import datetime

def initialize_chromadb(persist_dir="./chroma_data"):
    """Initialize ChromaDB with persistent storage"""
    print("=" * 60)
    print("CHROMADB VECTOR STORE SETUP")
    print("=" * 60)
    
    print(f"\n1. Initializing ChromaDB...")
    print(f"   Persist directory: {persist_dir}")
    
    # Create persistent client
    client = chromadb.PersistentClient(path=persist_dir)
    
    print(f"   ✅ ChromaDB initialized")
    
    return client

def create_collection(client, collection_name="documents"):
    """Create or get a collection"""
    print(f"\n2. Creating collection: '{collection_name}'")
    
    # Delete existing collection if it exists
    try:
        client.delete_collection(name=collection_name)
        print(f"   Deleted existing collection")
    except:
        pass
    
    # Create new collection
    collection = client.create_collection(
        name=collection_name,
        metadata={"description": "Sample document collection"}
    )
    
    print(f"   ✅ Collection created")
    
    return collection

def add_sample_documents(collection):
    """Add sample documents to the collection"""
    print(f"\n3. Adding sample documents...")
    
    documents = [
        "Python is a versatile programming language widely used in AI and machine learning.",
        "Vector databases enable fast similarity search for AI applications.",
        "Machine learning algorithms learn patterns from data to make predictions.",
        "Natural language processing helps computers understand human language.",
        "Deep learning uses neural networks with multiple layers.",
        "Transformers revolutionized NLP with attention mechanisms.",
        "RAG combines retrieval with generation for better AI responses.",
        "Embeddings represent text as numerical vectors.",
        "Fine-tuning adapts pre-trained models to specific tasks.",
        "Prompt engineering improves AI model outputs through better instructions."
    ]
    
    # Generate IDs and metadata
    ids = [f"doc_{i}" for i in range(len(documents))]
    metadatas = [
        {"topic": "programming", "category": "python"},
        {"topic": "database", "category": "ai-infrastructure"},
        {"topic": "ml-basics", "category": "algorithms"},
        {"topic": "nlp", "category": "ai"},
        {"topic": "deep-learning", "category": "ai"},
        {"topic": "transformers", "category": "ai"},
        {"topic": "rag", "category": "ai"},
        {"topic": "embeddings", "category": "ai"},
        {"topic": "fine-tuning", "category": "ai"},
        {"topic": "prompts", "category": "ai"},
    ]
    
    # Add to collection
    collection.add(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )
    
    print(f"   ✅ Added {len(documents)} documents")
    
    return len(documents)

def query_collection(collection):
    """Demonstrate various query patterns"""
    print(f"\n4. Querying the collection...")
    
    # Query 1: Basic similarity search
    print(f"\n   Query 1: Basic Similarity Search")
    query = "How do computers understand text?"
    results = collection.query(
        query_texts=[query],
        n_results=3
    )
    
    print(f"   🔍 Query: '{query}'")
    print(f"   📄 Top 3 results:")
    for i, (doc, metadata) in enumerate(zip(results['documents'][0], results['metadatas'][0]), 1):
        print(f"      {i}. [{metadata['topic']}] {doc[:60]}...")
    
    # Query 2: With metadata filtering
    print(f"\n   Query 2: With Metadata Filtering")
    query = "AI technologies"
    results = collection.query(
        query_texts=[query],
        n_results=3,
        where={"category": "ai"}
    )
    
    print(f"   🔍 Query: '{query}' (category='ai')")
    print(f"   📄 Results:")
    for doc in results['documents'][0]:
        print(f"      - {doc[:60]}...")
    
    # Query 3: Get by IDs
    print(f"\n   Query 3: Get Specific Documents")
    results = collection.get(
        ids=["doc_0", "doc_1", "doc_2"]
    )
    
    print(f"   📄 Retrieved documents by ID:")
    for id, doc in zip(results['ids'], results['documents']):
        print(f"      {id}: {doc[:50]}...")

def bulk_operations(collection):
    """Demonstrate bulk operations"""
    print(f"\n5. Bulk Operations...")
    
    # Add more documents in bulk
    bulk_docs = [
        "Convolutional neural networks excel at image processing.",
        "Recurrent neural networks handle sequential data.",
        "Attention mechanisms allow models to focus on relevant information.",
    ]
    
    bulk_ids = [f"bulk_{i}" for i in range(len(bulk_docs))]
    bulk_metadata = [{"topic": "cnn", "category": "deep-learning"},
                     {"topic": "rnn", "category": "deep-learning"},
                     {"topic": "attention", "category": "deep-learning"}]
    
    collection.add(
        documents=bulk_docs,
        ids=bulk_ids,
        metadatas=bulk_metadata
    )
    
    print(f"   ✅ Added {len(bulk_docs)} more documents in bulk")
    
    # Count total documents
    count = collection.count()
    print(f"   📊 Total documents in collection: {count}")

def collection_info(collection):
    """Display collection information"""
    print(f"\n6. Collection Information...")
    
    count = collection.count()
    print(f"   Name: {collection.name}")
    print(f"   Total documents: {count}")
    print(f"   Metadata: {collection.metadata}")

def main():
    """Run all vector store setup examples"""
    
    # Initialize
    client = initialize_chromadb()
    
    # Create collection
    collection = create_collection(client)
    
    # Add documents
    add_sample_documents(collection)
    
    # Query examples
    query_collection(collection)
    
    # Bulk operations
    bulk_operations(collection)
    
    # Show info
    collection_info(collection)
    
    print("\n" + "=" * 60)
    print("✅ Vector store setup completed!")
    print("=" * 60)
    print("\n💡 Key Features Demonstrated:")
    print("   1. Persistent storage configuration")
    print("   2. Collection creation and management")
    print("   3. Document ingestion with metadata")
    print("   4. Similarity search queries")
    print("   5. Metadata filtering")
    print("   6. Bulk operations")
    print("\n🗑️  Clean up: Remove ./chroma_data directory when done")
    print("\n")

if __name__ == "__main__":
    main()
