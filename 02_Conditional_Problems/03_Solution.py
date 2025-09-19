score = int(input("Enter your score:\t"))

if score >= 100:
    print("Please verify your grade again.")

    # Or exit() can be used instead of else block
else:
    if score >=90:
        grade = "A"

    elif score >=80:
        grade = "B"

    elif score >= 70:
        grade = "C"

    elif score >= 60:
        grade = "D"

    else:
        grade = "F"

    print("Grade: ", grade)