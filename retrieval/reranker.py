from pathlib import Path
from sentence_transformers import CrossEncoder

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "AI_MODELS" / "rerankers"

_reranker = None

def get_reranker() -> CrossEncoder:
    global _reranker

    if _reranker is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Local reranker model not found at {MODEL_PATH}. "
                "Place the model files in AI_MODELS/rerankers before using reranking."
            )

        _reranker = CrossEncoder(
            str(MODEL_PATH),
            trust_remote_code=True,
            device="cpu",
        )

    return _reranker


def rerank(
    query: str,
    documents: list[dict],
    top_k: int = 2,
) -> list[dict]:
    docs_with_text = [
        doc for doc in documents
        if doc.get("text")
    ]

    if not docs_with_text:
        return []

    pairs = [
        (query, doc["text"])
        for doc in docs_with_text
    ]

    reranker = get_reranker()
    scores = reranker.predict(pairs)

    scored_docs = []
    for doc, score in zip(docs_with_text, scores):
        scored_doc = {**doc, "rerank_score": float(score)}
        scored_docs.append(scored_doc)

    scored_docs.sort(
        key=lambda item: item["rerank_score"],
        reverse=True,
    )

    return scored_docs[:top_k]
