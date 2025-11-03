import os, time

width = 40
snake = "=====>"

for i in range(100):
    os.system('cls')
    print(" " * (i % width) + snake)
    time.sleep(0.05)
