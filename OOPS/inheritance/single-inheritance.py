class animal:
    def eat(self):
        print("eating....")
class dog(animal):
    def bark(self):
        print("barking..,")

a=dog()
a.eat()
a.bark()