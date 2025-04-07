from utils.map_functions import map_deep


def remove_line_breaks_end_of_string(data):
    return map_deep(data, lambda x: x.rstrip())
