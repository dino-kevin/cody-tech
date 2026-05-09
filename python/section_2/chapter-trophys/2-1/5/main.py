price = float(75.5)
discount_percentaje = float(10)

def calculate_discount(price, discount_percentage):
    # Write code here
    discount_amount = (price * (discount_percentage / 100))
    final_price = round(price - discount_amount, 2)
    return final_price

final_discounted_price = calculate_discount(price,discount_percentaje)
print(final_discounted_price)
