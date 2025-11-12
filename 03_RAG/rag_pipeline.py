"""
RAG Pipeline Example
A complete retrieval-augmented generation system using LangChain and ChromaDB.
"""

import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.schema import Document

# Load environment variables
load_dotenv()

def check_api_key():
    """Check if OpenAI API key is set"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        print("⚠️  WARNING: OPENAI_API_KEY not set in .env file")
        print("   This example requires a valid OpenAI API key")
        return False
    return True

def create_sample_documents():
    """Create sample documents for demonstration"""
    documents = [
        Document(
            page_content="Python is a high-level, interpreted programming language known for its simplicity and readability. It's widely used in web development, data science, and artificial intelligence.",
            metadata={"source": "python_guide.txt", "topic": "programming"}
        ),
        Document(
            page_content="Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed. It uses algorithms to analyze data and make predictions.",
            metadata={"source": "ml_basics.txt", "topic": "ai"}
        ),
        Document(
            page_content="Large Language Models (LLMs) are neural networks trained on vast amounts of text data. They can understand context, generate human-like text, and perform various language tasks like translation and summarization.",
            metadata={"source": "llm_intro.txt", "topic": "ai"}
        ),
        Document(
            page_content="Vector databases store data as high-dimensional vectors, enabling fast similarity searches. They're essential for AI applications like semantic search, recommendation systems, and RAG pipelines.",
            metadata={"source": "vector_db.txt", "topic": "database"}
        ),
        Document(
            page_content="Retrieval-Augmented Generation (RAG) combines information retrieval with language model generation. It retrieves relevant documents from a knowledge base and uses them to provide context for LLM responses.",
            metadata={"source": "rag_explained.txt", "topic": "ai"}
        ),
    ]
    return documents

def setup_vectorstore(documents):
    """Create and populate vector store"""
    print("\n📊 Setting up vector store...")
    
    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )
    
    splits = text_splitter.split_documents(documents)
    print(f"   Split {len(documents)} documents into {len(splits)} chunks")
    
    # Create embeddings and vector store
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    
    print(f"   ✅ Vector store created with {vectorstore._collection.count()} vectors")
    
    return vectorstore

def test_similarity_search(vectorstore):
    """Test basic similarity search"""
    print("\n" + "=" * 60)
    print("TEST 1: SIMILARITY SEARCH")
    print("=" * 60)
    
    query = "What is machine learning?"
    print(f"\n🔍 Query: '{query}'")
    
    results = vectorstore.similarity_search(query, k=2)
    
    print(f"\n📄 Top {len(results)} relevant documents:")
    for i, doc in enumerate(results, 1):
        print(f"\n{i}. Source: {doc.metadata['source']}")
        print(f"   Topic: {doc.metadata['topic']}")
        print(f"   Content: {doc.page_content[:150]}...")

def test_qa_chain(vectorstore):
    """Test RAG with QA chain"""
    print("\n" + "=" * 60)
    print("TEST 2: RAG QUESTION ANSWERING")
    print("=" * 60)
    
    # Create QA chain
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )
    
    questions = [
        "What is RAG and how does it work?",
        "What programming language is good for AI?",
        "How do vector databases help with AI applications?"
    ]
    
    for question in questions:
        print(f"\n❓ Question: {question}")
        
        result = qa_chain({"query": question})
        
        print(f"🤖 Answer: {result['result']}")
        print(f"\n📚 Sources used:")
        for doc in result['source_documents']:
            print(f"   - {doc.metadata['source']} ({doc.metadata['topic']})")

def test_metadata_filtering(vectorstore):
    """Test filtering by metadata"""
    print("\n" + "=" * 60)
    print("TEST 3: METADATA FILTERING")
    print("=" * 60)
    
    query = "Tell me about AI"
    print(f"\n🔍 Query: '{query}'")
    print(f"🏷️  Filter: topic='ai'")
    
    results = vectorstore.similarity_search(
        query,
        k=3,
        filter={"topic": "ai"}
    )
    
    print(f"\n📄 Found {len(results)} AI-related documents:")
    for doc in results:
        print(f"   - {doc.metadata['source']}")

def main():
    """Run RAG pipeline examples"""
    print("\n" + "=" * 60)
    print("RAG PIPELINE EXAMPLE")
    print("=" * 60)
    
    # Check API key
    if not check_api_key():
        print("\n⚠️  Skipping examples - API key not configured")
        return
    
    # Create sample documents
    print("\n1. Creating sample documents...")
    documents = create_sample_documents()
    print(f"   Created {len(documents)} sample documents")
    
    # Setup vector store
    print("\n2. Building vector store...")
    vectorstore = setup_vectorstore(documents)
    
    # Run tests
    test_similarity_search(vectorstore)
    test_qa_chain(vectorstore)
    test_metadata_filtering(vectorstore)
    
    print("\n" + "=" * 60)
    print("✅ RAG Pipeline examples completed!")
    print("=" * 60)
    print("\n💡 Key Concepts Demonstrated:")
    print("   1. Document chunking and embedding")
    print("   2. Vector similarity search")
    print("   3. RAG-based question answering")
    print("   4. Metadata filtering")
    print("\n🗑️  Clean up: Remove ./chroma_db directory when done")
    print("\n")

if __name__ == "__main__":
    main()
