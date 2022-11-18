while True:
    try:

        Fraction = input("Fraction: ")
        x, z = Fraction.split("/")
        xx = int(x)
        zz = int(z)
        total = round((xx / zz) * 100)
        if xx > zz:
            pass
        elif total >= 99:
            print("F")
            break
        elif total <= 1:
            print("E")
            break
        else:
            print(f"{total}%")
            break

    except ValueError:
        pass

    except ZeroDivisionError:
        pass

    