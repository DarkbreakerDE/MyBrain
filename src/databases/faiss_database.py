from typing import Optional
import Config
import faiss
from models.model import dimension
import os
import numpy as np
from numpy.typing import NDArray
import atexit

index: Optional[faiss.IndexFlatL2] = None


def init():
    global index
    if Config.overwrite or not os.path.exists(Config.faiss_database_path):
        index = faiss.IndexFlatL2(dimension)
    else:
        index = faiss.read_index(Config.faiss_database_path)
    atexit.register(save)


def add(embeddings: NDArray[np.float32]):
    assert index is not None
    index.add(embeddings)  # pyright: ignore


def search(query_embedding: NDArray[np.float32], k=1):
    assert index is not None
    distances, indices = index.search(query_embedding, k)  # pyright: ignore
    return distances, indices


def save():
    assert index is not None
    faiss.write_index(index, Config.faiss_database_path)


def clear():
    global index
    index = faiss.IndexFlatL2(dimension)
