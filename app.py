import streamlit as st

st.title("My First Data App")
st.header(" I am SHAMBHAVI")
st.subheader("WELCOME TO MY PAGE")
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader('HAPPY :blue[ ME] :sunglasses:')
    st.balloons()