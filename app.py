# app.py
import streamlit as st

import streamlit as st

@st.cache_resource
def load_predict():
    from src.predict import predict_yield
    return predict_yield

predict_yield = load_predict()

st.set_page_config(page_title="Mushroom Yield Forecast", layout="centered")
st.title("Polyhouse Yield Predictor")
st.caption("Agritech environmental forecasting from sensor data")

with st.sidebar:
    st.header("Sensor readings")
    temp = st.slider("Temperature (°C)", 10.0, 35.0, 22.0, 0.1)
    humid = st.slider("Humidity (%)", 50.0, 100.0, 88.0, 0.5)
    co2 = st.slider("CO₂ (ppm)", 400, 2000, 920, 10)

if st.button("Predict yield"):
    kg = predict_yield(temp, humid, co2)
    st.metric(label="Estimated daily yield", value=f"{kg:.2f} kg")