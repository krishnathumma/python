import streamlit as st
from send_mail import send_mail

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Please Enter Email")
    message = st.text_area("Your Message")
    message = message + "\n" + user_email
    button = st.form_submit_button()
    if button:
        send_mail(message)