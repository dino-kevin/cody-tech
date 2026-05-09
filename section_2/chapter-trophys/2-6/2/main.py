def append_element(list1: list, element_to_append: int):
    list1.append(element_to_append)
    return list1

def remove_element(list1: list, index_to_remove: int):
    if index_to_remove in list1:
        list1.pop(index_to_remove)
    return list1


def manage_list(list1, element_to_append, index_to_remove):
    list1 = append_element(list1, element_to_append)
    list1 = remove_element(list1, index_to_remove)
    if len(list1) > 3:
        return "The list has more than 3 elements"
    else:
        return "The list has 3 or fewer elements"
    # return list1

"""def check_elements(list1: list):
    if len(list1) > 3:
        return "The list has more than 3 elements"
    else:
        return "The list has 3 or fewer elements"
"""