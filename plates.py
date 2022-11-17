Capital_letters = []
for i in range(65, 91):
    Capital_letters.append(chr(i))

Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length of input

    if not 2 <= len(s) <= 6:
        return False
    # Check if first two characters of the string are in the Capital_letters

    elif s[0] not in Capital_letters and s[1] not in Capital_letters:
        return False
    # Check if the input only has letters and numbers

    else:
        # Check if the first number used is not 0

        if len(s) == 2:
            if (s[0] in Capital_letters or s[0] in Numbers) and \
                    (s[1] in Capital_letters or s[1] in Numbers):
                if s[0] not in Capital_letters and s[1] not in Capital_letters:
                    return False
                else:
                    return True
            else:
                return False
        elif len(s) == 3:
            if (s[0] in Capital_letters or s[0] in Numbers) and \
                    (s[1] in Capital_letters or s[1] in Numbers) and \
                    (s[2] in Capital_letters or s[2] in Numbers):
                if s[2] in Numbers and s[2] != "0":
                    return True
                elif s[0] in Capital_letters and s[1] in Capital_letters and s[2] in Capital_letters:
                    return True
                else:
                    return False
            else:
                return False
        elif len(s) == 4:
            if (s[0] in Capital_letters or s[0] in Numbers) and \
                    (s[1] in Capital_letters or s[1] in Numbers) and \
                    (s[2] in Capital_letters or s[2] in Numbers) and \
                    (s[3] in Capital_letters or s[3] in Numbers):
                if s[1] in Numbers:
                    return False
                elif s[2] in Numbers and s[3] in Numbers and s[2] != "0":
                    return True
                elif s[3] in Numbers and s[2] != "0" and s[3] != "0":
                    return True
                elif s[0] in Capital_letters and s[1] in Capital_letters and s[2] in Capital_letters and \
                        s[3] in Capital_letters:
                    return True
                else:
                    return False
            else:
                return False
        elif len(s) == 5:
            if (s[0] in Capital_letters or s[0] in Numbers) and \
                    (s[1] in Capital_letters or s[1] in Numbers) and \
                    (s[2] in Capital_letters or s[2] in Numbers) and \
                    (s[3] in Capital_letters or s[3] in Numbers) and \
                    (s[4] in Capital_letters or s[4] in Numbers):
                if s[2] in Numbers:
                    return False
                elif s[3] in Numbers and s[4] in Numbers and s[3] != "0":
                    return True
                elif s[4] in Numbers and s[3] != "0" and s[4] != "0":
                    return True
                elif s[0] in Capital_letters and s[1] in Capital_letters and s[2] in Capital_letters and \
                        s[3] in Capital_letters and s[4] in Capital_letters:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if (s[0] in Capital_letters or s[0] in Numbers) and \
                    (s[1] in Capital_letters or s[1] in Numbers) and \
                    (s[2] in Capital_letters or s[2] in Numbers) and \
                    (s[3] in Capital_letters or s[3] in Numbers) and \
                    (s[4] in Capital_letters or s[4] in Numbers) and \
                    (s[5] in Capital_letters or s[5] in Numbers):
                if s[2] in Numbers:
                    return False
                elif s[3] in Numbers and s[4] in Numbers and s[5] in Numbers and s[3] != "0":
                    return True
                elif s[4] in Numbers and s[5] in Numbers and s[4] != "0":
                    return True
                elif s[5] in Numbers and s[5] != "0":
                    return True
                elif s[0] in Capital_letters and s[1] in Capital_letters and s[2] in Capital_letters \
                        and s[3] in Capital_letters and s[4] in Capital_letters and s[5] in Capital_letters:
                    return True
                else:
                    return False
            else:
                return False


main()