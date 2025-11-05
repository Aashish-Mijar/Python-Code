import os
import time

heart = [
    " **   ** ",
    "*  * *  *",
    "*   *   *",
    " *     * ",
    "  *   *  ",
    "   * *   ",
    "    *    "
]
for shift in range(20):
    os.system('cls')
    for line in heart:
        print(" " * shift + line)
    time.sleep(0.1)
    time.sleep(0.1)


