import re
from utils.map_functions import map_deep


def remove_hyphenated_line_break(data):
    return map_deep(data, lambda x: re.sub(r"-\s*\n\s*", "", x))
