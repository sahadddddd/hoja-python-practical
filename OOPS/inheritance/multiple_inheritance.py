class mother():
    def cook(self):
        print("cooking...")

class father():
    def drive(self):
        print("driving...")

class son(mother,father):
    pass

c=son()
c.drive()
c.cook()