import json
import pandas as pd
import urllib.request
import streamlit as st
import altair as alt

# Load the JSON object
url = "https://www.reddit.com/r/AskMen/new/.json"
response = urllib.request.urlopen(url)
data = json.load(response)

# Use json_normalize to create a DataFrame from the JSON data
df = pd.json_normalize(data, record_path=["data", "children"])

# Clean the data
df = df.dropna()

# Create a Streamlit app
st.title("AskMen Top Posts")
st.write("This app showcases the top posts on AskMen.")

# Display the data in the app
st.write("Top Post Titles:")
st.write(df['data.title'])

# Create a bar chart of the top 10 posts by score
st.write("Top 10 Posts by Score:")
top_scores = df.sort_values(by=['data.score'], ascending=False).head(10)
bar_chart = alt.Chart(top_scores).mark_bar().encode(
    x='data.score',
    y=alt.Y('data.title', sort='-x')
).properties(
    width=600,
    height=400
)
st.altair_chart(bar_chart)

# Create a pie chart of the distribution of post types
st.write("Distribution of Post Types:")
post_type_counts = df['data.post_hint'].value_counts()
pie_chart = alt.Chart(post_type_counts.reset_index()).mark_circle().encode(
    alt.X('data.post_hint', title='Post Type'),
    alt.Y('data.index', title='Count')
).properties(
    width=600,
    height=400
)
st.altair_chart(pie_chart)
