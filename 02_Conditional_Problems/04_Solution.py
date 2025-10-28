fruit = input("Enter fruit:\t")
color = input("Enter color of fruit:\t")

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")
else:
    print("For now just for Banana....")