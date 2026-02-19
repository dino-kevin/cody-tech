def change_element(list1, index, list2):
    if list1 != None or list2 != None:
        list1[index] = list2[0]
        return list1
    else:
        return None