#Binary Search

def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid  #or you can return True
        elif lst[mid] < target:
            left = mid + 1
        else: #lst[mid] > target:
            right = mid - 1
    
    return None #or you can return False

lst = [-6, -2, 0, 5, 7, 10, 27]
print("TEST 1: ", binary_search(lst, 10)) #IN THE LST
print("TEST 2: ", binary_search(lst, -6)) #IN THE LST
print("TEST 3: ", binary_search(lst, 15)) #NOT IN THE LST
print("TEST 4: ", binary_search(lst, 99)) #NOT IN THE LST

lst2 = ["cpp", "java", "javascript", "kotlin", "python", "ruby", "swift"]
print("TEST 5: ", binary_search(lst2, "java"))  #IN THE LST
print("TEST 6: ", binary_search(lst2, "go"))    #NOT IN THE LST
