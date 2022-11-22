import sys

try:
    i = 0
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        with open(sys.argv[1]) as file:
            f = file.readlines()
            for line in f:
                if line.lstrip().startswith("#") or line.isspace():
                    pass
                else:
                    i += 1

    print(i)


except FileNotFoundError:
    sys.exit("File does not exist")