import pypdfium2


def load_and_print(file_path):
    pdf = pypdfium2.PdfDocument(file_path)

    print(pdf.get_metadata_dict(), "\n")
    for page in pdf:
        print(page.get_textpage().get_text_range())

    pdf.close()


def load_and_map(file_path, func):
    pdf = pypdfium2.PdfDocument(file_path)

    for page in pdf:
        func(page.get_textpage().get_text_bounded())

    pdf.close()


def load_and_map_ret(file_path, func):
    pdf = pypdfium2.PdfDocument(file_path)

    r = [func(page.get_textpage().get_text_bounded()) for page in pdf]

    pdf.close()

    return r
