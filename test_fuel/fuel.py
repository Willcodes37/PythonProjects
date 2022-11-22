def main():
    fraction = input("fraction: ")
    percentage = convert(fraction)
    fuel_reading = gauge(percentage)
    print(fuel_reading)


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    z = x / y
    if 0 <= z <= 1:
        percent = round(z * 100)
        return percent
    elif x > y:
        raise ValueError
    elif x < 0 or y < 0:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    else:
        pass


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
