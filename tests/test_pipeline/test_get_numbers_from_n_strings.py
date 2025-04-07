from text_pipeline.remove_page_numbers import _get_numbers_from_n_strings


def test_empty():
    data = [[]]
    r1, r2 = _get_numbers_from_n_strings(data, 2)

    assert r1 == [[]]
    assert r2 == [[]]

    data = []
    r1, r2 = _get_numbers_from_n_strings(data, 2)

    assert r1 == []
    assert r2 == []


def test_empty2():
    data = [["Hellloo"]]
    r1, r2 = _get_numbers_from_n_strings(data, 2)

    assert r1 == [[]]
    assert r2 == [[]]


def test_empty3():
    data = [["Hellloo", "bauuuuuum"]]
    r1, r2 = _get_numbers_from_n_strings(data, 2)

    assert r1 == [[]]
    assert r2 == [[]]


def test_empty4():
    data = [["Hellloo", "bauuuuuum", "Schnitzel"]]
    r1, r2 = _get_numbers_from_n_strings(data, 2)

    assert r1 == [[]]
    assert r2 == [[]]


def test_empty5():
    data = [["Hellloo", "bauuuuuum", "Schnitzel", "eimer"]]
    r1, r2 = _get_numbers_from_n_strings(data, 2)

    assert r1 == [[]]
    assert r2 == [[]]


def test_2():
    data = [["Hellloo 10"]]
    r1, r2 = _get_numbers_from_n_strings(data, 2)

    assert r1 == [[10]]
    assert r2 == [[10]]


def test_3():
    data = [["Hellloo 10", "bauuuuuum 20"]]
    r1, r2 = _get_numbers_from_n_strings(data, 2)

    assert r1 == [[10, 20]]
    assert r2 == [[10, 20]]


def test_4():
    data = [["Hellloo 10", "bauuuuuum 20", "Schnitzel  30"]]
    r1, r2 = _get_numbers_from_n_strings(data, 2)

    assert r1 == [[10, 20]]
    assert r2 == [[20, 30]]


def test_5():
    data = [["Hellloo 10", "bauuuuuum 20", "Schnitzel 30", "Eimer 40"]]
    r1, r2 = _get_numbers_from_n_strings(data, 2)

    assert r1 == [[10, 20]]
    assert r2 == [[30, 40]]


def test_6():
    data = [["Hellloo 10", "bauuuuuum 20", "nichte 50", "Schnitzel 30", "Eimer 40"]]
    r1, r2 = _get_numbers_from_n_strings(data, 2)

    assert r1 == [[10, 20]]
    assert r2 == [[30, 40]]
