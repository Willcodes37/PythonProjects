from plates import is_valid


def main():
    test_case_acceptable()
    test_over_char_limit()
    test_case_0()
    test_under_char_limit()
    test_case_alphanumeric()
    test_case_numplacement()
    test_case_beginningletters()
    test_under_first_2()


def test_case_acceptable():
    assert is_valid('AAA222') is True
    assert is_valid('FHTH33') is True


def test_over_char_limit():
    assert is_valid("ASFTNB55") is False
    assert is_valid("HJKGFYU78") is False


def test_under_char_limit():
    assert is_valid("A") is False
    assert is_valid("H") is False

def test_under_first_2():
    assert is_valid("A2") is False
    assert is_valid("HA") is True
    assert is_valid("78") is False
    assert is_valid("3A") is False


def test_case_0():
    assert is_valid("0ABNR1") is False
    assert is_valid("0KSFTD") is False

def test_case_alphanumeric():
    assert is_valid("1A2b#$") is False
    assert is_valid("A&bN#Z") is False
    assert is_valid("AIbN#,") is False
    assert is_valid("IJ*%wY,") is False

def test_case_numplacement():
    assert is_valid("AYRG02") is False
    assert is_valid("YI54SD") is False

def test_case_beginningletters():
    assert is_valid("56DJFD") is False
    assert is_valid("29DEIG") is False

if __name__ == "__main__":
    main()

    