from abc import ABC,abstractmethod
class atm(ABC):
    @abstractmethod
    def withdraw(self):
        pass

class MyBankAccount(atm):
    def withdraw(self):
        self.__verify_pin()
        self.__balance_check()
        self.__server_update()
        print("amount withdraw succefully")

    def __verify_pin(self):
        print("pin varified")
    def __balance_check(self):
            print("balance checked")
    def __server_update(self):
            print("server updated")
atm=MyBankAccount()
atm.withdraw()


