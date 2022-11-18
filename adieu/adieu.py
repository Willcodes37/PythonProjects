import inflect

p = inflect.engine()

Names = []

try:
    while True:
        n = input("Name: ")
        Names.append(n)

except EOFError:
    Name_list = p.join(Names)
    if len(Names) == 1:
        print(f"Adieu, adieu, to {Names[0]}")
    elif len(Names) == 2:
        print(f"Adieu, adieu, to {Names[0]} and {Names[1]}")
    else:
        print(f"Adieu, adieu, to {Name_list}")