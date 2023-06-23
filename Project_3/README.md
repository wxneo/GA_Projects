# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Unveiling the Recipe for Comedy Success: Analyzing Viewer Preferences and Sentiment towards Popular Sitcoms

### **Try Out our B99 vs BBT Classifier Application Streamlit App by clicking the link below.**
### [Brooklyn's Nine Nine and The Big Bang Theory Classifier and Sentiment Analysis](https://project-3-recipe-for-comedy-success-tj0ysfqfwsi.streamlit.app/)

<br>

![Brooklyn's Nine Nine](https://github.com/khammingfatt/Project-3-Quantifying-TV-Laughter/blob/main/B99_Image.jpg?raw=true)

<br>

## Content Directory:
### Contents:
- [Background](#Background)
- [Data Import & Cleaning](#Data-Import-&-Cleaning)
- [Feature Engineering](#Feature-Engineering)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
    - [Sentiment Analysis](#Sentiment-Analysis)
- [Modeling](#Modeling)
    - [Fine Tuning of Best Models](#Fine-Tuning-of-Best-Models)
- [Key Insights & Recommendations](#Key-Insights-&-Recommendations)
- [Reference](#reference)

<br>


## Background
The streaming services market has witnessed significant growth in recent years, revolutionizing the way people consume entertainment content. With the advent of high-speed internet and advancements in technology, streaming platforms have become increasingly popular, offering a wide range of TV shows, movies, and original content to millions of subscribers worldwide.

Leading the industry is Netflix, with an impressive subscriber base of 223.09 million, followed closely by Prime Video with over 200 million subscribers. These platforms provide extensive libraries of content, personalized recommendations, and user-friendly interfaces to enhance the streaming experience.

Disney+ quickly gained traction after its 2019 launch, amassing 164.2 million subscribers by leveraging Disney's iconic franchises and family-friendly content. HBO Max, backed by WarnerMedia, offers a premium streaming experience with its diverse catalog of original series, blockbuster movies, and exclusive streaming rights.

The competition among these major players reflects the growing demand for on-demand content and the convenience of streaming platforms. As the market evolves, it presents immense opportunities for content creators, production studios, and consumers alike, shaping the future of entertainment consumption.

<br>


## Problem Statement
Netflix aims to optimize their limited budget by retaining the most popular and engaging sitcom for their platform. To make an informed decision, they require an efficient machine learning solution that can accurately classify and analyze user comments from various platforms, paricularly two famous sitcom "Big Bang Theory" and "Brooklyn Nine Nine." The goal is to develop an infrastructure that can effectively identify which show the viewers' comments are referring to and analyze the sentiments expressed towards each show. This solution will enable the streaming company to gain valuable insights into viewers' preferences, aiding them in determining the sitcom to retain, maximizing viewer satisfaction and engagement within the budgetary constraints.

	(1) Identify what show elements in the sitcom are popular among the viewers

	(2) To build an infrastructure that can help to classify and analyse user's comments about the show from various platforms


<br>
<br>

---

## Datasets:
* [`bigbangtheory_hot_full.csv`](../data/bigbangtheory_hot_full.csv): this data contains all of the posts scraped from the subreddit 'r/bigbangtheory' with the 'hot' tag
* [`brooklynninenine_hot_full.csv`](../data/brooklynninenine_hot_full.csv): this data contains all of the posts scraped from the subreddit 'r/brooklynninenine' with the 'hot' tag

<br>

### Brief Description of Our Data Exploration
Upon studying the datasets, we found out that these are the most important 10 factors that affects the housing price are given as below. Starting from the most important factor, we have floor area per square feet, max floor level and lease commence date.
 
![SHAP Importance of Variables](https://github.com/khammingfatt/Project-3-Quantifying-TV-Laughter/blob/main/SHAP.png?raw=true)
<br>

We went further and break down the important features to classify the two shows separately and here are the details we get. The more positive the coefficient values, the more likely it is classified to Class 1 - Brooklyn's Nine Nine; On the other hand, the more negative the coefficient values, the more likely it is classified to Class 0 - The Big Bang Theory.

<br>

| **Brooklyn's Nine Nine** | **The Big Bang Theory**  |
| ------------------------ | -----------------------  |
| ![Brooklyn's Nine Nine](https://github.com/khammingfatt/Project-3-Quantifying-TV-Laughter/blob/main/Feature%20Importance%20B99.png?raw=true)| ![The Big Bang Theory](https://github.com/khammingfatt/Project-3-Quantifying-TV-Laughter/blob/main/Feature%20Importance%20BBT.png?raw=true) |

<br>

## Data Dictionary
| **Feature**         | **Type** | **Dataset**  | **Description**                                                  |
|---------------------|----------|--------------|------------------------------------------------------------------|
| **posts**           | object   | sitcom_df    | Combination of the reddit post title & the text in the main post |
| **subreddit_**      | interger | sitcom_df    | Target feature, where 0 = Big Bang Theory, 1 = Brooklyn Nine Nine|
| **len_posts**       | interger | sitcom_df    | Number of characters in a post                                   |
| **post_word_count** | integer  | sitcom_df    | Number of words in a post                                        |
| **emojis**          | objects  | sitcom_df    | Emojis found in a post                                           |
| **num_emojis**      | interger | sitcom_df    | Number of emojis found in a post                                 |
| **neg**             | interger | sitcom_df    | Negative sentiment values                                        |
| **neu**             | interger | sitcom_df    | Neutral sentiment values                                         |
| **pos**             | interger | sitcom_df    | Positive sentiment values                                        |
| **compound**        | interger | sitcom_df    | Compound sentiment values                                        |


---

<br>
<br>

## Modeling

In the field of Natural Language Processing (NLP), several techniques are employed to process and analyze textual data. These techniques play a crucial role in extracting meaningful information and insights from text documents. In our project, we applied various NLP techniques to preprocess and analyze the data.

**Tokenization** is the first step in NLP, where a text document is divided into smaller units called tokens. These tokens can be words, sentences, or even subwords, depending on the level of granularity required. By breaking down the text into tokens, we gain a better understanding of the underlying structure and can perform further analysis on individual units.

**Stopword removal** is another important step in NLP. Stopwords are common words that do not carry significant meaning in a given context, such as articles (e.g., "a", "an", "the"), pronouns, and prepositions. Removing stopwords helps to reduce noise and focus on the more relevant and informative words in the text.

**Lemmatization** is a technique used to reduce words to their base or dictionary form, known as the lemma. It helps to standardize words by considering their morphological variations, such as different verb tenses or plural forms. By lemmatizing words, we ensure that similar forms of a word are treated as the same, which aids in effective text analysis and understanding.

Upon finished preprocessing the input, we are ready to deploy our data into **Machine Learning**.

<br>

![Model Workflow](https://github.com/khammingfatt/Project-3-Recipe-for-Comedy-Success/blob/main/Modeling%20Workflow.png?raw=true)


With reference to the workflow above, we used **vectorization techniques**. Vectorization involves transforming text data into numerical representations that machine learning models can process. One common approach is the **Count Vectorisation Model**, where each word in the text is represented as a separate feature, and the frequency or occurrence of each word is captured. Another approach is **Term Frequency-Inverse Document Frequency (TF-IDF)**, which considers not only the frequency of a word in a document but also its importance in the entire corpus.

Upon finished running the model, we ran a total of 17 combinations of models with more than 1,000 hyperparameters tuning by using **GridSearchCV**. Eventually, the Mutilnomial with Naive Bayes + TF-IDF with GridSearchCV turned out to be the best performed model of all and we are deploying the model into our Streamlit Applications.



<br>
<br>

## Summary of Model

|  | Accuracy (Train) | Accuracy (Test) | Cross Validation Score |
|---|---|---|---|
| Baseline Model | 0.520833 | 0.520833 | NA |
| Multinomial(NB) + CountVect + GridSearchCV | 0.97050 | 0.90653 | 0.88123 |  |  |
| Logistic Regression + TF-IDF + GridSearchCV | 0.97957 | 0.90652 | 0.87368 |  |
| **(Best Model)**<br>**Multinomial(NB) + TF-IDF + GridSearchCV** | **0.98865** | **0.92063** | **0.87973** |

---

<br>




## Key Insights
### Overall 
* Viewers frequently engage in discussions about popular show elements such as Cold Open, Halloween Heist, and potential sequels.
* Topics that garner significant attention from viewers include their favorite characters and least favorite scenes.
* Viewers actively discuss sitcom characters in their comments about the shows. 

### Brooklyn's Nine Nine
* 'Scene' is commonly mentioned in Brooklyn's Nine Nine
* 'Halloween' and 'Heist' is identified as a very popular topic among reddit users
* 'Cold Open' is identified as a unique X-factor of B99

### The Big Bang Theory
* ‘Sheldon’ has very strong impact on viewers in the show
* 'Season' is commonly mentioned in Big Bang Theory
* ‘Young’ is seen on BBT very often due to sequel of Young Sheldon



## Key Recommendations
 
	(1) Create memorable and likable characters to enhance viewer engagement.
	(2) Utilize the "Cold Open" narrative technique, which is widely discussed by viewers.
	(3) Incorporate periodic special events within the show to generate anticipation and excitement among viewers. 

## Future Work
	(1) Model can be expanded to Multi-Class Classification
	(2) Further collect text inputs from other sources periodically
	(3) To analyse further sentiments, we will no longer limit the number of posts to be even

---
## Reference
(1) The source of data for comments and posts for Brooklyn's Nine Nine <br>
https://www.reddit.com/r/brooklynninenine/

(2) The source of data for comments and posts for The Big Bang Theory <br> https://www.reddit.com/r/bigbangtheory/

(3) Preferred digital video content by genre in the U.S. as of March 2023
<br> https://www.statista.com/forecasts/997166/preferred-digital-video-content-by-genre-in-the-us#:~:text=%22Comedies%22%20and%20%22Dramas%22,the%20United%20States%2C%20in%202023

(4) Importance of Video Streaming Attributes
<br> https://www.nielsen.com/insights/2020/playback-time-which-consumer-attitudes-will-shape-the-streaming-wars/

(5) Reasons for Subcribing to Additional Paid Video Streaming Services
<br>  https://www.nielsen.com/insights/2020/playback-time-which-consumer-attitudes-will-shape-the-streaming-wars/

(6) Most Attractive Features of Video Streaming Service
<br> https://www.cloudwards.net/streaming-services-statistics/

(7) Top Reasons to Subscribe to a New Streaming Service
<br> https://www.cloudwards.net/streaming-services-statistics/

(8) Streaming Industry Digital Market Share
<br> https://www.similarweb.com/blog/insights/media-entertainment-news/streaming-q1-2023/#:~:text=The%20streaming%20industry%20has%20shown,in%20a%20post%2Dpandemic%20world

(9) Singaporeans Asked if They Would Discontinue Their Current Streaming Services in The Next 6 Months.
<br> https://blackbox.com.sg/everyone/streaming-services-in-singapore
