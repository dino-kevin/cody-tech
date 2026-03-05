def create_student_dict(name, age, major):
    # Write code here
    new_dictionary = {"name": name, "age": age, "major": major}
    return new_dictionary

major_students = create_student_dict("Alice", 20, "Computer Science")
print(f"{major_students}")
