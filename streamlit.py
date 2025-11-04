import streamlit as st

st.write("hello")
x = st.text_input("What's your favourite sport?")
st.write("Your favourite sport is:",x)
click = st.button("Click here")