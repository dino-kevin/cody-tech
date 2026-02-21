lst = input().split(",")
# Write your code below

def filter_lst(lst, lenght):
    lst_to_filter = []
    for word in lst:
        if (len(word)) > lenght:
            lst_to_filter.append(word)
    return lst_to_filter

filtered_lst=filter_lst(lst, 5)
print(filtered_lst)