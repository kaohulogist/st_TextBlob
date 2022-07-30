from re import A
from typing import Text
import streamlit as st
from textblob import TextBlob
from PIL import Image
from newspaper import Article
from textblob import Word
import nltk
nltk.download('omw-1.4')

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

col1, col2,col3 = st.columns([1,1,1])
col2.image(Image.open('KH.jpg'))

st.markdown('''
## Natural Language Processing Web Application
- **Python libraries:** streamlit, textblob, PIL, playsound

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
    
user_url_input = st.sidebar.text_input('Please enter the URL')

