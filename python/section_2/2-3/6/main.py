def frequency_counter(data_list: list):
    # Write code here
    counter_dict = {}
    unique_attribute = list(set(data_list))
    for repeated_attribute in unique_attribute:
        count = sum(1 for value in data_list if value == repeated_attribute)
        counter_dict[repeated_attribute] = count
    return counter_dict    
data_to_count = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency_counter = frequency_counter(data_to_count)
print(frequency_counter)