from um import count


def main():
    test_case_valid()


def test_case_valid():
    assert count("Yummy, um, um") == 2
    assert count("um, um, um, hello um") == 4

def test_uppercase():
    assert count("Um, Um, Yummy") == 2
    assert count("um, um, Um, hello Um") == 4

if __name__ == "__main__":
    main()
