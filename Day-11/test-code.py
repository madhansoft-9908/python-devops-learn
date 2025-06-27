#Get pull request information on a repo using python?
#Details of Users who created Pull requests(Active) on Kubernetes Github repo.
#eg:
    #python script to talk with github api
	#request module is used to talk with api.
	#install request module --- pip install request
	#1.use the request module
	#2.api call - using request module make the api(url to make the api call) call.
	#3.json --most of info will get in json format ---convert json to dictionary
	#4.print the required information
import requests
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
print(response)   #output = <Response [200]>
complete_details = response.json()
#print(result)      #out put = all the details about all the pull request
print(complete_details[0]["id"])   #output = 2624535490
print(complete_details[0]["user"]["login"])  #output = stlaz

#to get the multiple user details use for loop
import requests
url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
response = requests.get(url)
complete_details = response.json()    #output will be list = <class 'list'>

for i in range(len(complete_details)):
    output = complete_details[i]["user"]["login"]
    print(output)
#len(complete_details) gives the total number of items in the list.
#range(len(...)) gives you the indexes: 0, 1, 2, ..., n-1

#output = 
#itssimrank
#stlaz
#drigz
#pohly
#serathius .... etc.
