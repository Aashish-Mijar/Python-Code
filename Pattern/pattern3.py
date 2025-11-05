import os
import time

n = 5
for k in range(20):  # Number of moves
    os.system('cls')
    print("\n" * (k % 10))  # moves down
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    time.sleep(0.2)
    time.sleep(0.2)
