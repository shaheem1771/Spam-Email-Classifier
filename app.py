import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Spam Email Classifier", page_icon="📧")

st.title("📧 Spam Email Classifier")
st.write("Enter a message below to check if it's **Spam** or **Ham (Not Spam)**.")

# Input
message = st.text_area("✉️ Enter your message here:", height=150)

# Predict button
if st.button("🔍 Check"):
    if message.strip() == "":
        st.warning("Please enter a message first.")
    else:
        # Transform and predict
        transformed = tfidf.transform([message])
        prediction = model.predict(transformed)[0]

        if prediction == 1 or prediction == 'spam':
            st.error("🚨 This message is **SPAM!**")
        else:
            st.success("✅ This message is **Ham (Not Spam)**.")

st.markdown("---")
st.caption("Built with Scikit-learn & Streamlit | Muhammed Shaheem")
