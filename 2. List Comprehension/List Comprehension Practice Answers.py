
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
result = [char.upper() for char in s]
print(result)


''' Problem 2 '''
#Given
s = "Watermelon"
#Result: ['W', 't', 'r', 'm', 'l', 'n']  (without vowels)
result = [char for char in s if char not in "aeiouAEIOU"]
print(result)


''' Problem 3 '''
#Given
s = "Watermelon"
#Result: ['W', 'a', 't', 'e', 'r'] (first 5 characters)
result = [s[i] for i in range(5)]
print(result)


''' Problem 4 '''
#Given
s = "Watermelon"
#Result: ['n', 'o', 'l', 'e', 'm', 'r', 'e', 't', 'a', 'W'] (reverse order)
result = [s[i] for i in range(len(s)-1, -1, -1)]
print(result)