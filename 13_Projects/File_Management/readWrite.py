# Writing content in file
# file = open('sample.txt', 'w')
# file.write("Hello! This is python")
# file.close()

file = open('/sample.txt', 'r')
content = file.read()
file.close()
print(f"Content of file is : {content}")