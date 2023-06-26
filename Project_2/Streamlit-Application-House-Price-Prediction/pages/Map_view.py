# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
import plotly.express as px
import plotly.graph_objects as go

from pathlib import Path


# ## Set Page configuration -------------------------------------------------------------------------------------------------------------------------

st.title('🏠 :blue[Your House, Your Future]🔮')
st.markdown("***Make your real estate plans with technology of the future***")


## Feature 3: Map -----------------------------------------------------------------------------------------------------------------------------------------
@st.cache_data(experimental_allow_widgets=True)
def show_map():
	# Get unique town values from the DataFrame
	towns = st.session_state['df']['town'].unique().tolist()

	st.subheader("A closer look at each transaction")

	# Create a selection widget for the town
	selected_town = st.selectbox("Select a town", towns)

	# Filter the DataFrame based on the selected town
	selected_df = st.session_state['df'][st.session_state['df']['town'] == selected_town]

	# Get the latitude and longitude coordinates of the selected town
	selected_lat = selected_df['latitude'].values[0]
	selected_lon = selected_df['longitude'].values[0]

	# Create a Folium map centered on the selected town
	m = folium.Map(location=[selected_lat, selected_lon], zoom_start=14, tiles='CartoDB positron')

	# Iterate over each row in the selected DataFrame
	for index, row in selected_df.iterrows():
	    # Extract the latitude and longitude values
		lat = row['latitude']
		lon = row['longitude']

	    # Extract additional information
		town_name = row['town'].replace("_", " ").capitalize()
		address = "Blk " + row['block'].replace("_", " ").capitalize() +' ' + row['street_name'].replace("_", " ").capitalize()
		price = row['resale_price']
		info = f"Town: {town_name}<br>Address: {address}<br>Resale Price: ${price}"

	        # Check if the resale price is within the budget range
		if st.session_state['budget_min'] <= price <= st.session_state['budget_max']:
	        # Create a marker at the latitude and longitude coordinates with red color
			marker = folium.Marker([lat, lon], popup=folium.Popup(info, max_width=250), icon=folium.Icon(color='red'))
		else:
	        # Create a marker at the latitude and longitude coordinates with default color
			marker = folium.Marker([lat, lon], popup=folium.Popup(info, max_width=250))

	    # # Create a marker at the latitude and longitude coordinates
	    # marker = folium.Marker([lat, lon], popup=folium.Popup(info, max_width=250))



		marker.add_to(m)

	# Display the map using Streamlit
	st.markdown("**Click on the marker to see unit information**")
	# st.markdown("Dots represent transactions")
	folium_static(m)

show_map()


# st.title('🔧 Premium content coming your way... ')

# # # Set title of the app
# # st.title('🏠 Page 2🔮')
# st.markdown("Please support our efforts in empowering all in their real estate journey ❤️")



# Define the layout of your Streamlit app
# st.title("Resale Price Insights")
