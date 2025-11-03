import os, time, math

for t in range(20):
    os.system('cls')
    radius = abs(10 - t % 20)
    for y in range(-10, 11):
        for x in range(-20, 21):
            if abs(math.sqrt(x*x + y*y) - radius) < 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    time.sleep(0.1)
