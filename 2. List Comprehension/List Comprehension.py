
#Use Python's Comprehension Syntax to generate the following results
'''
Syntax: [val for x in iterable]
iterable refers to any iterable collection - string, list, dict, tup, set, range etc

You may also specify a condition to add the val
Syntax: [val for x in iterable if (condition)]
'''

''' Problem 1 '''
#Result: [1, 2, 3, 4, 5, 6]
result = [i for i in range(1, 7)]
print(result)


''' Problem 2 '''
#Result: [1, 4, 9, 16, 25, 36] (squares of 1 to 6)
result = [i*i for i in range(1, 7)] 
print(result)


''' Problem 3 '''
#Given
lst = [-1, 10, -5, -2, 3, -4]

#Result: [1, 10, 5, 2, 3, 4] (absolute value of all elem in lst)
result = [abs(elem) for elem in lst]
print(result) 


''' Problem 4 '''
#Given
lst = [-1, 10, -5, -2, 3, -4]

#Result: [-1, -5, -2, -4] (all negative values in lst)
result = [elem for elem in lst if elem < 0]
print(result)


''' Problem 5 '''
#Given
lst = [-1, 10, -5, -2, 3, -4]

#Result: 13 (sum of all positive values in lst)
result = sum([elem for elem in lst if elem > 0])
print(result)


''' Problem 6 '''
#Given
lst = [1, 4, 5, 8, 10]

#Result: [2, 3, 6, 7, 9] (values from 1 to 10 if value not in lst)
result = [i for i in range(1, 10) if i not in lst]
print(result)
