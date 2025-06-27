#Dictionary: A dictionary in Python is a data structure that allows you to store and retrieve values using keys.
        # A dictionary is a key vaule pairs to store the properties
#eg:1
   #my_list = {"name": "john", "age": 25, "city": "hyderabad"}
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict["name"])    #output = John

#Modifying and Adding Elements:
my_dict["age"] = 30
print(my_dict)      #output = {'name': 'John', 'age': 30, 'city': 'New York'}

my_dict["occupation"] = "engineer"
print(my_dict)    #output = {'name': 'John', 'age': 30, 'city': 'New York', 'occupation': 'engineer'}

#Removing Elements:
del my_dict["city"]
print(my_dict)    # output = {'name': 'John', 'age': 30, 'occupation': 'engineer'}

#Checking Key Existence:
if "age" in my_dict:
    print("age is present in the dictionary")

#Iterating Through Keys and Values:
#.items() is a dictionary method that returns a view of the dictionary’s key-value pairs.
for key, value in my_dict.items():
    print(key, value)
#output 
#name John
#age 30
#occupation engineer

#eg:2 =2.eg: adding the multiple students data.
my_list = [
    { "name" : "suresh",
      "age"  : 26,
      "city" : "hyderabad"
    },
    { "name" : "naresh",
      "age"  : 24,
      "city" : "chennai"
    },
    { "name" : "chandra",
      "age"  : 29,
      "city" : "tamil"
    }
]

print(my_list[0]["name"])  #output = suresh
print(my_list[2]["city"])  #output = tamil

print(my_list[0]["name"], my_list[0]["city"])  #output = suresh hyderabad
