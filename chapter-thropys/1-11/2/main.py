def change_element(list1, index, list2):
    if list1 != None or list2 != None:
        list1[index] = list2[0]
        return list1
    else:
        return None

list1 = [1, 2, 3, 4, 5]
list2 = [11, 12, 13, 14, 15]
print(f"{change_element(list1, 0, list2)}")

