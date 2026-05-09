def find_occurrences(text: str, pattern: str):
    # Write your code here
    is_ocurrence_found = False
    positions = []
    for i, val in enumerate(text):
        if text[i:i+len(pattern)] == pattern: 
            positions.append(i)
            is_ocurrence_found = True
    return (is_ocurrence_found, len(positions), positions)
    
# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)