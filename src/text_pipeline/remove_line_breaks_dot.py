import re
from utils.map_functions import map_deep


def remove_line_breaks_dot(data):
    return map_deep(data, lambda x: re.sub(r"(?<=.)\n(?=[a-zA-Z0-9])", " ", x))
