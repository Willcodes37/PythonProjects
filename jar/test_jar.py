from jar import Jar


def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(5)
    assert jar.size == 7
    jar.deposit(2)
    assert jar.size == 9


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    jar.withdraw(1)
    assert jar.size == 9
    jar.withdraw(3)
    assert jar.size == 6


if __name__ == "__main__":
    main()