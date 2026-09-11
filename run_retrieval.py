from retrieval.retriever import get_relevant_documents

docs = get_relevant_documents(
    "What medications were prescribed?"      #type your query here
)

for doc in docs:
    print("=" * 50)
    print(doc.page_content)
    print(doc.metadata)