import streamlit as st
from model import predict_news

# Page config
st.set_page_config(page_title="Fake News Detector")

st.title("📰 Fake News Detector")

st.write("Enter a news headline/article to check if it is Fake or Real.")

user_input = st.text_area("Enter News Text")

if st.button("Check News"):
    if user_input:
        result = predict_news(user_input)

        if result == "Fake":
            st.error("🚨 This news looks FAKE!")
        else:
            st.success("✅ This news looks REAL!")
    else:
        st.warning("Please enter some text.")