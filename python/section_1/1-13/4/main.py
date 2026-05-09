#lst1 = input().split(",")
#lst2 = input().split(",")
# Write your code below
lst1 = [1,2,3,4,5]
lst2 = [2,4,1,8,9]

def splice_lists(lst1, lst2):
    if lst1 and lst2:
        spliced_list = []
        for i in lst1:
            if i not in lst2:
                spliced_list.append(i)
        return spliced_list
    else:
        return None

spliced_list = splice_lists(lst1, lst2)
print(f"{spliced_list}")




"""Create a program that receives two lists and prints a new list of all elements that are in the first list but NOT in the second list."""