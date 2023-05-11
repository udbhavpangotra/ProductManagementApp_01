import json
import pandas as pd
import urllib.request
import streamlit as st
import altair as alt


# Load the JSON object
url = "https://www.reddit.com/r/AskMen/new/.json"
response = urllib.request.urlopen(url)
data = json.load(response)
print("Script is running 0")

# Use json_normalize to create a DataFrame from the JSON data
df = pd.json_normalize(data, record_path=["data", "children"])

# Clean the data
df = df.dropna()

# Create a Streamlit app
st.title("AskMen Top Posts")
st.write("This app showcases the top posts on AskMen.")

# Display the data in the app
st.dataframe(df)
print(df.head(1))
print(df.columns)

# Create a bar chart of upvotes by title
chart = alt.Chart(df).mark_bar().encode(
    x='data.score:Q',
    y="data.title:N"
).properties(
    width=500,
    height=400
)

# Display the chart in the app
st.altair_chart(chart)
