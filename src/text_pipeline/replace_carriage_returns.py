from utils.map_functions import map_deep


def replace_carriage_returns(data):
    return map_deep(data, lambda x: x.replace("\r", "\n"))
