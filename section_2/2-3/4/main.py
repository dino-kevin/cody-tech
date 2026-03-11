employees = {"Alice": "HR", "Bob": "Engineering", "Diana": "Marketing"}

# Write code here
def check_employee(directory: dict, key: str):
    if key in directory.keys():
        return key + " is in the company."
    else:
        return key + " is not in the company."
    
print(check_employee(employees, "Alice"))
print(check_employee(employees, "John"))
