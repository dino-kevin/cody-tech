# Platform example

# sales = eval(input())
# starting_cash = eval(input())

# Write code here
def sum_cash(sales: list, starting_cash: int):
    total_cash = sum(sales, starting_cash)
    return total_cash

# Running example:
sales = [100, 200, 150, 300]
starting_cash = 50
print(sum_cash(sales, starting_cash))
