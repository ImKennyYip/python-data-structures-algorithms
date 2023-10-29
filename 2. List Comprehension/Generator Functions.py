'''
Generator functions allow you create functions that behave like iterators
This means that you could use them in a for loop.
In a normal function, you would return a value. However, in a generator function, you use the 'yield'
keyword to give a value from the function. Unlike return, yield does not end the function.
The generator function ends when there is nothing left to yield.
'''

''' Problem 1 '''
def func():
    return 5
    return 10


''' Problem 2 '''
def gen_func():
    yield 5         #1st iteration
    yield 10        #2nd iteration
    yield "Python"  #3rd iteration
    yield 100       #4th iteration




''' Problem 3 '''
def twos_power(n):
    total = 1
    while n >= 0:
        yield total
        total *= 2
        n -= 1



''' Problem 4 

Why is it that we can write the following?

for elem in lst:
    print(elem)

Because built into the list class, there is a generator function that allows us to!
'''

def iter_lst(lst):
    for i in range(len(lst)):
        yield lst[i]

lst = [10, 12, 40, "python"]

for elem in iter_lst(lst):
    print(elem)


''' Problem 5 
Is Range a generator function then? No! 
But, we can use a generator function to create something similar!

'''

# for i in range(1, 10, 1):
#     print(i)

def my_range(start, stop, step):
    while start < stop:
        yield start
        start += step

for i in my_range(1, 10, 2):
    print(i)


