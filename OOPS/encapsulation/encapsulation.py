class demo():
    def __init__(self):
        self.public_var="iam public"
        self._protected_var="iam protected"
        self.__private_var="iam private"

    def show(self):
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)