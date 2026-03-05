def merged_List(lst1, lst2):
    merged_list = []
    merged_list = lst1
    second_list_lenght = len(lst2)
    for i in range(second_list_lenght):
        merged_list.append(lst2[i])
    merged_list.sort()
    return merged_list

def merge(lst1, lst2):
    # Write code here
        if not lst2: # [1, 2 ,3] []
            return lst1
        return merged_List(lst1, lst2) # [1, 2, 3] [6, 7 ,8] = [1, 2, 3, 6, 7, 8]
    

list_1 = [1, 2]
list_2 = [3, 4]
print(f"{merge(list_1, list_2)}")

