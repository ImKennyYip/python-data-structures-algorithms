#strings and lists

#1
s1 = "PYTHON"
s1.lower()       
s2 = s1.lower()  

print("s1 =", s1)
print("s2 =", s2)


#2
lst1 = [10, 15, 20]
lst2 = lst1
lst1.append(25) 
lst2[0] = 100   

print("lst1 =", lst1)
print("lst2 =", lst2)


#3
s1 = "PYTHON"
lst1 = [10, 15, 20]
lst2 = [lst1, s1]
s1 = s1.lower()
lst1.append(25)

print("s1 =", s1)
print("lst1 =", lst1)
print("lst2 =", lst2)

