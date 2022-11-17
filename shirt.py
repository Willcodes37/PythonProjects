while True:
    try:
        Menu = {
                "Baja Taco": 4.00,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
                }

        total = 0

        while True:
            Item = input("Input: ").title()

            if Item in Menu:
                cost = Menu.get(Item)
                total += cost
                print(F"Total: ${total:.2f}")
            else:
                pass

    except EOFError:
        break