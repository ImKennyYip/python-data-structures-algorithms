# Space Complexity
'''
Write a function that takes in a list of values and returns True if the list is a palindrome
and False if not. A palindrome is a sequence that reads the same forward and backward.

ex) [1, 2, 3, 2, 1] returns True because it is the same forward and backward
ex) [5, 5, 5, 5] returns True because it is the same forward and backward
ex) [1, 2, 4, 2] returns False since if read backwards, it is [2, 4, 2, 1], and therefore, not the same
'''

def reverse(lst): #O(N) runtime, O(1) space
    left = 0
    right = len(lst) - 1
    while left < right:
        temp = lst[left]
        lst[left] = lst[right]
        lst[right] = temp

        left += 1
        right -= 1
    
    return lst

def reverse2(lst):
    n = len(lst)
    for i in range(n//2):
        temp = lst[i]
        lst[i] = lst[n-1-i]
        lst[n-1-i] = temp
    return lst



def is_palindrome(lst): #O(N) runtime, O(1) space
    left = 0
    right = len(lst) - 1
    while left < right:
        if (lst[left] != lst[right]):
            return False
        left += 1
        right -= 1

    return True

def is_palindrome2(lst):
    n = len(lst)
    for i in range(n//2):
        if (lst[i] != lst[n-1-i]):
            return False
    return True
        

# def is_palindrome(lst): #O(N)
#     lst2 = lst.copy()   #O(N) runtime, O(N) space
#     lst2.reverse()      #O(N)
#     return lst == lst2  #O(N)


print("TEST 1: ", is_palindrome2([1, 2, 3, 2, 1]))
print("TEST 2: ", is_palindrome2([5, 5, 5, 5]))
print("TEST 3: ", is_palindrome2([1, 2, 4, 2]))