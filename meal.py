def main():
    c = convert(input("What time is it? "))
    if 7 <= c <= 8:
        print("breakfast time")
    elif 12 <= c <= 13:
        print("lunch time")
    elif 18 <= c <= 19:
        print("dinner time")
    else:
        pass


def convert(time):
    hours, minutes = time.split(":")
    h = int(hours)
    m = int(minutes)
    mm = m / 60
    return h + mm


if __name__ == "__main__":
    main()