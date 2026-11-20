import math

print("Area Calculator")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
choice = input("Choose a shape (1-3): ")

if choice == "1":
    radius = float(input("Enter radius: "))
    print("Area of circle:", round(math.pi * radius * radius, 2))
elif choice == "2":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area of rectangle:", length * width)
elif choice == "3":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of triangle:", 0.5 * base * height)
else:
    print("Invalid choice")
