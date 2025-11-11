import os, time, math

for t in range(200):
    os.system('cls')
    for x in range(60):
        y = int(10 + 5 * math.sin((x + t) * 0.3))
        print(" " * y + "*")
    time.sleep(0.05)
    
