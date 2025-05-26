#keywords and variables
#to define a local and global variable , will show you using function

#Global variable - which is defined outside of the function and can be used to any of function.
a = 5
b = 4
def addition():
    result = a + b
    print(result)
addition()

def sub():
    result = a - b
    print(result)
sub()
print(a)

#local variable ---which is specific to that function
def addition():
    a = 4
    b = 2
    print(a+b)
addition()
