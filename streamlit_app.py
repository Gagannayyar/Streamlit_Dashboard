import streamlit as st
import pandas as pd
#from transformers import pipeline
from textblob import TextBlob
#classifier = pipeline("summarization")
import time
import yake
kw_extractor = yake.KeywordExtractor(top=2, stopwords=None)


def get_sentiments(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment < 0:
        xpres = "Negative"
    elif sentiment > 0:
        xpres = "Positive"
    
        return st.write(f"{text} the sentiments are: {xpres}")

def get_keywords(text):
    keywords = kw_extractor.extract_keywords(text)
    return st.write(f"keywords: {keywords[:2]}") 



st.title("Mood Analyser")

input_file = st.file_uploader("Please upload a file")




if input_file is not None:
    df = pd.read_csv(input_file)
    st.write(df.head())
else:
    st.markdown("Please upload a file to proceed")

st.columns(1)
if input_file is not None:
    container = st.empty()
    for text in df['comments']:
        with container.container():
            get_sentiments(text)
            get_keywords(text)
            time.sleep(1)