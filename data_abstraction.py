## DATA ABSTRACTION ##
#1
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @ abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def area(self):
            return self.length * self.breath
    def perimeter(self):
            return 2*(self.length+self.breath)
class Circle (Shape):
    def __init__(self,radius):
        self.radius=radius
    def area (self):
            return 3.14*self.radius**2
    def perimeter (self):
            return 2*3.14*self.radius
rectangle=Rectangle(6,7)
print("area of rectangle =",rectangle.area())
print("perimeter of rectangle =",rectangle.perimeter())    

circle = Circle(4)
print("area of cicle =",circle.area())
print("perimeter of circle=",circle.perimeter())
    
#2
from abc import ABC, abstractmethod
class empolyee(ABC):
     def __init__ (self,name):
          self.name=name
     @abstractmethod
     def salary(self):
          pass
class time_worked(empolyee):
     def __init__ (self,name,time):
          super().__init__(name)
          self.time=time 
     def salary (self):
          return self.time*150
amount=time_worked("raja",6)
print("salary of ",amount.name,"=",amount.salary())     
     
     
