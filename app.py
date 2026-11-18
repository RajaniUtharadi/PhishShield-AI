import streamlit as st
import joblib
from feature import extract_features

# Load model
model = joblib.load("model.pkl")

# Page config
st.set_page_config(
    page_title="PhishShield AI",
    page_icon="🛡️",
    layout="centered"
)

# Premium Styling
st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0f172a;
    color: white;
}

.stTextInput input {
    background-color: #1e293b;
    color: white;
    border-radius: 12px;
}

.stButton button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    background: linear-gradient(to right,#ff416c,#ff4b2b);
    color: white;
    font-size: 18px;
    border: none;
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    background: rgba(255,255,255,0.05);
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🛡️ PhishShield AI")
st.caption("AI-Powered Phishing URL Detection System")

# Input
url = st.text_input("Enter URL")

# Button
if st.button("Analyze URL"):

    features = extract_features(url)

    prediction = model.predict([features])[0]

    probability = model.predict_proba([features])[0][1]

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    if prediction == 1:
        st.error("⚠️ Phishing URL Detected")
    else:
        st.success("✅ Safe URL")

    st.progress(int(probability * 100))

    st.write(f"### Threat Score: {probability*100:.2f}%")

    st.write("### Extracted Features")
    st.write(features)

    st.markdown("</div>", unsafe_allow_html=True)