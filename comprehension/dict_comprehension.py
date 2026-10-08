#square numbers as key value pair
square_numbers={x:x**2 for x in range(6)}
print(square_numbers)

#even_num square
even_num={x:x**2 for x in range(10) if x%2==0}
print(even_num)