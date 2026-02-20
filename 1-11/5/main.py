def prod(lst):
    # Write code here
    prod_list = get_prod_List(lst)
    return prod_list[-1]

def get_prod_List(lst):
    for i in range(len(lst) - 1):
        lst[i]*= lst[i+1]
        lst[i+1]= lst[i]
    return lst

test_list = [1, 4, 4, 2, 4, 98]
test_prod = prod(test_list)
print(f"{test_prod}")

    
