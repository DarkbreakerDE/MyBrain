#!/usr/bin/python3
from pathlib import Path
import Config
from args.import_pdf_parse import parse_args_and_set
from databases import faiss_database, sqlite_database
from gui.file_dialog import get_file_paths_gui_qt5
from load_files.load_pdf import load_and_map_ret
from models import model
from pipelines import clean_page, clean_pages
from pipelines.edit_text_editor import edit
from utils.hash_file import hash_file
from utils.pritty_format_list import pretty_format_list
from utils.pritty_print_list import pretty_print_list
from utils.flatten_nested_list import flatten_nested_list


def main():
    files = parse_args_and_set()

    print("MyBrain Started\n")
    print("Faiss Database Path:", Config.faiss_database_path)
    print("Sqlite Database Path:", Config.sqlite_database_path)

    sqlite_database.init()
    faiss_database.init()

    if not files:
        files = get_file_paths_gui_qt5()

    for file in files:

        fingerprint = hash_file(file)
        if id := sqlite_database.insert_file_or_none(Path(file).name, fingerprint):
            data = load_and_map_ret(file, clean_page.clean)
            text_before = pretty_format_list(data)

            clean_pages.clean(data)

            text_after = pretty_format_list(data)

            if Config.edit:
                data = edit(text_before, text_after)

            # data = remove_common_substring(data)

            pretty_print_list(data)

            embeddings = model.create_entry_embeddings_float32(
                flatten_nested_list(data)
            )
            faiss_database.add(embeddings)
            sqlite_database.insert_passages(flatten_nested_list(data), id)
        else:
            print("Datei Bereits Vorhanden")
    # testScript.sliding_window()

    # testScript.splitting_sentences()


if __name__ == "__main__":
    main()
