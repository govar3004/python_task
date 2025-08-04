#exception handling
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
    "age":"six",
    "school":"petit",
    "std":3,
    "hobby":"painting"
}
try:
    a=int(input('enter the password='))
    12345==details
    print('you enter password is',a)
except ValueError:
    print(invalid)
else:
    print(details)



