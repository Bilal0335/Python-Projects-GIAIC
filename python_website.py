import streamlit as st

st.set_page_config(page_title="Python Web App", page_icon="🚀", layout="centered")

st.title('🚀 Welcome to My Python Website Project')

st.header('🌟 Project Overview')
st.write('This is a **simple and interactive** website built using Streamlit.')

if st.button("Click Me!"):
    st.success('🎉 Thank You for Clicking!')

name = st.text_input("👤 What is your name?")

if st.button("Greet Me!"):
    if name:
        st.write(f"👋 Hello, {name}! Welcome to my website project.")
    else:
        st.warning("⚠️ Please enter your name before clicking!")

st.write("💡 Did you know? Streamlit makes Python web apps easy!")

st.markdown(
    """
    ---
    🚀 **Innovate. Code. Build.**  
    👨‍💻 Created by **Muhammad Bilal Hussain** | Powered by **Streamlit**  
    📌 *Explore more projects and keep coding!*
    """
)
