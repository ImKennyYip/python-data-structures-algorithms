
#functions

def func1(s):
    s = s.lower()
    print("Inside function s =", s)

s = "PYTHON"
func1(s)
print("Outside function s =", s)



def func2(lst):
    lst.append(100)
    lst = [3, 6, 12]
    print("Inside function lst =", lst)

lst = [1, 5]
func2(lst)
print("Outside function l =", lst)

