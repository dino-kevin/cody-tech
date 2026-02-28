lst = (input().split(","))
# Write your code below
def slice_lst(lst: list):
    lst_length = len(lst)
    lst_index = (len(lst) // 2)
    if lst_length % 2 == 0:
        return lst[(lst_index -1):(lst_index + 1):1]
    elif lst_length % 2 != 0:
        return lst[(lst_index -1):(lst_index + 2):1]
    else:
        return lst

print(slice_lst(lst))

"""
#First code result, the uncommented is the optimal
lst = list(input().split(","))
# Write your code below
def slice_lst(lst):
    lst_lenght = len(lst)
    lst_final = []
    if lst_lenght % 2 == 0:
        lst_final.append(lst[(lst_lenght//2) - 1])
        lst_final.append(lst[(lst_lenght//2)])
        
    elif lst_lenght > 1:
        lst_final.append(lst[(lst_lenght//2) - 1])
        lst_final.append(lst[lst_lenght//2])
        lst_final.append(lst[(lst_lenght//2) + 1])
    else:
        return lst
    return lst_final
#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(slice_lst(lst))
"""