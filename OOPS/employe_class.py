class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print("name:",self.name)
        print("salary:",self.salary)

emp1=employee("sahad",5000000)
emp1.display()