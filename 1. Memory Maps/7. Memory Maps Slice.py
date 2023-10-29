#slice (shallow copy)
lst1 = [1, 2, [3, 4]]
lst2 = lst1[1:]

print("lst1 =", lst1)
print("lst2 =", lst2)

lst1[2][0] = 50
lst2[1][1] = 70

print("lst1 =", lst1)
print("lst2 =", lst2)
