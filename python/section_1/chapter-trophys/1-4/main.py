# Initialize variables
is_sunny = True
temperature = 25
wind_speed = 10
water_temperature = 22

# Calculate conditions
can_go_hiking = all ([is_sunny, temperature > 15, wind_speed < 20])
can_go_swimming = all ([is_sunny, temperature > 20, water_temperature > 18])
cannot_go_outside = any ([not is_sunny or temperature < 10 or wind_speed > 30])

# Don't delete the lines below
print("Can go hiking:", can_go_hiking)
print("Can go swimming:", can_go_swimming)
print("Cannot go outside:", cannot_go_outside)
