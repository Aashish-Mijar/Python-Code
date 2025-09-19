user_age = int(input("Enter your age:\t"))
day = "Wednesday"

price = 12 if user_age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price-=2

print("Ticket price for you is $",price)