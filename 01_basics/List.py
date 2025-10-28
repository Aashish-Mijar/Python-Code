tea_varities = ["White", "Black", "Green", "Oolang"]
# print(tea_varities)
# print(tea_varities[1:])
# print(tea_varities[::-1])

# tea_varities[1:2]="Lemon"
# print(tea_varities)

tea_varities[1:2]=["Lemon"]
# print(tea_varities)

tea_varities[1:3]=["Herbal", "Strong ginger"]
# print(tea_varities)

# ---- Gives empty list
# print(tea_varities[1:1])

# ---- Insert nothing / delete---
tea_varities[1:2]=[]
# print(tea_varities)

# for tea in tea_varities:
#     print(tea, end="-->")

# if "Oolang" in tea_varities:
    # print("I have Oolang tea")


# ------ append method------
tea_varities.append("Cinnamon tea")
# print(tea_varities)

# ------ pop method --> remove last method
tea_varities.pop()
# print(tea_varities)

# ---- remove method---
# tea_varities.remove("Herbal")
# print(tea_varities)

# ------ insert method
tea_varities.insert(1, "Green tea")
print(tea_varities)

# ----- copying list in different reference -------
# tea_varities_copy = tea_varities.copy()
