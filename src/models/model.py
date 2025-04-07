from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

# model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
dimension = model.get_sentence_embedding_dimension()


def create_entry_embeddings_float32(passages):
    embeddings = model.encode(passages, convert_to_numpy=True)
    # FAISS benötigt Vektoren im Format float32
    return np.array(embeddings).astype("float32")


def create_query_embedding_float32(query):
    embedding = model.encode([query], convert_to_numpy=True)
    return np.array(embedding).astype("float32")
