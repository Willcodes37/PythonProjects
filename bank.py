x = input("Greeting: ").strip()

if x.startswith("Hello"):
    print("$0")
elif x.startswith("H"):
    print("$20")
else:
    print("$100")
