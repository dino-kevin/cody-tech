group1 = {"Alice", "Bob", "Charlie", "Diana"}
group2 = {"Bob", "Charlie", "Eve"}
group3 = {"Charlie", "Frank", "Bob"}


# Write your code below
intersection_result = group1.intersection(group2, group3)
difference_result = group1.difference(group2, group3)

# Print the results
print("Members in all groups:", sorted(list(intersection_result)))
print("Unique members in group1:", sorted(list(difference_result)))