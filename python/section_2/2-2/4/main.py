def update_employee_info(employee_dict, key, value):
    # Write code here
    employee_dict[key] = value
    return employee_dict


new_dict = {"name": "Alice", "age": 30, "department": "HR"}
key = "name"
value = "Bob"
updated_dict = update_employee_info(new_dict, key, value)
print(updated_dict)