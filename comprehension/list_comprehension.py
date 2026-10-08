square=[]
for x in range(1,6):
    square.append(x**2)
print(square)

#using list comprehension we can return code in one line
square_comp=[x**2 for x in range (1,6)]
print(square_comp)

#even numbers
even_num=[x for x in range(1,7)if x%2 ==0]
print(even_num)

#with string
letters=[ch.upper() for ch in "hello"]
print(letters)