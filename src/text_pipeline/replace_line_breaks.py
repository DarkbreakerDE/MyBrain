import re
from utils.map_functions import map_deep


def replace_line_breaks(data):
    return map_deep(
        data,
        lambda x: re.sub(
            r"(?<=[\w.,:;{}\[\]\"'”'”`%?!])\n(?=[\w.,:;{}\[\]\"'”'”`%?!])", " ", x
        ),
    )
