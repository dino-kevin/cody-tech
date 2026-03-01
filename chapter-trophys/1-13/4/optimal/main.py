def not_mutual_friends(list1:list, list2:list):
    # Write your code below
    if list1 and list2:
        set1 = set(list1)
        set2 = set(list2)
        not_mutual_set = sorted(set1 ^ set2)
        not_mutual_list = list(not_mutual_set)
        return not_mutual_list
    elif list1 and not list2:
        return list1
    else:
        return []

omar_friends = ["John", "Emma", "Mike", "Sarah"]
mike_friends = ["Emma", "Tom", "Sarah", "Peter"]

not_friends_from_mutual = not_mutual_friends(omar_friends, mike_friends)
print(f"{not_friends_from_mutual}")
