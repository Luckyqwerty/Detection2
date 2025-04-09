import streamlit as st
import joblib
import tldextract

# Load model and vectorizer
model = joblib.load("best_phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# App title and config
st.set_page_config(page_title="Phishing Website Detector", layout="centered")
st.title("🔐 Phishing Website Detection using NLP")

# User input
url_input = st.text_input("🔗 Enter the website URL you want to check:")

# Button
if st.button("Check URL"):
    if not url_input.strip():
        st.warning("⚠️ Please enter a URL.")
    else:
        try:
            # Clean domain (optional step)
            ext = tldextract.extract(url_input)
            domain = f"{ext.domain}.{ext.suffix}" if ext.suffix else url_input

            # Transform the input URL
            url_vector = vectorizer.transform([url_input])

            # Predict
            prediction = model.predict(url_vector)[0]

            # Display result
            if prediction == 0:
                st.success("✅ Legitimate Website")
            else:
                st.error("🚨 Phishing Website Detected!")

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
