input_list = input().split(', ')
# Write your code below
def slice_list(input_list: list):
    list_length = len(input_list)
    sliced_list = []
    if list_length > 4:
        sliced_list = input_list[0:2:1] + input_list[(list_length -2)::1]
        
    elif list_length <= 4:
        sliced_list = input_list[0:1:1] + input_list[(list_length -1)::1]

    else: 
        return input_list    
    return sliced_list

print(slice_list(input_list))