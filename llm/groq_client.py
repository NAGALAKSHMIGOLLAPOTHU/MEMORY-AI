from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.3-8b-instant",
    "mixtral-8x7b-32768"
]

def generate_response(prompt: str):
    for model in MODELS:
        try:
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a smart AI assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return completion.choices[0].message.content

        except Exception:
            continue

    return "⚠️ All models failed. Check API key or model availability."