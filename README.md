# 🧠 AI-Essentials — The Ultimate AI Learning Directory

A community-driven repository helping anyone learn Artificial Intelligence — with **runnable examples**, **concise explanations**, and **visual guides** for foundational to modern AI topics.

## ⭐ Why This Repo Exists

- 💻 **Practical Examples** - All code runs out-of-the-box  
- 📊 **Visual Learning** - Mermaid diagrams and clear explanations  
- ⚡ **Quick Start** - "AI in 5 Minutes" summaries for every topic  
- 🎯 **Comprehensive** - From ML fundamentals to cutting-edge techniques  
- 🔗 **Curated Resources** - Best tutorials, docs, and learning paths  

![Stars](https://img.shields.io/github/stars/6NineLives/AI-Essentials?style=flat) ![License](https://img.shields.io/badge/license-MIT-green) ![Python](https://img.shields.io/badge/python-3.10+-blue) ![Node](https://img.shields.io/badge/node-18+-orange)

⭐ **Star this repo** to follow updates and contribute!

---

## 🚀 Quick Start

### 1. Clone and Install

```bash
# Clone the repository
git clone https://github.com/6NineLives/AI-Essentials.git
cd AI-Essentials

# Python setup
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\activate
pip install -r requirements.txt

# Node.js setup
npm install
```

### 2. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env and add your API keys
# OPENAI_API_KEY=your_key_here
# PINECONE_API_KEY=your_key_here (optional)
```

### 3. Run Examples

```bash
# Foundations
python 01_Foundations/linear_regression.py
python 01_Foundations/perceptron_example.py

# LLMs
python 02_LLMs/openai_example.py
python 02_LLMs/transformers_example.py
jupyter notebook 02_LLMs/llm_basics.ipynb

# RAG
python 03_RAG/rag_pipeline.py
python 03_RAG/vectorstore_setup.py

# MCP
python 04_MCP/mcp_server_example.py
node 04_MCP/client_example.js

# Agents
python 05_Agents/openai_agent.py
python 05_Agents/crewai_agent_example.py

# Vector Databases
python 06_Vector_Databases/chromadb_example.py
python 06_Vector_Databases/pinecone_example.py

# Prompt Engineering
python 07_Prompt_Engineering/examples/system_prompt_tuning.py
```

---

## 📂 Repository Structure

```
AI-Essentials/
├── 01_Foundations/          # ML fundamentals
│   ├── README.md            # Linear regression & perceptron concepts
│   ├── linear_regression.py # Working example with visualization
│   ├── perceptron_example.py # Neural network basics
│   └── resources.md         # Curated learning materials
│
├── 02_LLMs/                 # Large Language Models
│   ├── README.md            # LLM concepts and architecture
│   ├── openai_example.py    # OpenAI API usage
│   ├── transformers_example.py # Hugging Face transformers
│   ├── llm_basics.ipynb     # Interactive Jupyter notebook
│   └── ai_in_5_minutes.md   # Quick LLM overview
│
├── 03_RAG/                  # Retrieval-Augmented Generation
│   ├── README.md            # RAG pipeline explanation
│   ├── rag_pipeline.py      # Complete RAG implementation
│   ├── vectorstore_setup.py # Vector database setup
│   └── ai_in_5_minutes.md   # Quick RAG overview
│
├── 04_MCP/                  # Model Context Protocol
│   ├── README.md            # MCP concepts and usage
│   ├── mcp_server_example.py # Python MCP server
│   ├── client_example.js    # JavaScript MCP client
│   └── ai_in_5_minutes.md   # Quick MCP overview
│
├── 05_Agents/               # AI Agents
│   ├── README.md            # Agent architecture
│   ├── openai_agent.py      # Function-calling agent
│   ├── crewai_agent_example.py # Multi-agent collaboration
│   └── ai_in_5_minutes.md   # Quick agents overview
│
├── 06_Vector_Databases/     # Vector storage and search
│   ├── README.md            # Vector DB concepts
│   ├── chromadb_example.py  # Local vector database
│   ├── pinecone_example.py  # Cloud vector database
│   └── ai_in_5_minutes.md   # Quick vector DB overview
│
└── 07_Prompt_Engineering/   # Prompt optimization
    ├── README.md            # Prompt engineering guide
    ├── examples/
    │   ├── system_prompt_tuning.py # System prompt examples
    │   └── few_shot_examples.md    # Few-shot learning
    └── ai_in_5_minutes.md   # Quick prompt engineering overview
```

---

## 📚 Learning Paths

### 🔰 Absolute Beginner Path
Perfect if you're new to AI and machine learning:

1. **[01_Foundations](./01_Foundations/)** - Start here! Learn ML basics
   - Linear Regression - Predict continuous values
   - Perceptron - First neural network
   - Resources - Curated beginner guides

2. **[02_LLMs](./02_LLMs/)** - Understand modern AI
   - What are LLMs and how they work
   - Run your first LLM example
   - Interactive Jupyter exploration

3. **[07_Prompt_Engineering](./07_Prompt_Engineering/)** - Get better results
   - Learn to communicate with AI
   - Master prompt techniques
   - Practical examples

### 🚀 Modern AI Stack Path
For developers wanting to build production AI applications:

1. **[02_LLMs](./02_LLMs/)** - Master language models
2. **[03_RAG](./03_RAG/)** - Add knowledge retrieval
3. **[06_Vector_Databases](./06_Vector_Databases/)** - Optimize storage
4. **[05_Agents](./05_Agents/)** - Build autonomous systems
5. **[04_MCP](./04_MCP/)** - Standardize integrations

### 🎯 Quick Professional Catch-Up
For experienced developers new to modern AI:

- Read all **"AI in 5 Minutes"** summaries (30 minutes total)
- Run one example from each folder (2-3 hours)
- Deep dive into topics relevant to your use case

---

## 🎓 Topics Covered

### [01_Foundations](./01_Foundations/) - Machine Learning Basics
Learn the fundamental building blocks of AI:
- **Linear Regression** - Predict values from data
- **Perceptron** - Simplest neural network
- **Core Concepts** - Features, training, predictions

**🔍 Use Cases**: Price prediction, trend analysis, classification

### [02_LLMs](./02_LLMs/) - Large Language Models
Master modern AI language understanding:
- **OpenAI API** - GPT-3.5, GPT-4 usage
- **Transformers** - Hugging Face models
- **Tokenization** - How LLMs process text
- **Function Calling** - Give LLMs capabilities

**🔍 Use Cases**: Chatbots, code generation, content creation

### [03_RAG](./03_RAG/) - Retrieval-Augmented Generation
Ground LLM responses in your own data:
- **RAG Pipeline** - End-to-end implementation
- **Document Chunking** - Optimal text splitting
- **Vector Search** - Semantic retrieval
- **Context Injection** - Enhance LLM prompts

**🔍 Use Cases**: Knowledge bases, Q&A systems, document search

### [04_MCP](./04_MCP/) - Model Context Protocol
Standardize AI-to-tool communication:
- **MCP Servers** - Expose data and functions
- **MCP Clients** - Connect applications
- **Protocol** - Standard integration pattern

**🔍 Use Cases**: Claude Desktop integration, tool access, data connectors

### [05_Agents](./05_Agents/) - AI Agents
Build autonomous AI systems:
- **ReAct Pattern** - Reasoning + Acting
- **Tool Usage** - API calls, database queries
- **Multi-Agent** - Collaborative AI teams
- **Planning** - Multi-step task execution

**🔍 Use Cases**: Customer support, research assistants, automation

### [06_Vector_Databases](./06_Vector_Databases/) - Semantic Search
Store and query embeddings efficiently:
- **ChromaDB** - Local, lightweight option
- **Pinecone** - Cloud, production-scale
- **Similarity Search** - Find related content
- **Metadata Filtering** - Hybrid search

**🔍 Use Cases**: Semantic search, recommendations, RAG systems

### [07_Prompt_Engineering](./07_Prompt_Engineering/) - Optimize AI Outputs
Get better results through better prompts:
- **System Prompts** - Set behavior and tone
- **Few-Shot Learning** - Teach by example
- **Chain-of-Thought** - Step-by-step reasoning
- **Output Formatting** - Control structure

**🔍 Use Cases**: All LLM applications benefit from good prompting

---

## 💡 "AI in 5 Minutes" Series

Quick, professional summaries for busy developers:

- 🤖 [LLMs in 5 Minutes](./02_LLMs/ai_in_5_minutes.md) - Language models explained
- 🔍 [RAG in 5 Minutes](./03_RAG/ai_in_5_minutes.md) - Retrieval-augmented generation
- 🔌 [MCP in 5 Minutes](./04_MCP/ai_in_5_minutes.md) - Model Context Protocol
- 🤖 [Agents in 5 Minutes](./05_Agents/ai_in_5_minutes.md) - Autonomous AI systems
- 🗄️ [Vector Databases in 5 Minutes](./06_Vector_Databases/ai_in_5_minutes.md) - Semantic search
- 📝 [Prompt Engineering in 5 Minutes](./07_Prompt_Engineering/ai_in_5_minutes.md) - Better prompts

**Total reading time**: ~30 minutes to understand the entire modern AI stack!

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

**Ways to contribute**:
- 🐛 Report bugs or issues
- ✨ Suggest new examples or topics
- 📝 Improve documentation
- 🔗 Add learning resources
- 💻 Submit code improvements

**Good first contributions**:
- Add examples in other languages (JavaScript, Go, etc.)
- Create additional "AI in 5 Minutes" guides
- Expand the resources.md files
- Add more visualization examples

---

## 🗺️ Roadmap

### Coming Soon
- [ ] Evaluation patterns (RAGAS, G-Eval)
- [ ] Fine-tuning guides
- [ ] Production deployment examples
- [ ] Multi-modal AI (images, audio)
- [ ] Agent safety and guardrails

### Community Requests
- LangChain/LlamaIndex variants
- More MCP server examples
- Dockerized quickstart
- Video tutorials
- Interactive web demos

**Have an idea?** [Open an issue](https://github.com/6NineLives/AI-Essentials/issues) to suggest it!

---

## 📖 Additional Resources

### Official Documentation
- [OpenAI Platform](https://platform.openai.com/docs)
- [Anthropic Claude](https://docs.anthropic.com/)
- [Hugging Face](https://huggingface.co/docs)
- [LangChain](https://python.langchain.com/)

### Community
- [r/MachineLearning](https://www.reddit.com/r/MachineLearning/)
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/)
- [Papers with Code](https://paperswithcode.com/)
- [Hugging Face Forums](https://discuss.huggingface.co/)

### Keep Learning
- [Fast.ai Course](https://course.fast.ai/)
- [DeepLearning.AI](https://www.deeplearning.ai/)
- [Machine Learning Mastery](https://machinelearningmastery.com/)

---

## ⚖️ License

MIT License - see [LICENSE](./LICENSE) file for details.

Feel free to use this code for learning, projects, or commercial applications.

---

## 🌟 Acknowledgments

Built with contributions from the AI community. Special thanks to:
- OpenAI for GPT models and API
- Anthropic for Claude and MCP
- Hugging Face for transformers
- All open-source AI tool creators

---

## 📬 Contact

- **Issues**: [GitHub Issues](https://github.com/6NineLives/AI-Essentials/issues)
- **Discussions**: [GitHub Discussions](https://github.com/6NineLives/AI-Essentials/discussions)

---

<div align="center">

**Made with ❤️ by the AI community**

If this repo helped you, give it a ⭐ and share it!

[⬆ Back to Top](#-ai-essentials--the-ultimate-ai-learning-directory)

</div>
