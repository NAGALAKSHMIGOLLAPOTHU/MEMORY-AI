# app.py

import os
import warnings

# 🔇 Suppress warnings
warnings.filterwarnings("ignore")

# 🔇 Suppress transformers logs
from transformers import logging
logging.set_verbosity_error()

# 🔇 Optional: suppress HF warnings
os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "true"
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"

# 📦 Imports
from llm.groq_client import generate_response
from memory.chroma_store import add_memory
from memory.hybrid_search import hybrid_search
from memory.summarize import summarize_memories

# 🧠 In-memory chat history
chat_history = []


def process_input(user_id, user_input):
    global chat_history

    # 🔍 Step 1: Retrieve relevant past memories
    memories = hybrid_search(user_id, user_input)

    # Convert memory list → string
    context = "\n".join(memories) if memories else "No relevant past memory."

    # 🧠 Step 2: Build improved prompt
    prompt = f"""
You are a helpful AI assistant.

- Use past memory only if it adds value
- Do not repeat previous phrases unnecessarily
- Be natural and conversational
- Avoid saying things like "we've met before" unless truly needed

Past memories:
{context}

User: {user_input}

Assistant:
"""

    # 🤖 Step 3: Generate response
    response = generate_response(prompt)

    # 💾 Step 4: Store conversation
    entry = f"User: {user_input} | AI: {response}"
    chat_history.append(entry)

    add_memory(user_id, entry)

    # 🗜️ Step 5: Memory compression (every 10 chats)
    if len(chat_history) >= 10:
        summary = summarize_memories(chat_history)
        add_memory(user_id, f"SUMMARY: {summary}")
        chat_history.clear()

    return response