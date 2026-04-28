# memory/summarize.py

from llm.groq_client import generate_response

def summarize_memories(memories):
    """
    Compress multiple memory entries into a short summary
    """

    if not memories:
        return ""

    text_block = "\n".join(memories)

    prompt = f"""
You are a memory compression system.

Summarize the following conversation history into key facts, preferences, and important details.

Keep it concise but meaningful.

Memory:
{text_block}
"""

    summary = generate_response(prompt)

    return summary