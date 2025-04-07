from utils.map_functions import map_deep
import re


def replace_non_breaking(data):
    return map_deep(data, lambda x: re.sub(r"[\xa0]", " ", x))
