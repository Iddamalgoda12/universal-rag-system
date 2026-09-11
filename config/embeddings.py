from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

# Single source of truth for every embedding-backed workflow in the app.
EMBEDDING_MODEL_NAME = "BAAI/bge-m3"
EMBEDDING_MODEL_PATH = BASE_DIR / "Models" / "embedding models" / "......"  # Add your embedding model here
EMBEDDING_DIMENSION = 1024                                                  #Set your embeddings dimension here
RAG_COLLECTION_NAME = "documents_bge_m3_1024"
