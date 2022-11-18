Amount_Due = 50

Change_Owed = int()

while True:
    if Amount_Due <= 0:
        print("Change Owed: " + str(abs(Change_Owed + Amount_Due)))
        break
    print(f"Amount Due: {Amount_Due}")
    x = int(input("Insert Coin: "))
    if x == 25:
        Amount_Due -= x
    elif x == 10:
        Amount_Due -= x
    elif x == 5:
        Amount_Due -= x
    else:
        pass
