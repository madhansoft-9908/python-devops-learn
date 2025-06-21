#operators
#Arithmatic operator
#1.Addition (+): Adds two numbers.
#2.Subtraction (-): Subtracts the right operand from the left operand.
#3.Multiplication (*): Multiplies two numbers.
#4.Division (/): Divides the left operand by the right operand (results in a floating-point number).
#5.Floor Division (//): Divides the left operand by the right operand and rounds down to the nearest whole number.
#6.Modulus (%): Returns the remainder of the division of the left operand by the right operand.
#7.Exponentiation ():** Raises the left operand to the power of the right operand.

a = 6
b = 3
addition = a+b
print(addition)  #output = 9

sub = a-b
print(sub) #output = 3

mul = a*b
print(mul) #output = 18

div = a/b 
print(div) #output = 2.0

floordiv = a//b
print(floordiv)  #output = 2

modulus = a%b
print(modulus) #output = 0

exponent = a**b
print(exponent) #output(6*6*6) = 216

#Assignment Operator
#1.Basic Assignment (=): Assigns a value to a variable.
#2.Addition Assignment (+=): Adds the right operand to the left operand and assigns the result to the left operand.
#3.Subtraction Assignment (-=): Subtracts the right operand from the left operand and assigns the result to the left operand.
#4.Multiplication Assignment (*=): Multiplies the left operand by the right operand and assigns the result to the left operand.
#5.Division Assignment (/=): Divides the left operand by the right operand and assigns the result to the left operand.
#6.Floor Division Assignment (//=): Performs floor division on the left operand and assigns the result to the left operand.
#7.Modulus Assignment (%=): Calculates the modulus of the left operand and assigns the result to the left operand.
#8.Exponentiation Assignment (=):** Raises the left operand to the power of the right operand and assigns the result to the left operand.

#Basic assignment x =5
#addition assignment
y = 10
y += 2 #equivalent to y = y+2
print(y) #output = 12

#relational operators

#Relational operators in Python are used to compare two values and determine the relationship between them. These operators return a Boolean result, which is either True or False.
#Equal to (==): Checks if two values are equal.
#Not equal to (!=): Checks if two values are not equal.
#Greater than (>): Checks if the left operand is greater than the right operand.
#Less than (<): Checks if the left operand is less than the right operand.
#Greater than or equal to (>=): Checks if the left operand is greater than or equal to the right operand.
#Less than or equal to (<=): Checks if the left operand is less than or equal to the right operand.

a = 5
b = 5
c = 10
result = a == b
print(result)

res = a != c 
print(res)
res1 = a == c 
print(res1)
print(c > a)
print(b < c)
print(a >= b)
print(a <= c)

#Examples
#Equal to
a = 5
b = 5
result = a == b
# result will be True
#Not equal to
x = 10
y = 7
result = x != y
# result will be True

#Logical Operations in Python
#Logical operators in Python are used to manipulate and combine Boolean values. These operators allow you to perform logical operations such as AND, OR, and NOT.
#AND (and): Returns True if both operands are True.
#OR (or): Returns True if at least one of the operands is True.
#NOT (not): Returns the opposite Boolean value of the operand.
#Examples
#AND Operator
x = True
y = False
result = x and y
# result will be False
#OR Operator
a = True
b = False
result = a or b
# result will be True

a = True

result = not a
print("not a =", result) # returns the opposite value

#Identity Operations
#dentity operators in Python are used to compare the memory locations of two objects to determine if they are the same object or not. The two identity operators are "is" and "is not."
#is: Returns True if both operands refer to the same object.
#is not: Returns True if both operands refer to different objects.
#Examples
#is Operator
x = [1, 2, 3]
y = x  # y now refers to the same object as x
result = x is y
# result will be True
#is not Operator
a = "hello"
b = "world"
result = a is not b
# result will be True

a = 4
b = 5
result = a is not b
print("is not operator:",result) #returns true

words = ["apple","carrot","banana"]
output = "apple" in words
print("membership in operator:",output)

output2 = "grapes" not in words
print("membership not in operator:",output2)

output2 = "grapes" in words
print("membership not in operator:",output2)

#Precedence of Operations will check later
