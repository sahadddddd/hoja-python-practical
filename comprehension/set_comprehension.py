numbers=[1,2,3,4,5,6,6]
unique_numbers={x**2 for x in numbers}
print(unique_numbers)

#even numbers
even_num={x for x in numbers if x %2==0}
print(even_num)