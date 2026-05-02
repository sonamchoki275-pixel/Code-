import streamlit as st
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load trained model and tokenizer
model = load_model("sentiment_model.keras")
tokenizer = joblib.load("tokenizer.pkl")

# App UI
st.title("Sentiment Analysis App")

user_input = st.text_area("Enter a review:")

if st.button("Analyse"):
    if user_input.strip() == "":
        st.warning("Please enter a review")
    else:
        sequence = tokenizer.texts_to_sequences([user_input])
        padded = pad_sequences(sequence, maxlen=100)
        prediction = model.predict(padded)
        score = prediction[0][0]

        if score >= 0.5:
            st.success("Positive review")
        else:
            st.error("Negative review")
