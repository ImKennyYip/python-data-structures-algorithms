#shallow copy vs deep copy

#1
lst1 = [1, 2, 3]
lst2 = lst1.copy()
lst1[0] = 10
lst2[2] = 30
print("lst1 =", lst1)
print("lst2 =", lst2)

print()

#2
lst1 = [1, 2, [3, 4]]
lst2 = lst1.copy()
lst1[0] = 10
lst2[2][0] = 30
print("lst1 =", lst1)
print("lst2 =", lst2)

print()

#3
import copy
lst1 = [1, 2, [3, 4]]
lst2 = copy.deepcopy(lst1)
lst1[0] = 10
lst2[2][0] = 30
print("lst1 =", lst1)
print("lst2 =", lst2)
