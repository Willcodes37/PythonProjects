from working import convert
import pytest


def main():
    test_case_words()
    test_case_valid()
    test_case_symbols()
    test_case_without_to()
    test_case_outofrange()


def test_case_words():
    with pytest.raises(ValueError):
        convert('cat AM to chicken PM')
        convert('Hello AM to Bye PM')


def test_case_valid():
    assert convert("8:50 AM to 5:30 PM") == "08:50 to 17:30"
    assert convert("9:00 AM to 3:20 PM") == "09:00 to 15:20"


def test_case_symbols():
    with pytest.raises(ValueError):
        convert("@#$ to *%$")
        convert("123 to ^%2")


def test_case_without_to():
    with pytest.raises(ValueError):
        convert("9:50 AM 6:30 PM")
        convert("12:50 AM 8:30 PM")


def test_case_outofrange():
    with pytest.raises(ValueError):
        convert("9:70 AM to 6:30 PM")
        convert("12:50 AM to 8:80 PM")


if __name__ == "__main__":
    main()