"""
Pinecone Example
Demonstrates using Pinecone cloud vector database.
Note: Requires Pinecone API key and may incur costs.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_pinecone_key():
    """Check if Pinecone API key is set"""
    api_key = os.getenv("PINECONE_API_KEY")
    if not api_key or api_key == "your_pinecone_api_key_here":
        return False
    return True

def simulate_pinecone_example():
    """
    Simulated Pinecone example (actual usage requires: pip install pinecone-client)
    """
    
    print("=" * 60)
    print("PINECONE VECTOR DATABASE EXAMPLE (SIMULATED)")
    print("=" * 60)
    
    print("\n📋 Pinecone is a cloud-hosted vector database")
    print("   Perfect for production applications at scale")
    
    # Show the actual code structure
    print("\n1. Initialization (Actual Code):")
    print("""
    import pinecone
    
    # Initialize Pinecone
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENVIRONMENT")
    )
    
    # Create index (if doesn't exist)
    index_name = "ai-documents"
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(
            name=index_name,
            dimension=1536,  # OpenAI embedding dimension
            metric="cosine"
        )
    
    # Connect to index
    index = pinecone.Index(index_name)
    """)
    
    print("\n2. Upserting Vectors (Actual Code):")
    print("""
    from openai import OpenAI
    
    client = OpenAI()
    
    documents = [
        "Large Language Models are powerful AI systems.",
        "Vector databases enable semantic search."
    ]
    
    # Generate embeddings
    embeddings = []
    for doc in documents:
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=doc
        )
        embeddings.append(response.data[0].embedding)
    
    # Upsert to Pinecone
    vectors = []
    for i, (doc, emb) in enumerate(zip(documents, embeddings)):
        vectors.append({
            "id": f"doc_{i}",
            "values": emb,
            "metadata": {"text": doc, "category": "ai"}
        })
    
    index.upsert(vectors=vectors)
    """)
    
    print("\n3. Querying (Actual Code):")
    print("""
    # Generate query embedding
    query = "What are language models?"
    query_embedding = client.embeddings.create(
        model="text-embedding-ada-002",
        input=query
    ).data[0].embedding
    
    # Query Pinecone
    results = index.query(
        vector=query_embedding,
        top_k=3,
        include_metadata=True,
        filter={"category": "ai"}
    )
    
    # Process results
    for match in results['matches']:
        print(f"Score: {match['score']:.4f}")
        print(f"Text: {match['metadata']['text']}")
    """)
    
    print("\n4. Advanced Features:")
    print("""
    # Namespace isolation
    index.upsert(vectors=vectors, namespace="user_123")
    results = index.query(
        vector=query_embedding,
        top_k=5,
        namespace="user_123"
    )
    
    # Batch operations
    index.upsert(vectors=large_batch, batch_size=100)
    
    # Delete vectors
    index.delete(ids=["doc_0", "doc_1"])
    
    # Get statistics
    stats = index.describe_index_stats()
    print(f"Total vectors: {stats['total_vector_count']}")
    """)

def show_pinecone_features():
    """Show Pinecone key features"""
    print("\n" + "=" * 60)
    print("PINECONE KEY FEATURES")
    print("=" * 60)
    
    print("\n✨ Cloud-Native")
    print("   • Fully managed service")
    print("   • No infrastructure management")
    print("   • Automatic scaling")
    
    print("\n⚡ High Performance")
    print("   • Sub-10ms query latency")
    print("   • Billions of vectors")
    print("   • Horizontal scaling")
    
    print("\n🔒 Production-Ready")
    print("   • 99.9% uptime SLA")
    print("   • Built-in security")
    print("   • Multi-region support")
    
    print("\n🛠️ Developer-Friendly")
    print("   • Simple API")
    print("   • Multiple language SDKs")
    print("   • Excellent documentation")

def compare_vector_databases():
    """Compare different vector database options"""
    print("\n" + "=" * 60)
    print("VECTOR DATABASE COMPARISON")
    print("=" * 60)
    
    comparison = """
    
    ┌──────────────┬──────────────┬──────────────┬──────────────┐
    │   Feature    │   ChromaDB   │   Pinecone   │   Weaviate   │
    ├──────────────┼──────────────┼──────────────┼──────────────┤
    │ Hosting      │ Self-hosted  │ Cloud        │ Both         │
    │ Scale        │ Small-Med    │ Large        │ Medium-Large │
    │ Setup        │ Very Easy    │ Easy         │ Moderate     │
    │ Cost         │ Free         │ $70+/month   │ Free/Paid    │
    │ Performance  │ Good         │ Excellent    │ Very Good    │
    │ Best For     │ Prototypes   │ Production   │ Flexibility  │
    └──────────────┴──────────────┴──────────────┴──────────────┘
    
    When to use each:
    
    ChromaDB:
      ✓ Quick prototyping
      ✓ Small to medium datasets (< 1M vectors)
      ✓ Local development
      ✓ Budget constraints
    
    Pinecone:
      ✓ Production applications
      ✓ Large scale (> 1M vectors)
      ✓ Need managed service
      ✓ High availability required
    
    Weaviate:
      ✓ Want open source
      ✓ Need self-hosting
      ✓ Complex filtering needs
      ✓ GraphQL interface
    """
    print(comparison)

def main():
    """Run Pinecone examples"""
    
    print("\n" + "=" * 60)
    print("PINECONE VECTOR DATABASE")
    print("=" * 60)
    
    if not check_pinecone_key():
        print("\n⚠️  PINECONE_API_KEY not set in .env file")
        print("   This example shows the code structure")
        print("   For actual usage:")
        print("   1. Sign up at: https://www.pinecone.io/")
        print("   2. Get API key from dashboard")
        print("   3. Add to .env: PINECONE_API_KEY=your_key")
        print("   4. Install: pip install pinecone-client")
    
    # Show simulated example
    simulate_pinecone_example()
    
    # Show features
    show_pinecone_features()
    
    # Compare databases
    compare_vector_databases()
    
    print("\n" + "=" * 60)
    print("✅ Pinecone overview completed!")
    print("=" * 60)
    
    print("\n💡 Key Takeaways:")
    print("   1. Pinecone is production-ready and scalable")
    print("   2. Simple API similar to other vector DBs")
    print("   3. Managed service eliminates ops overhead")
    print("   4. Great for large-scale applications")
    
    print("\n📚 Resources:")
    print("   • Pinecone Docs: https://docs.pinecone.io/")
    print("   • Free tier available for testing")
    print("   • Python SDK: pip install pinecone-client")
    print("\n")

if __name__ == "__main__":
    main()
