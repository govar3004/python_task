#1
num=[2,3,4,5,28]
square=list(map(lambda x: x*x,num))
print(square)
#2
string=['apple','banana','berry','cherry']
capital=list(map(lambda x: x.upper(),string))
print(capital)
#3
number=[2,5,7,8,4,40]
add_num=list(map(lambda x: x+10,number))
print(add_num)
#4
num=[2,3,4,5,28]
double=list(map(lambda x: x*2,num))
print(double)
#5
fruits=['strawberry','kiwi','orange','watermelon']
first_letter=list(map(lambda x: x.capitalize(), fruits))
print(first_letter)
#6
num=[2,3,4,5,6,7,8]
odd=list(filter(lambda x: x%2!=0,num))
print(odd)
#7
fruits=['strawberry','kiwi','lem','orange','watermelon','app',]
four=list(filter(lambda x: len(x)>=5,fruits))
print(four)
#8
number=[2,54,7,89,4,40,12,9,3]
add_num=list(filter(lambda x: x<10 ,number))
print(add_num)
#9
fruits=['strawberry','kiwi','lemon','grape','orange','watermelon']
word=list(filter(lambda x: 'a' not in x, fruits))
print(word)
#10
number=[3,4,6,9,12,17,20,24,27,31]
divisible=list(filter(lambda x: x % 3 !=0 ,number))
print(divisible)
#11
intger=[2,-7,5,-9,4,3,-12,40]
negative=list(filter(lambda x: x>0 ,intger))
print(negative)
#12     SAME AS 10
#13
from functools import reduce
num=[2,3,4,5,28]
product=reduce(lambda x,y: x*y,num)
print(product)
#14

string=[ 'python',' ','rule',' ', 'the',' ','world','!!!']
concaterate=reduce(lambda x,y: x+y ,string )
print(concaterate)
#15

number=[2,54,7,89,4,40,12,9,3]
largest=reduce(lambda x,y: x if x>y else y,number)
print(largest)
#16

num=[2,3,4,5,8]
sum_square=reduce(lambda x,y:   x+y **2 ,num)
print(sum_square)
#17
n=int(input('enter anumber='))
factorial=reduce(lambda x,y:  x*y, range(1,n+1))
print(factorial)












\



  

