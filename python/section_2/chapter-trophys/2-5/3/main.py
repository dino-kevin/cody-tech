def compare_strings(str1: str, str2: str):
    if str1 and str2:
        final_dict = {}
        final_dict["is_substring"] = True if str1 in str2 else False
        final_dict["starts_with"] = True if str2.startswith(str1) else False
        final_dict["ends_with"] = True if str2.endswith(str1) else False
        final_dict["is_equal"] = True if str1.lower() == str2.lower() else False
        return final_dict

# Example to test the code
"""
str1 = "world"
str2 = "hello world"
dict1 = compare_strings(str1, str2)
print(dict1)
"""