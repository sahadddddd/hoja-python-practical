square=[]
for x in range(1,6):
    square.append(x**2)
print(square)

#using list comprehension we can return code in one line
square_comp=[x**2 for x in range (1,6)]
print(square_comp)