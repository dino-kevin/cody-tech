# Required variables
PI = 3.14159
radius = int(input())

# Create the function to calculate the area of a circle
def calculate_circle_area(PI, radius):
    area = PI * radius ** 2
    return area

# Call the function
new_area = calculate_circle_area(PI, radius)
print(f"{new_area}")
