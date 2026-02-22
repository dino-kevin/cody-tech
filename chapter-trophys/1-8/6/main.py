# Get input from user
start = int(input())
end = int(input())
step = int(input())

# Write your for loop here

for i in range (start, end, step):
    print(i)

"""
One liner within a dictionary
print(f"{[start for start in range(start, end, step)]}")
"""
