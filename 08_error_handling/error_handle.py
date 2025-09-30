# file = open('youtube.txt', 'w')

# try:
#     file.write('code and sleep')
# finally:
#     file.close()

with open('test.txt', 'w') as file:
    file.write('code and sleep')