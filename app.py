import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('best_model.pkl')

st.title(" Health Crystal Ball")
st.subheader("AI Health Risk Predictor")

# Inputs
age = st.number_input("Age", 1, 100)
gender = st.selectbox("Gender", ["Male", "Female"])
tb = st.number_input("Total Bilirubin")
db = st.number_input("Direct Bilirubin")
alk = st.number_input("Alkaline Phosphotase")
alt = st.number_input("ALT")
ast = st.number_input("AST")
tp = st.number_input("Total Proteins")
alb = st.number_input("Albumin")
agr = st.number_input("A/G Ratio")

# Convert gender
gender = 1 if gender == "Male" else 0

# Prediction
if st.button("Predict"):
    data = np.array([[age, gender, tb, db, alk, alt, ast, tp, alb, agr]])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Liver Disease")
    else:
        st.success("✅ Low Risk")