class dog():
    def speak(self):
        return "bark"
class cat():
    def speak(self):
        return "meaw"
# Polymorphism
def animal_sound(animal):
    print(animal.speak())

d=dog()
c=cat()
animal_sound(d)
animal_sound(c)

