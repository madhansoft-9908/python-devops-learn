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
#Suppose you have a Python file named my_module.py --- already my_module.py file ispresent in the day-04 folder 
# my_module.py
def square(x):
    return x ** 2
print(square(5))
pi = 3.14159265

#You can use the module in another script:
#we can import the module using import keyword
#This is importing the module
import my_module
result = my_module.square(10)  #10 power 2 = 10*10 = 100
print(result) #or print(my_module.square(5))
print(my_module.square(10))

#import package
#Suppose you have a package structure as follows:
#my_package/
#    __init__.py
#    module1.py
#    module2.py

#You can use modules from this package as follows:
#This is importing the package and module from that package

#from my_package import module1
#result = module1.function_from_module1()   #function_from_module is just a function name from module1.

#python workspace

# 1.pip install virtualenv
# 2.python -m venv project-abc   ----create the project
# 3.source project-abc/bin/activate ----switch to the project
# 4.deactivate --- come out of the project.
