import chromadb
from chromadb.utils import embedding_functions
from utils.embeddings import get_embedding

client = chromadb.Client()

collection = client.get_or_create_collection(name="memory")

def add_memory(user_id, text):
    embedding = get_embedding(text).tolist()

    collection.add(
        documents=[text],
        embeddings=[embedding],
        metadatas=[{"user_id": user_id}],
        ids=[f"{user_id}_{hash(text)}"]
    )

def query_memory(user_id, query, k=5):
    query_embedding = get_embedding(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    # filter by user
    filtered = [
        doc for doc, meta in zip(docs, metas)
        if meta["user_id"] == user_id
    ]

    return filtered