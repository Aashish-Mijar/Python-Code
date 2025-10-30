def sum_all(*args):
    print(args)
    for i in args:
        print(i*4)
    return sum(args)

print(sum_all(1,3))
print(sum_all(1,4,5,6))
print(sum_all(2,4,6,3,7,5))
print(sum_all(4,5,3,2,9))