from bank import value


def main():
    test_case_hello()
    test_case_h()
    test_case_other()


def test_case_hello():
    assert value('Hello, Michael ') == 0
    assert value('Hello, how are you?') == 0


def test_case_h():
    assert value("Hi, Adam") == 20
    assert value("Howdy") == 20


def test_case_other():
    assert value("What's up?") == 100
    assert value("Good morning") == 100


if __name__ == "__main__":
    main()
