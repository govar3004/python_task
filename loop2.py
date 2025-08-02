#11
for a in range(10,21):
    if  a > 1:
        for i in range(2,a):
            if a % i==0:
              break
print(a)
#12
num=[32,76,4,64,28,93]
largest=num[0]
for b in num:
    if b > largest:
        largest=b
print("the largest number=",largest)
#13    
a="apple"
vowel_count=0
for text in a:
    if text.lower() in["a","e","i","o","u"]:
        vowel_count +=1
print("the number of vowel=",vowel_count)
#14
product=1
for i in range(1,6):
    product*=i
print("answer=",product)
#15
product=1
while True:
  num=int(input("enter a number(0 )="))
  if num==0:
       break
  product *=num
    
print("answer=",product)
#16
sum=0
while True:
    num=int(input("enter a number(-)="))
    if num<0:
        break
    sum+=num
print("answer=",sum)
        
    
    

