def repeat_sequence(lst,repeats):
    addition_reversed_list = [lst[0]] + lst + lst[::-1] + [lst[len(lst) - 1]]
    return addition_reversed_list * repeats
    
lst = [1, 2, 3]
repeated_list = repeat_sequence(lst, 2)
print(f"{repeated_list}")

"""Contains the original list followed by its reverse
Has the first element of the original list inserted at the beginning and the last element inserted at the end
Repeats this entire sequence twice"""