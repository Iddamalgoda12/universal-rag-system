# Universal RAG Pipeline System

A general-purpose **RAG (Retrieval-Augmented Generation)** system designed to be used across different projects and environments.

The system is not tied to a specific vector database, embedding model, or reranker. These components can be changed depending on the requirements of the application.

## Features

* Currently supports **PDF documents**.
* Supports different vector databases.
* Supports different embedding models.
* Supports different rerankers.
* Customizable chunking.
* Shows the number of chunks created during ingestion.
* Can be configured to run models on **CPU or GPU**.

## RAG Pipeline

```text
Documents
    ↓
Ingestion
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Retrieval
    ↓
Reranking
    ↓
Relevant Chunks
```

## Vector Database

The current implementation uses **Qdrant**, but Qdrant is not compulsory.

The vector database can be changed depending on the application requirements.

Examples:

* Qdrant
* FAISS
* Chroma
* Weaviate
* Milvus
* Pinecone
* Elasticsearch

## Embedding Model

The embedding model can be changed depending on the requirements of the application.

Different embedding models can be used based on factors such as accuracy, speed, language support, and available hardware.

## Reranker

The reranker can also be changed depending on the requirements.

A different reranking model can be used, or reranking can be disabled if it is not required.

## Chunking

The chunking strategy can be customized depending on the document type and application.

## Current Document Support

Currently, the system supports:

```text
PDF
```

Support for other document types can be added later.

## Running the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add documents

Place PDF files inside:

```text
data/pdfs/
```

### 3. Run ingestion

```bash
python run_ingestion.py
```

This loads the PDFs, creates chunks, generates embeddings, and stores them in the configured vector database.

The system also shows the number of chunks created for each PDF.

### 4. Run retrieval

Then run:

```bash
python run_retrieval.py
```


## Goal

The goal of this project is to provide a **universal RAG system** that can be reused across different applications without being tied to one particular vector database, embedding model, reranker, or hardware configuration.
