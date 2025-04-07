from Config import faiss_database_name
import faiss
from models.model import dimension
import os
import numpy as np
from numpy.typing import NDArray
import atexit


if os.path.exists(faiss_database_name):
    index = faiss.read_index(faiss_database_name)
else:
    index = faiss.IndexFlatL2(dimension)


def add(embeddings: NDArray[np.float32]):
    index.add(embeddings)  # pyright: ignore


def search(query_embedding: NDArray[np.float32], k=1):
    distances, indices = index.search(query_embedding, k)  # pyright: ignore
    return distances, indices


def save():
    faiss.write_index(index, faiss_database_name)


atexit.register(save)
