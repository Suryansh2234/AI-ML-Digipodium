import os
import streamlit as st
from joblib import load


MODEL_LOCATION = ["models/nb_model.joblib", "nbmodel.joblib"]
VECTORIZER_LOCATION = ["models/vectorizer.joblib", "vectorizer_model.joblib"]  


#goes through the list  of paths
def find_first(paths):
    for p in paths:
        if os.path.exists(p):
            return p
    return None



#streamlit page configuration
st.set_page_config(page_title="Spam Classifier", layout="centered")
st.title("Spam/Ham Classifier")


#load the model
model_path = find_first(MODEL_LOCATION)
vectorizer_path = find_first(VECTORIZER_LOCATION)

if model_path and vectorizer_path:
    try:
        model = load(model_path)
        vectorizer = load(vectorizer_path)
        st.sidebar.success(f"Loaded model from {os.path.basename(model_path)}and \
                           {os.path.basename(vectorizer_path)}")
    except Exception as e:
        st.sidebar.error(f"Error loading model: {e}")
        st.stop()
else:
    st.warning("Place nb_model.joblib and count_vectorizer.joblib in models/or project root folder")
    st.stop()


message = st.text_area(
    "Enter message to classify:",
    value =st.session_state.get("message", ""),
    key = "message",
    height=150
)

if st.button("Classify"):
    if not message.strip():
        st.warning("Please enter a message to classify.")
    else:
        try:
            X = vectorizer.transform([message])
            prediction = model.predict(X)[0]
            if prediction.lower() == "spam":
                st.error("The message is classified as: SPAM")
            else:
                st.success("The message is classified as: HAM")
            if hasattr(model,"predict_proba"):
                proba = model.predict_proba(X)[0]
                st.info(f"Prediction Probabilities - Ham: {proba[0]:.2f}, Spam: {proba[1]:.2f}")
        except Exception as e:
            st.error(f"Error during classification: {e}")

st.markdown("--------------")            

            