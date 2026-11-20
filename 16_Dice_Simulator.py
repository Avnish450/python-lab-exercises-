import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()

    if choice == "y":
        result = random.randint(1, 6)
        print("You rolled:", result)
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Please enter y or n.")
