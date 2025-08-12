class animal():
    def __init__(self,name,food):
        self.name=name
        self.food=food
class lion(animal):
    def __init__ (self,name,food,color,habit):
        super().__init__(name,food)
        self.color=color
        self.habit=habit

my_lion=lion("raja","carinvores","golden yellow","forest")
print(f"my lion name is {my_lion.name} and it lives in {my_lion.habit}")
print (f"it eats meat so its {my_lion.food} and it has {my_lion.color} hair around its body")



