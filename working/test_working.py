import re

am = {
    "12": "00",
    "1": "01",
    "2": "02",
    "3": "03",
    "4": "04",
    "5": "05",
    "6": "06",
    "7": "07",
    "8": "08",
    "9": "09",
    "10": "10",
    "11": "11"
}

pm = {
    "12": "12",
    "1": "13",
    "2": "14",
    "3": "15",
    "4": "16",
    "5": "17",
    "6": "18",
    "7": "19",
    "8": "20",
    "9": "21",
    "10": "22",
    "11": "23"
}


def main():
    print(convert(input("Hours: ")))


def convert(s):

    x = re.search(r"^([1-9]|1[0-2])(:[0-5]{1}[0-9]{1})\s(AM|PM)\sto\s([1-9]|1[0-2])(:[0-5]{1}[0-9]{1})\s(AM|PM)$", s)
    x2 = re.search(r"^([1-9]|1[0-2])\s(AM|PM)\sto\s([1-9]|1[0-2])?\s(AM|PM)$", s)

    if x:
        if x.group(3) == "AM":
            h = am.get(x.group(1))
            m = x.group(2)
        else:
            h = pm.get(x.group(1))
            m = x.group(2)

        if x.group(6) == "AM":
            h2 = am.get(x.group(4))
            m2 = x.group(5)
        else:
            h2 = pm.get(x.group(4))
            m2 = x.group(5)

        return h + m + " " + "to" + " " + h2 + m2

    elif x2:
        if x2.group(2) == "AM":
            h = am.get(x2.group(1))
            m = "00"
        else:
            h = pm.get(x2.group(1))
            m = "00"

        if x2.group(4) == "AM":
            h2 = am.get(x2.group(3))
            m2 = "00"
        else:
            h2 = pm.get(x2.group(3))
            m2 = "00"

        return h + ":" + m + " " + "to" + " " + h2 + ":" + m2

    else:
        raise ValueError


if __name__ == "__main__":
    main()