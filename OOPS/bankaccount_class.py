class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("new balance:",self.balance)

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            print("new balance:",self.balance)
        else:
            print("insufficiant balance")

account1=bankaccount('sahad',5000)
account1.deposit(2000)
account1.withdraw(1000)