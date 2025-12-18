import os
import time

width = 30
pos = 0
direction = 1

while True:
    print(" "* pos + "*")
    time.sleep(0.05)
    os.system('cls')

    pos += direction
    if pos == width or pos == 0:
        direction *= -1
        direction *= -1
    
    
