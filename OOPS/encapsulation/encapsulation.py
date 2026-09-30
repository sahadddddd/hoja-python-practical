class demo():
    def __init__(self):
        self.public_var="iam public"
        self._protected_var="iam protected"
        self.__private_var="iam private"

    def show(self):
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)

    def get_private(self):
        return self.__private_var


    
#public variable printeyyan
obj=demo()
print(obj.public_var)
print(obj._protected_var)
print(obj.get_private())
#print(obj.__private_var)#cannot accessible directly from outside
