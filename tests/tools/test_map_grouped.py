import pytest
from tools.map_functions import map_grouped
from statistics import mean


def test_map_grouped_sum_basic():
    data = [[2, 3], 4, 5, [[6, 7]], 8, 9]
    result = map_grouped(data, sum)
    assert result == [[5], 9, [[13]], 17]


def test_map_grouped_mean():
    data = [[2, 4], 3, 3, [[6, 10]], 10]
    result = map_grouped(data, mean)
    assert result == [[3.0], 3.0, [[8.0]], 10.0]


def test_map_grouped_wrap_false():
    data = [[1, 2], 3, 4, [[5, 5]], 6]
    result = map_grouped(data, sum, wrap=False)
    assert result == [3, 7, [10], 6]


def test_map_grouped_empty_list():
    data = []
    result = map_grouped(data, sum, False)
    assert result == 0  # sum of empty list


def test_map_grouped_list_of_empty_lists():
    data = [[], [[]], [[[]]]]
    result = map_grouped(data, sum, False)
    assert result == [0, [0], [[0]]]


def test_map_grouped_only_scalars():
    data = [1, 2, 3]
    result = map_grouped(data, sum)
    assert result == [6]


def test_map_grouped_only_nested_lists():
    data = [[1, 2], [3, 4]]
    result = map_grouped(data, sum)
    assert result == [[3], [7]]


def test_map_grouped_scalar_input():
    data = 42
    result = map_grouped(data, lambda x: x + 1)  # scalar is returned unchanged
    assert result == 42


def test_map_grouped_with_none_values():
    data = [None, 1, 2, [None, 3]]
    result = map_grouped(data, lambda x: sum(v or 0 for v in x))
    assert result == [
        3,
        [3],
    ], "None + 1 + 2 = 3, [None, 3] = 3 → total = 3 (inner wrapped result)"


def test_map_grouped_custom_function():
    data = [[2, 3, 4], 1, 1, [10]]
    result = map_grouped(data, lambda lst: max(lst) - min(lst))
    assert result == [[2], 0, [0]]
