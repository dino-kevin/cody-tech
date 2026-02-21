numbers = input().split(',')
# Write your code below
def even_lst(lst_numbers):
    numbers = [int(number) for number in lst_numbers]
    sum_of_numbers = 0
    for number in numbers:
        if number % 2 == 0:
            sum_of_numbers+= number
    return sum_of_numbers


even_sum_lst = even_lst(numbers)
print(f"{even_sum_lst}")   
    