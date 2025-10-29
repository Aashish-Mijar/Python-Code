tea_shop = {
    "Chiya": {"Masala":"Spicy", "Ginger": "Zesty"},
    "Tea": {"Green":"Mild", "Black":"Strong"}
}

print(tea_shop["Chiya"]["Masala"])

# --- comprehensive list comprehension in dict
squared_num = {x: x**2 for x in range(10)}
print(squared_num)
