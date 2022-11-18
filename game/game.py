import random
import sys

level = None
guess = None

while level is None:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
while guess is None:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass

rn = random.randint(1, level)

while True:
    if rn == guess:
        print("Just right!")
        sys.exit()
    elif rn < guess:
        try:
            print("Too large!")
            guess = int(input("Guess: "))
        except ValueError:
            pass
    elif rn > guess:
        try:
            print("Too small!")
            guess = int(input("Guess: "))
        except ValueError:
            pass
    else:
        pass
