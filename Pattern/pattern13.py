import os, time

text = ">>> Python Animation Rocks! <<<"

for i in range(50):
    os.system('cls')
    print(" " * (i % 30) + text)
    time.sleep(0.1)
    
