#Q1 . Create a list of squares for numbers from 1 to 10 using list comprehension.
sq=[x**2 for x in range(1,11)]
print(sq)


#Q2 . Generate a list of even numbers between 1 and 20 using list comprehension.
even_num=[x for x in range(1,21) if x%2==0]
print(even_num)


#Q3 . From the string "programming", make a list of unique letters using set comprehension.
ch="programming"
unique_letters={i for i in ch}
print(unique_letters)


#Q4 . Make a dictionary where keys are numbers 1 to 5 and values are their cubes using dictionary comprehension.
cube={x:x**3 for x in range(1,6) }
print(cube)


#Q5 . Convert a list of words ["apple", "banana", "cherry"] into a list of their lengths using list comprehension.
words=["apple", "banana", "cherry"]
length=[len(i) for i in words]
print(length)


#Q6 . Use set comprehension to create a set of even squares from [1, 2, 3, 4, 5, 6].
num=[1, 2, 3, 4, 5, 6]
even={x**2 for x in num if x%2==0}
print(even)


#Q7 . Make a dictionary that stores each character and its ASCII value for the word "hello".
word="hello"
result={ch:ord(ch) for ch in word}
print(result)


#Q8 . Create a list of numbers from 1-30 that are divisible by both 2 and 3 using list comprehension.
lis=[x for x in range (1,31) if x%2==0 and x%3==0]
print(lis)


#Q9. Flatten the nested list [[1, 2], [3,4], [5,6]] using a nested list comprehension.
list=[[1, 2], [3,4], [5,6]]
flat=[]

#Q10 Convert the tuple (1, 2, 3, 4, 5) into a generator that yields each number squared,then convert it to a tuple and print it.

