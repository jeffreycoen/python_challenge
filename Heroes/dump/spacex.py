# Dependencies
import requests as req
import json

# specify url for json requests
url = "https://api.spacexdata.com/v1/launches/upcoming?year="

# retrieve the information from the url
#print(req.get(url))

# format contents as json and print
#response = (req.get(url).json())

# pretty the contents
#print(json.dumps(print(req.get(url).json())))


# Get the user's selection
launch_year= input("Which year would you like to see upcoming launches for? ")

# Retrieve the information from the User
response = req.get(url + str(launch_year)).json()

# Print the JSON
#print(json.dumps(response, indent=4, sort_keys=True))

# print that response!!
print(response[2])

