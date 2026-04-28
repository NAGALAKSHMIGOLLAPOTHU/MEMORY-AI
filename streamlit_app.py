import os
import logging
import warnings

# 🔥 Clean logs
os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"
logging.getLogger("transformers").setLevel(logging.ERROR)
warnings.filterwarnings("ignore")

import streamlit as st
from db.database import init_db
from app import process_input

# Init DB
init_db()

st.set_page_config(page_title="Memory AI", layout="centered")

# 🎨 UI Styling
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 👤 USERNAME INPUT
# =========================

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if not st.session_state.user_id:
    st.title("🧠 Memory AI")

    username = st.text_input("Enter your name to start:")

    if st.button("Start Chat"):
        if username.strip():
            st.session_state.user_id = username.strip()
            st.success(f"Welcome {username} 👋")
            st.rerun()
        else:
            st.warning("Please enter a name")

# =========================
# 💬 CHAT PAGE
# =========================
else:
    st.title(f"🧠 Memory AI Chat — {st.session_state.user_id}")

    # 🔄 Switch user
    if st.button("Change User"):
        st.session_state.user_id = None
        st.session_state.messages = []
        st.rerun()

    # Chat memory (UI only)
    # 🆕 Reset chat on page refresh
    if "chat_initialized" not in st.session_state:
        st.session_state.messages = []
        st.session_state.chat_initialized = True

    # Show chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Input
    user_input = st.chat_input("Ask something...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.write(user_input)

        # 🧠 Use username as user_id
        response = process_input(st.session_state.user_id, user_input)

        with st.chat_message("assistant"):
            st.write(response)

        st.session_state.messages.append({"role": "assistant", "content": response})