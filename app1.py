'''
SUML Task 4.2
s18465
'''
import pickle
from datetime import datetime
import streamlit as st

startTime = datetime.now()

FILENAME = "model.sv"
model = pickle.load(open(FILENAME, 'rb'))

sex_d = {0: "Female", 1: "Male"}
chest_pain_type_d = {0: "ASY", 1: "ATA", 2: "NAP", 3: "TA"}
fasting_bs_d = {0: "No", 1: "Yes"}
resting_ecg_d = {0: "LVH", 1: "Normal", 2: "ST"}
exercise_angina_d = {0: "No", 1: "Yes"}


def main():
    st.set_page_config(page_title="Task 4.2 | s18465")
    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    st.image("https://i.makeagif.com/media/8-24-2021/mtvF9V.gif")

    with overview:
        st.title("Task 4.2 - s18465")

    with left:
        sex_radio = st.radio("Sex", list(sex_d.keys()),format_func=lambda x: sex_d[x])
        chest_pain_radio = st.radio("Chest Pain Type", list(chest_pain_type_d.keys()),format_func=lambda x: chest_pain_type_d[x])
        fasting_bs_radio = st.radio("Fasting Blood Sugar > 120 mg/dl", list(fasting_bs_d.keys()),format_func=lambda x: fasting_bs_d[x])
        resting_ecg_radio = st.radio("Resting Electrocardiographic Results", list(resting_ecg_d.keys()),format_func=lambda x: resting_ecg_d[x])
        exercise_angina_radio = st.radio("Exercise Induced Angina", list(exercise_angina_d.keys()),format_func=lambda x: exercise_angina_d[x])

    with right:
        age_slider = st.slider("Age", min_value=28, max_value=77)
        restingbp_slider = st.slider("Resting Blood Pressure", min_value=80, max_value=200)
        cholesterol_slider = st.slider("Cholestoral in mg/dl", min_value=85, max_value=603)
        max_hr_slider = st.slider("Maximum Heart Rate", min_value=60, max_value=202)
        oldpeak_slider = st.slider("Previous Peak", min_value=0.0, max_value=7.0, step=0.1)

    data = [[age_slider, sex_radio, chest_pain_radio, restingbp_slider, cholesterol_slider, fasting_bs_radio, resting_ecg_radio, max_hr_slider, exercise_angina_radio, oldpeak_slider]]
    heart_disease = model.predict(data)
    confidence = model.predict_proba(data)

    with prediction:
        st.subheader("Heart Disease Prediction")
        st.subheader(("Yes" if heart_disease[0] == 1 else "No"))
        st.write("Prediction confidence {0:.2f} %".format(confidence[0][heart_disease][0] * 100))


if __name__ == "__main__":
    main()
