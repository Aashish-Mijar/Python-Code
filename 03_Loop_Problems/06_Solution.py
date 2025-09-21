fact_number = int(input("Enter a number to find factorial:\t"))
factorial = 1

while fact_number > 0:
    factorial = factorial * fact_number
    fact_number = fact_number-1

print(factorial)