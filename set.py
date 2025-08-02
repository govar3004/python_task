#       SET
#1 union   
fruit1={'apple','cherry','kiwi'}
fruit2={'banana','berry','mango'}
fruit=fruit1|fruit2
print(fruit)
#2 update
fruit={'apple','cherry','kiwi'}
fruit.update(['mango'])
print(fruit)
#3  intersection
fruit1={'apple','cherry','kiwi','mango','banana'}
fruit2={'banana','berry','mango'}
fruit=fruit1&fruit2
print(fruit)
#4   intersection_update
num1={1,2,3,7,8}
num2={2,3,4,5,6,7}
num1.intersection_update(num2)
print(num1)
#5    difference
fruit1={'apple','cherry','kiwi','mango','banana'}
fruit2={'banana','berry','mango'}
fruit=fruit1-fruit2
print(fruit)
#6   difference_update
num1={1,2,3,7,8}
num2={2,3,4,5,6,7}
num1-=num2
print(num1)
#7   symmteric_difference
fruit1={'apple','cherry','kiwi','berry'}
fruit2={'banana','berry','mango','apple'}
fruit=fruit1^fruit2
print(fruit)
#8   symmteric_difference_update
fruit1={'apple','cherry','kiwi','mango','banana'}
fruit2={'banana','berry','mango'}
fruit1^=fruit2
print(fruit1)
#9   issubset
fruit2={'banana','mango'}
fruit1={'apple','cherry','kiwi','mango','banana'}
result=fruit1<fruit2
print(result)
#10  issuperset
fruit1={'apple','cherry','kiwi','mango','banana'}
fruit2={'banana','mango'}
result=fruit1>=fruit2
print(result)











