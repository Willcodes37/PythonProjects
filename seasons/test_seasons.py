from seasons import convert


def main():
    test_case_valid()


def test_case_valid():
    assert convert("2000-02-12") == "Eleven million, eight hundred fifty-one thousand, two hundred minutes"
    assert convert("1999-01-01") == "Twelve million, four hundred thirty-seven thousand, two hundred eighty minutes"


if __name__ == "__main__":
    main()
