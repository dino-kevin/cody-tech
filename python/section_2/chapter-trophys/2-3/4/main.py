def check_inventory(inventory: dict, item: str):
    if item in inventory.keys():
        return item + " is in stock. Quantity: " + str(inventory[item])
    else:
        return item + " is not in stock."

inventory = {"apple":10,"banana":5,"orange":7}
item = "banana"
print(check_inventory(inventory, item))
