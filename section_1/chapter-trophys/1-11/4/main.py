def combine_and_filter(lst, threshold):
    # Write code here
    lst.sort() # Sorts the code from min to max
    return filter_lst(lst, threshold)
    
def filter_lst(lst, threshold):
    try: 
        filtered_lst = lst[lst.index(threshold) + 1:]
        return filtered_lst
    except:
        return []

list1 = [1, 2, 3, 4, 5, 6, 8, 9]
threshold = 5
print(combine_and_filter(list1, threshold))