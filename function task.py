#1     FUNCTION TASK
def my_function(a):
    return a*a
print(my_function(4))
print(my_function(9))
print(my_function(17))
print(my_function(5))
#2
def area(lenght,width):
    print(lenght*width)
area(2,4)
area(8,20)
#3
def number(a):
    if a%2==0:
        print("it even",a)
    else :
        print("its odd",a)
number(a=5)
number(8)
#4
def number(a):
    if a <2:
         print("its not a prime number",a)
         return
    for i in range(2,int(a**0.5)+1):
            if a % i ==0:
                print("it is not a prime number",a)
                return
    print("its  a prime number",a)
number(13)
number(26)
#5
def string(a):
    return  ' '. join(reversed(a))
print(string(a='apple'))
#6
import math
def function(a):
    if a <0:
        return'the factorial is not for negative number'
    else:
        return math.factorial(a)
num = 8
print('the factorial=',function(num))
#7
def function(a):
    return a*a
b= function(4)
c=function(9)
d=function(7)
e=function(5)  
def square_num():
    return b+c+d+e
print('the sum of square=',square_num())
#8
def function(text):

    s=str(text)
    reversed_s=s[::-1]
    if  s== reversed_s:
        print('true')
    else:
        print('false')
print(function('madam'))
#9
def function(a):
    if  a%4==0:
        print('true')
    else:
       print('false')
print(function(2000))
#10
def function(x):
    if x < 0:
        return false
    number =str(x)
    num_digit=len(number)
    sum_of_power=0
    for a in number:
        digit=int(a)
        sum_of_power+=digit**num_digit
    return sum_of_power==x
print(function(153))









