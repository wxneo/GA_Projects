import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="West Nile Virus Dashboard", page_icon='🦟', layout="wide")

# https://plotly.com/python/mapbox-density-heatmaps/

# Load the train dataset
@st.cache_data
def load_file(filepath):
    pd.read_csv(filepath)
    return pd.read_csv(filepath)

df = load_file("./streamlit/data/train_merge_df.csv")

# st.sidebar.title('Data NineNine West Nile Virus')
# st.sidebar.write('Graph of Monthly total number of mosquitoes caught by year')

st.title("📊 Exploratory Data Analysis")
st.write("-- Data Nine Nine Project 4") 

st.markdown("""___""")



# st.write(df)



# FIGURE 0: Percentage WN Virus Present by Species
total_wnv_count = df['wnv_present'].value_counts().reset_index()
total_wnv_count.columns = ['wnv_present','count']
# total_wnv_count


df0 = total_wnv_count

fig0 = px.bar(df0, x = 'wnv_present', y = 'count', color = 'count',
              title = ('Target Class Count'))


fig0.update_layout(width = 800)

st.write(fig0)



st.text('')
st.text('')
st.text('')
st.markdown("""___""")
st.text('')
st.text('')
st.text('')



# FIGURE 1: Percentage WN Virus Present by Species

# species_count_wnv = pd.concat([species_count, species_wnv['wnv_present']], axis=1)
# species_count_wnv['percentage wnv_present'] = species_count_wnv['wnv_present'] / species_count_wnv['count'] * 100
# species_count_wnv


df1 = df[['day','num_mosquitos']]

df1 = df1.groupby(['day'])['num_mosquitos'].sum().reset_index()



fig1 = px.bar(df1, x = 'day', y = 'num_mosquitos', color = 'num_mosquitos',
              title = ('Total Number Of Mosquitos Caught By Day'))

fig1.update_layout(width = 800)

st.write(fig1)



st.text('')
st.text('')
st.text('')
st.markdown("""___""")
st.text('')
st.text('')
st.text('')



# FIGURE 2: MONTHLY TOTAL NUMBER OF MOSQUITOES CAUGHT BY YEAR

year_options = df['year'].unique().tolist()
# year  = st.selectbox('Which year would you like to see?', year_options,0)
# df = df[df['year']==year]

# fig = px.bar(df, x = 'month', y = 'num_mosquitos', color = 'month', 
#              range_y = [0,45000])

df2 = df[['year','month', 'num_mosquitos']]

df2 = df2.groupby(['year', 'month'])['num_mosquitos'].sum().reset_index()

# df2

fig2 = px.bar(df2, x = 'month', y = 'num_mosquitos', color = 'month', 
             range_y = [0,45000], animation_frame = 'year', animation_group = 'num_mosquitos', 
             title = 'Monthly total number of mosquitoes caught by year')

fig2.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 5500
fig2.layout.updatemenus[0].buttons[0].args[1]['transition']['pause'] = 0.05
fig2.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5000

fig2.update_layout(width = 800)

st.write(fig2)
#st.write('As mentioned, summer months seems to shows most numbers of mosquitos caught. However over the years, the overall number of mosquitoes caught by year does decrease')



st.text('')
st.text('')
st.text('')
st.markdown("""___""")
st.text('')
st.text('')
st.text('')



# FIGURE 3: TOTAL NUMBER OF West Nile Virus Present BY MONTH

month_options = df['month'].unique().tolist()

df3 = df[['year','month', 'wnv_present']]

df3 = df3.groupby(['year', 'month'])['wnv_present'].sum().reset_index()

# df2

fig3 = px.bar(df3, x = 'month', y = 'wnv_present', color = 'month', 
             range_y = [0,80], animation_frame = 'year', animation_group = 'wnv_present', 
             title = 'Total Number of West Nile Virus Present by Month')

fig3.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 6000
fig3.layout.updatemenus[0].buttons[0].args[1]['transition']['pause'] = 0.05
fig3.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5000

fig3.update_layout(width = 800)

st.write(fig3)



st.text('')
st.text('')
st.text('')
st.markdown("""___""")
st.text('')
st.text('')
st.text('')




# FIGURE 4: Mosquitos Populated Areas by Species

species_count = df.groupby('species').size().reset_index(name='count')
# species_count

df4 = species_count

fig4 = px.bar(df4, x = 'count', y = 'species', color = 'species',
              title = ('Mosquitos Populated Areas by Species'))

fig4.update_layout(width = 800)

st.write(fig4)



st.text('')
st.text('')
st.text('')
st.markdown("""___""")
st.text('')
st.text('')
st.text('')



# FIGURE 5: West Nile Virus Affected Areas by Species

species_wnv = df.groupby('species')['wnv_present'].sum().reset_index()
# species_wnv

df5 = species_wnv

fig5 = px.bar(df5, x = 'wnv_present', y = 'species', color = 'species',
              title = ('West Nile Virus Affected Areas by Species'))


fig5.update_layout(width = 800)

st.write(fig5)



st.text('')
st.text('')
st.text('')
st.markdown("""___""")
st.text('')
st.text('')
st.text('')



# FIGURE 6: Percentage WN Virus Present by Species

species_count_wnv = pd.concat([species_count, species_wnv['wnv_present']], axis=1)
species_count_wnv['percentage wnv_present'] = species_count_wnv['wnv_present'] / species_count_wnv['count'] * 100
# species_count_wnv

df6 = species_count_wnv

fig6 = px.bar(df6, x = 'percentage wnv_present', y = 'species', color = 'species',
              title = ('Percentage WN Virus Present by Species'))


fig6.update_layout(width = 800)

st.write(fig6)
