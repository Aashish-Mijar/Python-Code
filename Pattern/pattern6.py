import os, time

width = 40
pos = 0
direction = 1

while True:
    os.system('cls')
    print(" " * pos + "O")  # The ball
    time.sleep(0.05)
    pos += direction
    if pos == 0 or pos == width:
        direction *= -1
        direction *= -1