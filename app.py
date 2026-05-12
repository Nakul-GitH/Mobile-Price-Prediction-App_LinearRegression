import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="Mobile Price Prediction",
    page_icon="📱",
    layout="wide"
)

# ==============================
# LOAD MODEL & SCALER
# ==============================

model = joblib.load("mobile_price_model.pkl")
scaler = joblib.load("scaler.pkl")

# Load feature importance
feature_importance = pd.read_csv("feature_importance.csv")

# ==============================
# TITLE
# ==============================

st.title("📱 Mobile Price Prediction App")

st.markdown("""
Predict mobile prices based on technical specifications.
""")

# ==============================
# INPUT SECTIONS
# ==============================

st.sidebar.header("Enter Mobile Specifications")

# --------------------------------
# SALES
# --------------------------------

sale = st.sidebar.slider("Sale", 10, 10000, 500)

# --------------------------------
# DISPLAY SPECIFICATIONS
# --------------------------------

st.subheader("📱 Display Specifications")

col1, col2 = st.columns(2)

with col1:
    resolution = st.slider("Resolution", 1.4, 12.2, 5.5)

    ppi = st.slider("PPI", 121, 806, 300)

with col2:
    weight = st.slider("Weight", 66.0, 753.0, 150.0)

    thickness = st.slider("Thickness", 5.1, 18.5, 8.0)

# --------------------------------
# HARDWARE SPECIFICATIONS
# --------------------------------

st.subheader("⚙ Hardware Specifications")

col3, col4 = st.columns(2)

with col3:

    cpu_core = st.selectbox(
        "CPU Core",
        options=[1, 2, 4, 6, 8]
    )

    cpu_freq = st.slider("CPU Frequency", 0.5, 3.0, 2.0)

with col4:

    internal_mem = st.selectbox(
        "Internal Memory (GB)",
        options=[0.004, 0.128, 0.256, 4, 8, 16, 32, 64, 128],
        index=5
    )

    ram = st.selectbox(
        "RAM (GB)",
        options=[0.004, 0.008, 0.032, 0.128, 0.512, 1, 1.5, 2, 3, 4, 6],
        index=9
    )

# --------------------------------
# CAMERA SPECIFICATIONS
# --------------------------------

st.subheader("📸 Camera Specifications")

col5, col6 = st.columns(2)

with col5:
    rear_cam = st.slider("Rear Camera", 0.0, 23.0, 12.0)

with col6:
    front_cam = st.slider("Front Camera", 0.0, 20.0, 8.0)

# --------------------------------
# BATTERY SPECIFICATIONS
# --------------------------------

st.subheader("🔋 Battery Specifications")

battery = st.slider("Battery", 800, 9500, 4000)

# ==============================
# CREATE INPUT DATAFRAME
# ==============================

input_df = pd.DataFrame({
    'Sale': [sale],
    'weight': [weight],
    'resolution': [resolution],
    'ppi': [ppi],
    'cpu core': [cpu_core],
    'cpu freq': [cpu_freq],
    'internal mem': [internal_mem],
    'ram': [ram],
    'RearCam': [rear_cam],
    'Front_Cam': [front_cam],
    'battery': [battery],
    'thickness': [thickness]
})

# ==============================
# DISPLAY INPUTS
# ==============================

st.subheader("📋 Input Preview")

st.dataframe(input_df)

# ==============================
# APPLY LOG TRANSFORMATION
# ==============================

skewed_cols = ['Sale', 'weight', 'internal mem', 'battery']

for col in skewed_cols:
    input_df[col] = np.log1p(input_df[col])

# ==============================
# SCALE INPUT
# ==============================

input_scaled = scaler.transform(input_df)

# ==============================
# PREDICT BUTTON
# ==============================

if st.button("Predict Mobile Price"):

    prediction = model.predict(input_scaled)

    # ==============================
    # DISPLAY PREDICTION
    # ==============================

    st.subheader("💰 Predicted Mobile Price")

    col1, col2, col3 = st.columns(3)

    with col2:
        st.metric(
            label="Estimated Price",
            value=f"₹ {prediction[0]:,.2f}"
        )


# ==============================
# FEATURE IMPORTANCE SECTION
# ==============================

st.subheader("📊 Feature Importance")

st.write("Features influencing mobile price prediction.")

st.bar_chart(
    feature_importance.set_index("Feature")["Coefficient"]
)


# ==============================
# FOOTER
# ==============================

st.markdown("---")

st.markdown("Developed by Nakul Gupta using Streamlit & Machine Learning")