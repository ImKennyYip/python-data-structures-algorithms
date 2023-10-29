'''
Write a function where, given a sorted list of integers and a target integer number

if there are two distinct numbers in the sorted list that can add up to the target, return true
otherwise, false

Input: numbers = [2, 7, 11, 15, 20, 21], target = 9
Output: True because 2 + 7 == 9

Input: numbers = [2, 7, 11, 15, 19, 20, 21], target = 26
Output: True because 11 + 15 == 26, and also 7 + 19 == 26

Input: numbers = [2, 7, 11, 15, 20, 21], target = 12
Output: False, no two numbers add up to 12

'''

# def two_sum(numbers, target): #O(n^2) 
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] + numbers[j] == target:
#                 return True
#     return False

def two_sum(numbers, target): #O(n)
    left = 0
    right = len(numbers) - 1

    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if (curr_sum == target):
            return True
        elif (curr_sum < target):
            left += 1
        elif (curr_sum > target):
            right -= 1
    
    return False

lst = [2, 7, 11, 15, 19, 20, 21]

print("Test 1:", two_sum(lst, 9))
print("Test 2:", two_sum(lst, 26))
print("Test 3:", two_sum(lst, 12))
