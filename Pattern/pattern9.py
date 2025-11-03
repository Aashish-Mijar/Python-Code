import os, time

heart1 = [
    " **   ** ",
    "*  * *  *",
    "*   *   *",
    " *     * ",
    "  *   *  ",
    "   * *   ",
    "    *    "
]

heart2 = [
    " *** *** ",
    "*   *   *",
    "*       *",
    " *     * ",
    "  *   *  ",
    "   * *   ",
    "    *    "
]

for i in range(20):
    os.system('cls')
    for line in (heart1 if i % 2 == 0 else heart2):
        print(line)
    time.sleep(0.3)
