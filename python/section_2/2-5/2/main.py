# Given data
names = ["Alice", "Bob", "Charlie"]
grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

# Check if the names provided are within the names list
def is_name_in_the_list(names: list, name: str):
    if name in names:
        return f"{name} is in the list."
    else:
        return f"{name} is not in the list."

# Check if the names provided are within the grades dict by key
def is_name_in_the_dict(grades: dict, name: str):
    if name in grades:
        return f"{name} is in the dictionary."
    else:
        return f"{name} is not in the dictionary."

# Results
print(is_name_in_the_list(names, "Alice"))
print(is_name_in_the_list(names, "David"))

print(is_name_in_the_dict(grades, "Bob"))
print(is_name_in_the_dict(grades, "Eve"))
