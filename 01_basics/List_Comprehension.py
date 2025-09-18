squared_nums = [x**2 for x in range(10)]
# print(squared_nums)

cube_nums = [x**3 for x in range(5)]
# print(cube_nums)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newList = [x for x in fruits if "a" in x]

# newList = [x for x in fruits if x != "apple"]
# print(newList)

rangeList = [x for x in range(10)]
newRangeList = [ x for x in range(10) if x < 5]
print(rangeList)
print(newRangeList)

# newList = [ x.upper() for x in fruits]
newList = ["hello" for x in fruits]
print(newList)