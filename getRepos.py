#For importing the required libraries
import urllib2
import json

print("Enter the username")
#To take username as an input
username = raw_input("")

#URL pattern to get the user repositories
url = 'https://api.github.com/users/' + username +'/repos'

#To store the json object obtained from the url
json_obj = urllib2.urlopen(url)

#Loads the json object into a variable
data = json.load(json_obj)

#to print the repository names
for i in range(0, len(data)):
	print data[i]['name']

