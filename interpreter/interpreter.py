expression = input("Expression: ")

x, y, z = expression.split(" ")

x = round(float(x), 1)
z = round(float(z), 1)

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
else:
    print(x / z)
