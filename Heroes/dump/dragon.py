# Dependencies
import json
import requests as req

# URL for GET requests for the Dragon
url = "https://api.spacexdata.com/v1/vehicles/dragon"

# Perform a GET request to the above URL, and save the response.
response = req.get(url).json()

# # Call the response's json() method. Print the result.
#print(response)

# # Retrieve and print the orbit duration of the Dragon
print(response["orbit_duration_yr"])

# # Retrieve the sidewall_angle_deg
print(response["sidewall_angle_deg"])

# # BONUS: Determine the full number of vehicles listed in the API
newurl = "https://api.spacexdata.com/v1/vehicle"
response2 = req.get(newurl).json()[1]["stages"]
print(response2)