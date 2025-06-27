#real time use case
#list all the files in the list of folders that user provided?
#we should assume what is input and output
#input = list of the folder names
#output = list of the file names in the provided folder
###break the programme in to a small parts
#1.Read the input from the user(folder name) 
    #three different ways to read the input
     #a.command line arguments
     #b.env vars
     #c.input     ----- input executes at the run time.
        ## number = input("please provide a number: ")
#2.for loop to run on all the folder
#3.Identify required module in the programme
#4.print file
#5.Handle any known error.

#eg:step.1
#folders = input("please provide list of the folder names with spaces: ")
#print(folders) #output = please provide list of the folder names with spaces: /opt /tmp
                        # /opt /tmp
#folders = input("please provide list of the folder names with spaces: ").split()  #convert in to list using .split()
#print(folders) #output = please provide list of the folder names with spaces: /opt /tmp
                         #['/opt', '/tmp']
#eg:step.2
#for folder in folders:
    #print(folder)
#output = /opt
        # /tmp
#eg:step.3-- identify the required module
        #os - is the module which will talk to operating system
        #listdir- is function 
#import os
#folders = input("please provide list of the folder names with spaces: ").split()
#for folder in folders:
#    files = os.listdir(folder)
#    print("====listing files from the folder -" + folder)  #output  = ====listing files from the folder -/opt
#    print(files)  #output  = ['containerd', 'python', 'dotnet', 'oryx', 'tmp', 'conda']
#    #we don't want list as an output
#    for file in files:
#        print(file)
#out put 
#containerd
#python
#dotnet
#oryx
#tmp
#conda


#print(files) vs for file in files: print(file)
#first loop output 
#files = os.listdir(folder)
#print(files)
#os.listdir(folder) returns a list of file/folder names.
#print(files) prints the entire list as a single object.   #output = ['containerd', 'python', 'dotnet', 'oryx', 'tmp', 'conda']

#second loop:
#for file in files:
    #print(file)
#You’re now looping through each item in the list.
#print(file) prints each item one-by-one, not as a list, but as a string.

#eg: same example in single code
import os
folders = input("please provide list of the folder names with spaces: ").split()
for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide a valid folder name,looks like this folder doesnot exist:" + folder)

