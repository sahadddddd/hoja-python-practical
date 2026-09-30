class bankaccount():
    def __init__(self,balance):
        self.balance=balance

acc=bankaccount(1000)
print(acc.balance)
acc.balance-=500
print(acc.balance)