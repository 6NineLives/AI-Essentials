"""
ChromaDB Example
Demonstrates using ChromaDB for vector storage and similarity search.
"""

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

def initialize_chromadb():
    """Initialize ChromaDB client"""
    print("=" * 60)
    print("CHROMADB VECTOR DATABASE EXAMPLE")
    print("=" * 60)
    
    print("\n1. Initializing ChromaDB...")
    
    # Create client (in-memory for demo)
    client = chromadb.Client()
    
    print("   ✅ Client initialized (in-memory mode)")
    
    return client

def create_and_populate_collection(client):
    """Create a collection and add documents"""
    print("\n2. Creating collection...")
    
    # Delete if exists
    try:
        client.delete_collection("ai_documents")
    except:
        pass
    
    # Create collection
    collection = client.create_collection(
        name="ai_documents",
        metadata={"description": "AI-related documents"}
    )
    
    print("   ✅ Collection 'ai_documents' created")
    
    # Sample documents
    documents = [
        "Large Language Models are neural networks trained on vast amounts of text data.",
        "Vector databases store embeddings for fast similarity search.",
        "RAG combines retrieval with generation for better AI responses.",
        "Transformers use attention mechanisms to process sequences.",
        "Fine-tuning adapts pre-trained models to specific tasks.",
        "Prompt engineering improves AI outputs through better instructions.",
        "Embeddings convert text into numerical vector representations.",
        "Neural networks consist of layers of interconnected nodes.",
        "Machine learning algorithms learn patterns from data.",
        "Natural language processing helps computers understand human language.",
    ]
    
    # Metadata for each document
    metadatas = [
        {"topic": "llm", "category": "ai", "difficulty": "advanced"},
        {"topic": "vector-db", "category": "infrastructure", "difficulty": "intermediate"},
        {"topic": "rag", "category": "ai", "difficulty": "advanced"},
        {"topic": "transformers", "category": "ai", "difficulty": "advanced"},
        {"topic": "fine-tuning", "category": "ai", "difficulty": "advanced"},
        {"topic": "prompts", "category": "ai", "difficulty": "beginner"},
        {"topic": "embeddings", "category": "ai", "difficulty": "intermediate"},
        {"topic": "neural-nets", "category": "ai", "difficulty": "intermediate"},
        {"topic": "ml", "category": "ai", "difficulty": "beginner"},
        {"topic": "nlp", "category": "ai", "difficulty": "intermediate"},
    ]
    
    # IDs for documents
    ids = [f"doc_{i}" for i in range(len(documents))]
    
    # Add to collection
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    
    print(f"   ✅ Added {len(documents)} documents")
    
    return collection

def similarity_search_examples(collection):
    """Demonstrate various similarity searches"""
    print("\n3. Similarity Search Examples...")
    
    # Query 1: Basic search
    print("\n   Query 1: 'How do language models work?'")
    results = collection.query(
        query_texts=["How do language models work?"],
        n_results=3
    )
    
    print("   📄 Top 3 results:")
    for i, (doc, metadata, distance) in enumerate(zip(
        results['documents'][0],
        results['metadatas'][0],
        results['distances'][0]
    ), 1):
        print(f"      {i}. [{metadata['topic']}] {doc[:60]}...")
        print(f"         Distance: {distance:.4f}")
    
    # Query 2: With metadata filter
    print("\n   Query 2: 'AI technology' (beginner level only)")
    results = collection.query(
        query_texts=["AI technology"],
        n_results=3,
        where={"difficulty": "beginner"}
    )
    
    print("   📄 Beginner-level results:")
    for doc, metadata in zip(results['documents'][0], results['metadatas'][0]):
        print(f"      - [{metadata['topic']}] {doc[:60]}...")
    
    # Query 3: Multiple filters
    print("\n   Query 3: 'neural networks' (advanced AI topics)")
    results = collection.query(
        query_texts=["neural networks"],
        n_results=3,
        where={
            "category": "ai",
            "difficulty": "advanced"
        }
    )
    
    print("   📄 Advanced AI results:")
    for doc in results['documents'][0]:
        print(f"      - {doc[:60]}...")

def get_by_ids_example(collection):
    """Get specific documents by IDs"""
    print("\n4. Get Documents by ID...")
    
    results = collection.get(
        ids=["doc_0", "doc_1", "doc_2"]
    )
    
    print("   📄 Retrieved documents:")
    for id, doc, metadata in zip(
        results['ids'],
        results['documents'],
        results['metadatas']
    ):
        print(f"      {id}: [{metadata['topic']}] {doc[:50]}...")

def update_and_delete_examples(collection):
    """Demonstrate update and delete operations"""
    print("\n5. Update and Delete Operations...")
    
    # Update metadata
    collection.update(
        ids=["doc_0"],
        metadatas=[{"topic": "llm", "category": "ai", "difficulty": "expert"}]
    )
    print("   ✅ Updated doc_0 difficulty to 'expert'")
    
    # Delete a document
    collection.delete(ids=["doc_9"])
    print("   ✅ Deleted doc_9")
    
    count = collection.count()
    print(f"   📊 Collection now has {count} documents")

def peek_and_count(collection):
    """Show collection stats"""
    print("\n6. Collection Statistics...")
    
    count = collection.count()
    print(f"   Total documents: {count}")
    
    # Peek at first few documents
    results = collection.peek(limit=3)
    print(f"   First 3 documents:")
    for id, doc in zip(results['ids'], results['documents']):
        print(f"      {id}: {doc[:50]}...")

def main():
    """Run all ChromaDB examples"""
    
    # Check if sentence-transformers is available
    try:
        # ChromaDB will use sentence-transformers if available
        _ = SentenceTransformer('all-MiniLM-L6-v2')
        print("\n✅ Using sentence-transformers for embeddings")
    except:
        print("\n⚠️  sentence-transformers not installed")
        print("   Install with: pip install sentence-transformers")
        print("   ChromaDB will use default embeddings")
    
    # Initialize
    client = initialize_chromadb()
    
    # Create and populate
    collection = create_and_populate_collection(client)
    
    # Search examples
    similarity_search_examples(collection)
    
    # Get by IDs
    get_by_ids_example(collection)
    
    # Update/delete
    update_and_delete_examples(collection)
    
    # Stats
    peek_and_count(collection)
    
    print("\n" + "=" * 60)
    print("✅ ChromaDB examples completed!")
    print("=" * 60)
    
    print("\n💡 Key Features Demonstrated:")
    print("   1. Collection creation and management")
    print("   2. Document insertion with metadata")
    print("   3. Similarity search")
    print("   4. Metadata filtering")
    print("   5. Update and delete operations")
    print("   6. Collection statistics")
    
    print("\n📚 ChromaDB Features:")
    print("   • In-memory or persistent storage")
    print("   • Automatic embedding generation")
    print("   • Metadata filtering")
    print("   • Simple Python API")
    print("   • Perfect for prototyping")
    
    print("\n🔗 For production:")
    print("   • Use persistent storage: PersistentClient(path='./db')")
    print("   • Consider hosted solutions for scale")
    print("   • Monitor memory usage")
    print("\n")

if __name__ == "__main__":
    main()
