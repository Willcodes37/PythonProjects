from validator_collection import checkers


def main():
    print(validate(input("Text: ")))


def validate(s):

    valid_email = checkers.is_email(s)

    if valid_email is True:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()