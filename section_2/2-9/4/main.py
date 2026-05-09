def dictionary_sorter(data_dict: dict):
    # Use sorted() to sort the dictionary items by their values
    # Hint: data_dict.items() returns (key, value) pairs
    # Hint: Use the 'key' parameter of sorted() to sort by value
    if data_dict:
        sorted_dict = sorted(data_dict.items(), key=lambda item: item[1])
        return dict(sorted_dict)
    else:
        return {}

    # Write code here
data_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dictionary_sorter(data_dict)
print(sorted_dict)