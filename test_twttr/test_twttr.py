def main():
    word = input("Input: ")
    word_shortened = shorten(word)
    print(F"Output: {word_shortened}")


def shorten(x):
    omitted = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    output = ""

    for letter in x:
        if letter not in omitted:
            output += letter
        else:
            letter.replace(letter, "")

    return output


if __name__ == "__main__":
    main()
