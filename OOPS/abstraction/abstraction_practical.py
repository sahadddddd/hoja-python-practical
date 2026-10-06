# Q1. Write an abstract class Vehicle with an abstract method start(). Create Car and Bike classes that implement it.
from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        return "car started"
class bike(vehicle):
    def start(self):
        return "bike started"

c=car()
b=bike()
print(c.start())
print(b.start())


# Q2. Create an abstract class Payment with a method pay(). Implement it in CardPayment and UPIPayment.
from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def methord_pay(self):
        pass
class card_pay(payment):
    def methord_pay(self):
        print("payment done through card")
class upi_pay(payment):
    def methord_pay(self):
        print("payment done through upi")

card=card_pay()
upi=upi_pay()
card.methord_pay()
upi.methord_pay()


# Q3.Make an abstract class Device with a method boot(). Hide internal steps like __ load_os() and__ check_hardware() inside boot().
from abc import ABC,abstractmethod
class device(ABC):
    @abstractmethod
    def boot(self):
        pass
class computer(device):
    def __check_hardware(self):
        print("hardware loading")
    
    def __load_os(self):
        print("loading operating system")
    
    def boot(self):
        self.__check_hardware()
        self.__load_os()
        print("device booted sussfully")
c=computer()
c.boot()
print("---------------")


# Q4. Create a non-abstract version of the same program and compare readability.
class Device:

    def boot(self):
        self.__check_hardware()
        self.__load_os()
        print("Device booted successfully")

    def __check_hardware(self):
        print("Hardware loading")

    def __load_os(self):
        print("Loading operating system")

class Computer(Device):
    pass
c = Computer()
c.boot()


# Q5. Create an abstract class Account with a method calculate_interest(). Subclasses: SavingAccount,CurrentAccount.
from abc import ABC,abstractmethod
class account(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass
class savingaccount(account):
    def __init__(self,balance):
        self.balance=balance
    def calculate_interest(self):
        rate=5
        time=1
        interest=(self.balance*rate*time)/100
        print("saving account interest :",interest)
class currentaccount(account):
    def __init__(self,balance):
        self.balance=balance
    def calculate_interest(self):
        rate=2
        time=1
        interest=(self.balance*rate*time)/100
        print("current account interest :",interest)
saving=savingaccount(50000)
current=currentaccount(35000)
saving.calculate_interest()
current.calculate_interest()
        


# Q6. Create an abstract class LoginSystem with login(). Inside login, call private methods like __ verify_user() and__ check_password().
from abc import ABC,abstractmethod
class LoginSystem(ABC):
    @abstractmethod
    def login(self):
        pass

class userlogin(LoginSystem):
    def __varify_user(self):
        print("varifying user...")
    def __check_password(self):
        print("checking password...")
    def login(self):
        self.__varify_user()
        self.__check_password()
        print("login succesfull")
user=userlogin()
user.login()


# Q7. Build a simple CoffeeMachine class where internal steps (grind beans, heat water, brew) are hidden inside make_coffee().
class CoffeeMachine:

    def __grind_beans(self):
        print("Grinding coffee beans...")

    def __heat_water(self):
        print("Heating water...")

    def __brew(self):
        print("Brewing coffee...")

    def make_coffee(self):
        self.__grind_beans()
        self.__heat_water()
        self.__brew()
        print("Coffee is ready!")


# Creating object
coffee = CoffeeMachine()
# Making coffee
coffee.make_coffee()


# Q8. Create a Shape class with an abstract method area() and implement it in Square, Circle, Triangle.
from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Square class
class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Circle class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


# Triangle class
class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Creating objects
square = Square(5)
circle = Circle(3)
triangle = Triangle(4, 6)

print("Square area:", square.area())
print("Circle area:", circle.area())
print("Triangle area:", triangle.area())


# Q9. Make a ReportGenerator abstract class with a method generate(), hiding internal steps inside the method.
from abc import ABC, abstractmethod

class ReportGenerator(ABC):

    @abstractmethod
    def generate(self):
        pass


class SalesReport(ReportGenerator):

    def __get_data(self):
        print("Getting data...")

    def __process_data(self):
        print("Processing data...")

    def __create_report(self):
        print("Creating report...")

    def generate(self):
        self.__get_data()
        self.__process_data()
        self.__create_report()
        print("Report generated successfully!")


# Creating object
report = SalesReport()
report.generate()


# Q10.class CoffeeMachine:

    def grind_beans(self):
        print("Grinding beans...")

    def heat_water(self):
        print("Heating water...")

    def brew(self):
        print("Brewing coffee...")


coffee = CoffeeMachine()

# Wrong order
coffee.brew()
coffee.grind_beans()
coffee.heat_water()



