#conditional handling
#if Statement:The if statement is used to execute a block of code if a specified condition is True. If the condition is False, the code block is skipped.

#if condition:
    # Code to execute if the condition is True
#Example:
x = 10
if x > 5:
    print("x is greater than 5")

#elif Statement:The elif statement allows you to check additional conditions if the previous if or elif conditions are False. You can have multiple elif statements after the initial if statement.

#if condition1:
    # Code to execute if condition1 is True
#elif condition2:
    # Code to execute if condition2 is True
#elif condition3:
    # Code to execute if condition3 is True
# ...
#else:
    # Code to execute if none of the conditions are True
#Example:
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:
    print("x is not greater than 5")

#eg:1
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than 5")

#eg:2
score = 70
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade F")
# output is Grade C

#eg:3 - Multiple Conditions with and, or
age = 25
has_ticket = "true"

if age >=18 and has_ticket:
    print("allowed to enter")
else:
    print("not allowed as your less than 18")

#eg:4

user_name = "admin"
password = "12345"

if user_name == "admin" and password == "12345":
    print("login succesful")
else:
    print("invalid credentials")

#eg:5
import sys
type = sys.argv[1]
if type == "t2.micro":
    print("t2 micro will charge you 2 dollars per day")
elif type == "t2.medium":
    print("t2 medium will charge you 4 dollars per day")
elif type == "t2.xlarge":
    print("t2 xlarge will charge you 6 dollars per day")
else:
    print("please provide a valid instance type")
#python test.py t2.medium  --- output is t2 medium will charge you 4 dollars per day.
