# rag-powered-question-answering-system
# RAG-Powered Document Q&A System

A Retrieval-Augmented Generation (RAG) application that enables users to interact with PDF documents using natural language questions. Instead of relying solely on an LLM's pre-trained knowledge, the system retrieves relevant information from uploaded documents and generates context-aware answers grounded in the source material.

## Overview

Large Language Models are powerful, but they can hallucinate and lack access to user-specific documents. This project addresses that problem by implementing a Retrieval-Augmented Generation (RAG) pipeline.

Users can upload a PDF document, ask questions about its contents, and receive answers generated from the most relevant sections of the document. The system uses semantic search to identify relevant content and Gemini to generate accurate responses.

## Features

* Upload and process PDF documents
* Extract text from PDFs
* Intelligent text chunking
* Generate semantic embeddings using Sentence Transformers
* Store and search embeddings using FAISS
* Retrieve the most relevant document chunks
* Generate context-aware answers using Gemini
* Display source pages for transparency
* Interactive Streamlit web interface

## System Architecture

```text
PDF Upload
    ↓
Text Extraction
    ↓
Document Chunking
    ↓
Embedding Generation
    ↓
FAISS Vector Database
    ↓
User Question
    ↓
Question Embedding
    ↓
Similarity Search
    ↓
Relevant Chunks Retrieved
    ↓
Gemini LLM
    ↓
Final Answer
```

## Tech Stack

| Component              | Technology                 |
| ---------------------- | -------------------------- |
| Programming Language   | Python                     |
| Frontend               | Streamlit                  |
| PDF Processing         | PyPDF                      |
| Embedding Model        | Sentence Transformers      |
| Vector Database        | FAISS                      |
| LLM                    | Google Gemini              |
| Environment Management | Python Virtual Environment |

## Project Structure

```text
rag-system/
│
├── app.py
│
├── data/
│   └── sample.pdf
│
├── modules/
│   ├── pdf_loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── retriever.py
│   └── llm.py
│
├── vector-store/
│
├── test_chunker.py
├── test_embedder.py
├── test_retrieval.py
├── test_rag.py
│
├── .env
├── requirements.txt
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/revathikrishnapk/rag-document-question-answering-system.git
cd rag-document-question-answering-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

macOS/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit
pip install pypdf
pip install sentence-transformers
pip install faiss-cpu
pip install google-generativeai
pip install python-dotenv
```

## Configuration

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Get your API key from Google AI Studio.

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## How It Works

### 1. Document Processing

The uploaded PDF is read using PyPDF and converted into plain text.

### 2. Chunking

Large documents are split into smaller overlapping chunks to improve retrieval accuracy and stay within LLM context limits.

### 3. Embedding Generation

Each chunk is converted into a numerical vector representation using the `all-MiniLM-L6-v2` Sentence Transformer model.

### 4. Vector Storage

The embeddings are stored in a FAISS vector index for efficient similarity search.

### 5. Retrieval

When a user asks a question, the query is converted into an embedding and compared against stored document embeddings. The most relevant chunks are retrieved.

### 6. Answer Generation

Retrieved chunks are provided as context to Gemini, which generates a grounded and context-aware answer.

## Example Workflow

```text
Upload PDF
      ↓
Ask Question
      ↓
Retrieve Relevant Chunks
      ↓
Generate Answer
      ↓
Display Sources
```

## Sample Questions

* What is the main objective of this document?
* Summarize the introduction section.
* What are the key findings mentioned?
* Explain the methodology used.
* What recommendations are provided?

## Future Improvements

* Multiple PDF support
* Conversational memory
* Hybrid search (BM25 + Vector Search)
* Source highlighting
* Chat history persistence
* User authentication
* Cloud deployment
* Docker support

## Learning Outcomes

This project demonstrates practical understanding of:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Embeddings
* Information Retrieval
* Prompt Engineering
* Large Language Model Integration
* AI Application Development

## Author

Revathi Krishna

M.Sc. Artificial Intelligence & Machine Learning, VIT Vellore


