number = int(input("Enter number to find table of:\t"))

for i in range(1, 11):
    if i == 5:
        continue
    else:
        print(f"{number} x {i} = {number*i}")