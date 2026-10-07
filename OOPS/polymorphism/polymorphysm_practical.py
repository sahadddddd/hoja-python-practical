# Q1. Create two classes Car and Bike, both having a method start(). Call the same method for both objects and observe the different outputs.
class car:
    def start(self):
        print("car start with key")
class bike:
    def start(self):
        print("bike start with self")
car=car()
bike=bike()
car.start()
bike.start()        


# Q2. Create a parent class Animal with a method sound(). Create two subclasses Lion and Elephant that override sound(). Print the sound of each animal using a loop.
class animal:
    def sound(self):
        pass
class elephant(animal):
    def sound(self):
        print("elephant trumpet")
class lion(animal):
    def sound(self):
        print("lion roar")

animal=[elephant(),lion()]

for i in animal:
    i.sound()


# Q3. Write a function show_area(shape) that calls shape.area(). Create classes Square and Circle with their own area() methods and test the function.
import math
class square:
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius*self.radius
def show_area(shape):
    print("area:",shape.area())
square=square(5)
circle=circle(7)
show_area(square)
show_area(circle)
        

# Q4. Create a class EnglishGreeting with a method greet() returning "Hello". Create a class SpanishGreeting returning "Hola". Write afunction that accepts any greeting object and calls greet().
class EnglishGreeting:
    def greet(self):
        return "hello"
class SpanishGreeting:
    def greet(self):
        return "hola"
def show_greeting(greeting):
    print(greeting.greet())

englsh=EnglishGreeting()
spanish=SpanishGreeting()
show_greeting(englsh)
show_greeting(spanish)


# Q5. Use the built-in function len() with different data types-string, list, tuple-and identify how built-in polymorphism works.
name = "Sahad"
numbers = [10, 20, 30, 40]
marks = (80, 90, 75)

print(len(name))
print(len(numbers))
print(len(marks))


# Q6. Create a class Laptop with a method price(). Create two subclasses GamingLaptop and BusinessLaptop overriding price(). Print prices using polymorphism.
class laptop:
    def price(self):
        pass
class gaminglaptop(laptop):
    def price(self):
        return("gaming laptop price:100000")
class businesslaptop(laptop):
    def price(self):
        return("business laptop price:90000")
laptop=[gaminglaptop(),businesslaptop()]
for l in laptop:
    print(l.price())


# Q7. Make classes Dog, Cat, and Cow with a speak() method. Store objects in a list and call speak() inside a loop.
class Dog:
    def speak(self):
        print("Dog says: Woof")

class Cat:
    def speak(self):
        print("Cat says: Meow")

class Cow:
    def speak(self):
        print("Cow says: Moo")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()


# Q8. Create a class Shape with a method draw(). Override it in subclasses Triangle and Circle. Demonstrate polymorphism by calling draw() on each.
class Shape:
    def draw(self):
        pass


class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")


class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")


shapes = [Triangle(), Circle()]

for shape in shapes:
    shape.draw()


# Q9. Write a function that receives any object with a show() method. Create two classes with different show() behaviors and use them with the function.
class Student:
    def show(self):
        print("This is a Student")


class Teacher:
    def show(self):
        print("This is a Teacher")


def display(obj):
    obj.show()


student = Student()
teacher = Teacher()

display(student)
display(teacher)


# Q10. Create classes PDFReader and ImageViewer, each having an open() method. Call open() for both objects and observe polymorphism.
class PDFReader:
    def open(self):
        print("Opening PDF file")


class ImageViewer:
    def open(self):
        print("Opening image file")


pdf = PDFReader()
image = ImageViewer()

pdf.open()
image.open()