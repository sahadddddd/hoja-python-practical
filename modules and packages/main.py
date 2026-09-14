import utility
from my_package import calculator,greeter

print(utility.greet('alice'))
print(utility.add(10,30))

print(greeter.say_hello("sahad"))

added=calculator.add(100,200)
print('add:',added)

sub=calculator.substract(added,20)
print('sub:',sub)