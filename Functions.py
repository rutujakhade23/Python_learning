def hello():
    print("hello")

hello()

def sum(a,b):
    s = a+b
    return s
print(sum(3,5))

def sum(a, b=1):
    return a + b
print(sum(5))

sum = lambda a,b: a+b
print(sum(4,5))