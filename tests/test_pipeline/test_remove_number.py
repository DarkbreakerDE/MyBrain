from text_pipeline.remove_page_numbers import _remove_number


def test_1():
    text = ""
    r, b = _remove_number(text, 10)

    assert r == ""
    assert not b


def test_2():
    text = "10"
    r, b = _remove_number(text, 10)

    assert r == ""
    assert b


def test_3():
    text = "-10"
    r, b = _remove_number(text, 10)

    assert r == "-10"
    assert not b


def test_4():
    text = "+10"
    r, b = _remove_number(text, 10)

    assert r == "+10"
    assert not b


def test_6():
    text = "10."
    r, b = _remove_number(text, 10)

    assert r == "."
    assert b


def test_7():
    text = "10.0"
    r, b = _remove_number(text, 10)

    assert r == "10.0"
    assert not b


def test_8():
    for a in "B !.,:;_'`\\?=){]}&/\"'#":
        text = f"{a}10"
        r, b = _remove_number(text, 10)

        assert r == f"{a}"
        assert b


def test_9():
    for a in "B !.,:;_'`\\?=({[}&/\"'#":
        text = f"10{a}"
        r, b = _remove_number(text, 10)

        assert r == f"{a}"
        assert b


def test_10():
    for a in "B !.,:;_'`\\?={}&/\"'#":
        text = f"{a}10{a}"
        r, b = _remove_number(text, 10)

        assert r == f"{a}{a}"
        assert b


def test_12():
    for a in "B !.,:;-_'`\\?=)({[]}&/\"'#":
        text = f"{a}.10"
        r, b = _remove_number(text, 10)

        assert r == f"{a}."
        assert b


def test_13():
    for a in "B !.,:;-_'`\\?=)({[]}&/\"'#":
        text = f"10.{a}"
        r, b = _remove_number(text, 10)

        assert r == f".{a}"
        assert b


def test_14():
    for a in "B !.,:;-_'`\\?=)({[]}&/\"'#":
        text = f"{a},10"
        r, b = _remove_number(text, 10)

        assert r == f"{a},"
        assert b


def test_15():
    for a in "B !.,:;-_'`\\?=)({[]}&/\"'#":
        text = f"10,{a}"
        r, b = _remove_number(text, 10)

        assert r == f",{a}"
        assert b


def test_16():
    text = "Hello 30.30b30 hihi 30 30.30"
    r, b = _remove_number(text, 30)

    assert r == "Hello 30.30b hihi 30 30.30"
    assert b
