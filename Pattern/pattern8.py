import sys, time

spinner = ['|', '/', '-', '\\']
for _ in range(50):
    for frame in spinner:
        sys.stdout.write('\rLoading... ' + frame)
        sys.stdout.flush()
        time.sleep(0.1)
