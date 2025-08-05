#1
a=int(input("number1="))
b=int(input("number2="))
c=int(input("number3="))
if a>b and a>c:
    large=a
    if b>a and b>c:
        large=b
else:
    large=c
print("the largest number is ",large)
#2
d=int(input("enter a number="))
if d%5==0:
    if d%11==0:
        print("the number is divisible by 5 and 11")
else:
    print(" its not divisible by 5 and 11")
#3
e=int(input("enter a number="))
if e>10:
    if e<50:
        print("its lies between 10 to 50")
else:
    print("its does not lies between 10 to 50")
#4
f=int(input("enter a number="))
if f>0:
    if f%2==0:
        print("number is postive and even")
else:
    print("number is invalid")
#match case 1
day=str(input("enter the day="))
match day:
    case "monday" |"tuesday" | "wednesday" | "thursday" | "friday":
        print("its weeday")
    case "sunday" | "saturday":
        print("its weedend")
#2
month=str(input("enter the month="))
match month:
    case "jan"|"mar"|"may"|"jul"|"aug"|"oct"|"dec":
        print("it has 31 days")
    case "apr"|"jun"|"sep"|"nov":
        print("it has 30 days")
    case "feb":
         print("it has 28 days")
#3


















         














