#1
welcome_screen = str("Bill Split Calculator")
print(f'{welcome_screen}')

#2
#print(f'Please. Type your billing amount:')
bill_amount = float(input())
#print(f'Please. Type the tip that you will spare:')
tip_percentaje = float(input())

#3
tip_amount = float(tip_percentaje / 100) * bill_amount
total_amount = bill_amount + tip_amount

#4
split_percentaje = int(input())
split_total_amount = (total_amount / split_percentaje)

#5
print(f'Total (including tip): ${total_amount}')
print(f'Each person pays: ${split_total_amount}')
