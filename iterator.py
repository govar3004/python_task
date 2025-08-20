##  ITERATOR ##
#1
fruits=['apple','banana','cherry','kiwi','orange']
a=iter(fruits)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#2
name="GOVARADHAN"
b=iter(name)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
#3 
class Number:
    def __iter__(self):
      self.a=1
      return self
    def __next__(self):
      x=self.a
      self.a +=2
      return x
c=Number()
d=iter(c)
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
#4 stopiterator
class num:
   def __iter__(self):
      self.q =1
      return self
   def __next__(self):
      if self.q<11:
         z= self.q
         self.q+=1
         return z**2
      else:
         raise StopIteration
classs=num()
t=iter(classs)
for z in t:
   print(z)


      





