def set_operations(set1, set2):
    # Calculate the union
    union_result = set1.union(set2)

    # Calculate the intersection
    intersection_result = set1.intersection(set2)

    # Calculate the difference
    difference_result = set1.difference(set2)

    # Calculate the symmetric difference
    symmetric_difference_result = set1.symmetric_difference(set2)

    # Return a dictionary containing the results
    return {
        "union": union_result,
        "intersection": intersection_result,
        "difference": difference_result,
        "symmetric_difference": symmetric_difference_result
    }

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set_operations(set1, set2))