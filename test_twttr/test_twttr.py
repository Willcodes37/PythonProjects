from twttr import shorten


def main():
    test_lower_case()
    test_upper_case()
    test_numbers()
    test_punctuation()


def test_lower_case():
    assert shorten('twitter') == "twttr"
    assert shorten('apple') == "ppl"


def test_numbers():
    assert shorten("a8893pple") == "8893ppl"
    assert shorten("1048545") == "1048545"


def test_upper_case():
    assert shorten("APPLE") == "PPL"
    assert shorten("ELEPHANT") == "LPHNT"


def test_punctuation():
    assert shorten(",./'") == ",./'"


if __name__ == "__main__":
    main()



        