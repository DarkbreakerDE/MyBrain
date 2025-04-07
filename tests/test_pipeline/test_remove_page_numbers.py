from text_pipeline.remove_page_numbers import remove_page_numbers


def test_1():
    data = [
        ["0", "23"],
        ["1", "23"],
        ["2", "23"],
        ["3", "23"],
    ]
    r = remove_page_numbers(data, threshold_min_len_chain=1)

    assert r == [
        ["", "23"],
        ["", "23"],
        ["", "23"],
        ["", "23"],
    ]


def test_2():
    data = [
        ["Anders", "23"],
        ["1", "23"],
        ["2", "23"],
        ["3", "23"],
    ]
    r = remove_page_numbers(data)

    assert r == [
        ["Anders", "23"],
        ["", "23"],
        ["", "23"],
        ["", "23"],
    ]


def test_3():
    data = [
        ["Anders", "23"],
        ["I1", "23"],
        ["O2", "23"],
        ["P3", "23"],
    ]
    r = remove_page_numbers(data)

    assert r == [
        ["Anders", "23"],
        ["I", "23"],
        ["O", "23"],
        ["P", "23"],
    ]


def test_4():
    data = [
        ["Anders", "1"],
        ["I1", "1"],
        ["O2", "2"],
        ["P3", "3"],
    ]
    r = remove_page_numbers(data)

    assert r == [
        ["Anders", "1"],
        ["I", ""],
        ["O", ""],
        ["P", ""],
    ]


def test_5():
    data = [
        ["Anders", "1", "1", "Anders"],
        ["I1", "1", "1", "I1"],
        ["O2", "2", "2", "O2"],
        ["P3", "3", "3", "P3"],
    ]
    r = remove_page_numbers(data)

    assert r == [
        ["Anders", "1", "1", "Anders"],
        ["I", "1", "1", "I"],
        ["O", "2", "2", "O"],
        ["P", "3", "3", "P"],
    ]
