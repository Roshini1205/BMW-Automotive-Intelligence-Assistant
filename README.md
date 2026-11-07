# BMW Automotive Intelligence Assistant

An AI-powered automotive platform combining a BMW virtual showroom and engineering knowledge assistant using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), LangGraph, and Model Context Protocol (MCP).

## Project Overview

BMW Automotive Intelligence Assistant is designed to provide intelligent assistance for BMW customers, automotive enthusiasts, and engineering professionals.

The platform combines two major modules:

### 1. BMW Virtual Showroom
- Explore BMW vehicle models.
- View vehicle specifications and features.
- Compare different BMW models.
- Get intelligent vehicle recommendations.
- Ask questions about BMW technology.

### 2. BMW Engineering Assistant
- Search automotive technical documentation.
- Answer maintenance-related questions.
- Explain vehicle components and technologies.
- Assist with diagnostic fault-code explanations.
- Retrieve relevant technical information with source citations.

## Supported BMW Models

Initial focus:
- BMW 3 Series
- BMW 5 Series
- BMW X5

Future expansion:
- BMW 1, 2, 4, 7 and 8 Series
- BMW X Series
- BMW Z4
- BMW i Series

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| LangChain | RAG components |
| LangGraph | Multi-agent orchestration |
| ChromaDB | Vector database |
| Sentence Transformers | Text embeddings |
| LLM | AI answer generation |
| MCP | Tool integration |
| FastAPI | Backend API |
| React | Frontend |
| Git & GitHub | Version control |

## System Architecture

User Interface → FastAPI → LangGraph Supervisor → Specialized AI Agents → RAG / MCP Tools → Knowledge Databases → AI Response with Citations.

## Development Roadmap

- [x] PDF ingestion
- [x] Text chunking
- [x] Embedding generation
- [x] ChromaDB vector storage
- [x] Initial semantic search
- [ ] BMW document ingestion
- [ ] BMW RAG pipeline
- [ ] LLM integration
- [ ] LangGraph multi-agent system
- [ ] MCP server and tools
- [ ] FastAPI backend
- [ ] React virtual showroom
- [ ] Testing and deployment

## Project Setup

Clone the repository:

```bash
git clone https://github.com/Roshini1205/BMW-Automotive-Intelligence-Assistant.git
cd BMW-Automotive-Intelligence-Assistant
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies (once requirements.txt is prepared):

```bash
pip install -r requirements.txt
```

Run the backend:

```bash
python -m backend.app.main
```

## Project Status

Currently under active development. The initial PDF ingestion, chunking, embedding generation, ChromaDB storage, and semantic retrieval stages have been implemented and tested using an automotive owner manual.

## Author

**Sai Lakshmi Roshini Bandaru**

GitHub: https://github.com/Roshini1205

LinkedIn: https://www.linkedin.com/in/RoshiniBandaru/
