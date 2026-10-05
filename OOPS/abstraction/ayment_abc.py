from abc import ABC ,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class upi(payment):
    def pay(self,amount):
        print("paid",amount,"using upi")

class card(payment):
    def pay(self,amount):
        print("paid",amount,"using card")

p=upi()
c=card()
p.pay(1000)
c.pay(3000)

        