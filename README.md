# 🧠 MyBrain

**MyBrain** is a personal knowledge management tool that combines semantic search with efficient data storage using FAISS and SQLite. It processes PDF files, cleans their content, embeds text passages using sentence-transformers, and enables fast semantic querying with contextual results.

---

## 🚀 Features

- 🧾 **PDF Import** with advanced cleaning (removes headers, footers, page numbers, etc.)
- 📦 **Passage-level storage** in a SQLite database
- 🧠 **Semantic search** via FAISS and sentence-transformers
- 📁 **File fingerprinting** (robust recognition even if file names change)
- 🔄 **Contextual output**: retrieves the matching sentence with one before and one after
- 🔍 **Command-line interaction** for adding and querying data

---

## ⚙️ Setup

> ✅ Tested with **Python 3.11**  
> ⚠️ Other versions are untested and may not work as expected.

### 1. Create a virtual environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

This installs all required libraries, including:

- `sentence-transformers` for embedding text
- `faiss-cpu` for fast similarity search
- `sqlite3` (standard in Python) for database management
- `pypdfium2` and others for PDF parsing and cleaning

---

## 📥 Add data

To extract text from PDFs, clean and embed it, and insert it into the database, run:

```bash
python src/add_main.py
```

This script performs the following steps:

- Processes all selected PDFs
- Cleans and segments their content into meaningful passages
- Embeds the passages using sentence-transformers
- Stores vectors in FAISS and metadata in SQLite

---

## 🔎 Query data

To search the semantic database with a terminal input, run:

```bash
python src/query_main.py
```

You will be prompted to enter a query.  
The script will then:

- Encode your query as an embedding
- Search similar passages via FAISS
- Retrieve the passage **before**, **matching**, and **after** from SQLite

### Example output

```
Previous: This is the sentence before.
Match: This sentence matches your query.
Next: This is the following sentence.
```

---

## 📁 Project Structure

```
MyBrain/
├── src/
│   ├── add_main.py           # Add PDF data to database
│   ├── query_main.py         # Query the semantic index
│   ├── databases/
│   │   ├── faiss_database.py
│   │   └── sqlite_database.py
├── tests/
│   └── test_*.py             # Optional tests
├── requirements.txt
├── README.md
```

---

## 🛠️ Notes

- The project uses a dual-database architecture:
  - FAISS for fast semantic vector search
  - SQLite for storing passage text and file metadata
- PDF content is fingerprinted using a hash, so files are recognized even if renamed
- You can extend the search logic, filtering, or context length easily

---

## 📌 License

This project is private / internal and not (yet) published under a license.
