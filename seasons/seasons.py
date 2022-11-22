from datetime import date
import inflect
import re
import sys


def main():
    date_input = input("Date of birth: ")
    print(convert(date_input))


def convert(a):
    p = inflect.engine()
    c = re.search("^([1-2]{1}[0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])$", a)

    if c:
        x, y, z = a.split("-")
        if y[0] == "0" and z[0] == "0":
            y = y.replace("0", "")
            z = z.replace("0", "")
            if date(int(x), int(y), int(z)):
                days = date.today() - date(int(x), int(y), int(z))
                days = str(days)
                days_index = days.split(" ")
                minutes = round(int(days_index[0]) * 24 * 60)
                return p.number_to_words(minutes).replace("and ", "").capitalize() + " minutes"
            else:
                sys.exit("Invalid date")
        elif y[0] == "0" and not z[0] == "0":
            y = y.replace("0", "")
            if date(int(x), int(y), int(z)):
                days = date.today() - date(int(x), int(y), int(z))
                days = str(days)
                days_index = days.split(" ")
                minutes = round(int(days_index[0]) * 24 * 60)
                return p.number_to_words(minutes).replace("and ", "").capitalize() + " minutes"
            else:
                sys.exit("Invalid date")
        elif not y[0] == "0" and z[0] == "0":
            z = z.replace("0", "")
            if date(int(x), int(y), int(z)):
                days = date.today() - date(int(x), int(y), int(z))
                days = str(days)
                days_index = days.split(" ")
                minutes = round(int(days_index[0]) * 24 * 60)
                return p.number_to_words(minutes).replace("and ", "").capitalize() + " minutes"
            else:
                sys.exit("Invalid date")
        else:
            if date(int(x), int(y), int(z)):
                days = date.today() - date(int(x), int(y), int(z))
                days = str(days)
                days_index = days.split(" ")
                minutes = round(int(days_index[0]) * 24 * 60)
                return p.number_to_words(minutes).replace("and ", "").capitalize() + " minutes"
            else:
                sys.exit("Invalid date")
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
