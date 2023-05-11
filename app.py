import streamlit as st
import requests
import pandas as pd

# Scrape the data from AskMen
url = "https://www.reddit.com/r/AskMen/top/.json"
response = requests.get(url)
data = response.json()

# Clean the data
df = pd.DataFrame(data["data"]["children"])
df = df[["title", "score", "created_utc"]]
df = df.dropna()

# Create a Streamlit app
st.title("AskMen Top Posts")
st.write("This app showcases the top posts on AskMen.")

# Display the data in the app
st.dataframe(df)
