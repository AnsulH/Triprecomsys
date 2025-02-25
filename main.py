import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans


st.title("Location Based Recommender System Using Clustering")

# Load the data
df = pd.read_csv('RawCityfiles.csv')

# Extract relevant columns for clustering
L2 = df.iloc[:, -1: -3: -1]

# Perform KMeans clustering
kmeans = KMeans(n_clusters=10, random_state=0)  #north South West East and Central India
kmeans.fit(L2)

# Add cluster labels to the dataframe
df['loc_clusters'] = kmeans.labels_

# Create input box for user to enter city name
input_city = st.text_input("Enter a city name:").capitalize()

if input_city:
    # Find the cluster of the input city
    try:
        cluster = int(df.loc[df['location'] == input_city, 'loc_clusters'].iloc[0])
        
        # Find cities in the same cluster and display them
        cities = df.loc[df['loc_clusters'] == cluster, 'location']
        st.write("Cities in the same cluster:")
        for c in cities:
            if c != input_city:
                st.write(c)
    except IndexError:
        st.write("City not found in the dataset.")

from sklearn.metrics import silhouette_score

silhouette_avg = silhouette_score(L2, kmeans.labels_)
st.write(f"Silhouette Score: {silhouette_avg}")