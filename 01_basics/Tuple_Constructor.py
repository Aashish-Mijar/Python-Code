thisTuple = tuple(("Aashish", "Meera", "Dipisha"))
print(thisTuple)
print(thisTuple[-1])

# ------ Return third, fourth and fifth item
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# ------ Return items from the beginning to, but NOT included, "kiwi":
print(thistuple[:4])

# ------ Return items from "cherry" and to the end:
print(thistuple[2:])

# ----- Return the items from index -4 (included) to index -1 (excluded)
print(thistuple[-4:-1])