n1 = int(input())
n2 = int(input())
first_div_by_7 = 0
for i in range(n1 , n2):
    if i % 2 == 0 and i > 5:
        print(f"First even number greater than 5: {i}")
        break

for i in range(n1, n2):
    if i % 7 == 0:
        first_div_by_7 = i
        break
print(f"First number divisible by 7: {first_div_by_7}")
    
