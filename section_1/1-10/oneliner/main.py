# Subchapter 1: Welcome message
print(f"Welcome to FizzBuzz!")

def calculate_fizzbuzz (number: int): 
    return ("Fizz"*(number%3==0) + "Buzz"*(number%7==0)) or str(number)

def fizzBuzz(numbers: int):
    for i in range(1 , numbers + 1): 
        print(f"{calculate_fizzbuzz(i)}")
number = fizzBuzz(numbers = int(input()))