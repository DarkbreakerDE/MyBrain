from tools.map_functions import map_deep


def test_map_deep_simple():
    data = [[1, 2], [3, [4, 5]]]
    result = map_deep(data, lambda x: x * 2)
    assert result == [[2, 4], [6, [8, 10]]]


def test_map_deep_strings():
    data = [["a", "b"], ["c", ["d"]]]
    result = map_deep(data, str.upper)
    assert result == [["A", "B"], ["C", ["D"]]]


def test_map_deep_empty_list():
    data = []
    result = map_deep(data, lambda x: x * 2)
    assert result == []


def test_map_deep_scalar_input():
    data = 10
    result = map_deep(data, lambda x: x + 1)
    assert result == 11


def test_map_deep_none_value():
    data = [[None, 1], [2, [None]]]
    result = map_deep(data, lambda x: 0 if x is None else x * 10)
    assert result == [[0, 10], [20, [0]]]


def test_map_deep_mixed_types():
    data = [1, "a", [2.5, ["b"]]]
    result = map_deep(data, lambda x: str(x) + "!")
    assert result == ["1!", "a!", ["2.5!", ["b!"]]]


def test_map_deep_nested_empty_lists():
    data = [[], [[]], [[[]]]]
    result = map_deep(data, lambda x: x)
    assert result == [[], [[]], [[[]]]]
