# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import datetime
import os

#from wnv_historical_data_viz import df (NOT NEEDED)


## Set Page configuration ------------------------------------------------------------------------------------------------------------------------

st.set_page_config(page_title='West Nile Virus Dashboard', page_icon='🦟', layout='wide', initial_sidebar_state='expanded')
# Set title of the app
st.title('🎯 Are you at risk?')
st.write("-- Data Nine Nine Project 4")

st.markdown("***Keep yourself safe by predicting the presence of West Nile Virus at a chosen address***")

@st.cache_data
def get_data(filepath):
    actual_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filepath)
    df = pd.read_csv(actual_filepath)

    # Data needed for model 1
    df_filtered = df[[  # Categorical data:
                        'species', 'street', 'trap', 'address_number_and_street', 
                        # Numerical data:
                        'block', 'latitude', 'longitude',
    'year', 'month', 'day', 'stat_1_tmax', 'stat_1_tmin', 'stat_1_tavg',
    'stat_1_precip_total', 'day_length_mprec', 'day_length_nearh',
    'sunrise_hours', 'sunset_hours', 'mixed_tmax', 'mixed_tmin',
    'mixed_precip_total', 'stat_2_tmax', 'stat_2_tmin', 'stat_2_tavg', 'stat_2_precip_total']]

    # Model's Numerical data only
    df_filtered_num = df[[  'block', 'latitude', 'longitude',
    'year', 'month', 'day', 'stat_1_tmax', 'stat_1_tmin', 'stat_1_tavg',
    'stat_1_precip_total', 'day_length_mprec', 'day_length_nearh',
    'sunrise_hours', 'sunset_hours', 'mixed_tmax', 'mixed_tmin',
    'mixed_precip_total', 'stat_2_tmax', 'stat_2_tmin', 'stat_2_tavg', 'stat_2_precip_total']]

    # Model's Categorical data only
    df_filtered_cat = df[['species','street', 'trap']]

    return df, df_filtered, df_filtered_num, df_filtered_cat

df, df_filtered, df_filtered_num, df_filtered_cat = get_data('../data/train_merge_df.csv')


