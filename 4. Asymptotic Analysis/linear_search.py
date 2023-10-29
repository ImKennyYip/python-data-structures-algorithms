# Linear Search
def func(lst, target):
    return target in lst

def linear_search(lst, target):
    for val in lst:
        if val == target:
            return True
    return False

def get_min(lst):
    curr_min = None

    for val in lst:
        if curr_min is None or curr_min > val:
            curr_min = val

    return curr_min

def get_max(lst):
    curr_max = None
    for val in lst:
        if curr_max is None or curr_max < val:
            curr_max = val
    
    return curr_max

def get_count(lst, target):
    count = 0
    for val in lst:
        count += val == target

    return count

lst = [11, 20, 50, 35, 47, 99, 80, 20, 99, 99, 99]

print("Min of lst: ", get_min(lst))
print("Max of lst: ", get_max(lst))

print("Count 20 of lst: ", get_count(lst, 20))
print("Count 99 of lst: ", get_count(lst, 99))

# print("Test 1: ", linear_search(lst, 20))
# print("Test 2: ", linear_search(lst, 99))
# print("Test 3: ", linear_search(lst, 1000))


