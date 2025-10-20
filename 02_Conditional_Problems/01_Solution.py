user_age = int(input("Enter your age:\t"))

if user_age < 13:
    print("User is child.")

elif user_age >= 13 and user_age <= 19:
    print("User is Teenager.")

elif user_age > 19 and user_age <= 59:
    print("User is Adult.")

else:
    print("USer is Senior as per his/her age.")

