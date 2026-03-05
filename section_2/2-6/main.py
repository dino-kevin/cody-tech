# Write code here
new_tuple = (10, 20, 30)
new_string = "python"
new_ranged_tuple = range(1, 6)

def convert_data_type_into_list(data):
    return list(data)

list1 = convert_data_type_into_list(new_tuple)
list2 = convert_data_type_into_list(new_string)
list3 = convert_data_type_into_list(new_ranged_tuple)

print(list1)
print(list2)
print(list3)
