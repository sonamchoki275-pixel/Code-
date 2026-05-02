import streamlit as st
import pickle
import string

# Load saved model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Simple cleaning function
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

# App title
st.title("Sentiment Analysis App")

st.write("Enter a product review to check if it is Positive or Negative.")

# Input box
review = st.text_area("Enter your review:")

# Button
if st.button("Predict Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        clean_review = clean_text(review)
        review_vector = vectorizer.transform([clean_review])
        prediction = model.predict(review_vector)[0]

        st.success(f"Prediction: {prediction}")
