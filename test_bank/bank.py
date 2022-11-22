def main():
    x = input("Greeting: ").strip()
    greet = value(x)
    print(greet)


def value(greeting):
    if greeting.startswith("Hello"):
        return 0
    elif greeting.startswith("H"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()


