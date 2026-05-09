def analyze_grades(grades):
    if grades:
        analyze_dict = {}
        average_grade = sum(grades.values()) / len(grades.values())
        rounded_average_grade = round(average_grade, 2)
        lowest_grade = min(grades.values())
        highest_grade = max(grades.values())
        lowest_student_grade = list(grades.keys())[list(grades.values()).index(lowest_grade)]
        highest_student_grade = list(grades.keys())[list(grades.values()).index(highest_grade)]
        analyze_dict = {'average': rounded_average_grade, 'highest': highest_grade, 'lowest': lowest_grade, 'top_student': highest_student_grade, 'bottom_student': lowest_student_grade}
        return analyze_dict
    else:
        return {}

# Test the function
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
result = analyze_grades(student_grades)
print(result)