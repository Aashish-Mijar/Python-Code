username = "Aashish"

# scope/namespace starts from ':'
if username == "test@":
    pass

def func():
    username = "Coffee"
    print(username)

func()
print(username)


x = 34
def func2(y):
    z = x + y
    return z

# x = 50   # Value changed 
# result = func2(5)
# print(result)

def func3():
    # This action should not be done..
    global x
    x = 90

# func3()
# print(x)

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()

def coder(num):
    def actualFunction(x):
        return x ** num
    return actualFunction

funR = coder(3)
funG = coder(2)

print(funR(3))
print(funG(5))

