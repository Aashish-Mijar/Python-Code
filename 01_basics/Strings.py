name = "Aashish Mijar"

# ----- String Methods -----
# print(name.lower())
# print(name.upper())

# ----- Strip method
txt = "   Not done   "
# print(txt.strip())

# ----- replace method
# print(txt.replace("done", "should be done").strip())

hobbies = "Drawing, Reading, Listening"
# ------ String to List----
# print(hobbies.split())
# print(hobbies.split(", "))
# print(hobbies.find("Listening"))

tarif = "wah wah wah kasto ramro"
# print(tarif.count("wah"))

chiya = "Ginger milk tea"
quantity = 3
order = "I ordered {} cups of {} chiya"
# print(order.format(quantity, chiya))

food_variety = ['Pizza', 'Burger', 'Mo:Mo']
# ------ List to string
# print(" ".join(food_variety))

# ------ length of string ----
print(len(food_variety))

for letter in food_variety:
    print(letter)

# ----- r method
tea = "Masala\ntea"
# print(tea)   # print in next line

tea = r"Masala\ntea"
print(tea)   # print as it is

path = r"c:\\user\\files\\"  # if put '\' in last gives error but '\\' won't give error
# print(path)

# ---- contain ----
print("files" in path)


