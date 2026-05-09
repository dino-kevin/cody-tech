def print_product_details(product_data:dict):
    # Write code here
    if product_data:
        for key, value in product_data.items():
            if isinstance(key,str):
                print(f"{key.capitalize()}: {value}")
            else:
                print(f"{key}: {value}")
    else:
        print("No product information available")

product_data = {"name":"Laptop","brand":"Dell","price":799.99,"stock":15}
print_product_details(product_data)