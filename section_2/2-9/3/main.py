# Starter inputs
numbers = [5, 3, 8, 1, 2]
words = ["elephant", "cat", "dolphin", "bee"]

# Task 1: Sort numbers in ascending order and in descending order
def ascending_descending_sorted_numbers(numbers: list):
    if numbers:
        ascending_numbers = sorted(numbers, reverse=False)
        descending_numbers = sorted(numbers, reverse=True)
        return ascending_numbers, descending_numbers
    else:
        return [], []
# Task 2: Sort words alphabetically and sort words by length
def alphabetical_length_sorted_words(words: list):
    if words:
        alphabetical_words = sorted(words, reverse=False)
        length_sorted_words = sorted(words, key=len)
        return alphabetical_words, length_sorted_words
    else:
        return [], []

# Replace 'pass' with your code for each task
ascending_numbers, descending_numbers = ascending_descending_sorted_numbers(numbers)
alphabetical_words, length_sorted_words = alphabetical_length_sorted_words(words)

# Print the results
print("Ascending:", ascending_numbers)
print("Descending:", descending_numbers)
print("Alphabetical:", alphabetical_words)
print("By Length:", length_sorted_words)