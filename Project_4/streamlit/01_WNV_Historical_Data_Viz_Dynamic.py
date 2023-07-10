import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static
import os

st.set_page_config(page_title="West Nile Virus Dashboard", page_icon='🦟')
st.title("🌍 Visualizing historical data relating to the West Nile Virus")
st.write("-- Data Nine Nine Project 4")
st.markdown("***Map showing weather stations locations, trap locations, number of mosquitos caught in trap, spray data, and whether wnv was present, for selected date.***")

# Load the train dataset
@st.cache_data    
def load_file(filepath):
    current_directory = os.getcwd()
    
    file_path_concat = os.path.join(current_directory, filepath)
    train_df = pd.read_csv(file_path_concat)
    
    pd.read_csv(filepath)
    return pd.read_csv(filepath)

df = load_file("../assets/train.csv")

# Load the spray dataset

spray_df = load_file("../assets/spray.csv")

# Convert date columns to datetime
df['Date'] = pd.to_datetime(df['Date'])
spray_df['Date'] = pd.to_datetime(spray_df['Date'])

# Sidebar - Date selection
st.sidebar.subheader("Date Selection")
dates_df = df['Date'].dt.strftime('%Y-%m-%d').unique()
dates_spray = spray_df['Date'].dt.strftime('%Y-%m-%d').unique()
dates = sorted(list(set(dates_df).union(dates_spray)))
selected_date = st.sidebar.selectbox("Select Date", dates)

# Filter the train dataset based on the selected date
filtered_data = df[df['Date'] == selected_date]

# Group the data by location and date to get the number of mosquitos and WNV_present cases
grouped_data = filtered_data.groupby(['Latitude', 'Longitude', 'Date']).agg({
    'NumMosquitos': 'sum',
    'WnvPresent': 'sum'
}).reset_index()

# Filter the spray dataset based on the selected date
spray_data = spray_df[spray_df['Date'] == selected_date]

# Create the map
m = folium.Map(location=[41.8781, -87.6298], zoom_start=10, tiles='cartodbpositron')

# Add markers for the two weather stations
weather_stations = {
    'station1': {
        'name': "Chicago O'Hare International Airport",
        'lon': -87.933,
        'lat': 41.995,
        'elev': 662
    },
    'station2': {
        'name': "Chicago Midway International Airport",
        'lon': -87.752,
        'lat': 41.786,
        'elev': 612
    }
}

for station in weather_stations.values():
    folium.Marker(
        location=[station['lat'], station['lon']],
        popup=station['name']+' Weather Station',
        icon=folium.Icon(icon='star', color='blue', prefix='fa')
    ).add_to(m)


# Add base grey marker for all trap locations
for _, row in df.iterrows():
    # Marker for all trap locations
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=2.5,
        popup=f"Trap: {row['Trap']}",
        color='lightgrey',
        fill=True,
        fill_color='lightgrey',
        fill_opacity=0.5,
        weight=0
    ).add_to(m)


# Add markers for number of mosquitos and WNV_present cases
for _, row in grouped_data.iterrows():
    # Marker for number of mosquitos
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=row['NumMosquitos'] / 5,
        popup=f"NumMosquitos: {row['NumMosquitos']}",
        color='green',
        fill=True,
        fill_color='green'
    ).add_to(m)

    # Marker for WNV Present
    if row['WnvPresent'] == 1:
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=1,
            popup=f"WNV Present: {row['WnvPresent']}",
            color='red'
        ).add_to(m)

# Add markers for spray data
for _, spray_row in spray_data.iterrows():
    folium.CircleMarker(
        location=[spray_row['Latitude'], spray_row['Longitude']],
        radius=2,
        color='goldenrod',
        popup=f"Sprayed",
        fill=True,
        fill_color='goldenrod',
        fill_opacity=0.2,
        weight=0
    ).add_to(m)

# Add the boundary of Chicago using GeoJSON data
# chicago_boundary_url = 'https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON/master/il_illinois_zip_codes_geo.min.json'
# folium.GeoJson(chicago_boundary_url).add_to(m)

# Display the map in Streamlit
folium_static(m)
