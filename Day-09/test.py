#for and while loop
#for loop:when we need to execute a block of code with definite/specific number of times use for loop
    #for loop syntax : for var in sequence:
    #in the sequence we can use : range, list and tuple
#The "for" loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a set of statements for each item in the sequence.
# he loop continues until all items in the sequence have been processed.
#eg:
for i in range(10):
    print("apple")  #output = apple will print 10 times

#Example 2: Using range()
for i in range(1,6):
    print(i)             #output = 1,2,3,4,5

colors = ["red", "green", "white"]
for col in colors:
    print(col)   #output = red, green, white

#loop controls
#break statement:The "break" statement is used to exit the loop prematurely. It can be applied to both "for" and "while" loops
#eg:
numbers = [1,2,3,4,5,6,7]
for number in numbers:
    if number == 5:
        break
    print("break staement:",number)     #output = 1,2,3,4

#Continue statement:The "continue" statement is used to skip the current iteration of the loop and proceed to the next one. It can be used in both "for" and "while" loops
#eg:
numbers = [1,2,3,4,5,6,7]
for number in numbers:
    if number == 5:
        continue
    print("continue statement:",number)  #output = 1,2,3,4,6,7

#eg:
log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed"
]
for file in log_file:
    if "ERROR" in file:
        print(file)      #output = ERROR: File not found, ERROR: Database connection failed

#while loop:The "while" loop continues to execute a block of code as long as a specified condition is true. 
      #It's often used when you don't know in advance how many times the loop should run.
#syntax = while condition:
    # Code to be executed as long as the condition is true
count = 0
while count < 5:
    print(count)
    count += 1    #output = 0,1,2,3,4

#eg:
i = 1
while i <= 5:
    print(i)
    i += 2      #output = 1,3,5

#eg:exit on condition
#if password is not equal to admin loop continuos. if password is admin then out put is access granted.
password = ""
while password != "admin":
    password = input("enter the password: ")
print("access granted")    #enter the password: admin    ---output = access granted

#example for environments
environments = ["dev", "stagging", "prod"]
def deploy_configuration(env):
    print(f"deploying to {env} environment")
for env in environments:
    deploy_configuration(env)

#output = deploying to dev environment
         #deploying to stagging environment
         #deploying to prod environment
