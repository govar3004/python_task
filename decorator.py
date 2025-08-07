#       DECORATOR 
#1
def decorator(func):
    def wrapper():
        print("'good morning',hello!!!!")
        func()
        print("how are you?")
    return wrapper
@decorator
def a():
    print("john")

a()
#2 higher order function
def func(f,x):
    return f(x)
def multipy(x):
    return x**3
answer=func(multipy,7)
print(answer)
#3 first class object (1)
def func(n):
    return f"sweet,{n}!"
a=func
print(a("dreams"))
# frist class object (2)
def apply(f,x):
    return f(x)
ans=apply(a,"food")
print(ans)
# frist class object (3)
def good(f):
    def bad (x):
        return f/x
    return bad
a= good(15)
print(a(3))
#4 math opertaion
class MathOpertation:
    @staticmethod
    def add(x,y):
        return x + y
    @staticmethod
    def sub(x,y):
        return x-y
    @staticmethod
    def divide(x,y):
        return x/y
    @staticmethod
    def mul(x,y):
        return x*y
    @staticmethod
    def square2(y):
        return y*y
a=MathOpertation.add(5,3)
print(a)
b=MathOpertation.sub(8,4)
print(b)
c=MathOpertation.divide(20,4)
print(c)
d=MathOpertation.mul(5,6)
print(d)
e=MathOpertation.square2(9)
print(e)
