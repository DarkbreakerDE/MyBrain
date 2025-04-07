from pathlib import Path
from databases import faiss_database, sqlite_database
from gui.file_dialog import get_file_paths_gui_qt5
from load_files.load_pdf import load_and_map_ret
from Config import faiss_database_name, sqlite_database_name
from models import model
from pipelines import clean_page, clean_pages
from utils.hash_file import hash_file
from utils.pritty_format_list import pretty_format_list
from utils.pritty_print_list import pretty_print_list
from utils.write_string_to_file import write_string_to_file
from utils.flatten_nested_list import flatten_nested_list

if __name__ == "__main__":
    print("MyBrain Started\n")
    # testScript.foo(folder_name, file_name)

    print("Faiss Database Path:", faiss_database_name)
    print("Sqlite Database Path:", sqlite_database_name)

    files = get_file_paths_gui_qt5()

    for file in files:

        fingerprint = hash_file(file)
        if id := sqlite_database.insert_file_or_none(Path(file).name, fingerprint):
            data = load_and_map_ret(file, clean_page.clean)
            text_before = pretty_format_list(data)

            clean_pages.clean(data)

            text_after = pretty_format_list(data)

            write_string_to_file("text_before.txt", text_before)
            write_string_to_file("text_after.txt", text_after)
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
