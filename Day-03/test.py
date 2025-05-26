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

#examples
# Define configuration variables for a web server
server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000

# Print the configuration
print(f"Server Name: {server_name}")
print(f"Port: {port}")
print(f"HTTPS Enabled: {is_https_enabled}")
print(f"Max Connections: {max_connections}")

#updated configuration
port = 443
is_https_enabled = False

print(f"updated Port: {port}")
print(f"updated Https enabled: {is_https_enabled}")


#1. f"...{...}" — f-strings (formatted string literals):
#Introduced in Python 3.6, f-strings allow you to embed variables or expressions directly inside string literals.
#Advantage: It's cleaner and more readable, especially when formatting longer strings or inserting multiple variables.
user = "Alice"
age = 30
print(f"User: {user}, Age: {age}")
