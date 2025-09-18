# ------ List Constructor ------
# thisList = list(("apple", "banana", '"cherry'))
# print(thisList)

thisList = ["apple", "banana", "cherry"]
# thisList[1] = "blackcurrant"
# thisList[1:3]= ["durian", "watermelon"]

# ------ Delete the list completely -----
# del thisList

# ------ Clear() method empties the list
# thisList.clear()
# print(thisList)

for x in thisList:
    print(x)

# ----- Loop through the index numbers -----
for i in range(len(thisList)):
    print(thisList[i])

# ---- Loop using While ----
i = 0
while i < len(thisList):
    print(thisList[i])
    i = i + 1

# ----- Looping using list comprehension ----
[print(x) for x in thisList]