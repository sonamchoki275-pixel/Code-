import streamlit as st

st.title("Sentiment Analysis App")

st.write("Enter a product review below to predict the sentiment.")

review = st.text_area("Enter your review:")

if st.button("Predict Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        st.success("Prediction: Positive or Negative will appear here after model connection.")
