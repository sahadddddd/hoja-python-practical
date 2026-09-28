class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print("area:",self.length * self.width)

    def perimeter(self):
        print("perimeter:",2 *(self.length + self.width))

r1=rectangle(8,6)
r1.area()
r1.perimeter()
