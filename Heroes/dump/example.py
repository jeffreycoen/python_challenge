# Dependencies
import requests as req 
import json

vehicles = ["falcon9", "dragon", "falcon3"]

# URL for making requests to 
url = "https://api.spacexdata.com/v1/vehicles/falcon9"

# Retrieve the information from the User
response = req.get(url).json()

# Retrieve the cost_per_launch
print(response["cost_per_launch"])

# Figure out the number of payloads
print(len(response["payload_weights"]))

# Print the Engine Type
print(response["engines"]["type"])