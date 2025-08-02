#      MATH AND RANDOM MODULE
#1
import math
a=int(input("enter a square number= "))
print(math.sqrt(a))
#2
b=int(input("enter the radius of circle="))
print(math.pi*b*b)
#3
c=int(input("enter the number for factorial="))
print(math.factorial(c))
#4
import random
print('the number from dice=',random.randint(1,6))
#5
import string
password=' '.join(random.choices(string.ascii_letters + string.digits, k=6))
print("new password is ",password)
#6
number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,16,17,18,19,20]
random.shuffle(number)
print("shuffled list is ",number)