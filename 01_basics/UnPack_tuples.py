fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# --- Unpacking a tuple
# (green, yellow, red) = fruits

# --- assign the rest of the values as a list called "red"
(green, yellow, *red) = fruits

# ---- add a list of values the "tropic" varibles
(green, *tropic, red) = fruits

print(green)
# print(yellow)
print(tropic)
print(red)
