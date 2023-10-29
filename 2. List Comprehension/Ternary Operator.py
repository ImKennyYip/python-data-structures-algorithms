
#Use Python's Ternary Operator Syntax to generate the following results
'''
Syntax: x if (condition) else y
'''

#Given
grade = int(input("Enter a student's grade: "))
if grade >= 65: #student passes
    result = "P"
else:
    result = "F"

result = "P" if grade >= 65 else "F"
print(result)


#Use Python's Comprehension Syntax to generate the following results
'''
Syntax: [val for x in iterable]
iterable refers to any iterable collection - string, list, dict, tup, set, range etc

You may also specify a condition to add the val
Syntax: [val for x in iterable if (condition)]

You may also use list comprehension with the ternary operator
Syntax: [val if (condition) else val2 for x in iterable]
'''

''' Problem 1 '''
#Given
grades = [84, 99, 55, 65, 64, 78]
#Result: ['P', 'P', 'F', 'P', 'F', 'P'] 

result = ["P" if grade >= 65 else "F" for grade in grades]
print(result)


''' Problem 2 '''
#Given
grades = [84, 99, 55, None, 65, 64, 78, None, 0] #final grades, curve by giving each grade +5
#Result: [89, 104, 60, 0,   70, 69, 83, 0,    5]

result = [grade+5 if grade is not None else 0 for grade in grades]
print(result)


