#  OOP(OBJECT AND CLASS)
class bank:
    def account(self,account_number,account_name,balance):
        self.account_number= account_number
        self.account_name= account_name
        self.balance= balance

    def details(self):
        print("Account Number=", self.account_number )
        print("Account Name=", self.account_name )
        print("Balance=$",self.balance)
    
    def deposit(self,amount):
        self.balance+=amount
        print("Deposit=$",amount)

    def withdraw(self,amount):
        if amount>self.balance :
            print("less balance")
            print("Balance=$",self.balance)
        else:
            self.balance -=amount
            print("withdraw=$",amount)

account1= bank()
account1.account(101,"aurna",20000)

account2= bank()
account2.account(102,'bala',100000)

account3= bank()
account3.account(103,"charles",1500)

account2.details()
 
account2.withdraw(50000)
account2.details()

account3.details() 

account3.deposit(200)
account3.details()
 
 
