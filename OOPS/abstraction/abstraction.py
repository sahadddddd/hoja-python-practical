from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        return "woof"
class cat(animal):
    def sound(self):
        return "meaw"
d=dog()
c=cat()
print(d.sound())
print(c.sound())
