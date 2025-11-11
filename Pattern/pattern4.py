import time
import sys

spinner = ['|', '/', '-', '\\']
for _ in range(20):
    for frame in spinner:
        sys.stdout.write('\r' + frame)
        sys.stdout.flush()
        time.sleep(0.1)
        time.sleep(0.1)
