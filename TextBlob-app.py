from re import A
from typing import Text
import streamlit as st
from textblob import TextBlob
from PIL import Image
from newspaper import Article
from textblob import Word
import nltk
import pandas as pd
import plotly.express as px

nltk.download('omw-1.4')

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

col1, col2,col3 = st.columns([1,1,1])
col2.image(Image.open('KH.jpg'))

st.markdown('''
## Natural Language Processing Web Application
- **Python libraries:** streamlit, textblob, PIL, playsound, pandas, plotly.express

''')

user_words_input = st.sidebar.text_input('Please enter the word(s): ')
blob_user_words_input = TextBlob(user_words_input)
TextBlob_functions = ['word_counts','tags', 'noun_phrases', 'sentiment', 'definitions','count','correct','spellcheck']

if st.sidebar.button('tags'):
    st.write(blob_user_words_input.tags)
if st.sidebar.button('word counts'):
    st.write(blob_user_words_input.word_counts)
if st.sidebar.button('noun phrases'):
    st.write(blob_user_words_input.noun_phrases)
if st.sidebar.button('definitions'):
    for word in blob_user_words_input.words:
        w = Word(word.lower())
        st.write(w.definitions)
if st.sidebar.button('correct'):
    st.write(blob_user_words_input.correct())
if st.sidebar.button('spellcheck'):
    for word in blob_user_words_input.words:
        w = Word(word.lower())
        st.write(w.spellcheck())

user_url_input = st.sidebar.text_input('Please enter the URL')

def articleDownload(url):
    url = user_url_input
    article = Article(url)
    article.download()
    article.parse()
    text = article.text
    return text

amount_word = st.sidebar.slider('Amount of words')
if st.sidebar.button('plot words frequency from url'):
    blob = TextBlob(articleDownload(user_url_input))
    frequency = pd.DataFrame.from_dict(
        blob.word_counts, orient='index', columns=['count']
    )
    plot = px.bar(
        frequency.sort_values(by='count', ascending=False)
    )
    st.dataframe(frequency.sort_values(by=['count'], ascending=False).transpose())
    st.area_chart(frequency[:amount_word])





