def iterate_and_filter_set(input_set):
    # Write code here
    indexed_list = [x for x in input_set if x <= 10]
    sorted_list = list(sorted(indexed_list))
    return set(sorted_list)

# Test
unsorted_set = {5, 12, 7, 15, 3, 10}
indexed_set = iterate_and_filter_set(unsorted_set)
print(indexed_set)



