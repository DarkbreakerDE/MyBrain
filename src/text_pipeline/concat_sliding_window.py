from utils.map_functions import map_grouped


def _fun(arr, size, step):
    result = []
    if len(arr) < size:
        return [arr]
    for i in range(0, len(arr) - size + 1, step):
        result.append(arr[i : i + size])
    return result


def concat_sliding_window(data, size=4, step=1):
    return map_grouped(data, lambda x: _fun(x, size, step))
