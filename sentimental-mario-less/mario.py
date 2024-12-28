
x = None
while x is None or x < 1 or x > 8:
    x = input("Height: ")
    if x.isdigit():
        x = int(x)
        if x < 1 or x > 8:
            print("Invalid number! Please enter a number between 1 and 8.")
            x = None
    else:
        print("That's not a number! Please enter a numerical value.")
        x = None

for i in range(x):
    for j in range(x - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("#", end="")
    print()
