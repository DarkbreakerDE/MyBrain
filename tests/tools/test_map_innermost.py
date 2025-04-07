import pytest
from tools.map_functions import map_innermost
from statistics import mean


def test_map_innermost_basic_sum():
    data = [[[1, 2], [3, 4]], [5, 6], [[[[7, 8]]]]]
    result = map_innermost(data, sum)
    assert result == [[3, 7], 11, [[[15]]]]


def test_map_innermost_basic_mean():
    data = [[1, 2, 3], [[4, 6], [8, 12]]]
    result = map_innermost(data, mean)
    assert result == [2, [5.0, 10.0]]


def test_map_innermost_empty_list():
    data = []
    result = map_innermost(data, sum)
    assert result == 0  # sum([]) == 0


def test_map_innermost_nested_empty_lists():
    data = [[[]], [], [[[[]]]]]
    result = map_innermost(data, lambda x: len(x))
    assert result == [[0], 0, [[[0]]]]


def test_map_innermost_scalar_input():
    data = 42
    result = map_innermost(data, lambda x: x * 2)
    assert result == 42  # nothing to apply


def test_map_innermost_none_values():
    data = [[None, None], [1, 2]]
    result = map_innermost(
        data, lambda x: 0 if all(v is None for v in x) else sum(v or 0 for v in x)
    )
    assert result == [0, 3]


def test_map_innermost_mixed_depths():
    data = [1, [2, 3], [[4, 5]], [[[6, 7]]]]
    result = map_innermost(data, sum)
    assert result == [1, 5, [9], [[13]]]
