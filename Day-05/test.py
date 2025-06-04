#command line arguments 
#sample example other than command line arguments
#eg:1
def addition(a,b):
    add = a+b
    return add
x = addition(3,3)
print(x)

#To use the command line arguments import sys module
#eg:2
import sys
def addition(a,b):
    add = a+b
    return add
    
a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])

if operator == "addition":
    ouput = addition(a,b)
    print(ouput)           
#python test.py 2 addition 5
#out put is 25, bcz python take arguments as a string. so we need to int before sys.argv[1]
#after adding the int, output is 7
##############################

#eg:3
import sys
def addition(a,b):
    add = a+b
    return add
def sub(a,b):
    s = a-b
    return s
a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])
if operator == "addition":
    output = addition(a,b)
    print("second output for add:", output) 
#for addition = python test.py 2 addition 5
#output is 7

elif operator == "sub":
    result = sub(a,b)
    print(result)
#for substraction = python test.py 2 sub 5
#output is -3
else:
    print("pass the correct operator")
#other than addition and substraction = python test.py 2 mul 5
#output is pass the correct operator

#Environment variables: when you want to deal with sensitive information(like:password,token,api keys) go with env variables.
#To read the env variable in the code use the module "os":
#To read the env variables use command = env 
#Create the env variable using command
#export password="sink@123"
  
#eg:3

    import os
    secret = os.getenv("password")
    print(secret)
