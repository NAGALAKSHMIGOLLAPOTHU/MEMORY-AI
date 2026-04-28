import warnings
warnings.filterwarnings("ignore")

from sentence_transformers import SentenceTransformer

# Load lightweight model
model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

def get_embedding(text: str):
    return model.encode([text])[0]