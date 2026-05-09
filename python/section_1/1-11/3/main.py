def change_element(lst, index, new_element):
    if lst != None:
        lst[index] = new_element
        return lst
    else:
        return None

lst = [1, 2, 3, 4, 5]
print(f"{change_element(lst, 2, 4)}")
