lst = input().split()
# Write your code below
filtered_lst = []
for index, word in enumerate(lst):
    if len(word) > 3 or word.startswith("a"):
        filtered_lst.append(index)
print(f"{filtered_lst}")      