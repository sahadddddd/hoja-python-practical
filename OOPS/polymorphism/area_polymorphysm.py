class shape():
    def area(self):
        pass
class circle(shape):
    def area(self):
        return 3.14*5*5
class square(shape):
    def area(self):
        return 8*4

#polymorphism
shape=[circle(),square()]
for s in shape:
    print(s.area())