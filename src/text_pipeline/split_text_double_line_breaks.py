from utils.map_functions import map_deep


def split_text_double_line_breaks(data):
    return map_deep(data, lambda x: x.split("\n\n"))
