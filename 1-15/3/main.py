prices = input().split(",")
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input().split(",")
budget_per_item = int(input())

items_prices = dict(zip(items, prices))

affordable_items = []
cant_afford = 0
total_needed = 0

# Write your code below
def check_affordable_items(items_prices, budget_per_item):
    affordable = []
    cant_afford_count = 0
    total_needed = 0
    
    for item, price in items_prices.items():
        if price <= budget_per_item:
            affordable.append(item)
            total_needed += price
        else:
            cant_afford_count += 1
    
    return affordable, cant_afford_count, total_needed

affordable_items, cant_afford, total_needed = check_affordable_items(items_prices, budget_per_item)

print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)