def get_predictors():

    st.sidebar.header('Select predictors')
    date = st.sidebar.date_input('Date')
    year = date.year
    month = date.month
    day = date.day
    

    # User input
    address = st.sidebar.selectbox('Address', sorted(df_filtered['address_number_and_street'].unique()), index=0)
    

    #Get latitude and longitude, street and block from dataframe based on user input for address
    filtered_df = df[df['address_number_and_street']==address]
    if len(filtered_df) > 0:
        latitude = filtered_df['latitude'].mean()
        longitude = filtered_df['longitude'].mean()
        # Access street name for first row 
        street = filtered_df['street'].iloc[0]
        block = filtered_df['block'].mean()


    # latitude = st.sidebar.slider('Latitude',  float(df_filtered['latitude'].min()), float(df_filtered['latitude'].max()), float(df_filtered['latitude'].min()), key='3')
    # longitude = st.sidebar.slider('Longitude', float(df_filtered['longitude'].min()), float(df_filtered['longitude'].max()),float(df_filtered['longitude'].min()), key='4')

    # User input
    stat_1_tmax = st.sidebar.slider("Temp_max at O'Hare Weather Stn (F)", float(df_filtered['stat_1_tmax'].min()), float(df_filtered['stat_1_tmax'].max()),float(78), step=1.0, key='5')
    stat_1_tmin = st.sidebar.slider("Temp_min at O'Hare Weather Stn (F)", float(df_filtered['stat_1_tmin'].min()), float(df_filtered['stat_1_tmin'].max()),float(65), step=1.0, key='6')
    stat_1_tavg = (stat_1_tmax + stat_1_tmin)/2
    stat_1_precip_total = st.sidebar.slider("Precip_total at O'Hare Weather Stn (inches)", float(df_filtered['stat_1_precip_total'].min()), float(df_filtered['stat_1_precip_total'].max()),float(df_filtered['stat_1_precip_total'].min()), key='8')

    # User input
    sunrise_time = st.sidebar.time_input('Time of Sunrise', datetime.time(4, 52), step=60)
    sunset_time = st.sidebar.time_input('Time of Sunset', datetime.time(19, 3), step=60)


    sunrise_hours = sunrise_time.hour + sunrise_time.minute / 60
    sunset_hours = sunset_time.hour + sunset_time.minute / 60

    # Create dummy date and combine with time
    dummy_date = datetime.date(2000, 1, 1)  # Dummy date
    sunrise_datetime = datetime.datetime.combine(dummy_date, sunrise_time)
    sunset_datetime = datetime.datetime.combine(dummy_date, sunset_time)

    day_length_mprec = (sunset_datetime - sunrise_datetime).total_seconds() / 60
    # st.sidebar.write(f'day length in min is {day_length_mprec}')
    
    day_length_nearh = np.round((sunset_datetime - sunrise_datetime).total_seconds()/3600)
    # st.sidebar.write(f'day length in nearh is {day_length_nearh}')

    # day_length_mprec = st.sidebar.slider('Day Length Minute Precision', float(df_filtered['day_length_mprec'].min()), float(df_filtered['day_length_mprec'].max()),float(df_filtered['day_length_mprec'].min()), step=1.0, key='9')
    # day_length_nearh = st.sidebar.slider('Day Length to Nearest Hour', float(df_filtered['day_length_nearh'].min()), float(df_filtered['day_length_nearh'].max()),float(df_filtered['day_length_nearh'].min()), step=1.0, key='10')
    # sunrise_hours = st.sidebar.slider('Sunrise Hours', float(df_filtered['sunrise_hours'].min()), float(df_filtered['sunrise_hours'].max()),float(df_filtered['sunrise_hours'].min()), step=1.0, key='11')
    # sunset_hours = st.sidebar.slider('Sunset Hours', float(df_filtered['sunset_hours'].min()), float(df_filtered['sunset_hours'].max()),float(df_filtered['sunset_hours'].min()), step=1.0, key='12')
    stat_2_tmax = st.sidebar.slider('Temp_max at Midway Weather Stn (F)', float(df_filtered['stat_2_tmax'].min()), float(df_filtered['stat_2_tmax'].max()),float(79), step=1.0, key='16')
    stat_2_tmin = st.sidebar.slider('Temp_min at Midway Weather Stn (F)', float(df_filtered['stat_2_tmin'].min()), float(df_filtered['stat_2_tmin'].max()),float(69), step=1.0, key='17')
    stat_2_tavg = (stat_2_tmax + stat_2_tmin)/2
    stat_2_precip_total = st.sidebar.slider('Precip_total at Midway Weather Stn (inches)', float(df_filtered['stat_2_precip_total'].min()), float(df_filtered['stat_2_precip_total'].max()),float(df_filtered['stat_2_precip_total'].min()), key='19')
    mixed_tmax = (stat_1_tmax + stat_2_tmin)/2
    mixed_tmin = (stat_1_tmin + stat_2_tmin)/2
    mixed_precip_total = (stat_1_precip_total + stat_2_precip_total)/2

    species = 'CULEX PIPIENS'

    trap_filter= df[(df['latitude'] == latitude) & (df['longitude'] == longitude)]
    if not trap_filter.empty:
            trap = trap_filter['trap'].iloc[0]
    else:
        print("No matching traps found; check address input.")
        trap = None

    predictors = [species, trap, year, month, day, street, block, latitude, longitude, stat_1_tmax, stat_1_tmin, stat_1_tavg, stat_1_precip_total, day_length_mprec, day_length_nearh, sunrise_hours, sunset_hours, mixed_tmax, mixed_tmin, mixed_precip_total, stat_2_tmax, stat_2_tmin, stat_2_tavg, stat_2_precip_total]
    predictors_col_name = ['species', 'trap', 'year', 'month', 'day', 'street', 'block', 'latitude', 'longitude', 'stat_1_tmax', 'stat_1_tmin', 'stat_1_tavg', 'stat_1_precip_total', 'day_length_mprec', 'day_length_nearh', 'sunrise_hours', 'sunset_hours', 'mixed_tmax', 'mixed_tmin', 'mixed_precip_total', 'stat_2_tmax', 'stat_2_tmin', 'stat_2_tavg', 'stat_2_precip_total']
    predictors_df = pd.DataFrame([predictors], columns=predictors_col_name)

    return predictors_df

predictors_df = get_predictors()

def wnv_predictor(predictors_df):

    #st.write(predictors_df)
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../models/ada_model.pkl')
    model1 = pickle.load(open(filename, 'rb'))

    # Generate prediction based on user selected attributes
    y_pred = model1.predict(predictors_df)

    # Probability of class 1
    y_prob = model1.predict_proba(predictors_df)[:,1]

    # Print predicted wnv_present
    #st.title("Wnv Prescence Predictor")

    #st.write(formatted_pred)
    st.write('Prediction is: ', y_pred[0])
    st.write('Probability of virus is: ', y_prob[0])

wnv_predictor(predictors_df)