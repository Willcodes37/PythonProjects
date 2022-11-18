x = input("camelCase: ")

snake_case = ""

for letter in x:
    if letter.islower():
        snake_case += letter
    else:
        ll = letter.lower()
        snake_case += "_"
        snake_case += ll

print(F"snake_case: {snake_case}")
