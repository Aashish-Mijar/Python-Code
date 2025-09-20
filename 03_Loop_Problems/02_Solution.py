# sum of even numbers up to given n

n = int(input("Enter value of n:\t"))

sum_even = 0

for i in range(1, n+1):
    if i%2==0:
        sum_even+=i
    
print("Sum of even numbers up to n is: ",sum_even)