from text_pipeline.remove_page_numbers import _extract_numbers_only_int


def test_1():
    text = ""
    r = _extract_numbers_only_int(text)

    assert r == []


def test_2():
    text = "10"
    r = _extract_numbers_only_int(text)

    assert r == [10]


def test_3():
    text = "-10"
    r = _extract_numbers_only_int(text)

    assert r == []


def test_4():
    text = "+10"
    r = _extract_numbers_only_int(text)

    assert r == []


def test_6():
    text = "10."
    r = _extract_numbers_only_int(text)

    assert r == [10]


def test_7():
    text = "10.0"
    r = _extract_numbers_only_int(text)

    assert r == []


def test_8():
    text = " 10"
    r = _extract_numbers_only_int(text)

    assert r == [10]


def test_9():
    text = "10 "
    r = _extract_numbers_only_int(text)

    assert r == [10]


def test_10():
    text = " 10 "
    r = _extract_numbers_only_int(text)

    assert r == [10]


def test_11():
    text = ".10"
    r = _extract_numbers_only_int(text)

    assert r == [10]


def test_12():
    for b in "B !.,:;-_'`\\?=)({[]}&/\"'#":
        text = f"{b}.10"
        r = _extract_numbers_only_int(text)

        assert r == [10]


def test_13():
    for b in "B !.,:;-_'`\\?=)({[]}&/\"'#":
        text = f"10.{b}"
        r = _extract_numbers_only_int(text)

        assert r == [10]


def test_14():
    for b in "B !.,:;-_'`\\?=)({[]}&/\"'#":
        text = f"{b},10"
        r = _extract_numbers_only_int(text)

        assert r == [10]


def test_15():
    for b in "B !.,:;-_'`\\?=)({[]}&/\"'#":
        text = f"10,{b}"
        r = _extract_numbers_only_int(text)

        assert r == [10]
