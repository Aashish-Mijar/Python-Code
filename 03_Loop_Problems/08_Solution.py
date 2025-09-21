number = int(input("Enter a number:\t"))

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
      
            
else:
    print("Enter number greater than 1.")

print(is_prime)