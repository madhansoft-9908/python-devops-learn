print('hello world')
print("hello world")

#concatination
a = "nature is"
b = "beautiful"
concat = a + " " + b
print(concat)

#length of text
text = "python for devops"
length = len(text)
print("length of the text:", length)
print(text)

#upper and lower case of the text
upper = text.upper()
print("upper text:", upper)

lower = text.lower()
print("lower text:",lower)

#replace the character
word = "python is awesome"
replace = word.replace("awesome", "little dificult")
print("modified text:", replace)   #output = modified text: python is little dificult

#split
split = word.split()
print(split)  #output = ['python', 'is', 'awesome']

#strip is to remove the spaces between the character

text = " coconut water is good for health "
strip = text.strip()
print("removed the spaces for the sentence:", strip) #output = removed the spaces for the sentence: coconut water is good for health

#substring is to find the string in the sentence
text = " coconut water is good for health "
substring = "health"
if substring in text:
    print(substring, "substring found in the text")


#numaric data types
num1 = 12
num2 = 6

result1 = num1 + num2
print(result1)

result2 = num1 - num2
print(result2)

result3 = num1 * num2
print(result3)

#division
result4 = num1 / num2
print(result4) #output = 2.0

result40 = num1 // num2
print(result40) #output = 2

#remainder
result5 = num1 % num2
print(result5) #output = 0

#absolute value
res = abs(-7)
print("absolute value:",res)

# Rounding
result6 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result6) #output = 3.14

result7 = round(3.14159265359, 4)  # Rounds to 4 decimal places
print("Rounded:", result7) #output = 3.1416
