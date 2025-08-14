## POLYMORPHISM  ##
# 1 # COMPILE TIME POLYMORPHISM #
class calculator:
    def add(self,a=7,b=3,*args):
        result=a+b
        for num in args:
            result+=num
        return result

cal=calculator()

print(cal.add())
print(cal.add(1,9))
print('--------------------')
# 2 # RUNTIME POLYMORPHISM #
class Bank:
    def balance(self):
        return "more amount"
class John(Bank):
    def balance(self):
        return 1000000
class Rani(Bank):
    def balance (self):
        return 1
Banks=[John(),Rani(),Bank()]
for person in Banks:
    print(person.balance())
print('------------------')
# 3 # POLYMORPHISM IN BUILT IN FUNCTION #
print(len("POLYMORPHISM IN BUILT IN FUNCTION"))
print(len([34,56,78,23,98,76,93]))
print(max(34,56,78,23,98,76,93))
print(max('POLYMORPHISM IN BUILT IN FUNCTION'))
print('------------------')
# 4 # POLYMORPHISM IN FUNCTION #
class lion:
    def walk (self):
        return "run"
class eagle:
    def walk (self):
        return "fly"
def activite(tool):
    print(tool.walk())

activite(lion())
activite(eagle())
