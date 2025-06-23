#list and tuples
#list: A list is a mutable (changeable) collection.
      #Defined using square brackets [].
     #You can add, remove, or modify items.
#list is used to store a collection of items. Lists are ordered and can contain elements of various data types, such as numbers, strings, and objects.
#in list we store different type of data types eg: my_list = [1, 2, 3, 'apple', 'banana']

#eg:1
my_list = [1 ,2 ,3, "apple", "grapes"]
print(my_list)   #output = [1, 2, 3, 'apple', 'grapes']
print(type(my_list))  #output = <class 'list'>
#eg:2
fruits = ["apple", "banana", "mango"]
print(fruits)  #output = ['apple', 'banana', 'mango']

#accessing an element
print(fruits[1])  #output = banana

#adding an item
fruits.append("orange")
print(fruits)         #output = ['apple', 'banana', 'mango', 'orange']

#removing an item
fruits.remove("mango")
print(fruits)      #output = ['apple', 'banana', 'orange']

#modifying an item
fruits[0] = "grapes"
print(fruits)     #output = ['grapes', 'banana', 'orange']

#lenth of list
list_length = len(fruits)
print(list_length)            #output = 3

#Slicing a List
#Slicing allows you to create a new list from a subset of the original list.
subset = fruits[0:2] #output = ['grapes', 'banana']
print(subset)

#Concatenating Lists
#You can combine two or more lists to create a new list.
new_fruits = fruits + [1,2,"red"]
print(new_fruits)    #output = ['grapes', 'banana', 'orange', 1, 2, 'red']

#tuple: A tuple is an immutable (unchangeable) collection.
       #Defined using parentheses ().
       #Once created, you cannot change its values.

#eg:
colors = ("red", "green", "white")
print(colors)     #output = ('red', 'green', 'white')
print(colors[0])   #output = red

#example using both list and tuple
person_info = ("john", 25, "engineer")  #tuple(fixed)
skills = ["azure", "python", "devops"]  #list(can update)

#update the skills
skills.append("docker")
print(skills)           #output = ['azure', 'python', 'devops', 'docker']
