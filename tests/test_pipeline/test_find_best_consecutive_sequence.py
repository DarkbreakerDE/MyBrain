from text_pipeline.remove_page_numbers import _find_best_consecutive_sequence


def test_empty():
    r = _find_best_consecutive_sequence([], 0)
    assert r == {}


def test_simple():
    r = _find_best_consecutive_sequence([[0], [1], [2]], 0)
    assert r == {0: 0, 1: 1, 2: 2}


def test_simple_None():
    r = _find_best_consecutive_sequence([[0], [0], [2]], 0)
    assert r == {0: 0}


def test_simple_single():
    r = _find_best_consecutive_sequence([[0], [0], [1]], 0)
    assert r == {1: 0, 2: 1}


def test_simple_single_None():
    r = _find_best_consecutive_sequence([[1], [0], [0]], 0)
    assert r == {1: 0}


def test_simple_single_twice():
    r = _find_best_consecutive_sequence([[0], [1], [0], [1]], 0)
    assert r == {0: 0, 1: 1}


def test_complex():
    r = _find_best_consecutive_sequence([[0, 1], [1, 2], [2, 3]], 0)
    assert r == {0: 0, 1: 1, 2: 2}


def test_complex_none():
    r = _find_best_consecutive_sequence([[0, 1], [0, 3], [5, 6]], 0)
    assert r == {0: 0}


def test_complex_single():
    r = _find_best_consecutive_sequence([[0], [0, 2], [1, 3]], 0)
    assert r == {1: 0, 2: 1}


def test_complex_single_None():
    r = _find_best_consecutive_sequence([[1, 2, 3], [0], [0]], 0)
    assert r == {1: 0}


def test_complex_single_twice():
    r = _find_best_consecutive_sequence([[0, 1], [1, 2], [0, 1], [1, 2]], 0)
    assert r == {0: 0, 1: 1}
