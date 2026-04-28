from memory.chroma_store import query_memory

def keyword_score(query, text):
    return len(set(query.lower().split()) & set(text.lower().split()))

def hybrid_search(user_id, query):
    results = query_memory(user_id, query)

    scored = []
    for text in results:
        score = keyword_score(query, text)
        scored.append((score, text))

    scored.sort(reverse=True)
    return [s[1] for s in scored[:3]]