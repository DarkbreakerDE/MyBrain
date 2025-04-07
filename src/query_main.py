#!/usr/bin/python3
from databases import faiss_database, sqlite_database
from models import model


def main():
    # Dateipfade für FAISS-Index und SQLite-Datenbank

    # Eingabe der Suchanfrage über das Terminal
    query = input("Bitte geben Sie Ihre Suchanfrage ein: ")

    # Erzeugung des Query-Embeddings
    query_embedding = model.create_query_embedding_float32(query)
    # Suche im FAISS-Index (Top-1 Ergebnis)
    distances, indices = faiss_database.search(query_embedding, k=1)

    # Überprüfen, ob ein Ergebnis gefunden wurde
    if indices.size == 0 or indices[0][0] == -1:
        print("Keine passende Passage gefunden.")
        return

    # Abruf der Passage anhand der gefundenen ID
    passage_id = int(indices[0][0])
    passage_text = sqlite_database.get_passage_context(passage_id)

    print("\nGefundene Passage:")
    print(passage_text)
    print("\nDistanz:", distances[0][0])


if __name__ == "__main__":
    while True:
        main()
