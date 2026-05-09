text = input()
delimiter = input()
# Write your code below

def splice_and_join_text(text, delimiter):
    split_text = text.split()
    return delimiter.join(split_text)

final_text = splice_and_join_text(text, delimiter)
print(f"{final_text}")


