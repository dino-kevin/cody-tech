def add_to_set(set1: set, element_to_add: int):
    set1.add(element_to_add)
    return set1
def remove_to_set(set1: set, element_to_remove: int):
    set1.remove(element_to_remove)
    return set1

def check_number(set1: set, element_to_check: int):
    if element_to_check in set1:
        return "5 is in the set"
    else:
        return "5 is not in the set"

def manage_set(set1: set, element_to_add: int, element_to_remove: int):
    set1 = add_to_set(set1, element_to_add)
    set1 = remove_to_set(set1, element_to_remove)
    print(check_number(set1, 5))
    return set1

set1 = {1, 2, 3, 4}
number_to_add = 6
number_to_remove = 3

set1 = manage_set(set1, number_to_add, number_to_remove)
