import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.title("💪 Body Mass Index (BMI) Calculator")

st.write(
    "Calculate your **BMI** to determine whether you are underweight, normal, overweight, or obese. "
    "Simply enter your weight and height below."
)

st.sidebar.header("BMI Categories")
st.sidebar.info(
    "**Underweight:** BMI < 18.5\n"
    "**Normal weight:** 18.5 – 24.9\n"
    "**Overweight:** 25 – 29.9\n"
    "**Obese:** BMI ≥ 30"
)

weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (m)", min_value=0.1, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.subheader(f"📊 Your BMI: **{bmi:.2f}**")

        if bmi < 18.5:
            st.warning("⚠️ You are **Underweight**. Consider a balanced diet.")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ You have a **Normal weight**. Keep it up!")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are **Overweight**. Consider healthy lifestyle changes.")
        else:
            st.error("❌ You are **Obese**. Please consult a healthcare provider.")
    else:
        st.error("❗ Height must be greater than zero.")

st.markdown(
    """
    ---
    **Developed with ❤️ using Streamlit**  
    📌 *Note: This tool provides an estimate and should not replace professional medical advice.*  
    👨‍💻 Developed by **Muhammad Bilal Hussain**
    """
)
