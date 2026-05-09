# Get input for rows and columns
rows = int(input())
cols = int(input())

# Write your nested loops here
# Outer loop for rows
for i in range (rows):
    # Inner loop for columns
    row = ""
    for j in range (cols):
        row += "*"
    print(row)
  

          