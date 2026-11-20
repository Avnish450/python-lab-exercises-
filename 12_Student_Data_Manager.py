import json
from pathlib import Path

data_file = Path(__file__).parent / "Data" / "students.json"

if data_file.exists():
    with open(data_file, "r", encoding="utf-8") as file:
        students = json.load(file)
else:
    students = []

print("Student Data Manager")
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
course = input("Enter course: ")

students.append({
    "name": name,
    "roll_no": roll_no,
    "course": course
})

with open(data_file, "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

print("\nStudent record saved successfully.")
print("All Student Records:")
for student in students:
    print(
        "Name:", student["name"],
        "| Roll No:", student["roll_no"],
        "| Course:", student["course"]
    )
