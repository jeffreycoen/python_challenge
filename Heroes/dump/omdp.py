import requests

#* Who was the director of the movie **Aliens**?
#build query url
url = "http://www.omdbapi.com/?apikey=40e9cece&t="

# get a response
response = requests.get(url + "Aliens").json()

print(response["Director"] + " directed Aliens")

#* What was the movie **Gladiator** rated?

url2 = "http://www.omdbapi.com/?apikey=40e9cece&t="

# get a response
response2 = requests.get(url2 + "Gladiator").json()

print(response2["Rated"] + " was the rating for Gladiator")

#* What year was **50 First Dates** released? 
url3 = "http://www.omdbapi.com/?apikey=40e9cece&t="

# get a response
response3 = requests.get(url3 + "50+First+Dates").json()

print("50 First Dates was released in " + response3["Year"])
#* Who wrote **Moana**?
url4 = "http://www.omdbapi.com/?apikey=40e9cece&t="

# get a response
response4 = requests.get(url4 + "moana").json()

print(response4["Writer"] + "wrote the movie Moana")

#* What was the plot of the movie **Sing**?
url5 = "http://www.omdbapi.com/?apikey=40e9cece&t="

# get a response
response5 = requests.get(url5 + "sing").json()

print("The movie Sing is about: " + response5["Plot"])
