from utils.map_functions import map_grouped


def _fun(arr, threshold):
    result = []
    temp = ""
    for elem in arr:
        if len(elem) < threshold or len(temp) < threshold:
            temp = temp + elem
        else:
            result.append(temp)
            temp = elem
    if len(temp) > 0:
        result.append(temp)
    return result


def concat_too_small_chunks(data, threshold=50):
    return map_grouped(data, lambda x: _fun(x, threshold))
