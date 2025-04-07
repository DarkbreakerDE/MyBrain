def write_string_to_file(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
