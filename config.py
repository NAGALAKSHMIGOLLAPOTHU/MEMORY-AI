# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# =========================
# 🔑 GROQ API CONFIG
# =========================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# =========================
# 🤖 MODEL CONFIG
# =========================
# Fast + efficient model (recommended)
MODEL_NAME = "llama-3.3-8b-instant"

# Fallback models (used if main fails)
FALLBACK_MODELS = [
    "llama-3.3-70b-versatile",
    "mixtral-8x7b-32768"
]

# =========================
# 🧠 MEMORY CONFIG
# =========================
MEMORY_TOP_K = 5        # how many memories to retrieve
MAX_HISTORY = 10        # how many past chats to store

# =========================
# 🌡️ GENERATION SETTINGS
# =========================
TEMPERATURE = 0.7       # creativity (0 = strict, 1 = creative)
MAX_TOKENS = 500        # max response length

# =========================
# ⚙️ APP SETTINGS
# =========================
DEBUG = True