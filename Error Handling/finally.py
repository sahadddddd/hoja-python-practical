try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("enter a valid number")
except ZeroDivisionError:
    print('cannot devided by zero')
else:
    print('code run successfully!')
finally:
    print("program ended,thankyou......")