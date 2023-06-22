import pandas as pd
import numpy as np
import streamlit as st
import pickle
from pathlib import Path
import os
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

# Import for string manipulations
import re
import string
import nltk
nltk.download('wordnet')
nltk.download('stopwords')

# Vectorization import
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# For Sentiment Analysis
from textblob import TextBlob
import altair as alt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Plot the top 20 bar chart
def plot_horizontal_barplot(data, title):
    data_sorted = data.sort_values(by='coefficient', ascending=False)  # Sort the data in descending order
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=data_sorted['coefficient'],
        y=data_sorted['word'],
        orientation='h',
        marker_color='steelblue'
    ))
    fig.update_layout(
        title=title,
        xaxis_title='Coefficient',
        yaxis_title='Word',
        yaxis=dict(autorange="reversed"),  # Reverse the y-axis to display in descending order
        height=500,  # Set the figure height
        width=320,  # Set the figure width
        autosize=False  # Disable autosizing of the figure
    )
    st.plotly_chart(fig)

# Create a function to analyze token sentiment
def analyze_token_sentiment(docx):
    analyzer = SentimentIntensityAnalyzer()
    pos_list = []
    neg_list = []
    neu_list = []
    for i in docx.split():
        res = analyzer.polarity_scores(i)['compound']
        if res >= 0.1:
            pos_list.append(i)
            pos_list.append(res)
        elif res <= -0.1:
            neg_list.append(i)
            neg_list.append(res)
        else:
            neu_list.append(i)
            
    return {
        'positive': pos_list,
        'negative': neg_list,
        'neutral': neu_list
    }

# Create a function to convert sentiment results to DataFrame
def convert_to_df(sentiment):
    sentiment_dict = {
        'polarity': sentiment.polarity,
        'subjectivity': sentiment.subjectivity
    }
    sentiment_df = pd.DataFrame(sentiment_dict.items(),columns=['metric','value'])
    return sentiment_df

# Define a function that removes puntuation, tokenise the string & remove stopwords
def clean_text(text):
    
    extra_stopwords = ['subreddit', 'subreddits', 
#                    'show', 'like', 'episode',
#                    'would', 'character','one', 'think', 'season', 'time',
#                    'get', 'favourite', 'say', 'really', 'im', 'first',
#                     # Round 2
#                    'know', 'favorite', 'see', 'make', 'anyone', 'also',
#                    'love', 'got',
#                     # Round 3
#                    'series', 'much', 'could', 'dont', 'way',
#                     #Round 4
#                    'thing', 'watching', 'go',
#                     #Round 5
#                    'watch', 'thought',
#                     # Round 6
#                    'guy', 'always',
#                     # Round 7
#                    'character', 'else', 'even',
#                     # Round 8
#                    'want',
#                     # Round 9
#                    'something', 'feel',
#                     # Round 10
#                    'year',
#                     # Round 11
#                    'good',
#                     # Round 12
#                    'still',
#                     # Round 13
#                    'best', 'made',
#                     # Not a text
#                    'ampx200b'
                      ] 
    
    # Define Stopwords & initiate Lematizer
    stopwords = nltk.corpus.stopwords.words('english') + extra_stopwords
    wn = nltk.WordNetLemmatizer()
    
    # Punctuation removal.
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    
    # Tokenisation.
    # \W matches any non-word character (equivalent to [^a-zA-Z0-9_]). This does not include spaces i.e. \s
    # Add a + just in case there are 2 or more spaces between certain words
    tokens = re.split('\W+', text)
    
    # Apply lemmatisation and stopwords exclusion within the same step.
    text = [wn.lemmatize(word) for word in tokens if word not in stopwords]
    # Run stopwords removal again after lemmatizing
    text = [word for word in text if word not in stopwords]
    return text

