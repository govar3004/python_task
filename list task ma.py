#1 LIST TASK
fruit=['apple','mango','cherry','banana']
fruit.reverse()
print(fruit)
#2
number=[1,-7,6,8,-2,-9,-3,-4,5]
negative =[ num for num in number if num < 0]
a=len('negative ')
print('number of negative number in the list =',a)
postive =[ num for num in number if num > 0]
b=len('postive ')
print('number of postive number in the list =',b)
#3
list=[ a for a in range(0,31,3)]
print(list)
#4
number=[1,2,.3,5,3,6,2,3,7,2,5,4,8,3]
a=number.count(2)
print(a)
#5
num=[1,0,3,5,0,6,9,0,1,0]
remove_element=0
while remove_element in num:
    num.remove(remove_element)
print(num)
#6
number=[1,-7,6,8,-2,-9,-3,-4,5]
for i in range(number):
    if l















