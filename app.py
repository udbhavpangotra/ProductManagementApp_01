import json
import pandas as pd
import urllib.request
import streamlit as st

# Load the JSON object
url = "https://www.reddit.com/r/AskMen/new/.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print("Script is running 0")

# Print the JSON data
print(data)


# Clean the data
df = pd.DataFrame(data["data"]["children"])
df = df[["title", "score", "created_utc"]]
df = df.dropna()

# Create a Streamlit app
st.title("AskMen Top Posts")
st.write("This app showcases the top posts on AskMen.")

# Display the data in the app
st.dataframe(df)
