# Create a program that accepts marks of five subjects and
# calculates Total, Average, Grade, and Pass/Fail.
# Input:
# English
# Maths
# Science
# Social
# Computer
# Output:
# Total Marks : 435
# Average : 87
# Grade : A
# Result : PASS
# Functions to Create:
# get_marks()
# calculate_total()
# calculate_average()
# find_grade()
# display_result()
# Grade Rules:
# 90-100 +A+
# 80-89 -A
# 70-79 +B
# 60-69-C
# 50-59 -D
# Below 50 - Fail
def get_marks():
    subjects=['english','maths','science','social','computer']
    marks=[]
    for subject in subjects:
        mark=float(input(f'enter the {subject} mark:'))
        marks.append(mark)
    return marks

def calculate_total(marks):
    total=sum(marks)
    return total
def calculate_average(total):
    average=total/len(marks)
    return average

def find_grade(average):
    if average >=90:
        grade='A+'
    elif average >=80:
        grade='A'
    elif average >=70:
        grade='B'
    elif average >=60:
        grade='C'
    elif average >=50:
        grade='D'
    else:
        grade='fail'

    return grade
def display_result(total,average,grade):
    print('________________ ')
    print(f'Total Mark:{total}')
    print(f'Average:{average}')
    print(f'Grade:{grade}')

    if average >=50:
        print('Result:Pass')
    else:
        print('Result:Fail')

marks=get_marks()
total=calculate_total(marks)
average=calculate_average(total)
grade=find_grade(average)
display_result(total, average, grade)