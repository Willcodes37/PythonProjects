x = input("Input: ")
Omitted = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
Output = ""

for letter in x:
    if letter not in Omitted:
        Output += letter
    else:
        letter.replace(letter, "")

print(F"Output: {Output}")
