#1 RECURSION FUNCTION
def number(a):
    if a<=0:
        return
    number(a-1)
    print(a)
number(10)
#2
def number(b):
    if b>10:
        return
    number(b +1)
    print(b)
number(1)
#3
def fibonacci(n):
    if n==0:
        return 0
    elif  n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))
#4
def sum(a):
    if  len(a)==0:
        return 0
    else:    
        return a[0] + sum(a[1:])
list=[10,5,9,8,3,6,1]
result=sum(list)
print('the sum of list is',result)
#5
num=int(input("enter a number="))
def factorial(n):
    if n<0:
        return 'invalid input'
    elif  n==0:
        return 1
    else:
        return n*factorial(n-1)
result=factorial(num)
print(result)    





        










    

