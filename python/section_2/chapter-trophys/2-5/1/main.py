temperature = float(input())
warning = "Normal" if round(temperature, 1) <= 30 else "Hot"
print(warning)