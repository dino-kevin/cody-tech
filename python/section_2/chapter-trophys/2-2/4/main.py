def update_inventory(inventory_dict: dict, item: str, quantity: int):
    # Write code here
    if item in inventory_dict:
        inventory_dict[item]+= quantity
    else:
        inventory_dict[item] = quantity
    return inventory_dict

inventory_dict = {"apples":50,"bananas":30}
item = "apples"
quantity = 20

# Testing the function within an existing item
inventory_dict = update_inventory(inventory_dict, item, quantity)
print(f"{inventory_dict}")
# Placing a new item into the dictionary
item = "strawberry"
quantity = 40
inventory_dict = update_inventory(inventory_dict, item, quantity)
print(f"{inventory_dict}")


    
