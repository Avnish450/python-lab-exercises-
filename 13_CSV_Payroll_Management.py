import csv
from pathlib import Path

csv_file = Path(__file__).parent / "Data" / "payroll.csv"

name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
basic_salary = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
deduction = float(input("Enter deduction: "))

gross_salary = basic_salary + allowance
net_salary = gross_salary - deduction

file_exists = csv_file.exists()
with open(csv_file, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow([
            "Employee Name", "Employee ID", "Basic Salary",
            "Allowance", "Deduction", "Net Salary"
        ])
    writer.writerow([
        name, employee_id, basic_salary,
        allowance, deduction, net_salary
    ])

print("\nPayroll Summary")
print("Employee:", name)
print("Employee ID:", employee_id)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)
print("Payroll record saved to payroll.csv")
