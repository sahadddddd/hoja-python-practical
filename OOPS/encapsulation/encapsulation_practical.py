#1 . Create a class with public, protected, and private variables and print each one.
class student():
    def __init__(self):
        self.name="sahad"
        self._age=21
        self.__mark=90

    def show_private(self):
        print("private:",self.__mark)

s=student()
print("public:",s.name)
print("protected:",s._age)
s.show_private()
print("---------------------")


#2 . Write a class Student where __ marks is private. Add methods to set and get marks safely.
class student():
    def __init__(self):
        self.__marks=0

    def set_marks(self,marks):
        if 0<= marks <=100:
            self.__marks=marks
            print("mark updated successfully")
        else:
            print("enter a number between 0 to 100")

    def get_marks(self):
        return self.__marks
st=student()
st.set_marks(89)
print("mark:",st.get_marks())
print("------------------------------------")
        

#3 . Create a BankAccount class with a private balance and methods to deposit and withdraw.
class bankaccount():
    def __init__(self):
        self.__balance=0

    def deposit(self,amount):
        if amount >0:
            self.__balance+=amount
            print("amount deposited successfully")
        else:
            print("enter a valid amount")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance-=amount
            print("amount withdraw successfully")
        elif amount <0:
            print("enter a valid number")
        else:
            print("insufficiant balance")

    def get_balance(self):
        return self.__balance


account=bankaccount()
account.deposit(5000)
account.withdraw(2000)
print("current balance:",account.get_balance())
print("-------------------------------------")


#4 . Make a class Car with a protected variable _speed and a method to increase speed. Access _speed from a child class.
class car():
    def __init__(self):
        self._speed=0

    def increase_speed(self,amount):
        self._speed+=amount
        print("speed increase to:",self._speed)

class sportscar(car):
    def show_speed(self):
        print("current speed:",self._speed)

car=sportscar()
car.increase_speed(50)
car.increase_speed(100)
car.show_speed()
print("-----------------------------------")


#5 . Demonstrate that private variables cannot be accessed directly but can be accessed using name mangling.
class student():
    def __init__(self):
        self.__mark=90
st=student()
try:
    print(st.__mark)
except AttributeError:
    print("private variable cannot acces directly")
print("acces using name mangling:",st._student__mark)
print("----------------------------")


#6 . Create a class with a private method __ show_secret() and call it from another public method.c
class private():
    def __show_secret(self):
        print("sahad is a billionire")

    def display(self):
        self.__show_secret()
obj=private()
obj.display()
print("----------------------------")


#7 . Build a User class where password is private and only accessible through a check_password() method.
class user():
    def __init__(self,username,password):
        self.username=username
        self.__password=password

    def check_password(self,password):
        if self.__password==password:
            print("correct password")
        else:
            print("incorrect password")
user1=user("sahad",2967)
user1.check_password(2345)
user1.check_password(2967)


#8 . Make a class where a protected method _calculate_bonus() is inherited and used by a subclass.
class employe():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def _calculate_bonus(self):
        return self.salary*0.15
class manager(employe):
    def show_details(self):
        bonus=self._calculate_bonus()
        print("employee name:",self.name)
        print("salary:",self.salary)
        print("bonus:",bonus)
m=manager("sahad",50000)
m.show_details()


#9 . Create a class that hides a private variable but updates it using setter and getter methods.
class student():
    def __init__(self,name,mark):
        self.name=name
        self.__mark=mark
    
    #getter methord
    def getter(self):
        return self.__mark
    #settermethor
    def setter(self,mark):
        if 0<=mark<=100:
            self.__mark=mark
            print("mark updated successfullu")
        else:
            ("enter valid mark between 0 to 100")
st=student('sahad',95)
print("current mark is:",st.getter())
st.setter(70)
print("updated mark mark is:",st.getter())


#10 . Write a real-world example (like ATM, Employee Salary, Game Player Stats) using encapsulation with private data.
class atm():
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def check_balance(self):
        print("account holder:",self.name)
        print("account balance:",self.__balance)

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("amount deposited successfully")
        else:
            print("enter valid amount")

    def withdraw(self,amount):
        if amount<=0:
            print("enter a valid amount")
        elif amount<=self.__balance:
            self.__balance-=amount
            print("amount withdrawn successfully")
        else:
            print("insufficiant balance")
ac=atm('sahad',5000)
ac.check_balance()   
ac.deposit(2000)
ac.check_balance()
ac.withdraw(1000)
ac.check_balance()    
