import streamlit as st
import pickle
import string

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

st.title("Sentiment Analysis App")

review = st.text_area("Enter a product review:")

if st.button("Predict Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        clean_review = clean_text(review)
        review_vector = vectorizer.transform([clean_review])
        prediction = model.predict(review_vector)[0]
        st.success(f"Prediction: {prediction}")
