order_size = input("Enter your order size:\t")
extra_shot = input("Extra shot(espresso) Y/N:\t")

if extra_shot == 'Y':
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee with no extra shot"

print(coffee)