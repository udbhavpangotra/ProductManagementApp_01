import json
import pandas as pd
import urllib.request
import streamlit as st

# Load the JSON object
url = "https://www.reddit.com/r/AskMen/new/.json"
response = urllib.request.urlopen(url)
data = json.load(response)
print("Script is running 0")

# Print the JSON data
print(data)

# Clean the data
df = pd.DataFrame([{
    "title": post["data"]["title"],
    "score": post["data"]["score"],
    "created_utc": post["data"]["created_utc"]
} for post in data["data"]["children"]])
df = df.dropna()

# Create a Streamlit app
st.title("AskMen Top Posts")
st.write("This app showcases the top posts on AskMen.")

# Display the data in the app
st.dataframe(df)
