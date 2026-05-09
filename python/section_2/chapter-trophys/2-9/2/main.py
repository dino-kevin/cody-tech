temperatures = [72, 68, 75, 80, 65, 70, 78]
humidity = [60, 55, 65, 70, 50, 58, 62]

# TODO: Find the highest and lowest temperature from the 'temperatures' list using max() and min()
def lowest_highest_temperature(temperatures: list):
    if temperatures:
        lowest_temperature = min(temperatures)
        highest_temperature = max(temperatures)
        return lowest_temperature, highest_temperature
    else:
        return None, None
# TODO: Find the highest and lowest humidity from the 'humidity' list using max() and min()
def lowest_highest_humidity(humidity: list):
    if humidity:
        lowest_humidity = min(humidity)
        highest_humidity = max(humidity)
        return lowest_humidity, highest_humidity
    else:
        return None, None

# TODO: Get highest and lowest temperature:
lowest_temperature, highest_temperature = lowest_highest_temperature(temperatures)

# TODO: Print the highest temperature. Make sure to include the degree Fahrenheit symbol (°F).
# Example format: "Highest temperature: 80°F"
print(f"Highest temperature: {highest_temperature}°F")

# TODO: Print the lowest temperature. Use the same format.
# Example format: "Lowest temperature: 65°F"
print(f"Lowest temperature: {lowest_temperature}°F")

# TODO: Get highest and lowest temperature:
lowest_humidity, highest_humidity = lowest_highest_humidity(humidity)

# TODO: Print the highest humidity. Make sure to include the percentage symbol (%).
# Example format: "Highest humidity: 70%"
print(f"Highest humidity: {highest_humidity}%")

# TODO: Print the lowest humidity. Use the same format.
# Example format: "Lowest humidity: 50%"
print(f"Lowest humidity: {lowest_humidity}%")
