def flatten_nested_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_nested_list(item))
        else:
            result.append(item)
    return result
