import os, time, random

width, height = 50, 10
stars = ["." for _ in range(20)]

for _ in range(100):
    os.system('cls')
    for _ in range(10):
        print(" " * random.randint(0, width) + random.choice(stars))
    time.sleep(0.1)
