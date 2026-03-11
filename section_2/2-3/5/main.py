def print_employee_details(employee_data):
    if employee_data:
        for employee, department in employee_data.items():
            print(f"{employee}: {department}")
    
    else: print("No data available")

employees = {"Alice": "HR", "Bob": "Engineering", "Diana": "Marketing"}

print_employee_details(employees)