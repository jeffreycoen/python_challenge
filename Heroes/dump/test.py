# Dependencies
import requests as req 
import json
import os as os



# open the first file
with open('Resources/' 'post.json') as json_data:
    d = json.load(json_data)
   # print(d)

# Load post_with_comment.json
with open('Resources/' 'post_with_comment.json') as json_data:
    e = json.load(json_data)
   # print(e["comment"]["text"])

# Load post_with_comment.json
with open('Resources/' 'post_with_comments_list.json') as json_data:
    f = json.load(json_data)
   # print(f["comment"]["commenters"])

# Load post_with_comment.json
with open('Resources/' 'cobweb.json') as json_data:
    g = json.load(json_data)
    print("...")
    print(("I found my " ) + (g["biggestWeb"]["biggerWeb"]["items"][0]))
    print(("I found my " ) + (g["biggestWeb"]["biggerWeb"]["smallerWeb"]["item"]))
    print(("I found my " ) + (g["biggestWeb"]["otherBigWeb"]["item"]))
    print(("I found my " ) + (g["biggestWeb"]["biggerWeb"]["smallerWeb"]["tinyWeb"]["items"][3]))