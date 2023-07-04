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


## Preparing data -----------------------------------------------------------------------------------------------------------------------------------

# Using .cache_data so to reduce lag
@st.cache_data
def get_data(filename):
    df = pd.read_csv(filename)

    # Data needed for model 1
    df_filtered = df[[  # Categorical data:
                        'town', 'storey_range', 'full_flat_type', 'pri_sch_name',  
                        # Numerical data:
                        'floor_area_sqm', 'lease_commence_date', 'mall_nearest_distance', 'hawker_nearest_distance', 'mrt_nearest_distance', 
                        'pri_sch_nearest_distance', 'sec_sch_nearest_dist', 'resale_price']]
    # Model's Numerical data only
    df_filtered_num = df[[  'floor_area_sqm', 'lease_commence_date', 'mrt_nearest_distance', 'hawker_nearest_distance',
                            'mall_nearest_distance', 'pri_sch_nearest_distance', 'sec_sch_nearest_dist', 'resale_price']]
    # Model's Categorical data only
    df_filtered_cat = df[['town', 'storey_range', 'full_flat_type', 'pri_sch_name']]


    # user_fr_dict will store the caterogrical values as a user-friendly form,
    # by removing '_' and capitalising first letter of each word
    user_fr_dict = {}

    # Iterate over each column in df_filtered_cat, get the unique values, and add to dictionary
    for col in df_filtered_cat.columns:
        unique_values = df_filtered_cat[col].unique()
        transformed_unique_values = [value.replace('_', ' ').title() for value in unique_values]
        user_fr_dict[col] = transformed_unique_values

    return df, df_filtered, df_filtered_num, df_filtered_cat, user_fr_dict

df, df_filtered, df_filtered_num, df_filtered_cat, user_fr_dict = get_data(Path(__file__).parent /'../housing_df.csv')

## Feature 3: Map -----------------------------------------------------------------------------------------------------------------------------------------
@st.cache_data(experimental_allow_widgets=True)
def show_map():
	# Get unique town values from the DataFrame
	towns = df['town'].unique().tolist()

	st.subheader("A closer look at each transaction")

	# Create a selection widget for the town
	selected_town = st.selectbox("Select a town", towns)

	# Filter the DataFrame based on the selected town
	selected_df = df[df['town'] == selected_town]

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


# # Create the regression plot using Plotly
# fig = px.scatter(df_floors, x='lease_commence_date', y='resale_price', trendline='ols')

# # Customize the trendline color and thickness
# fig.update_traces(selector=dict(name='trendline'), line_color='maroon', line_width=3)

# # Customize the layout
# fig.update_layout(
#     title='Flat Lease Commence Date vs Resale Price',
#     xaxis_title='Lease Commence Date',
#     yaxis_title='Resale Price (SGD)',
# )

# # Display the plot in Streamlit
# st.plotly_chart(fig)



# st.title('🔧 Premium content coming your way... ')

# Set title of the app
#st.title('🏠 Page 1🔮')
# st.markdown("Please support our efforts in empowering all in their real estate journey ❤️")



# Define the layout of your Streamlit app
# st.title("Resale Price Insights")