def main():
    st.title("Project 3: Unveiling the Recipe for Comedy Success! 🎭")
    st.subheader("Brooklyn Nine Nine :cop: or :male-technologist: Big Bang Theory")

    menu = ["Home","Others"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Specify the relative path to the image files
    image_path_b99 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/B99_Image.jpg")
    image_path_bbt = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/BBT_Image.jpg")

    # Open the images using the relative paths
    b99 = Image.open(image_path_b99)
    bbt = Image.open(image_path_bbt)

    if choice == "Home":
        st.subheader("Home")
        with st.form(key='nlpForm'):
            raw_text = st.text_area("Enter your comments for either one of the show here:")
            submit_button = st.form_submit_button("Send")
        
        # Layout
        col1, col2, col3 = st.columns(3)
        container1 = st.container()
        col4, col5 = st.columns(2)
        col6, col7 = st.columns(2)
        
        if submit_button:

            # Retrieving model file
            model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mnm_tf_model.pkl")
            try:
                with open(model_path, 'rb') as file:
                        model = pickle.load(file)
            except FileNotFoundError:
                st.error("Failed to load the model file. Make sure it exists in the current directory.")
            
            # Reshape the input to a 2D array
            raw_text_2d = np.array([raw_text])
            y_pred = model.predict(raw_text_2d)
            y_pred_proba = model.predict_proba(raw_text_2d)
            
            # Extract scalar values from the pred_proba array
            bbt_proba = y_pred_proba[:, 0].item()
            b99_proba = y_pred_proba[:, 1].item()
            
            # Extract Feature name
            best_model_feature_names = model['tf'].get_feature_names_out()

            # feature log probabilities for class 1
            best_model_class1 = model['nb'].feature_log_prob_[1]
            best_model_class1_df=pd.DataFrame(data=[best_model_class1], columns=best_model_feature_names)

            # feature log probabilities for class 0
            best_model_class0 = model['nb'].feature_log_prob_[0]
            best_model_class0_df = pd.DataFrame(data=[best_model_class0], columns=best_model_feature_names)

            # calc the difference between class 1 and class 0 coefs
            best_b99 = best_model_class1_df - best_model_class0
            best_bbt = best_model_class0_df - best_model_class1
            
            # Extract the top 20 most predictive words
            b99_top20 = pd.DataFrame(best_b99.max().sort_values(ascending=False).head(20)).reset_index()
            bbt_top20 = pd.DataFrame(best_bbt.max().sort_values(ascending=False).head(20)).reset_index()
            b99_top20.columns = ['word','coefficient']
            bbt_top20.columns = ['word','coefficient']
            
            with col1:
                st.write(' ')

            with col2:
                if y_pred == 0:
                    st.image(bbt, caption = 'Big Bang Theory')
                    container1.markdown(f'The Machine Learning Model predicted Big Bang Theory at {(bbt_proba*100):.2f}% probability.')
                else:
                    st.image(b99, caption = 'Brooklyn Nine Nine')
                    container1.markdown(f'The Machine Learning Model predicted Brooklyn Nine Nine at {(b99_proba*100):.2f}% probability.')
            
            with col3:
                st.write(' ')
            
            with col4:
                plot_horizontal_barplot(b99_top20, 'Brooklyn Nine Nine Top 20 predictive words')
            
            with col5:
                plot_horizontal_barplot(bbt_top20, 'Big Bang Theory Top 20 predictive words')
            
            with col6:
                st.info("Sentiment Results")
                sentiment = TextBlob(raw_text).sentiment
                st.write(sentiment)
                
                # emoji
                if sentiment.polarity > 0:
                    st.markdown('Sentiment: Positive :blush:')
                elif sentiment.polarity < 0:
                    st.markdown('Sentiment: Negative :disappointed:')
                else:
                    st.markdown('Sentiment: Neutral :neutral_face:')
                    
                # Convert results to DataFrame
                result_df = convert_to_df(sentiment)
                st.dataframe(result_df)
                
                # Visualisation
                c = alt.Chart(result_df).mark_bar().encode(
                    x='metric',
                    y='value',
                    color='metric'
                )
                st.altair_chart(c,use_container_width=True)

            with col7:
                st.info('Token Sentiment')
                
                token_sentiments = analyze_token_sentiment(raw_text)
                st.write(token_sentiments)
                
    if choice == "Others":
        st.subheader("🚧 Under Construction! 🚧")
        st.markdown("Reserved for future updates.")
        

if __name__ == '__main__':
    main()
