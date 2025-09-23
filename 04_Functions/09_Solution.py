def even_generator(limit):
    li = []
    for i in range(2, limit + 1, 2):
        # print(i)
        yield i

# print(even_generator(30))
for num in even_generator(30):
    print(num)

