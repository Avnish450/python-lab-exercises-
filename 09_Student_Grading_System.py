name = input("Enter student name: ")
marks = []

for i in range(1, 4):
    mark = float(input(f"Enter marks for subject {i} (0-100): "))
    if mark < 0 or mark > 100:
        print("Invalid marks. Enter marks between 0 and 100.")
        raise SystemExit
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
elif average >= 40:
    grade = "E"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Total Marks:", total, "/ 300")
print("Average:", round(average, 2))
print("Grade:", grade)
