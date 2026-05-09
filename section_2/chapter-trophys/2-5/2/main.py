products = ["Apples","Bananas","Milk","Bread","Eggs"]
quantities = {"Bananas":30,"Milk":10,"Bread":20}

def check_inventory(products: list, quantities: dict):
    if products:
        if "Apples" in products:
            print("Apples are in stock.")
        if "Oranges" not in products:
            print("Oranges are not in stock.")
    if quantities:
        if "Bananas" in quantities:
            print("Bananas quantity is tracked.")
        if "Grapes" not in quantities:
            print("Grapes quantity is not tracked.")

check_inventory(products, quantities)