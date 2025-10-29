# ------ Converting tuple into a list 
x = ("apple", "banana", "cherry")
y = list(x)

# ---- It changes index 1 with kiwi
# y[1] = "kiwi"

# ---- append --
y.append("orange")
y.remove("apple")
x = tuple(y)
print(x)

print(x)