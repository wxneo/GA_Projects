# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Data Analysis of Singapore Rainfall

### Problem Statement:

An F&B company is keen on a new business and marketing model organizing food truck events in Singapore to increase the exposure of their branding and create a unique experience for consumers. However operating food trucks would mean exposing to the elements of weather and in Singapore, that is either sunny or rainy. The latter will pose a challenge to operation hence, this project aims to analyse the weather pattern over the years to identify patterns in rainfall distribution and provide recommendations for operation team planning needs.

---

### Data used:

The dataset used for this project contains daily meteorological data collected from 3 different locations in Singapore (Changi, Tuas South, Ang Mo Kio) from 1 Jan 2014 to 31 Dec 2022. Some datasets were downloaded from Kaggle, consolidated by users spanning from year 2014 to 2020 while the rest were retrieved from the Meteorological Service Singapore Historical Daily Weather records.

Variables:

1.	Date
2.	Daily Rainfall Total (mm)
3.	Highest 30-min Rainfall (mm)
4.	Highest 60-min Rainfall (mm)
5.	Highest 120-min Rainfall (mm)
6.	Mean Temperature (°C)
7.	Maximum Temperature (°C)
8.	Minimum Temperature (°C)
9.	Mean Wind Speed (km/h)
10.	Maximum Wind Speed (km/h)

Source:

Data from 2021 to 2020: http://www.weather.gov.sg/climate-historical-daily/<br>
Data for Changi year 2021: https://www.kaggle.com/datasets/lynnjunwei/singapore-rainfall-data-2021<br>
Data from 2014 to 2020: https://www.kaggle.com/datasets/cyanaspect/singapore-weather?resource=download

---

### Data Dictionary:

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**year**|integer|final_df|The year of data collection| 
|**month**|integer|final_df|The month of data collection| 
|**day**|integer|final_df|The day of data collection| 
|**datetimes**|datetime|final_df|The date of data collection| 
|**(region)_rain_total**|float|final_df|Daily Rainfall Total (mm) in 3 regions (central, east & west)| 
|**(region)_rain_30min**|float|final_df|Highest 30-min Rainfall (mm) in 3 regions (central, east & west)| 
|**(region)_rain_60min**|float|final_df|Highest 60-min Rainfall (mm) in 3 regions (central, east & west)| 
|**(region)_rain_120min**|float|final_df|Highest 120-min Rainfall (mm) in 3 regions (central, east & west)| 
|**(region)_mean_temp**|float|final_df|Mean Temperature (°C) in 3 regions (central, east & west)| 
|**(region)_max_temp**|float|final_df|Maximum Temperature (°C) in 3 regions (central, east & west)| 
|**(region)_min_temp**|float|final_df|Minimum Temperature (°C) in 3 regions (central, east & west)| 
|**(region)_mean_wind_speed**|float|final_df|Mean Wind Speed (km/h) in 3 regions (central, east & west)|
|**(region)_max_wind_speed**|float|final_df|Maximum Wind Speed (km/h) in 3 regions (central, east & west)|


---

### Key takeaways from the analysis:
1. Eastern parts of Singapore receive approximately 25% lesser rainfall as compared to the rest of the region. This is because the eastern part of Singapore is largely flat and that forms an area known as a rain shadow region.

2. The drier months in Singapore fall between February to March and from June to August. This is largely contributed by the annual recurrence of the northeast monsoon and southwest monsoon.

3. Higher wind speed does not equate to higher rainfall while the inverse relation was observed in the analysis. The higher wind speed is likely due to the monsoon wind during the drier season hence, the lower in rainfall.

---

### Recommendations:

1. After Knowing the rainfall trend through the analysis, it is advisable to organise the event during drier months from February to March or from June to August to minimise the risk of rainy weather.

2. Location situated in the eastern parts of Singapore is highly recommended given the lower in rainfall. Places like Singapore Expo, East Coast Park and Changi Exhibition Centre are great choices of location for the event.

3. Since it is generally windy in the eastern region, some wind-related props or products can also be considered if the event were to the held in that region.
