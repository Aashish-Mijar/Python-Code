list1 = ["a", "b", "c"]
list2 = [1,2,3]

# list3 = list1+list2
# print(list3)

# ---- append() method----
for x in list2:
    list1.append(x)

# print(list1)

# ----- extend() method, where the purpose is to add elements from one list to another list:

list1.extend(list2)
print(list1)
# print(list2)
print(list2)