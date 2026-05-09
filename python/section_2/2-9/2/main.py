numbers = [42, 17, 23, 56, 9, 34]
words = ["kiwi", "apple", "banana", "cherry", "date"]

def min_max_numbers (numbers: list):
    if numbers:
        min_number = min(numbers)
        max_number = max(numbers)
        return min_number, max_number
    else:
        return []

def min_max_words (words: list):
    if words:
        min_words = min(words)
        max_words = max(words)
        return min_words, max_words
    else:
        return []

min_number, max_number = min_max_numbers(numbers)
print(f"Smallest number: {min_number}")
print(f"Largest number: {max_number}")
min_word, max_word = min_max_words(words)
print(f"Smallest word: {min_word}")
print(f"Largest word: {max_word}")