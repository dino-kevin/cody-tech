lst = list(map(int, input().split(",")))
print(f"List before filtering{lst}")
number_lst = []
for i, number in enumerate(lst):
    if number <= 50 or number % 5 == 0:
        number_lst.append(i)
print(f"After filtering: {number_lst}")
