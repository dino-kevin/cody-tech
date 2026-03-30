# This program checks if the memory object is the same within the 'is' statement
list1 = [1, 2, 3]
list2 = list1

# list2 has the same memory object, it should return True
print(list1 is list2)
# Although list2 has now the same value as list1;
list2 = [1, 2, 3]
# It doesn't have the same memory object, that's why it should return False
print(list1 is list2)