import re

from utils.map_functions import map_deep


def remove_control_symbols(data):
    return map_deep(data, lambda x: re.sub(r"[\x00-\x1F\x7F]", "", x))
