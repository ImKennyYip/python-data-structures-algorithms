
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
#Generate a List containing letters A-Z all uppercase (use chr(i) to convert number to ASCII)
#Result: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
result = [chr(i) for i in range(65, 91)]
print(result)


''' Problem 2 '''
#Generate a list containing the following integers
#Result: [1, 2, 4, 8, 16, 32, 64, 128]
result = [2**i for i in range(8)]
print(result)


''' Problem 3 '''
#Generate a list containing the following integers
#Result: [1, 22, 333, 4444, 55555]
result = [int(str(i)*i) for i in range(1, 6)]
print(result)


''' Problem 4 '''
#Given
s = "Watermelon"
#Generate a list containing the characters of s, where all chars at even indices are lower case
#and all chars at odd indices are upper case. Hint: Use the ternary operator.
#Result: ['w', 'A', 't', 'E', 'r', 'M', 'e', 'L', 'o', 'N']
result = [s[i].lower() if i%2 == 0 else s[i].upper() for i in range(len(s))]
print(result)


''' Problem 5 '''
#Given
s = input("Enter a word")
#Generate a list containing the characters of s (user-input) repeated twice
#DO NOT USE ANY MATH OPERATORS: MULTIPLY s*2 or ADD s+s!
#s = "Python"
#Result: ['P', 'y', 't', 'h', 'o', 'n', 'P', 'y', 't', 'h', 'o', 'n']
#s = "Java"
#Result: ['J', 'a', 'v', 'a', 'J', 'a', 'v', 'a']
result = [s[i] for i in range(-len(s), len(s))]
print(result)

'''
len("Python") = 6
-6, 6 <- stop at 6

0    1  2   3  4   5  
P    y  t   h  o   n
-6  -5 -4  -3 -2  -1
'''