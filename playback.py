import random


def main():
    level = get_level()
    x1, y1 = generate_integer(level)
    z1 = x1 + y1
    wrong_answers = []
    wrong_guesses1 = 0
    while True:
        a1 = input(f"{x1} + {y1} = ").strip()
        if str(z1) == a1:
            break
        else:
            print("EEE")
            wrong_guesses1 += 1
            if wrong_guesses1 == 3:
                print(f"{x1} + {y1} = {z1}")
                wrong_answers.append("q1")
                break

    x2, y2 = generate_integer(level)
    z2 = x2 + y2
    wrong_guesses2 = 0
    while True:
        a2 = input(f"{x2} + {y2} = ").strip()
        if str(z2) == a2:
            break
        else:
            print("EEE")
            wrong_guesses2 += 1
            if wrong_guesses1 == 3:
                print(f"{x2} + {y2} = {z2}")
                wrong_answers.append("q2")
                break

    x3, y3 = generate_integer(level)
    z3 = x3 + y3
    wrong_guesses3 = 0
    while True:
        a3 = input(f"{x3} + {y3} = ").strip()
        if str(z3) == a3:
            break
        else:
            print("EEE")
            wrong_guesses3 += 1
            if wrong_guesses3 == 3:
                print(f"{x3} + {y3} = {z3}")
                wrong_answers.append("q3")
                break
    x4, y4 = generate_integer(level)
    z4 = x4 + y4
    wrong_guesses4 = 0
    while True:
        a4 = input(f"{x4} + {y4} = ").strip()
        if str(z4) == a4:
            break
        else:
            print("EEE")
            wrong_guesses4 += 1
            if wrong_guesses4 == 3:
                print(f"{x4} + {y4} = {z4}")
                wrong_answers.append("q4")
                break
    x5, y5 = generate_integer(level)
    z5 = x5 + y5
    wrong_guesses5 = 0
    while True:
        a5 = input(f"{x5} + {y5} = ").strip()
        if str(z5) == a5:
            break
        else:
            print("EEE")
            wrong_guesses5 += 1
            if wrong_guesses5 == 3:
                print(f"{x5} + {y5} = {z5}")
                wrong_answers.append("q5")
                break
    x6, y6 = generate_integer(level)
    z6 = x6 + y6
    wrong_guesses6 = 0
    while True:
        a6 = input(f"{x6} + {y6} = ").strip()
        if str(z6) == a6:
            break
        else:
            print("EEE")
            wrong_guesses6 += 1
            if wrong_guesses6 == 3:
                print(f"{x6} + {y6} = {z6}")
                wrong_answers.append("q6")
                break
    x7, y7 = generate_integer(level)
    z7 = x7 + y7
    wrong_guesses7 = 0
    while True:
        a7 = input(f"{x7} + {y7} = ").strip()
        if str(z7) == a7:
            break
        else:
            print("EEE")
            wrong_guesses7 += 1
            if wrong_guesses7 == 3:
                print(f"{x7} + {y7} = {z7}")
                wrong_answers.append("q7")
                break
    x8, y8 = generate_integer(level)
    z8 = x8 + y8
    wrong_guesses8 = 0
    while True:
        a8 = input(f"{x8} + {y8} = ").strip()
        if str(z8) == a8:
            break
        else:
            print("EEE")
            wrong_guesses8 += 1
            if wrong_guesses8 == 3:
                print(f"{x8} + {y8} = {z8}")
                wrong_answers.append("q8")
                break
    x9, y9 = generate_integer(level)
    z9 = x9 + y9
    wrong_guesses9 = 0
    while True:
        a9 = input(f"{x9} + {y9} = ").strip()
        if str(z9) == a9:
            break
        else:
            print("EEE")
            wrong_guesses9 += 1
            if wrong_guesses9 == 3:
                print(f"{x9} + {y9} = {z9}")
                wrong_answers.append("q9")
                break
    x10, y10 = generate_integer(level)
    z10 = x10 + y10
    wrong_guesses10 = 0
    while True:
        a10 = input(f"{x10} + {y10} = ").strip()
        if str(z10) == a10:
            break
        else:
            print("EEE")
            wrong_guesses10 += 1
            if wrong_guesses10 == 3:
                print(f"{x10} + {y10} = {z10}")
                wrong_answers.append("q10")
                break

    print("Score: " + str(10 - len(wrong_answers)))


def get_level():
    while True:
        level = input("Level: ")
        if level == "1" or level == "2" or level == "3":
            lvl = int(level)
            return lvl
        else:
            pass


def generate_integer(level):
    if level == 1:
        x_number = random.randint(0, 9)
        y_number = random.randint(0, 9)
        return x_number, y_number
    elif level == 2:
        x_number = random.randint(10, 99)
        y_number = random.randint(10, 99)
        return x_number, y_number
    else:
        x_number = random.randint(100, 999)
        y_number = random.randint(100, 999)
        return x_number, y_number


if __name__ == "__main__":
    main()