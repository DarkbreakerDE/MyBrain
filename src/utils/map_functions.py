from typing import Callable, Any, Union


def map_deep(data: Any, func: Callable[[Any], Any]) -> Any:
    """
    Recursively applies a function to every single element in a deeply nested list structure.

    Example:
    >>> map_deep(lambda x: x * 2, [[1, 2], [3, [4, 5]]])
    [[2, 4], [6, [8, 10]]]
    """
    if isinstance(data, list):
        return [map_deep(item, func) for item in data]
    else:
        return func(data)


def map_innermost(data: Any, func: Callable[[list], Any]) -> Any:
    """
    Applies a function only to the innermost lists in a nested structure.

    Example:
    >>> map_innermost(sum, [[[1, 2], [3, 4]], [5, 6], [[[[7, 8]]]]])
    [[3, 7], 11, [[[15]]]]
    """
    if isinstance(data, list):
        if any(isinstance(x, list) for x in data):
            return [map_innermost(x, func) for x in data]
        else:
            return func(data)
    else:
        return data


def map_grouped(
    data: Any, func: Callable[[Union[list, Any]], Any], wrap: bool = True
) -> Any:
    """
    Applies a function to grouped scalar values and innermost lists in a mixed nested structure.

    - Consecutive scalar values (e.g., 4, 5) are grouped into a list and passed to `func`.
    - Innermost lists (e.g., [2, 3]) are also passed to `func`.
    - If `wrap=True`, results from lists are returned wrapped in a list: [func(...)].

    Example:
    >>> map_grouped([[2, 3], 4, 5, [[6, 7]], 8, 9], sum)
    [[5], 9, [[13]], 17]
    """
    if isinstance(data, list):
        if all(not isinstance(x, list) for x in data):
            result = func(data)
            return result if wrap else result
        else:
            result = []
            group = []
            for item in data:
                if isinstance(item, list):
                    if group:
                        result.append(func(group))
                        group = []
                    result.append(map_grouped(item, func, wrap))
                else:
                    group.append(item)
            if group:
                result.append(func(group))
            return result
    else:
        return data
