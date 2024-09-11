import streamlit as st
import pandas as pa
from send_mail import send_mail


data = pa.read_csv("topics.csv")
topic= []
with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    for index, row in data.iterrows():
        topic.append(row['topic'])
        print(topic)
    option = st.selectbox("What Topic do you want to discuss?", topic)
    raw_message = st.text_area("Your Message")
    message = f"""\n
    Subject: New Mail from {user_email}
From : {user_email}
Topic: {option}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_mail(message)
