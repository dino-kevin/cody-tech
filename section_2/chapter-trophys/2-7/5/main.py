def filter_and_square_set(input_set: set):
    # Write code here
    odd_squared_set = set()
    for number in input_set:
        if number % 2 == 1:
            odd_squared_set.add(number * number)
    return odd_squared_set

# Test
unfiltered_set = {1, 2, 3, 4, 5}
filtered_set = filter_and_square_set(unfiltered_set)
print(filtered_set)
