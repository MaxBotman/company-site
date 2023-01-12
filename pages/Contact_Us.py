import streamlit as st
import pandas as pd
from send_email import send_email

# Getting the dropdown options from csv
df = pd.read_csv("pages/topics.csv")
topic_options = df["topic"]

# making the framework
st.header("Contact Us")

with st.form(key="form_contact"):
    user_email = st.text_input("Your email")
    topic = st.selectbox(label="What topic do you want to discuss?", options=topic_options)
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: Email from {user_email}

From: {user_email}
Topic: {topic}
{raw_message}
"""
    button = st.form_submit_button("Sent Email")
    if button:
        send_email(message)
        st.info("Email has been sent")
