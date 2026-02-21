# This recomendation was provided by choomtek at twitch, thank you choomtek
numbers = input().split(',') 
print(f"{sum(int(n) for n in numbers if int(n) % 2 == 0)}")
