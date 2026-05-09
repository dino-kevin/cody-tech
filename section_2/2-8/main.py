student_records = {}

def add_student(name: str, age: int, courses: list):
    if name in student_records:
        print(f"Student '{name}' already exists.")
        return student_records
    else:
        courses_set = set(courses)
        student_records[name] = {"age": age, "grades": set(), "courses": courses_set}
        print(f"Student '{name}' added successfully.")
        return student_records

def add_grade(name: str, grade: int):
    if name in student_records:
        student_records[name]['grades'].add(grade)
        print(f"Grade {grade} added for student '{name}'.")
    else:
        print(f"Student '{name}' not found.")

def is_enrolled (name: str, course: str):
    if name in student_records:
        if course in student_records[name]['courses']:
            return True
        else:
            return False
    else:
        print(f"Student '{name}' not found.")
        return False

def calculate_average_grade (name: str):
    if name in student_records:
        if student_records[name]['grades']:
            average_grade = sum(student_records[name]['grades']) / len(student_records[name]['grades'])
            return average_grade
        else:
            return 0
    else:
        print(f"Student '{name}' not found.")

def list_students_by_course (course: str):
    students_in_course = []
    for name in student_records:
        if course in student_records[name]['courses']:
            students_in_course.append(name)
    if students_in_course:
        return students_in_course
    else:
        return []

def filter_top_students (threshold: float):
    top_students = []
    for name in student_records:
        average_grade = calculate_average_grade(name)
        if average_grade >= threshold:
            top_students.append(name)
    if top_students:
        return top_students
    else:
        return []

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list