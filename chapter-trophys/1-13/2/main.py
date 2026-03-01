original_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# Write your code below
list1 = original_list[2::4]
list2 = original_list[2:-2:]
list3 = original_list[::-2]
list4 = original_list[0:3:] + original_list[len(original_list)-3::]

# Don't change below this line
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("List 4:", list4)