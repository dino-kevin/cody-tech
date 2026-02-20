def reverse(lst):
    # Write code here
    reversed_list = (lst)
    reversed_list = reversed_list[::-1]
    return (reversed_list)

list_numbers = [1, 2, 3, 4, 5, 6]
reversed_list = reverse(list_numbers)
print(f"{reversed_list}")

