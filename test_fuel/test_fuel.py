from fuel import convert, gauge
import pytest


def main():
    test_case_zero_division()
    test_case_x_greater_y()
    test_case_gauge_full()
    test_case_gauge_empty()
    test_case_gauge_int()
    test_case_string_ints()
    test_case_negative_ints()
    test_case_float()


def test_case_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
        convert("16/0")
        convert("22/0")


def test_case_negative_ints():
    with pytest.raises(ValueError):
        convert("-3/5")
        convert("5/-7")
        convert("-7/16")


def test_case_string_ints():
    with pytest.raises(ValueError):
        convert("up/down")
        convert("left/right")
    with pytest.raises(ValueError):
        convert("2/hello")
        convert("bye/7")


def test_case_x_greater_y():
    with pytest.raises(ValueError):
        convert("6/3")
        convert("5/2")
        convert("7/4")


def test_case_float():
    with pytest.raises(ValueError):
        convert("6.5/3")
        convert("5/2.5")
        convert("7.9/4")


def test_case_gauge_full():
    assert gauge(99) == "F"
    assert gauge(99.5) == "F"
    assert gauge(99.8) == "F"


def test_case_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(0.9) == "E"
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"


def test_case_gauge_int():
    assert gauge(75) == "75%"
    assert gauge(86) == "86%"
    assert gauge(45) == "45%"


if __name__ == "__main__":
    main()