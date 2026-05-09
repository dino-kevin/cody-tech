# Subchapter 1: Welcome message
print(f"Welcome to FizzBuzz!")

def calculate_fizzbuzz_twisted (number: int):
    number_to_string = str(number)
    result = ""
    result = ("Fizz"*(number%3==0) + "Buzz"*(number%7==0))
    if result == "":
        if "3" in number_to_string: #or "7" in number_to_string:
            result = "Almost Fizz"
        else:
            result = number_to_string
    return result

def fizzBuzz(numbers: int):
    for i in range(1 , numbers + 1): 
        print(f"{calculate_fizzbuzz_twisted(i)}")

number = fizzBuzz(numbers = int(input())
