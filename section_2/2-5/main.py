# Write code here
number = float(input())
places = int(input())

def round_number_by_places(number, places):
    number = round(number, places)
    return number

rounded_number = round_number_by_places(number, places)
print(rounded_number)
