from sentence_transformers import SentenceTransformer

print("Lade Modell ...")
model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L6-v2")
print("Erfolgreich geladen:", model.get_sentence_embedding_dimension())
