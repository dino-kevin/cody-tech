text = input()
# Write your code below

def find_char(text, letter):
    count = 0
    for index, char in enumerate(text):
        if letter in char:
            count+= 1
    return count

found_char = find_char(text.lower(), "s")
print(f"{found_char}")
