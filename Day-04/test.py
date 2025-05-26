#functions, packages and modules
#this is the normal approach in function
a = 5
b = 4
def addition():
    add = a + b
    print(add)
addition()

#below is the best approach
#takes the input
#perform the required action
#returns the output
def addition(a,b):
    add = a + b
    return add
print(addition(10,4))
#    or
x = addition(6,4)
print(x)

#module
#Suppose you have a Python file named my_module.py
# my_module.py
def square(x):
    return x ** 2
pi = 3.14159265

#You can use the above module in another script:
import my_module
result = my_module.square(10)
print(result)
