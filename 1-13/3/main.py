def create_pattern(numbers:list, repeats:int):
    # Write your code here
    if numbers and repeats:
        combined_list = numbers + numbers
        repeated_list = combined_list * repeats
        return repeated_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
repeats = 2
repeated_list = create_pattern(numbers, repeats)
print(f"{repeated_list}")
