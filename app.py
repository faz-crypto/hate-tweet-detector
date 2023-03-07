
import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

count = pickle.load(open('vectorizer.pkl','rb'))
log_model = pickle.load(open('model.pkl','rb'))

st.title("Hate Tweet Detection")

input_tweet = st.text_area("Enter the tweet")

if st.button('Predict'):

    # 1. preprocess
    transformed_tweet = transform_text(input_tweet)
    # 2. vectorize
    vector_input = count.transform([transformed_tweet])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Hate Tweet")
    else:
        st.header("Not Hate Tweet")

