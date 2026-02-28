#lst = input().split(",")
# Write your code below
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def triple_list(lst: list):
    if lst:
        result_lst = []
        result_lst = lst[1::3]
        return result_lst

def sixth_list(lst:list):
    if lst:
        result_lst = []
        result_lst = lst[0:6]
        result_lst.reverse()
        return result_lst

def second_list(lst: list):
    if lst:
        lst_length = len(lst)
        lst_index = (lst_length // 2)
        result_list = []
        result_list = lst[lst_index::2]
        return result_list
    

print(triple_list(lst))
print(sixth_list(lst))
print(second_list(lst))

"""A list containing every third element, starting from index 1 (the second element)
A list containing all the elements from the 6th element to the 1st in reverse order
A list containing every second element starting from the middle of the list to the end"""