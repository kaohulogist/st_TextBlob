import streamlit as st
from textblob import TextBlob
from PIL import Image


with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

col1, col2,col3 = st.columns([1,1,1])
col2.image(Image.open('KH.jpg'))

st.markdown('''
## Natural Language Processing Web Application
- **Python libraries:** streamlit, textblob, PIL, playsound

''')

user_words_input = TextBlob(st.sidebar.text_input('Please enter the word(s): '))

st.sidebar.multiselect('NLPK features:', ['tags', 'noun_phrases', 'sentiment', 'definitions','count','correct','spellcheck'])



