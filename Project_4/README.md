# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4: Data-backed solutions for combating West Nile Virus in Chicago

### **Try Out our West Nile Virus Streamlit Application by clicking the streamlit icon below!**
### [![West Nile Virus Interactive EDA and Predictor](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://west-nile-virus-dashboard-d99.streamlit.app/)

<br>

| **Concerning Numbers** | **Social Cost per Hospitalised Person**  |
| ------------------------ | -----------------------  |
|![Concerning Numbers](https://github.com/wxneo/GA_Projects/blob/main/Project_4/images/Concerning_Numbers.jpg) | ![Social Cost Per Person](https://github.com/wxneo/GA_Projects/blob/main/Project_4/images/Social_Cost_Loss_per_Person.jpg) |

<br>

## Content Directory:
- [Background](#Background)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [Data Preprocessing](#Data-Preprocessing)
- [Modeling](#Modeling)
- [Key Recommendations](#Key-Recommendations)

<br>


## Background
West Nile virus (WNV) is an infectious viral disease transmitted by mosquitoes, which can lead to flu-like symptoms, neurological complications, and potentially fatal illnesses in humans.

In the year 2002, the initial human cases of West Nile virus were reported in the city of Chicago. Subsequently, the City of Chicago and the **Chicago Department of Public Health (CDPH)** took significant measures to establish a comprehensive surveillance and control program. This program has been diligently maintained and remains in operation to this day. Over the course of 12 years, substantial efforts have been invested in combating the spread of West Nile Virus, resulting in the accumulation of a vast amount of data by the **CDPH**. This rich dataset now serves as a valuable resource for making evidence-based decisions.

Reference Website
- [Centre for Disease Control and Prevention](https://www.cdc.gov/about/index.html)
- [Chicago Department of Public Health](https://www.chicago.gov/city/en/depts/cdph.html)

<br>


## Problem Statement
We, **Data Nine-Nine**, have been engaged as a third-party consulting firm by the **Centre for Disease Control and Prevention (CDC)** to collaborate on a comprehensive review of their West Nile virus (WNV) control efforts. Our objective is to

	(1) build machine learning model to predict the presence of WNV; 

	(2) providing valuable insights and recommendations to further enhance their strategies 
<br>

in combatting the West Nile virus outbreak.

<br>

## Project Deliverables
Our project is centered around the following objectives:

1. Conduct comprehensive **research** on the occurrence and prevalence of the West Nile virus in the city of Chicago.
2. Develop and **train a machine learning model** capable of accurately predicting the probability of the presence of the West Nile virus.
3. Share our **insights and recommendations** with the esteemed members of the Centers for Disease Control and Prevention (CDC), including biostatisticians and epidemiologists.
4. Provide a thorough **cost-benefit analysis** to support the CDC members in making informed decisions based on data-driven recommendations for the future.

Project management and planning documentation is done via Github Projects here: https://github.com/users/khammingfatt/projects/1/views/1

<br>

---

## Datasets:
Public health workers in Chicago setup mosquito traps scattered across the city. The captured mosquitos are tested for the presence of West Nile virus.

* [`train.csv`](../assets/train.csv): The "train.csv" dataset comprises information regarding the geographical coordinates of mosquito traps, the count of mosquitos captured in each trap, and the presence or absence of the West Nile Virus. The dataset encompasses data collected during the years 2007, 2009, 2011, and 2013.

* [`test.csv`](../assets/test.csv): The "test.csv" dataset comprises information regarding the geographical coordinates of mosquito traps and the count of mosquitos captured in each trap. The dataset encompasses data collected during the years 2008, 2010, 2012, and 2014. We are to use test.csv to evaluate the results of machine learning.

* [`spray.csv`](../assets/spray.csv): The spray.csv consists of GIS data for City of Chicago spray efforts in 2011 and 2013. 

* [`weather.csv`](../assets/weather.csv): The weather.csv consists of weather condition data collected by National Oceanic and Atmospheric Administration (NOAA) from year 2007 to 2014.

<br>

## Data Dictionary
| Feature                   | Type    | Dataset                       | Description                                 |   
|---------------------------|---------|-------------------------------|---------------------------------------------|
| year                      | integer | train_merge_df, test_merge_df | Year that the WNV test is performed         |   
| month                     | integer | train_merge_df, test_merge_df | Month that the WNV test is performed        |   
| day                       | integer | train_merge_df, test_merge_df | Day of month that the WNV test is performed |   
| week                      | integer | train_merge_df, test_merge_df | Week that the WNV is performed              |   
| dayofweek                 | integer | train_merge_df, test_merge_df | Day of week that the WNV is performed       |  
| dayofyear                 | integer | train_merge_df, test_merge_df | Day of year that the WNV is performed       |   
| address                   | object  | train_merge_df, test_merge_df | Approximate address of the location of trap. This is used to send to the GeoCoder.  |   
| species                   | object  | train_merge_df, test_merge_df | Species of mosquitos                        |   
| block                     | integer | train_merge_df, test_merge_df | Block number                                |   
| street                    | object  | train_merge_df, test_merge_df | Street name                                 |   
| trap                      | object  | train_merge_df, test_merge_df | Id of the Mosquito trap                         |   
| address_number_and_street | object  | train_merge_df, test_merge_df | Address number and street name              |   
| latitude                  | float   | train_merge_df, test_merge_df | Latitude returned from GeoCoder                   |   
| longitude                 | float   | train_merge_df, test_merge_df | Longitude returned from GeoCoder            |   
| address_accuracy          | integer | train_merge_df, test_merge_df | Accuracy returned from GeoCoder      |   
| wnv_present               | integer | train_merge_df                | Whether West Nile Virus was present in these mosquitos. 1 means WNV is present, and 0 means not present.     |   
| num_mosquitos             | integer | train_merge_df                | Number of mosquitoes caught in this trap |   
| station                   | integer | train_merge_df, test_merge_df | Weather station number                     |   
| stat_1_tmax               | integer | train_merge_df, test_merge_df | Max temperature at Station 1                      |   
| stat_1_tmin               | integer | train_merge_df, test_merge_df | Min temperature at Station 1             |   
| stat_1_tavg               | float   | train_merge_df, test_merge_df | Average temperature at Station 1                |   
| stat_1_precip_total       | float   | train_merge_df, test_merge_df | Total precipitation at Station 1           |   
| day_length_mprec          | float   | train_merge_df, test_merge_df | Day duration in minutes                      |  
| day_length_nearh          | float   | train_merge_df, test_merge_df | Day duration in hours             |   
| sunrise_hours             | float   | train_merge_df, test_merge_df | Sunrise timing in hours                    |   
| sunset_hours              | float   | train_merge_df, test_merge_df | Sunset timing in hours                     |   
| yearweek                  | integer | train_merge_df, test_merge_df | Week number of the year                     |   
| weekpreciptotal           | float   | train_merge_df, test_merge_df | Weekly total precipitation                    |   
| weekavgtemp               | float   | train_merge_df, test_merge_df | Weekly average temperature                       |   
| r_humid                   | integer | train_merge_df, test_merge_df | Relative humidity                        |   
| templag1                  | float   | train_merge_df, test_merge_df | Temperature, lagged by 1 week (brought forward) |   
| templag2                  | float   | train_merge_df, test_merge_df | Temperature, lagged by 21 weeks (brought forward) |   
| templag3                  | float   | train_merge_df, test_merge_df | Temperature, lagged by 3 weeks (brought forward) |   
| templag4                  | float   | train_merge_df, test_merge_df | Temperature, lagged by 4 weeks (brought forward) |   
| rainlag1                  | float   | train_merge_df, test_merge_df | Rainfall, lagged by 1 week  |   
| rainlag2                  | float   | train_merge_df, test_merge_df | Rainfall, lagged by 2 weeks  |   
| rainlag3                  | float   | train_merge_df, test_merge_df | Rainfall, lagged by 3 weeks   |   
| rainlag4                  | float   | train_merge_df, test_merge_df | Rainfall, lagged by 4 weeks            |   
| humidlag1                 | float   | train_merge_df, test_merge_df | Relative humidity, lagged by 1 week  |   
| humidlag2                 | float   | train_merge_df, test_merge_df | Relative humidity, lagged by 2 weeks  |  
| humidlag3                 | float   | train_merge_df, test_merge_df | Relative humidity, lagged by 3 weeks   |   
| humidlag4                 | float   | train_merge_df, test_merge_df | Relative humidity, lagged by 4 weeks     |  
| mixed_tmax                | float   | train_merge_df, test_merge_df | The mean maximum temperature from both weather stations |   
| mixed_tmin                | float   | train_merge_df, test_merge_df | The mean minimum temperature from both weather stations |   
| mixed_precip_total        | float   | train_merge_df, test_merge_df | The mean maximum temperature from both weather stations |   
| mixed_weekpreciptotal     | float   | train_merge_df, test_merge_df | The mean weekly total precipitation from both weather stations |   
| mixed_weekavgtemp         | float   | train_merge_df, test_merge_df | The mean weekly average temperature from both weather stations  |   
| mixed_r_humid             | float   | train_merge_df, test_merge_df | The mean relative humidity from both weather stations |   
| stat_2_tmax               | integer | train_merge_df, test_merge_df | Max temperature at Station 2  |   |
| stat_2_tmin               | integer | train_merge_df, test_merge_df | Min temperature at Station 2   |   
| stat_2_tavg               | float   | train_merge_df, test_merge_df | Average temperature at Station 2    | 
| stat_2_precip_total       | float   | train_merge_df, test_merge_df | Total precipitation at Station 2      |  
| id                        | integer | test_merge_df                 | The ID of the record                        |  
| Date |datetime |spray_df|  Date of the spray|
| Time |object|spray_df| Time of the spray|
| Latitude|float|spray_df| Latitude of the spray|
| Longitude|float|spray_df| Longitude of the spray|



---

<br>
<br>

## Data Preprocessing
![Data Preprocessing](https://github.com/wxneo/GA_Projects/blob/main/Project_4/images/Data_Preprocessing.jpg)

We followed a rigorous data preprocessing pipeline consisting of three key steps. Firstly, we employed the **One Hot Encoder** technique to convert categorical data into **numerical format**, ensuring compatibility with our models. This transformation allowed us to effectively capture the information contained within the categorical variables.

Next, we applied the **Synthetic Minority Oversampling Technique (SMOTE)** to balance the target class distribution, aiming for a **50:50 ratio**. By oversampling the minority class, we addressed the issue of class imbalance and improved the performance of our models in handling the target variable.

In the final step of data preprocessing, we utilized the **Standard Scaler** method. This process involved transforming all features within the dataset to a **similar scale and distribution**. By doing so, we minimized the potential impact of varying feature magnitudes, allowing our models to better understand the relative importance of different features during the classification process.

## Modeling

![Modeling](https://github.com/wxneo/GA_Projects/blob/main/Project_4/images/Model_Workflow.jpg)

Following the data preprocessing stage, the preprocessed dataset was fed into a pipeline of five classification models: **logistic regression, random forest classifier, XGBoost, Adaboost, and Voting Classifier**. These models were carefully chosen based on their respective strengths and suitability for the classification task at hand. The use of multiple models allowed us to leverage their individual capabilities and ensemble them to make more robust predictions.

By employing this systematic approach, we aimed to enhance the quality and reliability of our classification results, enabling us to make informed decisions based on the predictions generated by the ensemble of models.


<br>
<br>

## Summary of Model Perforamance

|  | TPR<sup>1</sup> | TNR<sup>2</sup> | ROC(Train) | ROC(Test) |
|---|---|---|---|---|
| **Logistic Regression <br>(Baseline Model)** | 0.7802 | 0.7419 | 0.8670 | 0.8269 |
| **Random Forest Classifier** | 0.8352 | 0.7069 | 0.8597 | 0.8552 |
| **XGBoost Classifier** | 0.1319 | 0.9853 | 0.9238 | 0.8733 |
| **AdaBoost Classifier** | **0.7253** | **0.8124** | **0.8259** | **0.8564** |
| **Voting Classifier** | 0.6703 | 0.8443 | 0.8987 | 0.8645 |

<br>
1 - True Positive Rate or Sensitivity.

2 - True Negative Rate or Specificity.  
3 - Public Score on Kaggle.com (AUC)


---

<br>


## Key Recommendations

![Potential Cost Reduction](https://github.com/wxneo/GA_Projects/blob/main/Project_4/images/Potential_Cost_Reduction.jpg)

Leveraging the power of machine learning, we have developed an advanced predictive model to effectively combat the West Nile Virus. This innovative approach enables us to significantly reduce costs by an impressive 78.5%. We invite you to delve into the comprehensive details of our proposal outlined below, which showcase the technical prowess and formal methodologies employed in our solution.

| **Proposal** | **Proposal Evaluation**  |
| ------------------------ | -----------------------  |
|![Alt text](https://github.com/wxneo/GA_Projects/blob/main/Project_4/images/Proprosal.jpg)|![Alt text](https://github.com/wxneo/GA_Projects/blob/main/Project_4/images/Evaluation_of_Proposal.jpg) |

<br>

## (1) **Time** your effort
- May to October: Economist Approach
- November to April: Minimalist Approach

## (2) **Focus** on culex pipiens populated areas

## (3) **Initiate** localised social media campaign 


---
## Reference
(1) Center for Disease Control and Prevention <br>
https://www.cdc.gov/westnile/statsmaps/historic-data.html

(2) VDCI Mosquito Management <br> 
https://www.vdci.net/

(3) National Library of Medicine
<br> https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3945683/

(4) American Society of Tropical Medicine
<br> https://astmhpressroom.wordpress.com/journal/february-2014/

