import streamlit as st

st.title("🎓 Student Performance Predictor")
st.write("This is my ML project")

import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("🎓 Student Performance Predictor")

st.write("Enter student details:")

study_hours = st.slider("Study Hours", 0, 12, 5)
attendance = st.slider("Attendance (%)", 0, 100, 75)
sleep = st.slider("Sleep Hours", 0, 12, 7)
social_media = st.slider("Social Media (hrs)", 0, 10, 3)
mental_health = st.slider("Mental Health (1-10)", 1, 10, 5)

if st.button("Predict"):
    data = np.array([[study_hours, attendance, sleep, social_media, mental_health]])
    result = model.predict(data)

    if result[0] == 1:
        st.success("Good Performance 🎉")
    else:
        st.error("Needs Improvement 📉")
