# myList = ["orange", "mango", "kiwi", "pineapple", "banana"]

# ---- Sort() method -----
# myList.sort()

# ---- for descending we use reverser = true
myList = [100, 30, 56, 34,89]
myList.sort(reverse = True)
print(myList)


# ----- Case sensitivity---- By default sort() is case sensitive --- Capital letters executed first
myList2 = ["copy", "Pen", "Books", "pencil", "ruler"]
# myList2.sort()

# ----- perform case-insensitive sort
myList2.sort(key = str.lower)
print(myList2)

# ------ reverse() method reverses the current sorting order of the elements.
myList3 = ["bugati", "Lamborgini", "mercides", "suzuki"]
myList3.reverse()
print(myList3)

# ------ copy list using slice operator ----
myNewList3 = myList3[:]
print(myNewList3)