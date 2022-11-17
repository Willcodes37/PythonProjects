from numb3rs import validate


def main():
    test_case_words()
    test_case_valid()
    test_case_symbols()
    test_case_first_oct()




def test_case_words():
    assert validate('cat.dog.pig.chicken') is False
    assert validate('Hello.Bye') is False


def test_case_valid():
    assert validate("125.23.150.255") is True
    assert validate("230.125.220.83") is True


def test_case_symbols():
    assert validate("@#$.*&$.@#%.*%$") is False
    assert validate("123.#$$.23.^%2") is False


def test_case_first_oct():
    assert validate("125.345.75.55") is False
    assert validate("230.700.46.32") is False


if __name__ == "__main__":
    main()