#            exception handling
#1

try:
    a=int(input("enter a number 1="))
    b=int(input("enter a number2="))
    result=a/b
except ValueError:
    print('input is not a number')
except ZeroDivisionError:
    print('input is invalid')
else:
    print("answer",result)    

#2
try:
    a=float(input('enter a number:'))
    result=int(a)
except ValueError:
    print('it is not a number')
else:
    print('the intger is =',result)
#3    
details={
    "name":"john",
    "age":6,
    "school":"petit",
    "std":3,
    "hobby":"painting"
}
password=12345
try:
    a=int(input('enter the password='))
    print('you enter password is',a)
    if  password==a:
      print(details)
    else:
       print("incorrect password")
except ValueError:
    print('invalid' )
#4
try:
    a=int(input('enter even number'))
    if a%2==0 :
        print('the number is even=',a)
    else:
        print("invalid")
except ValueError:
    print("its value error")
#5
try:
    a=int(input("enter your age="))
except:
    print("invalid number")
else:
    if a<=0:
     print("age cannot be in negative")
    else:
     print("your age is",a)
#6
try:
    a=int(input("enter a number1="))
    b=int(input("enter a number2="))
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
except ZeroDivisionError:
    print("we cannot divide 0")
except ValueError:
    print("invalid")
except FloatingPointError:
    print("invalid , enter a intger")
except:
    print("another number")
else:
    print("addition=",add)
    print("subtract=",sub)
    print("division=",div)
    print("multipy =",mul)



