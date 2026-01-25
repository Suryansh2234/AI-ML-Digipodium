import os
import streamlit as st
from joblib import load 

MODEL_LOCATION = ["model/diamond_price_predictor.joblib", "diamond_price_predictor.joblib"]
#goes through the list  of paths
def find_first(paths):
    for p in paths:
        if os.path.exists(p):
            return p
    return None
#streamlit page configuration
st.set_page_config(page_title="Diamond Price Predictor", layout="centered")
st.title("Diamond Price Predictor")
#load the model
model_path = find_first(MODEL_LOCATION)
if model_path:
    try:
        model = load(model_path)
        st.sidebar.success(f"Loaded model from {os.path.basename(model_path)}")
    except Exception as e:
        st.sidebar.error(f"Error loading model: {e}")
        st.stop()
else:
    st.warning("Place diamond_price_predictor.joblib in models/or project root folder")
    st.stop()

carat = st.number_input("Carat:", min_value=0.0, step=0.01, value=0.5)
depth = st.number_input("Depth (%):", min_value=0.0, step=0.1, value=61.5)
table = st.number_input("Table (%):", min_value=0.0, step=0.1, value=55.0)
x = st.number_input("Length (mm):", min_value=0.0, step=0.1, value=5.0)
y = st.number_input("Width (mm):", min_value=0.0, step=0.1, value=5.0)
z = st.number_input("Depth (mm):", min_value=0.0, step=0.1, value=3.0)
if st.button("Predict Price"):
    try:
        features = [[carat, depth, table, x, y, z]]
        prediction = model.predict(features)[0]
        st.success(f"The predicted price of the diamond is: ${prediction:,.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")



