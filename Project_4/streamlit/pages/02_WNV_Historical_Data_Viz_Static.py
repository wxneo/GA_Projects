import streamlit as st
from PIL import Image

## Set Page configuration ------------------------------------------------------------------------------------------------------------------------

st.set_page_config(page_title='West Nile Virus Dashboard', page_icon='🦟', layout='wide', initial_sidebar_state='expanded')
# Set title of the app
st.title("🌍 Visualizing historical data relating to the West Nile Virus")
st.write("-- Data Nine Nine Project 4")
st.markdown("***Density heatmaps for 2007, 2009, 2011, and 2013.***")

st.markdown("""___""")

col1, col2 = st.columns(2)


col1.subheader("WNV Density Heatmap for 2007")
image2007 = Image.open('./streamlit/images/2007_density_map.png')
col1.image(image2007)
         
col1.markdown("""___""")

col1.subheader("WNV Density Heatmap for 2011")
image2011 = Image.open('./streamlit/images/2011_density_map.png')
col1.image(image2011)
col1.write('Blue indicates areas that were sprayed.')

col2.subheader("WNV Density Heatmap for 2009")
image2009 = Image.open('./streamlit/images/2009_density_map.png')
col2.image(image2009)
         
col2.markdown("""___""")

col2.subheader("WNV Density Heatmap for 2013")
image2013 = Image.open('./streamlit/images/2013_density_map.png')
col2.image(image2013)
col2.write('Blue indicates areas that were sprayed.')

st.markdown("""___""")