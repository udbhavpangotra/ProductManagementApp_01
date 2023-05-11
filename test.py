import json
import pandas as pd
import urllib.request

# Load the JSON object
url = "https://www.reddit.com/r/AskMen/new/.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print("Script is running 0")

# Print the JSON data
print(data)
