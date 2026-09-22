#class blue print
class person:

    #constructor = run when object is created
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #method=function inside class
    def greet(self):
        print("hello",self.name)

#object=created from class
p=person("sahad",21)
p1=person("sahal",22)

p.greet()
p1.greet()