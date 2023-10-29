
#Use Python's Comprehension Syntax to generate the following results
'''
Syntax: [val for x in iterable]
iterable refers to any iterable collection - string, list, dict, tup, set, range etc

You may also specify a condition to add the val
Syntax: [val for x in iterable if (condition)]
'''

''' Problem 1 '''
#Given
s = "Watermelon"
#Result: ['W', 'A', 'T', 'E', 'R', 'M', 'E', 'L', 'O', 'N'] (all upper case)


''' Problem 2 '''
#Given
s = "Watermelon"
#Result: ['W', 't', 'r', 'm', 'l', 'n']  (without vowels)


''' Problem 3 '''
#Given
s = "Watermelon"
#Result: ['W', 'a', 't', 'e', 'r'] (first 5 characters)


''' Problem 4 '''
#Given
s = "Watermelon"
#Result: ['n', 'o', 'l', 'e', 'm', 'r', 'e', 't', 'a', 'W'] (reverse order)